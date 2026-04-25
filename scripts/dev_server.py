#!/usr/bin/env python3
"""
Mira Palace dev server.

Like `python -m http.server` but with two refinements that matter for this
preview:
  1. HTML / CSS / JS get aggressive no-cache headers so the browser never
     serves a stale page after a rebuild.
  2. Media files (mp3, ogg, mp4, webm, etc.) are cacheable AND served with
     HTTP Range support, so cross-page audio resume can seek into the file
     correctly. Without Range support, browsers can't seek into a track —
     they'd have to wait for the whole file to download from byte zero.

Production hosting (GitHub Pages) handles all of this natively; this is for
local preview only.

Usage:
    python scripts/dev_server.py <port>
"""
import sys, os, http.server, socketserver, pathlib, mimetypes

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"

MEDIA_EXTS = ('.mp3', '.ogg', '.wav', '.m4a', '.aac', '.flac',
              '.mp4', '.webm', '.mov', '.m4v')


def _is_media_path(p: str) -> bool:
    return p.lower().split('?')[0].endswith(MEDIA_EXTS)


class DevHandler(http.server.SimpleHTTPRequestHandler):
    """Adds Range-request handling for media files. Falls back to the parent
    behaviour for everything else."""

    def end_headers(self):
        if _is_media_path(self.path):
            # Cacheable so cross-page navigations don't re-download.
            self.send_header("Cache-Control", "public, max-age=86400")
            self.send_header("Accept-Ranges", "bytes")
        else:
            # HTML / JS / CSS — never cache (rebuilds visible immediately).
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        rng = self.headers.get('Range')
        if rng and _is_media_path(self.path):
            try:
                self._serve_range(rng)
                return
            except Exception:
                # Fall through to the default handler on parse / IO errors.
                pass
        super().do_GET()

    def _serve_range(self, rng_header: str) -> None:
        """Serve a byte range from a media file. Implements the subset of
        RFC 7233 that browsers actually use for audio/video seeking."""
        path = self.translate_path(self.path)
        if not os.path.isfile(path):
            self.send_error(404, "File not found")
            return
        size = os.path.getsize(path)
        # "bytes=START-END" or "bytes=START-"
        rng_value = rng_header.strip()
        if not rng_value.lower().startswith('bytes='):
            self.send_error(416, "Invalid range unit")
            return
        rng_value = rng_value[6:]
        if ',' in rng_value:
            rng_value = rng_value.split(',', 1)[0]
        start_s, _, end_s = rng_value.partition('-')
        start = int(start_s) if start_s else 0
        end = int(end_s) if end_s else size - 1
        if start > end or start >= size:
            self.send_response(416)
            self.send_header('Content-Range', f'bytes */{size}')
            self.end_headers()
            return
        end = min(end, size - 1)
        length = end - start + 1

        ctype = self.guess_type(path) or mimetypes.guess_type(path)[0] or 'application/octet-stream'
        self.send_response(206)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(length))
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        # end_headers() will append the cache + Accept-Ranges headers.
        self.end_headers()

        with open(path, 'rb') as f:
            f.seek(start)
            remaining = length
            chunk = 64 * 1024
            while remaining > 0:
                buf = f.read(min(chunk, remaining))
                if not buf:
                    break
                try:
                    self.wfile.write(buf)
                except (BrokenPipeError, ConnectionResetError):
                    return
                remaining -= len(buf)


# Make sure .ogg files get the right MIME (older Pythons miss this).
mimetypes.add_type('audio/ogg', '.ogg')
mimetypes.add_type('audio/mpeg', '.mp3')
mimetypes.add_type('audio/wav', '.wav')
mimetypes.add_type('video/mp4', '.mp4')
mimetypes.add_type('video/webm', '.webm')


def main():
    os.chdir(ROOT)
    # Allow the OS to release the port faster between restarts.
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DevHandler) as httpd:
        print(f"Mira Palace dev server on http://localhost:{PORT}/  (no-cache for HTML, Range-aware for media)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down.")
            httpd.shutdown()


if __name__ == "__main__":
    main()

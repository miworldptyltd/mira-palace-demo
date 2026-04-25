# Agent Working Agreement

> **What this is.** The non-negotiable rules a dev agent (Claude or any
> LLM pair-programmer) must follow on a project where the person giving
> instructions is a non-developer project owner / product manager. Paste
> this into a new project's working folder as `AGENT_WORKING_AGREEMENT.md`
> and tell the agent: *"Read this before we start. These rules are
> binding for every session."*

> **Before you use it.** Replace the placeholders below. They are the
> only bits you should edit when adopting this template.
>
> - `<PROJECT_NAME>` — e.g. `Acme Bookings`
> - `<OWNER_NAME>` — e.g. `Jane Doe`
> - `<OWNER_EMAIL>` — e.g. `jane@acme.com`
> - `<PROJECT_ROOT>` — absolute path to the project's workspace folder
> - `<AGENT_MEMORY_DIR>` — folder under the project where the agent's
>   memory file lives. Suggested: `<PROJECT_ROOT>/Planning/claude-memory/`
> - `<PHASE_TWO_DIR>` — folder for the future-enhancements backlog.
>   Suggested: `<PROJECT_ROOT>/Planning/phase-two/`
> - `<RULES_DOC>` — name of the single-source-of-truth document for
>   business rules / locked numbers. E.g. `RULES_v1.docx`
> - `<BUILD_PROMPT>` — name of the phase-by-phase implementation
>   spec. E.g. `Build_Prompt_v2.docx`

---

## 1 — Session hygiene

1.1 At the start of **every** new session, the agent **reads the memory
file at `<AGENT_MEMORY_DIR>/MEMORY.md` first**, then this document, then
the phase plan. The agent never starts work assuming prior chat context
carries over — it doesn't.

1.2 At the end of every session (or after any meaningful change — a
phase advance, a decision, a file change, a direction shift), the agent
**updates `MEMORY.md`**. A dated changelog entry is appended at the top.
The relevant state section above is adjusted.

1.3 Never delete memory. Superseded facts move to the changelog, not
the bin.

1.4 The agent maintains `MEMORY.md` as its only persistent state. Chat
transcripts are treated as ephemeral.

---

## 2 — Business rules and numbers

2.1 **`<RULES_DOC>` is the single source of truth** for every pricing
number, tier, cap, limit, retention window, and rule that the business
cares about. The agent mirrors those values into a single shared code
module (e.g. `packages/shared/rules.ts` or equivalent for the stack).

2.2 **Never hardcode a business number** inside a component, route, or
validation rule. The code imports from the shared module. A hardcoded
literal that matches a rules value is a bug.

2.3 **If a rule is missing from `<RULES_DOC>`, stop and ask.** Never
invent a number. If the owner confirms a new value, the owner edits
`<RULES_DOC>` first, then the agent mirrors it in the shared module,
then the code can use it.

2.4 **`<RULES_DOC>` wins over everything else** — even the build plan.
If the build plan and `<RULES_DOC>` disagree on a number, the agent
stops and flags the conflict before coding around it.

---

## 3 — Code and git hygiene

3.1 **One phase at a time.** Each phase in the build plan has
acceptance criteria; a phase is done only when every criterion has been
verified running on the owner's machine. "It should work" is not
complete.

3.2 **Branch per phase.** Format: `feat/phase-x-shortname`,
`fix/phase-y-shortname`. PR to the main integration branch for every
phase. Owner's review is the quality gate — the agent doesn't merge
without approval.

3.3 **Small commits, clean history.** Conventional Commits format:
`feat(...)`, `fix(...)`, `chore(...)`, `docs(...)`. One logical change
per commit.

3.4 **Never commit secrets.** `.env` and `.env.*` are gitignored from
commit one. All secrets loaded via `process.env` (or stack equivalent),
with typed config parsing at app start. If a secret appears in a diff,
the agent stops and fixes before anything else happens.

3.5 **Sandbox external services from day one.** Payment gateways, email
senders, captcha, calendar APIs — all stubbed locally. The app runs
end-to-end with zero third-party credentials. Real sandbox keys arrive
only when the owner explicitly provides them, via `.env`, never chat.

3.6 **The agent does all git work.** Branching, committing, merging,
tagging, pushing, resolving conflicts. The owner doesn't run git
commands. See §11.

---

## 4 — Legal and compliance gates

4.1 **Legal sign-off is a hard gate for public launch.** If the project
handles personal data or has regulated terms (privacy notice, terms of
service, cookie notice, sector-specific regulation), those documents
must be reviewed and signed off by the responsible lawyer before any
public URL goes live. No exceptions.

4.2 **User consent must be explicit and unbundled.** On any form that
captures personal data, the privacy/data-processing consent is a
separate required checkbox, never bundled with marketing opt-in or any
other consent. Bundling is a compliance violation under most modern
data laws (GDPR / CCPA / KVKK / etc.).

4.3 **Sensitive attachments** (ID documents, medical forms, financial
documents) are encrypted at rest (AES-256-GCM or equivalent),
hard-deleted after a bounded retention window (the shortest defensible
period), and every read is logged (user, timestamp, reason). Raw files
never on disk unencrypted.

---

## 5 — Content and language

5.1 **All user-facing copy goes in i18n bundles** (or an equivalent
content-as-data store). Never hardcode visible strings in components.
There is one authoritative per-language bundle per namespace.

5.2 **Never translate before the source-language baseline is frozen.**
Retranslating is expensive; translating once is cheap. The owner
signals "content is locked" before any translation work begins.

5.3 **Ship one language fully at a time.** Partial translations produce
worse UX than a single-language site.

---

## 6 — Documentation and versioning

6.1 **Planning documents are versioned and never deleted.** When a
planning doc is updated, the old version moves to a sibling `archive/`
folder with its suffix intact (e.g. `FAQ_v2.docx` → `archive/FAQ_v2.docx`
and a new `FAQ_v3.docx` takes its place). Nothing is overwritten.

6.2 **When a form, feature, or agreement changes, the relevant planning
doc is updated in the same session** as the code change. The spec stays
in sync with the code. If the code has a field the spec doesn't
document, the agent closes that gap immediately.

6.3 **Every decision made in chat gets logged somewhere durable** —
either `MEMORY.md` (live state) or a planning doc (specification). Chat
transcripts are not durable memory; the agent doesn't rely on them.

---

## 7 — Future enhancements

7.1 **Ideas that aren't in the current phase scope go in
`<PHASE_TWO_DIR>/FUTURE_ENHANCEMENTS.md`**, the moment they come up.
Don't build them now, don't lose them either. Each entry captures: what,
why, when (which phase could land it), effort estimate (S / M / L), and
who raised it.

7.2 **Never quietly expand scope.** If a request looks like it belongs
to a later phase, the agent says so, logs it in
`FUTURE_ENHANCEMENTS.md`, and finishes the current phase first.

7.3 **Closed items stay under a "Closed / decided" heading at the
bottom of the file.** Nothing is ever deleted from the backlog. A
decision against an item includes the date and the reason.

---

## 8 — Working with the owner

8.1 **Change-capture protocol during content review.** Owner uses:

- `CHANGE: [doc] [where] — [from] → [to]` for minor edits
- `REWRITE: [doc] [section] — [explanation]` for bigger changes

The agent logs changes silently, batches them, and patches in one
coordinated pass when the owner signals "done reading".

8.2 **BLOCKED protocol.** When blocked, the agent posts exactly one
line: `BLOCKED on [thing]. Options: A) … B) … C) …`. The owner picks.
No long debates.

8.3 **Focused questions, not open ones.** The agent proposes a default
and asks for yes/no. Bad: *"How should the form work?"* Good:
*"Submitting without a phone number: allow with a warning, or block and
show an error — I'd lean 'allow with warning', agree?"*

8.4 **Every phase handover includes self-contained verification
commands.** The owner verifies by running a script and seeing what
they're told to see, not by reading code. (See §10 for what
"self-contained" means.)

8.5 **Step-by-step over info-dump.** When guiding the owner through
multi-step verification, the agent hands one step at a time with
explicit **▶ ACTION** / **EXPECT** / **QUESTION** labels, and waits for
a reply before the next step. Walls of numbered instructions get lost.

8.6 **Honest uncertainty.** The agent flags what it's sure of versus
what it's guessing. If it didn't verify something, it says so.

---

## 9 — File-edit workflow

9.1 **After any non-trivial file edit, verify by reading the file's
tail** and confirming the file ends as expected (closing brace, closing
bracket, trailing newline). Silent truncation and partial writes are
the specific failure mode to watch for — a file that looks right but is
missing its last 200 bytes will break the build with a confusing error.

9.2 **Always run `git status` and `git diff --stat` after a batch of
edits** and before committing, to spot discrepancies between what the
agent thinks it wrote and what the repository actually has.

9.3 **If an edit tool is unreliable in a given environment, switch to a
different write path** (raw file write, scripted write, rewrite via
heredoc) rather than persisting with the broken method.

---

## 10 — Verification and run scripts must be self-contained

10.1 **Any shell / PowerShell command handed to the owner must not
assume the current working directory.** Every script resolves its own
paths — typically by deriving from the script file's own location —
and changes to the project root before doing anything. The owner runs
scripts from wherever they happen to be sitting, and the script still
works.

10.2 **Scripts must check prerequisites and act, not assume.** Before
running anything, the script verifies:

- The repo is present and version control is reachable
- The expected branch is checked out (switches to it if not)
- Language runtime / package manager versions are in range (prompts if
  outside the supported band)
- Dependencies are installed (runs install if lock/manifest files are
  newer than the last install stamp)
- Required services (Docker, database, queue, cache) are running. **If a
  service isn't running, the script attempts to start it itself** (e.g.
  launches Docker Desktop from its install path and polls until the
  daemon is reachable). Only if that fails does the script prompt the
  owner.
- Required ports are free; if a dev server is already running on a
  needed port, kill it or reuse it rather than erroring
- `.env` exists (copies from `.env.example` if missing)

10.3 **Two-window pattern for dev runs.** The owner works with two
terminal windows:

- **Window A — dev servers** (foregrounded, live logs)
- **Window B — ops / git / ad-hoc commands**

Every run script for a phase opens both windows in the right directory,
with the dev servers starting in Window A.

10.4 **Every phase ships with a paired `Run-*` and `Stop-*` script.**
`Run` brings everything up (services, dev servers, browser tabs).
`Stop` tears it all down cleanly so nothing leaks ports or containers
between sessions.

10.5 **Verification scripts do content-level checks, not just
port-is-open checks.** After the dev server binds, the script fetches
a representative URL and asserts expected content is present. A script
that says `[OK] Web server running` while the page returns blank HTML
is worse than no script — it's a false confidence signal.

10.6 **Scripts name themselves by intent, not order.**
`Run-PhaseC1-Verify.ps1` not `7-start.ps1`. Ordering by filename stops
being useful the moment the sequence changes.

---

## 11 — Roles

11.1 **The owner is not a developer.** They are the project manager,
the tester in environments the agent can't reach (their browser, their
machine), and the final decision-maker on business and product
questions. The owner **does not**:

- Merge branches, open PRs, push commits, or run raw git commands
- Create files or folders, copy/paste code, edit config files
- Run package managers by hand (scripts do this automatically)
- Resolve merge conflicts, rebase, or cherry-pick

11.2 **The agent is the senior developer.** The agent does all:

- Git operations: branching, committing, pushing, merging, tagging
- File creation, edits, refactors
- Dependency management
- CI / infra configuration
- Writing scripts the owner runs (always self-contained per §10)

11.3 **The agent hands the owner `▶ ACTION` items for only three
things:**

- (a) Running a script in their environment
- (b) Eyeballing something in a browser or app window the agent can't
  see
- (c) Business / product / content decisions only they can make

Never a raw git command, never "now go do this file edit", never "now
merge this".

11.4 **When the agent says "merging now" or "pushing the branch", the
agent is doing it itself** — it's a status update, not a task for the
owner. Status updates after the fact: "merged", "pushed", "tagged
v0.3.0".

---

## 12 — Status summaries and version info

12.1 **Every status summary the agent produces includes a current
version block**, with four elements:

- App version (from the project's primary `package.json` or equivalent)
- Active branch
- Unmerged commits ahead of the last merged baseline
- Key planning doc versions (spec docs the code depends on)

12.2 **Summary format.** Phase status block is followed by a `VERSIONS`
block. Example:

```
PROJECT BUILD — STATUS
───────────────────────────────────────
✅ Phase A  ...                   100%
⏳ Phase B  ...                    33%
   ✅ B.1  Foo done
   ⬜ B.2  Bar next
⬜ Phase C  ...

VERSIONS
   App        : v0.2.0-dev
   Branch     : feat/phase-b2-bar
   Ahead of   : develop by 3 commits
   Planning   : BuildPrompt v2 · Rules v1 · Spec v4
───────────────────────────────────────
```

12.3 **Bump App version at the end of each phase**, in a
`chore: bump version` commit. Semver: sub-phases are patch bumps,
complete phases are minor bumps, soft launches to production are minor
or major depending on scope.

12.4 **Use a progress tick vocabulary.** ✅ merged / ⏳ in progress /
🕐 awaiting review / ⬜ not started / ❌ blocked. Consistent across
every summary, so the owner learns the symbols once.

---

## How to use this document

Drop this file into any project at the root, fill in the placeholders
at the top, then on the first turn with your agent say:

> *"Read `AGENT_WORKING_AGREEMENT.md` before we start. These rules are
> binding for every session, not just this one. Confirm you've read it
> by summarising §1, §10, and §11 back to me in one sentence each."*

If the agent can't summarise those three sections, make them read it
again. That's the smallest cost check that they actually took it in.

---

## Appendix — Companion files to create on day one

Create these files in `<AGENT_MEMORY_DIR>/` at the start of the project:

- **`MEMORY.md`** — the live state / context file. Updated every
  session. Starts with a project snapshot, a phase table, a
  what's-built section, and a changelog.
- **`README.md`** — one-pager explaining what the folder is for, so
  the convention survives agent transitions.

And these in `<PHASE_TWO_DIR>/`:

- **`FUTURE_ENHANCEMENTS.md`** — running backlog for ideas that aren't
  in current-phase scope. Seeded from the build plan's Phase 2+ items
  plus whatever comes up during the build.
- **`README.md`** — one-pager on how to use the backlog and when to
  promote an item into a real phase.

The scripts live at the project root with `Run-*.ps1` / `Stop-*.ps1`
naming. Every phase adds one pair.

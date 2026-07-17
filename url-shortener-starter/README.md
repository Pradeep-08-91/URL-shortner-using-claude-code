# shrtn — URL Shortener Agent Exercise

A starter kit for practicing an end-to-end plan → build → review → test → deploy loop with Claude Code subagents.

## What's in here
```
plan.md                        # the project plan (planner agent reads/updates this)
.github/workflows/ci.yml       # CI: lint + test on PRs, Docker build on main
```

Agent definitions live at the repo root, not here: `../.claude/agents/planner.md` (read-only planning), `../.claude/agents/code-reviewer.md` (read-only review, git diff access only), `../.claude/agents/test-runner.md` (runs pytest/ruff, fixes failures, cd's into `url-shortener-starter/` first).

## Setup
1. Create a new GitHub repo (e.g. `shrtn`), clone it, and copy these files in **preserving the folder structure** (`.claude/` and `.github/` are hidden folders).
2. Enable branch protection on `main`: require a PR and the `lint-and-test` check.
3. Open the folder in a terminal and run `claude`. Restart the session if agents don't appear (they load at startup). Verify with `/agents`.

## The loop (per milestone in plan.md)
1. **Plan** — "Use the planner agent to break down Milestone 1 from plan.md."
2. **Build** — implement in the main session on a feature branch: "Create branch m1-skeleton and implement the plan."
3. **Review** — "Use the code-reviewer agent on the diff against main." Fix CRITICALs.
4. **Test** — "Use the test-runner agent." Everything green before PR.
5. **Deploy** — push the branch, open a PR, let CI run, merge (squash). On main, CI builds and smoke-tests the Docker image. Locally: `docker compose up`.

## Your job as supervisor
- Approve git/bash commands only if you can explain them (Ctrl+E to compare with Claude's explanation).
- Never approve `push --force` or `reset --hard` on shared branches; propose revert or `--force-with-lease`.
- Watch that the reviewer's CRITICAL findings actually get fixed, not argued away.

## Stretch goals (v2)
Custom aliases, link expiry, auth tokens, deploy to a free host (Fly.io/Render) via Actions.

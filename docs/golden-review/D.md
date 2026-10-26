# D. Fork variants: review sheet

Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.

Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.


## D1

Installed skills:

- **release** (paperclipai/paperclip): Coordinate a full Paperclip release across engineering verification, npm, GitHub, smoke testing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss versioning.
- **release** (khulnasoft/TaskCore): Coordinate a full Taskcore release across engineering verification, npm, GitHub, smoke testing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss versioning.
- **release** (gancim/sprint): Coordinate a full Sprint release across engineering verification, npm, GitHub, smoke testing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss versioning.
- **release** (leoustc/teamclaw): Coordinate a full TeamClaw release across engineering verification, npm, GitHub, website publishing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss version bumps.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| D-D1-001 | Ship the new version: run the checks, publish to npm, create the GitHub release, smoke test it, and send word to everyone afterwards. | any of the 4 copies |  | clear | ok | |
| D-D1-002 | Leadership wants this version out today. Take it from final verification all the way through to announcing it. | any of the 4 copies |  | clear | ok | |
| D-D1-003 | Do the full release for this package: test it, publish it, and make sure the published build actually works. | any of the 4 copies |  | clear | ok | |
| D-D1-004 | We're cutting a release; coordinate everything from CI checks to the npm publish to the post-release comms. | any of the 4 copies |  | clear | ok | |
| D-D1-005 | Version 2.4 is approved. Handle the whole rollout, including smoke-testing what ends up on the registry. | any of the 4 copies |  | clear | ok | |
| D-D1-006 | I need this release to go out end to end: checks, registry, GitHub, and telling people about it. | any of the 4 copies |  | clear | ok | |
| D-D1-007 | Time to ship: get this tagged build verified, released, and announced. | any of the 4 copies |  | clear | ok | |
| D-D1-008 | Walk the release through every stage after merge: verify, publish to npm, GitHub release page, smoke test, comms. | any of the 4 copies |  | clear | ok | |

## D2

Installed skills:

- **apple-notes** (Bitterbot-AI/bitterbot-desktop): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Bitterbot to add a note, list notes, search notes, or manage note folders.
- **apple-notes** (Luzzer/Kraken): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks UAGENT to add a note, list notes, search notes, or manage note folders.
- **apple-notes** (spinabot/brigade): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Brigade to add a note, list notes, search notes, or manage note folders.
- **apple-notes** (0xKobold/0xkobolds): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Kobold to add a note, list notes, search notes, or manage note folders.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| D-D2-009 | Add a note called groceries with milk and eggs in my Apple Notes. | any of the 4 copies |  | clear | ok | |
| D-D2-010 | List all the notes in my Work folder. | any of the 4 copies |  | clear | ok | |
| D-D2-011 | Search my notes for the Wi-Fi password. | any of the 4 copies |  | clear | ok | |
| D-D2-012 | Move my Trip ideas note into the Travel folder. | any of the 4 copies |  | clear | ok | |
| D-D2-013 | Export my thesis notes. | any of the 4 copies |  | clear | ok | |
| D-D2-014 | Delete the old draft note. | any of the 4 copies |  | clear | ok | |
| D-D2-015 | Edit my shopping note and add bananas. | any of the 4 copies |  | clear | ok | |
| D-D2-016 | Show me what's in my meeting note. | any of the 4 copies |  | clear | ok | |

## D3

Installed skills:

- **skill-creator** (BidingCC/BuildingAI): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **fsi-fa-skill-creator** (d-wwei/openclaw-financial-services): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **skill-creator** (giocld/dotifles): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends OpenCode capabilities with specialized knowledge, workflows, or tool integrations.
- **skill-creator** (caelis-labs/caelis): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Caelis agent capabilities with specialized knowledge, workflows, or tool integrations.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| D-D3-017 | Help me create a new skill for summarizing meeting transcripts. | any of the 4 copies |  | clear | 4gram:create a new skill, 4gram:create a new skill, 4gram:create a new skill, 4gram:create a new skill | |
| D-D3-018 | I want to update an existing skill so it also handles PDFs. How should I structure it? | any of the 4 copies |  | clear | 4gram:update an existing skill, 4gram:update an existing skill, 4gram:update an existing skill, 4gram:update an existing skill | |
| D-D3-019 | Walk me through writing a skill that wraps our internal deploy tool. | any of the 4 copies |  | clear | ok | |
| D-D3-020 | How do I package specialized domain knowledge into a reusable skill? | any of the 4 copies |  | clear | ok | |
| D-D3-021 | Scaffold a skill for converting CSV files to JSON. | any of the 4 copies |  | clear | ok | |
| D-D3-022 | Review the structure of my skill and tell me how to make it more effective. | any of the 4 copies |  | clear | ok | |
| D-D3-023 | I'd like to extend the agent with a workflow for triaging bug reports, built as a skill. | any of the 4 copies |  | clear | ok | |
| D-D3-024 | Draft a new skill that bundles scripts and reference files for log analysis. | any of the 4 copies |  | clear | ok | |

## D4

Installed skills:

- **caveman-compress** (JuliusBrussee/caveman-code): Ultra-compressed communication mode (lite / full / ultra) that cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Use when the user requests "caveman mode", "less tokens", "be brief", or when output budget is tight.
- **caveman** (brendon-colburn/hs-skills-lesson): Ultra-compressed communication mode. Cuts token usage by ~75% by speaking like a smart caveman while keeping full technical accuracy. Use when the user says "caveman mode", "talk like caveman", "less tokens", or "be brief".
- **caveman** (JafarAbdi/myconfigs): Ultra-compressed communication mode. Cuts token usage ~75% by speaking like smart caveman while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "less tokens", "be brief", or when token efficiency is requested.
- **caveman** (kiran-capoor94/wizard): Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Use when user says "caveman", "caveman mode", "be terse", "minimal output", "drop the filler", "less tokens", or invokes /caveman.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| D-D4-025 | Talk like a caveman from now on. | any of the 4 copies |  | clear | ok | |
| D-D4-026 | Be brief; I'm running low on token budget. | any of the 4 copies |  | clear | ok | |
| D-D4-027 | Cut your answers way down but keep them technically accurate. | any of the 4 copies |  | clear | ok | |
| D-D4-028 | Use ultra-compressed replies for the rest of this session. | any of the 4 copies |  | clear | ok | |
| D-D4-029 | Drop the filler and give me terse answers. | any of the 4 copies |  | clear | ok | |
| D-D4-030 | Switch to minimal output mode. | any of the 4 copies |  | clear | ok | |
| D-D4-031 | Spend fewer tokens on each response; shorten everything. | any of the 4 copies |  | clear | ok | |
| D-D4-032 | Reply in the shortest form that stays correct. | any of the 4 copies |  | clear | ok | |

## D5

Installed skills:

- **slack** (understudy-ai/understudy): Use when you need to control Slack from Understudy via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
- **slack** (CodeAndCanvasLabs/Daemora): Use when you need to control Slack from Daemora via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
- **slack** (x402agent/NanoSolana): Use when you need to control Slack from NanoClawd via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
- **slack** (LuisvelMarketer/genome): Use when you need to control Slack from Genoma via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| D-D5-033 | React to the last message in #general with a thumbs up. | any of the 4 copies |  | clear | ok | |
| D-D5-034 | Pin the deploy announcement in the engineering channel. | any of the 4 copies |  | clear | ok | |
| D-D5-035 | Unpin the old standup reminder from the team channel. | any of the 4 copies |  | clear | ok | |
| D-D5-036 | Add an eyes emoji to the message in my DM with Sam. | any of the 4 copies |  | clear | ok | |
| D-D5-037 | Pin this message to the channel. | any of the 4 copies |  | clear | ok | |
| D-D5-038 | Remove the pin from yesterday's incident notice. | any of the 4 copies |  | clear | ok | |
| D-D5-039 | React with a checkmark to the approval message in #releases. | any of the 4 copies |  | clear | ok | |
| D-D5-040 | Pin the link I just shared in the project channel. | any of the 4 copies |  | clear | ok | |

## D6

Installed skills:

- **pull** (sushaantu/boxento): Pull latest origin/main into the current local branch and resolve merge conflicts (aka update-branch). Use when Codex needs to sync a feature branch with origin, perform a merge-based update, and resolve conflicts safely.
- **pull** (johngrandson/orkestry): Pull latest origin/main into the current local branch and resolve merge conflicts (aka update-branch). Use when the agent needs to sync a feature branch with origin, perform a merge-based update (not rebase), and guide conflict resolution best practices.
- **pull** (RGM-89sc/symphony-cc): Pull latest origin/main into the current local branch and resolve merge conflicts (aka update-branch). Use when Claude Code needs to sync a feature branch with origin, perform a merge-based update (not rebase), and guide conflict resolution best practices.
- **kairastra-pull** (dbachko/kairastra): Pull the latest origin default branch into the current local branch and resolve merge conflicts (aka update-branch). Use when the active agent needs to sync a feature branch with origin, perform a merge-based update (not rebase), and guide conflict resolution best practices.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| D-D6-041 | Pull the latest main into my branch and fix any merge conflicts. | any of the 4 copies |  | clear | ok | |
| D-D6-042 | Update my feature branch from origin with a merge, not a rebase. | any of the 4 copies |  | clear | ok | |
| D-D6-043 | Sync my branch with the remote default branch and resolve conflicts safely. | any of the 4 copies |  | clear | 4gram:and resolve conflicts safely | |
| D-D6-044 | My branch is behind main. Bring it up to date and sort out the conflicts. | any of the 4 copies |  | clear | ok | |
| D-D6-045 | Merge origin/main into what I'm working on and help me with the conflicting files. | any of the 4 copies |  | clear | ok | |
| D-D6-046 | Bring my local branch current with the remote default branch via merge. | any of the 4 copies |  | clear | ok | |
| D-D6-047 | I hit conflicts every time I update my branch. Pull in the latest and walk me through them. | any of the 4 copies |  | clear | ok | |
| D-D6-048 | Do an update-branch: fetch origin and merge it in here. | any of the 4 copies |  | clear | ok | |

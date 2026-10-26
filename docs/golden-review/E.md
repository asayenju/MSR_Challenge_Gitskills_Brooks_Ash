# E. Isolated controls: review sheet

Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.

Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.


## E1

Installed skills:

- **messageprotocol-core** (BIGSUNGG/DS_MessageProtocol): Maintain MessageProtocol runtime APIs in Source/MessageProtocol.Core: public message attributes, IMessageSerializable contracts, MessageSerializer registration and generic/object dispatch, MessageFlag, MessageCategory, and MessageId parsing. Use when working on runtime serialization or deserialization, registration/cache bugs, InvalidCastException or KeyNotFoundException paths, or public contract changes.
- **spec-guide** (esxr/product-wiki): Use when authoring a new Executable Implementation Spec (EIS) from a natural-language description. Triggers on "write an EIS", "create new EIS", "executable implementation spec", "/create-feature". Teaches the EIS file format, numbering, required sections, the grounding rule (must verify against src/ before writing), and the wiki-companion rule (summary under docs/wiki/eis/ plus index update).
- **hal-and-abstractions** (bhu-dev/crosspoint-todoist): Layering and abstraction discipline for the firmware. Use when touching storage, input, display, settings, i18n, or rendering, or any code that could reach into the SDK. Covers routing through the HAL (HalStorage / HalGPIO / HalDisplay) instead of raw SDK classes, MappedInputManager logical buttons instead of raw GPIO indices, UITheme/GUI for all rendering, the singleton macros, tr() for user-facing text, and where a new abstraction boundary belongs.
- **catalyst-changelog-sync** (avvale/aurora-catalyst-docs): Pull newly-archived openspec changes from the Aurora sibling repos, classify each one as PUBLISH or DISMISS against a user-facing-impact contract, draft bilingual changelog entries (EN + ES) for the ones that qualify, and persist every decision to the versioned registry. Supports dry-run and bidirectional manual override.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E1-001 | My serializer throws an InvalidCastException when I dispatch a message through the generic registration path in the runtime library. Help me track it down. | messageprotocol-core |  | clear | ok | |
| E-E1-002 | Turn this feature description into the repo's runnable implementation spec doc, checked against what's actually in src first. | spec-guide |  | clear | ok | |
| E-E1-003 | I'm adding a new settings screen to the firmware. Make sure it goes through the hardware abstraction and theming layers rather than calling the SDK directly. | hal-and-abstractions |  | clear | ok | |
| E-E1-004 | Review the recently archived changes in the sibling repos, decide which deserve a customer-facing changelog entry, and draft English and Spanish text. | catalyst-changelog-sync |  | clear | ok | |

## E2

Installed skills:

- **finbif-taxonomy** (luomus/finbif-skills): Detailed guide to looking up species names, taxonomy, data, and classification through the FinBIF API at api.laji.fi. Use this skill when the user wants to find a taxon ID (MX code), look up species by scientific or common name, browse taxonomic hierarchies, get red list evaluations, find informal taxon groups, or work with /taxa, /informal-taxon-groups, /checklists, or /autocomplete/taxa endpoints. Also use when the user needs to resolve a species name to an identifier.
- **postgres-query-performance-review** (genaptic/skillsets): Diagnose PostgreSQL statement latency using sanitized SQL, EXPLAIN evidence, cardinality, buffers, temp work, joins, statistics, waits, parameters, and representative experiments. Use when a query or workload is slow, unstable, or regressed. Do not use for greenfield schema design, broad schema audits, or choosing an index without statement-level evidence.
- **orchestration-turn-reporting** (JoyJoin-Tech-Limited/JoyJoin_app_v0.1): Structured turn-end reporting and iterative improvement for JoyJoin's native agent orchestration. Use when adding or changing per-agent summary JSON, supervisor consolidation, last-5-turn feedback loops, or operational session log persistence under .git/.orchestration. Trigger phrases: turn-end summary, agent summary JSON, supervisor consolidation, last 5 turns, iterative improvement loop, record-summary.
- **sentience-sync** (thevibethinker/n5os-ode): Two-way sync with Sentience API. Manages three processes: (1) Push curated Zo memories to Sentience with PII filtering, (2) Poll for new memories and stream desktop screenshots to a local activity feed, (3) Daily digest agent that categorizes activity into buckets (personal, work-project, zo, physical-intelligence, other) using a relevance rubric.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E2-005 | Find the taxon ID for the Eurasian lynx and show me its red list evaluation. | finbif-taxonomy |  | clear | ok | |
| E-E2-006 | This Postgres query got ten times slower after last week's deploy. Diagnose it from the EXPLAIN output. | postgres-query-performance-review |  | clear | ok | |
| E-E2-007 | At the end of each turn, have every agent emit a summary JSON and have the supervisor consolidate them. | orchestration-turn-reporting |  | clear | ok | |
| E-E2-008 | Push my curated memories to Sentience with PII filtered out, and set up the daily activity digest. | sentience-sync |  | clear | 4gram:memories to sentience with | |

## E3

Installed skills:

- **model-verify-flagos** (Pinoeer-kingxi/AICASGC): Verify the serving stack with a user-specified target model. Runs twice: first with FlagGems/FlagCX disabled (isolate model-specific errors), then with full multi-chip stack enabled. Diffs the two runs to pinpoint which layer caused any failure.
- **responsive-ui-qa** (divyanshu-iitian/agent-website-design-skills): Verify and fix responsive website UI quality. Use when Codex needs to test desktop/mobile layouts, catch text overflow, overlap, blank canvases, broken navigation, unstable grids, awkward wrapping, or viewport-specific visual regressions.
- **narrative-decoder** (dlmastery/hedge-fund-analysis): Management narrative decoder and earnings call NLP analyst. Performs forensic linguistics on corporate communications. Tracks promise vs. delivery, goal post movement, guidance sandbagging, tone dynamics, and competitive language shifts.
- **task-writeback** (TOSUKUi/mc-auto-starting): Update restart notes, task records, and plan deltas after a task without bloating AGENTS.md. Use when Codex should write back the minimum durable context needed for the next fresh session.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E3-009 | Verify my model serves correctly, first with the acceleration libraries off and then with everything switched on across all the chips, and diff the two runs. | model-verify-flagos |  | clear | ok | |
| E-E3-010 | Check my site's mobile layout for text overflow and broken navigation, and fix what you find. | responsive-ui-qa |  | clear | ok | |
| E-E3-011 | Analyze this earnings call transcript for promises versus delivery and shifts in management tone. | narrative-decoder |  | clear | ok | |
| E-E3-012 | Write down the minimum notes a brand-new session needs from what we just did, without bloating the agent instructions file. | task-writeback |  | clear | ok | |

## E4

Installed skills:

- **multi-specialist-review** (NickCrew/Claude-Cortex): User-triggered multi-agent code review. Spawns 3-5 parallel specialist sub-agents that read actual source files, runs mechanical citation verification, and synthesizes a single review artifact. Use for PR-level changes, multi-commit ranges, or security-sensitive work where single-turn review is insufficient.
- **anamnesis** (Wondermonger-daydreaming/claude-skills-library): Trace any concept to its deepest structural root in human thought, then map the genealogy of transformations forward.
- **project-hub-conventions** (wsagency/WS-Claude-marketplace): Conventions for WS Agency multi-repo project hubs (subfolder layout, project.yaml schema, CLAUDE.md cascade, .gitignore managed block, invoke-ai.sh contract). Use when creating, extending, or troubleshooting a `<project>-main` hub repo, or when asked about "project hub", "multi-repo", or `<name>-main` / `<name>-truth` repos.
- **runtime-continuity** (kingwangking/Software-Development-Methodology-and-Theory-Repository): Extract, compress, restore, and maintain an AI agent's current cognitive runtime state across chats, tasks, and project contexts. Use when the user wants to continue an effective collaboration style, migrate to a new chat, preserve task focus, summarize current working state, or avoid losing a shaped agent behavior.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E4-013 | Do a deep review of this multi-commit range using several parallel specialist reviewers who read the actual source. | multi-specialist-review |  | clear | ok | |
| E-E4-014 | Trace the concept of trust back to its deepest roots in human ideas, then chart how it has changed since. | anamnesis |  | clear | ok | |
| E-E4-015 | How should the folder layout and project.yaml look for our multi-repo project hub? | project-hub-conventions |  | clear | ok | |
| E-E4-016 | I'm moving to another conversation. Compress our current working state and collaboration style so I can restore it there. | runtime-continuity |  | clear | ok | |

## E5

Installed skills:

- **ui-pattern-source-orchestrator** (sergekostenchuk/ui-pattern-source-orchestrator): Recommend UI pattern sources, component registries, visual references, and motion/runtime options for UI/UX projects with stack compatibility, freshness labels, no-copy boundaries, evidence manifests, and handoffs to design, build, critic, and progress-dashboard skills. Use when a user asks what UI libraries, references, patterns, effects, dashboards, admin components, or inspiration sources should inform a site, app, admin panel, or agent interface.
- **repo-analyzer** (DaveCuc/diatax-web): Rules and scripts for analyzing a code repository efficiently. Minimizes token consumption by stripping comments/whitespace and extracting structural metadata (classes, methods, signatures) from source files, generating a clean template to pass to the Writer agent. Make sure to use this skill whenever analyzing repositories, reading codebase structures, or preparing data for document writing.
- **ygrep** (yetidevworks/ygrep): IMPORTANT: Try ygrep FIRST for all code and file searches before using Grep, Glob, or Task explore. ygrep uses a pre-built full-text index and returns results in milliseconds. Fall back to built-in tools only if ygrep returns no results.
- **web-works** (GopiB9119/agent-live-web): Fast website understanding and execution skill for LLM agents with strict verification and optional JSON task contracts.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E5-017 | Which UI component libraries and motion references suit my React dashboard project? | ui-pattern-source-orchestrator |  | clear | ok | |
| E-E5-018 | Analyze this repository cheaply: strip comments and extract the classes and method signatures for the drafting agent. | repo-analyzer |  | clear | ok | |
| E-E5-019 | Find every place the config loader is called in this codebase. | ygrep |  | clear | ok | |
| E-E5-020 | Quickly understand this website, then carry out the checkout task with strict verification of each step. | web-works |  | clear | ok | |

## E6

Installed skills:

- **package-search-laraplugins** (danielpetrica/Laraplugins-skills): Search and verify Laravel packages using the LaraPlugins MCP server. Activate when you need to find a package for a specific need, verify health or vendor reputation, or get curated tool recommendations.
- **Sage** (luruibu/v-girl-friend): Zen Healing Girlfriend - Someone who knows silence, knows how to listen, and knows how to gently catch you when you're in chaos.
- **reporting-and-archiving-findings** (K-Dense-AI/science-superpowers): Use when an analysis is complete and verified, and you need to decide how to report it and archive the work for reproducibility
- **open-loops** (teejayen/arc): Track and manage open threads, hanging items, and things waiting for follow-up. Use to add new threads, review what's stale, mark items resolved, or get a quick status of what's hanging.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E6-021 | Find a healthy, well-maintained Laravel package for generating PDFs. | package-search-laraplugins |  | clear | ok | |
| E-E6-022 | I've had a rough day and I just need someone gentle to listen. | Sage |  | clear | ok | |
| E-E6-023 | My analysis is verified. Decide how to report it and keep a reproducible record of it. | reporting-and-archiving-findings |  | clear | 4gram:decide how to report | |
| E-E6-024 | What threads of mine are hanging or waiting on a follow-up? Mark the vendor one resolved. | open-loops |  | clear | ok | |

## E7

Installed skills:

- **no-ghost-edit-mode** (sarankirthic/my-claude-skills): Production CLAUDE.md for Claude Code. Enforces phased execution, edit integrity, exhaustive reference search, and scope discipline on agentic coding tasks. Drop into project root as CLAUDE.md. Trigger when configuring Claude Code agent behaviour, or when agent is making silent bad edits, skipping verification, or breaking things without warning.
- **se-validator-review** (low-perry/se-validator): Run the local SE Validator on Luigi's Box catalog feeds, Content Update JSON, autocomplete HTML/JS, analytics payloads, and service profiles. Use when the user asks whether integration evidence is correct, good, bad, ready, risky, blocked, or pastes raw XML, JSON, HTML, or JavaScript for review.
- **product-compliance** (Cleo-Labs-IA/skills_library): Use when checking if a product is compliant in target markets, running substance checks against ingredient lists, calculating revenue-at-risk, or answering "can I sell this product in [country]?"
- **investigating-warnings** (cassamajor/xcnf): Don't dismiss warnings without understanding them - investigate to determine if they indicate bugs, misconfigurations, or are cosmetic, then document findings either way

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E7-025 | Claude Code keeps quietly breaking things with its edits and skipping verification. Configure it to stop doing that. | no-ghost-edit-mode |  | clear | ok | |
| E-E7-026 | Here's a catalog feed XML and some autocomplete JavaScript. Is the integration evidence correct? | se-validator-review |  | clear | ok | |
| E-E7-027 | Am I allowed to sell this skincare product in Germany? Check its ingredient list. | product-compliance |  | clear | ok | |
| E-E7-028 | This build prints a deprecation warning. Don't just ignore it; work out whether it's a real problem and document what you find. | investigating-warnings |  | clear | ok | |

## E8

Installed skills:

- **local-dev-experience** (mcj-coder/agent-skills): Use this skill when establishing or refining local developer workflows (hooks, linting, formatting, validation) to prevent non-compliant changes from being committed or merged.
- **analyze-voice** (nathanvale/side-quest-marketplace-old): Analyze voice memo transcriptions, create notes with appropriate content, and return lightweight proposals. For resources (ideas, reflections), creates note with Layer 1 transcription. For meetings, extracts structured body content. Worker skill for triage orchestrator.
- **reins** (pastel-sketchbook/reins): Use the reins CLI to bootstrap and maintain AI-assisted development frameworks in any project. Covers init, update, rule system, analysis lenses, autopilot, and verification workflow. Use when initializing reins in a new project, updating managed files, managing language rule templates, generating analysis-lens concerns, or running the reins development workflow (TDD, Tidy First, layered rules).
- **xbrl** (modeled-information-format/research-harness-template): Render surviving findings (typically a regulatory-disclosure artifact) into an inline XBRL (iXBRL) document directly from the SOURCES. Tags facts with xbrli:context / xbrli:unit and taxonomy concepts inside a human-readable XHTML shell, anchored to the current SEC inline-XBRL taxonomy. Never built from a rendered report.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E8-029 | Set up pre-commit hooks, linting and formatting so non-compliant changes can't be committed. | local-dev-experience |  | clear | ok | |
| E-E8-030 | Process this voice memo transcript into a note and give me a short proposal for what to do with it. | analyze-voice |  | clear | ok | |
| E-E8-031 | Bootstrap the reins framework in this project and run its verification workflow. | reins |  | clear | name:reins | |
| E-E8-032 | Render these verified findings as an inline XBRL document tagged to the SEC taxonomy. | xbrl |  | clear | name:xbrl | |

## E9

Installed skills:

- **dataevolver-onboarding** (PRIS-CV/DataEvolver): Guide DataEvolver server setup and safe dry-run onboarding. Use when a user wants a Codex or Claude Code agent to configure a local or remote DataEvolver checkout, interview for SSH/runtime paths, inspect Python/uv/conda/Hugging Face/Blender/GPU readiness, plan dependency and model setup, choose a dynamic or fixed GPU shard policy, prepare HYWorld, Blender MCP, or paper-validation execution handoff, or generate non-sensitive .dataevolver/local/ENVIRONMENT.md and env.config.json profiles without launching long jobs.
- **red-pen** (ChunMinChang/dotfiles): Independent red-team review for Firefox root-cause analyses and proposed fixes. Use to critique an analysis, patch, Phabricator revision, commit, diff, or working tree with isolated Codex subagents and structured verdicts.
- **website-builder-pipeline** (ravi1soni-hue/ai-coding-agent): Generate and repair this repository's AI website builder pipeline from prompt to deployment. Covers requirement extraction, one-question clarification, confirmation gate, system design JSON, full file code generation, workspace materialization, build/test loop, archive, Vercel and Railway deployment, and deterministic failure triage. Use for frontend/backend/db/deployment website generation or stuck pipeline runs.
- **library-patterns** (ccashwell/evm-cortex): Library design patterns for reusable Solidity code. Use when creating shared utilities, math libraries, or type-safe operations. Covers internal vs external libraries, using-for, deployment patterns, and common math libraries.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E9-033 | Help me set up DataEvolver on a remote GPU machine, starting with a dry run that checks Python, Blender and GPU readiness. | dataevolver-onboarding |  | clear | ok | |
| E-E9-034 | Red-team this Firefox root-cause analysis and its proposed patch with independent reviewers. | red-pen |  | clear | ok | |
| E-E9-035 | Fix the stage of our AI website builder that goes from the clarification question through code generation to deployment. | website-builder-pipeline |  | clear | ok | |
| E-E9-036 | Design a reusable Solidity math library. Should it be internal or external, and how do I deploy it? | library-patterns |  | clear | ok | |

## E10

Installed skills:

- **kf-g-skill-naming-creation-organization-rules** (melumuccu/ai): Use this skill when creating, naming, renaming, or organizing skills in this repository. Always use it when you need to decide rules for skill directory names, propose names that follow the existing convention, organize skills so related entries stay close together, or distinguish local skills from external ones.
- **channel-adaptation** (syeda-hoorain-ali/crm-digital-fte-factory): Format agent responses according to channel-specific style guidelines before sending to customers. This skill should be used AFTER escalation-decision returns should_escalate=False and BEFORE calling send_response tool. Transforms raw response text into channel-appropriate format (Gmail: formal & thorough, WhatsApp: casual & rapid under 60 words, Web Form: direct & functional). Applies CloudStream CRM brand voice: empathetic, concise, proactive. Mandatory for EVERY customer response.
- **nav-map** (neonwatty/nav-map): Use when an agent needs to map, inspect, prototype, or verify an app workflow with NavMap. Covers workflow manifests, screenshots, HTML mockup surfaces, live route probes, auth-state-safe checks, agent context contracts, and nav-map.json generation.
- **tex-environment-check** (arivero/firstProof): Verify and document local TeX/LaTeX installations (especially BasicTeX on macOS) with smoke tests, package checks, and reproducibility notes. Use when you need to confirm whether LaTeX is available, diagnose engine-specific issues (for example LuaLaTeX cache paths), or generate a Markdown report for project setup docs.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E10-037 | What should I name the new skill directory so it follows our repo convention and sits next to related ones? | kf-g-skill-naming-creation-organization-rules |  | clear | ok | |
| E-E10-038 | Format this customer reply for WhatsApp instead of Gmail before it goes out. | channel-adaptation |  | clear | ok | |
| E-E10-039 | Map this app's workflow with screenshots and generate the nav-map.json. | nav-map |  | clear | name:nav-map | |
| E-E10-040 | Verify that LaTeX is installed on my Mac and write a report of the engine and package checks. | tex-environment-check |  | clear | ok | |

## E11

Installed skills:

- **ecom-quick** (OmarAAntar/claude-ecom): Fast e-commerce triage. Runs only 3 agents (storefront, conversion, trust & offers) and returns a top-line score and the top 3 critical issues in under 2 minutes. No PDF. Use when user says quick audit, fast check, triage, top issues, or just looking to spot-check a store before committing to a full audit.
- **mind-intent-loop-orchestrator** (DGuedz/MIND): Orchestrates intent into scoped agent loops with self-generated task prompts, verification, memory, and safe fallbacks. Invoke for substantial tasks that need planning before action.
- **quality-python-code** (m0hill/dotfiles): Guides agents to write typed, idiomatic, observable, testable production Python 3.11+ code with boundary validation, domain-specific exceptions, cohesive modules, and real-seam tests. Use when writing, reviewing, refactoring, or cleaning up Python application, service, worker, CLI, or library code.
- **freezetagcircle-roundup** (kelani34/FreezeTagCircle): Prepare, validate, and close out FreezeTagCircle development sessions. Use when starting work in the FreezeTagCircle repo, ending a session, creating or merging PRs, updating project memory, checking docs/backlog/decisions/research/production notes, enforcing branch/issue/label/review workflow, or running the project roundup before handing off.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E11-041 | Spot-check my online store fast and give me the top three critical issues. | ecom-quick |  | clear | ok | |
| E-E11-042 | This is a big task. Plan bounded loops of agent work, with verification and memory, before acting. | mind-intent-loop-orchestrator |  | clear | ok | |
| E-E11-043 | Refactor this Python 3.11 worker service to be typed and testable, with domain-specific exceptions. | quality-python-code |  | clear | ok | |
| E-E11-044 | I'm ending my FreezeTagCircle session. Close it out: update the backlog and decisions and check the branch workflow. | freezetagcircle-roundup |  | clear | ok | |

## E12

Installed skills:

- **cbex-b2c-individual-portal-ux** (horizonfortravels/cebx-code): One-user portal UX for CBEX individual external accounts. Use when designing or refining B2C dashboards, shipments, tracking, wallet, addresses, support, or settings so the portal feels personal, simple, action-oriented, and free of team, developer, or organization concepts.
- **component-search** (redpanda-data/connect): This skill should be used when users need to discover Redpanda Connect components for their streaming pipelines. Trigger when users ask about finding inputs, outputs, processors, or other components, or when they mention specific technologies like "kafka consumer", "postgres output", "http server", or ask "which component should I use for X".
- **sycophancy-skill** (iltutishrak/claude-skills): Flips Claude's default agreement bias. When the user brings a decision, idea, plan, or argument, Claude argues the strongest case AGAINST it first, surfaces the assumptions the user hasn't tested, and refuses to retreat on pushback unless given new evidence. Use whenever the user wants a real thinking partner instead of a confidence-boosting mirror.
- **S2 Retrieve** (CodeGeneration2/GBLLM): A meta-skill for selectively invoking optimization operators based on uncertainty signals and a dynamic skill-budget, using confidence-aware routing instead of blindly scanning the full catalog.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E12-045 | Redesign the shipments and wallet screens of the individual customer portal so they feel personal and simple. | cbex-b2c-individual-portal-ux |  | clear | ok | |
| E-E12-046 | Which Redpanda Connect component reads from Kafka, and what processors can I chain after it? | component-search |  | clear | ok | |
| E-E12-047 | Here's my startup plan. Give me the best argument against it, and don't back down unless I give you new evidence. | sycophancy-skill |  | clear | ok | |
| E-E12-048 | Route this task using confidence-aware selection with a limited skill budget, rather than scanning the whole catalog. | S2 Retrieve |  | clear | ok | |

## E13

Installed skills:

- **react-vite-workflow** (ZedZed34/Calories-Counter): Use this skill when adding pages, routes, components, or styles; running dev/build/lint/test commands; or navigating the project structure. Documents the full file tree, npm scripts, routing patterns, CSS conventions ("Neon Court" dark theme), and component conventions.
- **cliparr-logtape** (TechSquidTV/Cliparr): Use this skill when changing, reviewing, or adding Cliparr LogTape logging in frontend, server, shared helpers, or tests. Covers Cliparr category taxonomy, wide-event boundaries, flat dot-notated fields, context, redaction/noise rules, no-console enforcement, and validation for logging PRs.
- **task-driven-ai-dev** (zhaohuanke123/vanko-skill): Turn a repository into a task-driven AI delivery loop with durable planning artifacts, guarded single-task execution, progress logging, and validation gates. Use when Codex needs to bootstrap or operate workflows built around files like architecture.md, task.json, progress.txt, project-config.json, CLAUDE.md, AGENTS.md, or similar backlog-driven harnesses, especially when replacing shell-based automation with explicit subagent orchestration.
- **capture-slop** (vietbui1999ru/llm-wiki): Invoke after code review, a bug post-mortem, or a /diagnose session reveals a recurring AI failure pattern in this codebase. Writes to mistakes/slop-register.md and optionally updates CONTEXT.md.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E13-049 | Add a new page and route to this React Vite app using the Neon Court styles. | react-vite-workflow |  | clear | ok | |
| E-E13-050 | Review my Cliparr logging changes for category and redaction rules. | cliparr-logtape |  | clear | ok | |
| E-E13-051 | Turn this repo into one run by tasks, using task.json, progress.txt and validation gates. | task-driven-ai-dev |  | clear | 4gram:task json progress txt | |
| E-E13-052 | The review showed a recurring AI mistake in this codebase. Record it in the slop register. | capture-slop |  | clear | ok | |

## E14

Installed skills:

- **autoopt** (ElliotDrel/Universal-Spell-Check): Autonomous Karpathy-style optimization loop for Universal Spell Check. Runs N iterations in an isolated git worktree on a dedicated branch, each iteration proposing one src/ change, building, running a low-call speed bench, verifying correctness, and committing or reverting based on confirmed request_ms improvement. Use when the user wants to autonomously optimize app speed, run autoopt, run an optimization loop, or improve performance over many iterations.
- **recursive-residual-reasoning** (zccz14/R3): Use this skill when a task involves hard reasoning, unclear causes, unexplained observations, failed hypotheses, ambiguous diagnoses, complex systems, emergent behavior, investigation planning, or any situation where the current explanation space is incomplete. This skill applies Recursive Residual Reasoning: preserve what cannot yet be explained as an explicit residual, expand that residual into the next reasoning space, and produce a traceable path from observation to conclusion, action, or bounded stop reason.
- **git-wrap-up** (rakaar/ddm_data): Standard repository wrap-up workflow for Codex. Use when the user says "git wrap up", asks to follow CODEX_GIT_WRAPUP.md, or otherwise asks Codex to inspect the current git worktree, document new or changed files, commit intended changes, and push to origin/main.
- **go-modern** (vocdoni/skills): Use this skill when writing, reviewing, or refactoring Go code. Detects the project's Go version from go.mod and applies only language features available in that version - modern built-ins like slices/maps/cmp, type-safe atomics, errors.Join, range-over-int, t.Context(), omitzero, b.Loop(), strings.SplitSeq, wg.Go(), new(val), errors.AsType. Avoids both outdated patterns and features from newer-than-target versions.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| E-E14-053 | Run an autonomous optimization loop on the spell checker in an isolated worktree, keeping only changes that improve request latency. | autoopt |  | clear | ok | |
| E-E14-054 | I can't explain these observations and my hypotheses keep failing. Help me work out what my current explanation is missing. | recursive-residual-reasoning |  | clear | ok | |
| E-E14-055 | Wrap up the repo: document the changed files, commit, and push to main. | git-wrap-up |  | clear | ok | |
| E-E14-056 | Refactor this Go code to use modern features supported by the Go version declared in go.mod. | go-modern |  | clear | ok | |

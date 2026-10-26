# N. Negatives (no skill should load): review sheet

Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.

Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.


## A1

Installed skills:

- **analysis-api-create-cherry-pick-issue** (JetBrains/kotlin): Create a KTIJ cherry-pick tracking issue for a KT fix that needs to be cherry-picked to an IntelliJ branch. Use when cherry-picking Analysis API fixes.
- **qa-cherry-picks** (Moonsong-Labs/knowledge-work-plugins): QA cherry-pick tracking documents for polkadot-sdk fork upgrades. Use when auditing, verifying, or updating cherry-pick tables in docs/cherry-picks/, when upgrading to a new polkadot-sdk stable branch, or when checking if a cherry-pick was applied.
- **release-create-tracker-issue** (pytorch/test-infra): Generate (and optionally open) a PyTorch release tracker / cherry-pick tracking issue from a release announcement, like https://github.com/pytorch/pytorch/issues/180506. Triggered by mentions of "release tracker", "release tracking issue", "cherry-pick tracker", or "cut a release branch issue".
- **cherry-pick-release** (tomsej/dotfiles): Create a release branch from main, cherry-pick specific commits from test, and validate the result. Use when preparing a production release by cherry-picking commits, checking scope and parity with the test branch.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-A1-001 | What does cherry-picking mean in git, and when is it a bad idea? | NONE |  | clear | ok | |

## A4

Installed skills:

- **graphite** (lightdash/lightdash): Manage stacked PRs with Graphite CLI (gt) instead of git for branch/PR operations. Auto-detects Graphite repos via .git/.graphite_repo_config. Use when: creating stacked PRs, navigating branches, submitting PRs, syncing with main, restacking after changes, or any gt command usage.
- **stackit** (ok-very/autoart): Manage stacked Git branches with Stackit. Use when creating/managing stacked branches, submitting PRs for branch stacks, navigating branch trees, rebasing stacks, syncing with main/trunk, troubleshooting stack issues, absorbing changes, resolving rebase conflicts, or any workflow involving dependent Git branches. Keywords stackit, stacked changes, stacked PRs, branch stack, restack, absorb, git stack.
- **socle-cli** (benekuehn/socle): Use this skill when you need to guide or automate usage of the socle CLI (the `so` command) for stacked-branch workflows, including installing `so`, tracking branch stacks, navigating up/down/top/bottom, creating stacked branches, restacking, syncing, or submitting stacked PRs.
- **git-spice** (carrieforde/grove): Manage stacked Git branches with Git Spice (gs). Use when working with stacked PRs, managing dependent branches, submitting multiple related PRs, restacking branches after changes, or navigating branch hierarchies. Triggers: gs, git-spice, stacked branches, stacked PRs, restack, upstack, downstack.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-A4-006 | Write a Python function that reverses a linked list. | NONE |  | clear | ok | |

## A6

Installed skills:

- **certificate-monitoring** (davepoon/buildwithclaude): Use when the user asks about SSL/TLS certificates, certificate expiration, monitoring domains for cert health, or issuing free Let's Encrypt certificates. Triggers include "is my cert expiring", "scan ssl on X", "check certificate", "monitor this domain", "issue a free cert", "renew certificate", "Let's Encrypt", "TLS Radar". This skill picks the right TLS Radar tool for each question.
- **ssl-certs** (KaiserWhoLearns/skillsbench): Manage SSL/TLS certificates and diagnose certificate issues. Use when the user says "cert expiring", "SSL error", "certificate problem", "renew certificate", "check certificate", "HTTPS not working", or asks about TLS/SSL.
- **leet-ssl-cert-create** (pengfeng/leet-ssl-cert-python): Issue an SSL/TLS certificate with leet-ssl-cert. Use when the user asks to create, issue, request, or renew a certificate for one or more domains. The only required input from the user is the domain name; everything else is loaded from .env defaults or sensible presets.
- **ssl-certificate-checker** (mcyork/skillseal-demo-plugin): Check SSL/TLS certificates on remote hosts using openssl s_client

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-A6-007 | What's the capital of Australia? | NONE |  | clear | ok | |

## A9

Installed skills:

- **string-database** (google-deepmind/science-skills): Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific proteins, interaction evidence, confidence scores, protein interaction partners, or pathway enrichments.
- **query-stringdb** (Runchuan-BU/BioClaw): Query STRING for protein-protein interactions. Use when user asks about protein interactions, interaction networks, binding partners, or interactome. Triggers on "string", "protein interaction", "interaction network", "binding partners", "interactome", "PPI".
- **string-ppi-enrichment** (InternScience/scp): Analyze protein-protein interaction enrichment using STRING database to identify functional networks and pathway associations.
- **lifesciences-proteomics** (donbr/lifesciences-deepagents): Queries protein databases (UniProt, STRING, BioGRID) via MCP tools for protein lookups, protein-protein interactions, functional enrichment analysis, and cross-database ID mapping. Falls back to curl when MCP is unavailable. This skill should be used when the user asks to "find protein interactions", "analyze interaction networks", "perform GO enrichment", "map protein IDs", or mentions PPI networks, UniProt accessions, STRING scores, BioGRID interactions, or protein ID conversion between databases.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-A9-008 | Explain how photosynthesis works. | NONE |  | clear | ok | |

## A12

Installed skills:

- **daily_briefing** (siddsachar/row-bot): Compile a morning briefing with weather, calendar, and news headlines.
- **morning** (tnez/dotfiles): Synthesize a morning briefing from GH notifications, calendar, reminders, and inbox.
- **start-the-day** (autonomy-cloud/kairos-interface): Get a personalized daily briefing with weather, news, and actionable insights
- **google_news** (0xmariowu/Autosearch): Current news headlines aggregated across publishers via Google News RSS (English US feed).

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-A12-009 | Convert 72 degrees Fahrenheit to Celsius. | NONE |  | clear | ok | |

## B1

Installed skills:

- **dca** (ourzora/zora-protocol): Dollar-cost-average into a chosen set of coins. On first invocation, collects the coin list, per-buy USD amount, optional caps, and which token to spend. Each subsequent invocation buys a fixed USD amount of every coin still under its cap.
- **whale-watcher** (ourzora/zora-protocol): Watch top holders and large trades on chosen coins, then alert or react. On first invocation, collects which coins to watch, the definition of a "whale" (top-N holders and/or a minimum USD trade size), the actions to take (alert, auto-sell on a top-holder dump, auto-buy on a whale entry), and any spend/sell caps. Each subsequent invocation polls holders and recent trades per coin, detects whale activity, and alerts and/or acts per config.
- **watchlist** (ourzora/zora-protocol): Track coins and alert when market cap thresholds are crossed. On first invocation, collects coins and alert conditions. Each subsequent invocation checks conditions and reports crossings.
- **trend-sniper** (ourzora/zora-protocol): Watch the global trending feed for new trend coins and snipe them during viral moments. On first invocation, collects a per-snipe budget, trigger rules (first appearance and/or 24h volume threshold), a spend cap, and an optional max market cap. Each subsequent invocation polls the trending feed and buys new qualifying trend coins.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-B1-002 | What is market capitalization and how is it calculated? | NONE |  | clear | ok | |

## B2

Installed skills:

- **hoyeon-specify** (team-attention/hoyeon): Hoyeon requirements workflow for Codex. Use when the user invokes "$hoyeon-specify" or wants to turn an unclear goal into structured requirements.md for Hoyeon. This adapter loads the canonical specify skill and follows its Codex runtime surface.
- **hoyeon-browser-work** (team-attention/hoyeon): Hoyeon browser automation workflow for Codex. Use when the user invokes "$hoyeon-browser-work" or asks Codex to perform a browser task through recon-first chromux automation. This adapter loads the canonical browser-work skill and follows its Codex runtime surface.
- **hoyeon-deep-research** (team-attention/hoyeon): Hoyeon deep research workflow for Codex. Use when the user invokes "$hoyeon-deep-research" or wants a multi-channel cited research report using web search, browser extraction, and optional Gemini. This adapter loads the canonical deep-research skill and follows its Codex runtime surface.
- **hoyeon-google-search** (team-attention/hoyeon): Hoyeon Google/chromux search workflow for Codex. Use when the user invokes "$hoyeon-google-search" or needs real-browser Google search, site-specific search, time filters, or body/comment enrichment. This adapter loads the canonical google-search skill and follows its Codex runtime surface.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-B2-012 | What is a good name for a pet goldfish? | NONE |  | clear | ok | |

## B3

Installed skills:

- **llmquant-events** (LLMQuant/skills): Router skill for LLMQuant event workflows. Use when the user needs earnings event briefs, M&A tracking, regulatory risk, catalysts, event calendars, or cross-asset event impact.
- **llmquant-portfolio** (LLMQuant/skills): Router skill for LLMQuant portfolio workflows. Use when the user needs company profiles, thesis tracking, theme research, watchlist monitoring, or alert management.
- **llmquant-options** (LLMQuant/skills): Router skill for LLMQuant options workflows. Use when the user needs IV rank, option scoring, strategy construction, Greeks, P&L simulation, volatility surface, unusual activity, earnings IV crush, backtests, or hedges.
- **llmquant-prediction-markets** (LLMQuant/skills): Router skill for LLMQuant prediction-market workflows. Use when the user needs event odds, settlement criteria, probability gaps, cross-market pricing, or prediction-market arbitrage review.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-B3-010 | What is the difference between a stock and a bond? | NONE |  | clear | ok | |

## B7

Installed skills:

- **upgradeability** (PurpleAILAB/Vigilo): Auto-loaded by access-control-auditor agent during Phase 2. Provides detection patterns for: UUPS/Transparent/Beacon proxy vulnerabilities, storage collision, initialization issues, function selector clashing, upgrade authorization. Core artifact: Proxy Architecture Map.
- **access-control** (PurpleAILAB/Vigilo): Auto-loaded by access-control-auditor agent during Phase 2. Provides detection patterns for: missing modifiers, privilege escalation, tx.origin phishing, OR/AND logic errors, missing two-step transfer. Core artifact: Permission Matrix.
- **flashloan** (PurpleAILAB/Vigilo): Auto-loaded by flashloan-auditor agent during Phase 2. Provides detection patterns for: price manipulation, governance manipulation, collateral manipulation, reward manipulation, oracle manipulation via flash loans. Core artifact: Flash Loan Attack Flow diagram.
- **economic-attack** (PurpleAILAB/Vigilo): Auto-loaded by flashloan-auditor and defi-auditor agents during Phase 2. Provides detection patterns for: spot price manipulation, oracle staleness, short TWAP, donation attacks, slippage, flash loan governance. Core artifact: Price Flow Map.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-B7-011 | Explain what a hash function is. | NONE |  | clear | ok | |

## B10

Installed skills:

- **umbraco-granular-user-permissions** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement granular user permissions in Umbraco backoffice using official docs
- **umbraco-package-view** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement package views in Umbraco backoffice using official docs
- **umbraco-property-editor-schema** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement property editor schemas in Umbraco backoffice using official docs
- **umbraco-icons** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement custom icons in Umbraco backoffice using official docs

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-B10-013 | Draft a polite email declining a meeting invitation. | NONE |  | clear | ok | |

## C1

Installed skills:

- **fret-workstream-lifecycle** (Latias94/fret): This skill should be used when the user asks to "start a new workstream", "resume a fearless refactor lane", "record workstream progress", "split a narrow follow-on", or "close out a lane". Provides a lightweight workstream lifecycle for Fret: scaffold the right docs, keep lane state explicit, resume existing lanes with an assumptions-first evidence pass, attach repro/gate/evidence to each slice, and leave closeout notes without reopening scope by accident.
- **fret-mobile-real-device-debug** (Latias94/fret): This skill should be used when the user asks to "debug on real mobile devices", "run the smallest Android/iOS target", "verify Vulkan/Metal constraints", or "capture mobile diagnostics evidence". Provides a real-device workflow (Android + iOS) to reproduce issues, capture bundles, and archive evidence for ADRs/workstreams.
- **fret-boundary-checks** (Latias94/fret): This skill should be used when the user asks to "run layering checks", "verify crate boundaries", "prevent winit/wgpu leakage", or "refactor across crates safely". Provides a guardrail workflow (layering checks, forbidden-dep spot checks, drift reports) to keep contract crates portable during refactors.
- **fret-repo-orientation** (Latias94/fret): This skill should be used when the user asks to "find the right crate/layer", "locate entry points", "choose the smallest runnable target", or "get oriented in the Fret repo". Provides a navigation workflow to map an intent to the correct layer and pick the fastest runnable demo/harness to iterate.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-C1-004 | Rename the variable tmp to buffer throughout this file. | NONE |  | clear | ok | |

## C2

Installed skills:

- **indexing** (zilliztech/milvus-marketplace): Use when user needs to create collections, indexes in Milvus. Triggers on: indexing, collection, create index, HNSW, IVF, schema, Milvus collection, vector storage.
- **embedding** (zilliztech/milvus-marketplace): Use when user needs to convert text/images to vectors. Triggers on: embedding, vectorize, encode, text-to-vector, model selection, sentence-transformers, OpenAI embeddings, BGE, CLIP.
- **rag** (zilliztech/milvus-marketplace): Use when user wants to build RAG, Q&A system, or knowledge base with documents. Triggers on: RAG, retrieval augmented generation, Q&A system, knowledge base, document Q&A, chat with docs, ChatGPT for docs, LLM + retrieval, semantic search over documents, ground LLM with facts, reduce hallucination, enterprise search.
- **pilot** (zilliztech/milvus-marketplace): Use when user wants to build AI applications, data pipelines, or any development project. Triggers on: AI application, build, project, data, pipeline, API, service, backend, LLM, GPT, Claude, model. Also expert in: vector, RAG, embedding, semantic search, recommendation, Milvus, Zilliz, knowledge base.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-C2-014 | How do I center a div in CSS? | NONE |  | clear | ok | |

## C3

Installed skills:

- **qa-auth** (baddenboy12/GroundWork): Automated QA testing for authentication flows including Keycloak sign-in, sign-up, callback handling, and session management
- **qa-sites** (baddenboy12/GroundWork): Automated QA testing for site management including create, edit, delete, sidebar, location picker, and team deletion voting
- **qa-landing** (baddenboy12/GroundWork): Automated QA testing for the GroundWork landing page, hero section, pricing carousel, navigation, and responsive layout
- **qa-export** (baddenboy12/GroundWork): Automated QA testing for PDF, Excel, and CSV export features including themes, filters, tier gating, and download verification

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-C3-015 | Write a haiku about autumn. | NONE |  | clear | ok | |

## C5

Installed skills:

- **code-standards** (saitarrun/devforge-ai): This skill should be used when the user mentions keywords related to code-standards.
- **cloud-infra** (saitarrun/devforge-ai): This skill should be used when the user mentions keywords related to cloud-infra.
- **requirements** (saitarrun/devforge-ai): This skill should be used when the user asks to "write requirements", "create user stories", "define acceptance criteria", "decompose a feature", "analyze an issue", "write a PRD", "create user stories", "acceptance criteria", "roadmap", "feature spec", or discusses "INVEST" criteria, "ambiguity", or "story estimation".
- **code-review** (saitarrun/devforge-ai): This skill should be used when the user mentions keywords related to code-review.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-C5-016 | Translate 'good morning' into Spanish. | NONE |  | clear | ok | |

## D1

Installed skills:

- **release** (paperclipai/paperclip): Coordinate a full Paperclip release across engineering verification, npm, GitHub, smoke testing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss versioning.
- **release** (khulnasoft/TaskCore): Coordinate a full Taskcore release across engineering verification, npm, GitHub, smoke testing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss versioning.
- **release** (gancim/sprint): Coordinate a full Sprint release across engineering verification, npm, GitHub, smoke testing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss versioning.
- **release** (leoustc/teamclaw): Coordinate a full TeamClaw release across engineering verification, npm, GitHub, website publishing, and announcement follow-up. Use when leadership asks to ship a release, not merely to discuss version bumps.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-D1-003 | What version number should this release get: is it a minor or a patch bump? | NONE |  | clear | name:release, name:release, name:release, name:release | |

## D2

Installed skills:

- **apple-notes** (Bitterbot-AI/bitterbot-desktop): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Bitterbot to add a note, list notes, search notes, or manage note folders.
- **apple-notes** (Luzzer/Kraken): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks UAGENT to add a note, list notes, search notes, or manage note folders.
- **apple-notes** (spinabot/brigade): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Brigade to add a note, list notes, search notes, or manage note folders.
- **apple-notes** (0xKobold/0xkobolds): Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Kobold to add a note, list notes, search notes, or manage note folders.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-D2-017 | Summarize the plot of Hamlet. | NONE |  | clear | ok | |

## D3

Installed skills:

- **skill-creator** (BidingCC/BuildingAI): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **fsi-fa-skill-creator** (d-wwei/openclaw-financial-services): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **skill-creator** (giocld/dotifles): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends OpenCode capabilities with specialized knowledge, workflows, or tool integrations.
- **skill-creator** (caelis-labs/caelis): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Caelis agent capabilities with specialized knowledge, workflows, or tool integrations.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-D3-018 | Fix the off-by-one error in this loop. | NONE |  | clear | ok | |

## D4

Installed skills:

- **caveman-compress** (JuliusBrussee/caveman-code): Ultra-compressed communication mode (lite / full / ultra) that cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Use when the user requests "caveman mode", "less tokens", "be brief", or when output budget is tight.
- **caveman** (brendon-colburn/hs-skills-lesson): Ultra-compressed communication mode. Cuts token usage by ~75% by speaking like a smart caveman while keeping full technical accuracy. Use when the user says "caveman mode", "talk like caveman", "less tokens", or "be brief".
- **caveman** (JafarAbdi/myconfigs): Ultra-compressed communication mode. Cuts token usage ~75% by speaking like smart caveman while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "less tokens", "be brief", or when token efficiency is requested.
- **caveman** (kiran-capoor94/wizard): Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Use when user says "caveman", "caveman mode", "be terse", "minimal output", "drop the filler", "less tokens", or invokes /caveman.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-D4-019 | Explain in detail how DNS resolution works. | NONE |  | clear | ok | |

## D5

Installed skills:

- **slack** (understudy-ai/understudy): Use when you need to control Slack from Understudy via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
- **slack** (CodeAndCanvasLabs/Daemora): Use when you need to control Slack from Daemora via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
- **slack** (x402agent/NanoSolana): Use when you need to control Slack from NanoClawd via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
- **slack** (LuisvelMarketer/genome): Use when you need to control Slack from Genoma via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-D5-020 | Generate a random 10-character password. | NONE |  | clear | ok | |

## E1

Installed skills:

- **messageprotocol-core** (BIGSUNGG/DS_MessageProtocol): Maintain MessageProtocol runtime APIs in Source/MessageProtocol.Core: public message attributes, IMessageSerializable contracts, MessageSerializer registration and generic/object dispatch, MessageFlag, MessageCategory, and MessageId parsing. Use when working on runtime serialization or deserialization, registration/cache bugs, InvalidCastException or KeyNotFoundException paths, or public contract changes.
- **spec-guide** (esxr/product-wiki): Use when authoring a new Executable Implementation Spec (EIS) from a natural-language description. Triggers on "write an EIS", "create new EIS", "executable implementation spec", "/create-feature". Teaches the EIS file format, numbering, required sections, the grounding rule (must verify against src/ before writing), and the wiki-companion rule (summary under docs/wiki/eis/ plus index update).
- **hal-and-abstractions** (bhu-dev/crosspoint-todoist): Layering and abstraction discipline for the firmware. Use when touching storage, input, display, settings, i18n, or rendering, or any code that could reach into the SDK. Covers routing through the HAL (HalStorage / HalGPIO / HalDisplay) instead of raw SDK classes, MappedInputManager logical buttons instead of raw GPIO indices, UITheme/GUI for all rendering, the singleton macros, tr() for user-facing text, and where a new abstraction boundary belongs.
- **catalyst-changelog-sync** (avvale/aurora-catalyst-docs): Pull newly-archived openspec changes from the Aurora sibling repos, classify each one as PUBLISH or DISMISS against a user-facing-impact contract, draft bilingual changelog entries (EN + ES) for the ones that qualify, and persist every decision to the versioned registry. Supports dry-run and bidirectional manual override.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-E1-005 | Explain the difference between TCP and UDP. | NONE |  | clear | ok | |

## E4

Installed skills:

- **multi-specialist-review** (NickCrew/Claude-Cortex): User-triggered multi-agent code review. Spawns 3-5 parallel specialist sub-agents that read actual source files, runs mechanical citation verification, and synthesizes a single review artifact. Use for PR-level changes, multi-commit ranges, or security-sensitive work where single-turn review is insufficient.
- **anamnesis** (Wondermonger-daydreaming/claude-skills-library): Trace any concept to its deepest structural root in human thought, then map the genealogy of transformations forward.
- **project-hub-conventions** (wsagency/WS-Claude-marketplace): Conventions for WS Agency multi-repo project hubs (subfolder layout, project.yaml schema, CLAUDE.md cascade, .gitignore managed block, invoke-ai.sh contract). Use when creating, extending, or troubleshooting a `<project>-main` hub repo, or when asked about "project hub", "multi-repo", or `<name>-main` / `<name>-truth` repos.
- **runtime-continuity** (kingwangking/Software-Development-Methodology-and-Theory-Repository): Extract, compress, restore, and maintain an AI agent's current cognitive runtime state across chats, tasks, and project contexts. Use when the user wants to continue an effective collaboration style, migrate to a new chat, preserve task focus, summarize current working state, or avoid losing a shaped agent behavior.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-E4-021 | What is 17 times 23? | NONE |  | clear | ok | |

## E8

Installed skills:

- **local-dev-experience** (mcj-coder/agent-skills): Use this skill when establishing or refining local developer workflows (hooks, linting, formatting, validation) to prevent non-compliant changes from being committed or merged.
- **analyze-voice** (nathanvale/side-quest-marketplace-old): Analyze voice memo transcriptions, create notes with appropriate content, and return lightweight proposals. For resources (ideas, reflections), creates note with Layer 1 transcription. For meetings, extracts structured body content. Worker skill for triage orchestrator.
- **reins** (pastel-sketchbook/reins): Use the reins CLI to bootstrap and maintain AI-assisted development frameworks in any project. Covers init, update, rule system, analysis lenses, autopilot, and verification workflow. Use when initializing reins in a new project, updating managed files, managing language rule templates, generating analysis-lens concerns, or running the reins development workflow (TDD, Tidy First, layered rules).
- **xbrl** (modeled-information-format/research-harness-template): Render surviving findings (typically a regulatory-disclosure artifact) into an inline XBRL (iXBRL) document directly from the SOURCES. Tags facts with xbrli:context / xbrli:unit and taxonomy concepts inside a human-readable XHTML shell, anchored to the current SEC inline-XBRL taxonomy. Never built from a rendered report.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-E8-022 | Write a limerick about cats. | NONE |  | clear | ok | |

## E10

Installed skills:

- **kf-g-skill-naming-creation-organization-rules** (melumuccu/ai): Use this skill when creating, naming, renaming, or organizing skills in this repository. Always use it when you need to decide rules for skill directory names, propose names that follow the existing convention, organize skills so related entries stay close together, or distinguish local skills from external ones.
- **channel-adaptation** (syeda-hoorain-ali/crm-digital-fte-factory): Format agent responses according to channel-specific style guidelines before sending to customers. This skill should be used AFTER escalation-decision returns should_escalate=False and BEFORE calling send_response tool. Transforms raw response text into channel-appropriate format (Gmail: formal & thorough, WhatsApp: casual & rapid under 60 words, Web Form: direct & functional). Applies CloudStream CRM brand voice: empathetic, concise, proactive. Mandatory for EVERY customer response.
- **nav-map** (neonwatty/nav-map): Use when an agent needs to map, inspect, prototype, or verify an app workflow with NavMap. Covers workflow manifests, screenshots, HTML mockup surfaces, live route probes, auth-state-safe checks, agent context contracts, and nav-map.json generation.
- **tex-environment-check** (arivero/firstProof): Verify and document local TeX/LaTeX installations (especially BasicTeX on macOS) with smoke tests, package checks, and reproducibility notes. Use when you need to confirm whether LaTeX is available, diagnose engine-specific issues (for example LuaLaTeX cache paths), or generate a Markdown report for project setup docs.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-E10-023 | Sort this list of numbers: 5, 2, 9, 1. | NONE |  | clear | ok | |

## E13

Installed skills:

- **react-vite-workflow** (ZedZed34/Calories-Counter): Use this skill when adding pages, routes, components, or styles; running dev/build/lint/test commands; or navigating the project structure. Documents the full file tree, npm scripts, routing patterns, CSS conventions ("Neon Court" dark theme), and component conventions.
- **cliparr-logtape** (TechSquidTV/Cliparr): Use this skill when changing, reviewing, or adding Cliparr LogTape logging in frontend, server, shared helpers, or tests. Covers Cliparr category taxonomy, wide-event boundaries, flat dot-notated fields, context, redaction/noise rules, no-console enforcement, and validation for logging PRs.
- **task-driven-ai-dev** (zhaohuanke123/vanko-skill): Turn a repository into a task-driven AI delivery loop with durable planning artifacts, guarded single-task execution, progress logging, and validation gates. Use when Codex needs to bootstrap or operate workflows built around files like architecture.md, task.json, progress.txt, project-config.json, CLAUDE.md, AGENTS.md, or similar backlog-driven harnesses, especially when replacing shell-based automation with explicit subagent orchestration.
- **capture-slop** (vietbui1999ru/llm-wiki): Invoke after code review, a bug post-mortem, or a /diagnose session reveals a recurring AI failure pattern in this codebase. Writes to mistakes/slop-register.md and optionally updates CONTEXT.md.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-E13-024 | What is the boiling point of water at sea level? | NONE |  | clear | ok | |

## E14

Installed skills:

- **autoopt** (ElliotDrel/Universal-Spell-Check): Autonomous Karpathy-style optimization loop for Universal Spell Check. Runs N iterations in an isolated git worktree on a dedicated branch, each iteration proposing one src/ change, building, running a low-call speed bench, verifying correctness, and committing or reverting based on confirmed request_ms improvement. Use when the user wants to autonomously optimize app speed, run autoopt, run an optimization loop, or improve performance over many iterations.
- **recursive-residual-reasoning** (zccz14/R3): Use this skill when a task involves hard reasoning, unclear causes, unexplained observations, failed hypotheses, ambiguous diagnoses, complex systems, emergent behavior, investigation planning, or any situation where the current explanation space is incomplete. This skill applies Recursive Residual Reasoning: preserve what cannot yet be explained as an explicit residual, expand that residual into the next reasoning space, and produce a traceable path from observation to conclusion, action, or bounded stop reason.
- **git-wrap-up** (rakaar/ddm_data): Standard repository wrap-up workflow for Codex. Use when the user says "git wrap up", asks to follow CODEX_GIT_WRAPUP.md, or otherwise asks Codex to inspect the current git worktree, document new or changed files, commit intended changes, and push to origin/main.
- **go-modern** (vocdoni/skills): Use this skill when writing, reviewing, or refactoring Go code. Detects the project's Go version from go.mod and applies only language features available in that version - modern built-ins like slices/maps/cmp, type-safe atomics, errors.Join, range-over-int, t.Context(), omitzero, b.Loop(), strings.SplitSeq, wg.Go(), new(val), errors.AsType. Avoids both outdated patterns and features from newer-than-target versions.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| N-E14-025 | List three prime numbers greater than 50. | NONE |  | clear | ok | |

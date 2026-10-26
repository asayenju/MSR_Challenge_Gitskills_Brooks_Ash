# B. Same-pack siblings: review sheet

Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.

Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.


## B1

Installed skills:

- **dca** (ourzora/zora-protocol): Dollar-cost-average into a chosen set of coins. On first invocation, collects the coin list, per-buy USD amount, optional caps, and which token to spend. Each subsequent invocation buys a fixed USD amount of every coin still under its cap.
- **whale-watcher** (ourzora/zora-protocol): Watch top holders and large trades on chosen coins, then alert or react. On first invocation, collects which coins to watch, the definition of a "whale" (top-N holders and/or a minimum USD trade size), the actions to take (alert, auto-sell on a top-holder dump, auto-buy on a whale entry), and any spend/sell caps. Each subsequent invocation polls holders and recent trades per coin, detects whale activity, and alerts and/or acts per config.
- **watchlist** (ourzora/zora-protocol): Track coins and alert when market cap thresholds are crossed. On first invocation, collects coins and alert conditions. Each subsequent invocation checks conditions and reports crossings.
- **trend-sniper** (ourzora/zora-protocol): Watch the global trending feed for new trend coins and snipe them during viral moments. On first invocation, collects a per-snipe budget, trigger rules (first appearance and/or 24h volume threshold), a spend cap, and an optional max market cap. Each subsequent invocation polls the trending feed and buys new qualifying trend coins.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B1-001 | Put $25 into each of these five coins every week, but stop topping up any coin once it hits its limit. | dca |  | clear | ok | |
| B-B1-002 | Notify me when a large holder dumps a coin I'm following, and sell my position automatically if it happens. | whale-watcher |  | clear | ok | |
| B-B1-003 | Let me know whenever any coin I'm following passes a $10M market cap. | watchlist |  | boundary | ok | |
| B-B1-004 | Whenever a brand-new coin starts going viral, buy a small amount of it for me right away, within a fixed budget. | trend-sniper |  | boundary | ok | |

## B2

Installed skills:

- **hoyeon-specify** (team-attention/hoyeon): Hoyeon requirements workflow for Codex. Use when the user invokes "$hoyeon-specify" or wants to turn an unclear goal into structured requirements.md for Hoyeon. This adapter loads the canonical specify skill and follows its Codex runtime surface.
- **hoyeon-browser-work** (team-attention/hoyeon): Hoyeon browser automation workflow for Codex. Use when the user invokes "$hoyeon-browser-work" or asks Codex to perform a browser task through recon-first chromux automation. This adapter loads the canonical browser-work skill and follows its Codex runtime surface.
- **hoyeon-deep-research** (team-attention/hoyeon): Hoyeon deep research workflow for Codex. Use when the user invokes "$hoyeon-deep-research" or wants a multi-channel cited research report using web search, browser extraction, and optional Gemini. This adapter loads the canonical deep-research skill and follows its Codex runtime surface.
- **hoyeon-google-search** (team-attention/hoyeon): Hoyeon Google/chromux search workflow for Codex. Use when the user invokes "$hoyeon-google-search" or needs real-browser Google search, site-specific search, time filters, or body/comment enrichment. This adapter loads the canonical google-search skill and follows its Codex runtime surface.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B2-005 | My goal is still fuzzy. Turn it into a structured requirements document for the project. | hoyeon-specify |  | boundary | ok | |
| B-B2-006 | Go to the vendor portal, log in, and download last month's invoices by driving the browser step by step. | hoyeon-browser-work |  | clear | ok | |
| B-B2-007 | Research the state of solid-state batteries and give me a cited report pulling from several channels. | hoyeon-deep-research |  | clear | ok | |
| B-B2-008 | Run a real Google search for this error message restricted to the past week, and pull the comments from the top results. | hoyeon-google-search |  | boundary | ok | |

## B3

Installed skills:

- **llmquant-events** (LLMQuant/skills): Router skill for LLMQuant event workflows. Use when the user needs earnings event briefs, M&A tracking, regulatory risk, catalysts, event calendars, or cross-asset event impact.
- **llmquant-portfolio** (LLMQuant/skills): Router skill for LLMQuant portfolio workflows. Use when the user needs company profiles, thesis tracking, theme research, watchlist monitoring, or alert management.
- **llmquant-options** (LLMQuant/skills): Router skill for LLMQuant options workflows. Use when the user needs IV rank, option scoring, strategy construction, Greeks, P&L simulation, volatility surface, unusual activity, earnings IV crush, backtests, or hedges.
- **llmquant-prediction-markets** (LLMQuant/skills): Router skill for LLMQuant prediction-market workflows. Use when the user needs event odds, settlement criteria, probability gaps, cross-market pricing, or prediction-market arbitrage review.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B3-009 | Give me an earnings brief for next week's reporting season and flag any regulatory risk to the catalysts. | llmquant-events |  | clear | ok | |
| B-B3-010 | Track my thesis on this company and alert me if anything on my watchlist changes. | llmquant-portfolio |  | clear | ok | |
| B-B3-011 | What's the IV rank on this ticker, and how would an earnings IV crush hit a straddle? | llmquant-options |  | clear | ok | |
| B-B3-012 | Compare the odds on this election outcome across two prediction markets and see if there's a probability gap to arbitrage. | llmquant-prediction-markets |  | boundary | ok | |

## B4

Installed skills:

- **kotlin-rules** (softspark/ai-toolkit): Kotlin coding rules: style, patterns, security, testing. Triggers: .kt, .kts, build.gradle.kts, Ktor, Jetpack Compose, coroutines, kotlinx.
- **cpp-rules** (softspark/ai-toolkit): C++ coding rules: style, patterns, security, testing. Triggers: .cpp, .cc, .cxx, .hpp, .h, CMakeLists.txt, Makefile, GoogleTest, clang-tidy.
- **python-rules** (softspark/ai-toolkit): Python coding rules: style, patterns, security, testing. Triggers: .py, .pyi, pyproject.toml, requirements.txt, Pipfile, FastAPI, Django, Flask, pytest, SQLAlchemy, ruff, mypy.
- **rust-rules** (softspark/ai-toolkit): Rust coding rules: style, patterns, security, testing. Triggers: .rs, Cargo.toml, Cargo.lock, Tokio, Axum, Serde, clippy, cargo test.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B4-013 | Review my Ktor handler's coroutine usage against our coding standards. | kotlin-rules |  | clear | ok | |
| B-B4-014 | Check my CMakeLists.txt and the new .hpp for style and security problems. | cpp-rules |  | clear | ok | |
| B-B4-015 | Does my FastAPI service and its pytest suite follow our house conventions? | python-rules |  | clear | ok | |
| B-B4-016 | Review my Axum handlers and the Tokio code for style issues clippy would flag. | rust-rules |  | clear | ok | |

## B5

Installed skills:

- **bpx-ref** (wilddogjp/openbpx): BPX `ref` command skill. Bulk-rewrite reference strings in NameMap and decoded properties.
- **bpx-write** (wilddogjp/openbpx): BPX `write` command skill. Rewrite a parsed package to a separate output path.
- **bpx-class** (wilddogjp/openbpx): BPX `class` command skill. Inspect one class export payload/header by index.
- **bpx-package** (wilddogjp/openbpx): BPX `package` command skill. Inspect package metadata/sections or update package flags.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B5-017 | Bulk-rewrite every reference string in the NameMap and the decoded properties of this BPX package. | bpx-ref |  | clear | ok | |
| B-B5-018 | Rewrite the parsed BPX package out to a different output path. | bpx-write |  | clear | ok | |
| B-B5-019 | Look at the class export at index 3 in this BPX file and show me its header. | bpx-class |  | clear | ok | |
| B-B5-020 | Show the metadata and sections of this BPX package and flip one of its flags. | bpx-package |  | boundary | ok | |

## B6

Installed skills:

- **zoom-webhooks** (hookdeck/webhook-skills): Receive and verify Zoom webhooks. Use when setting up Zoom webhook handlers, debugging signature verification, completing the endpoint.url_validation handshake, or handling meeting and recording events like meeting.started, meeting.ended, meeting.participant_joined, or recording.completed.
- **elevenlabs-webhooks** (hookdeck/webhook-skills): Receive and verify ElevenLabs webhooks. Use when setting up ElevenLabs webhook handlers, debugging signature verification, or handling call transcription events.
- **vercel-webhooks** (hookdeck/webhook-skills): Receive and verify Vercel webhooks. Use when setting up Vercel webhook handlers, debugging signature verification, or handling deployment events like deployment.created, deployment.succeeded, or project.created.
- **mailgun-webhooks** (hookdeck/webhook-skills): Receive and verify Mailgun webhooks. Use when setting up Mailgun webhook handlers, debugging Mailgun signature verification, or handling email events like delivered, failed, opened, clicked, unsubscribed, and complained.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B6-021 | Set up a handler for meeting.ended events and complete the endpoint URL validation handshake. | zoom-webhooks |  | clear | 4gram:endpoint url validation handshake | |
| B-B6-022 | Verify the signature on incoming call-transcription webhooks from ElevenLabs. | elevenlabs-webhooks |  | clear | ok | |
| B-B6-023 | Handle the deployment-succeeded events Vercel sends to my endpoint. | vercel-webhooks |  | clear | ok | |
| B-B6-024 | Process Mailgun's delivered, failed and complained email events in my webhook. | mailgun-webhooks |  | clear | ok | |

## B7

Installed skills:

- **upgradeability** (PurpleAILAB/Vigilo): Auto-loaded by access-control-auditor agent during Phase 2. Provides detection patterns for: UUPS/Transparent/Beacon proxy vulnerabilities, storage collision, initialization issues, function selector clashing, upgrade authorization. Core artifact: Proxy Architecture Map.
- **access-control** (PurpleAILAB/Vigilo): Auto-loaded by access-control-auditor agent during Phase 2. Provides detection patterns for: missing modifiers, privilege escalation, tx.origin phishing, OR/AND logic errors, missing two-step transfer. Core artifact: Permission Matrix.
- **flashloan** (PurpleAILAB/Vigilo): Auto-loaded by flashloan-auditor agent during Phase 2. Provides detection patterns for: price manipulation, governance manipulation, collateral manipulation, reward manipulation, oracle manipulation via flash loans. Core artifact: Flash Loan Attack Flow diagram.
- **economic-attack** (PurpleAILAB/Vigilo): Auto-loaded by flashloan-auditor and defi-auditor agents during Phase 2. Provides detection patterns for: spot price manipulation, oracle staleness, short TWAP, donation attacks, slippage, flash loan governance. Core artifact: Price Flow Map.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B7-025 | Audit this proxy contract for storage collisions and weak upgrade authorization. | upgradeability |  | clear | ok | |
| B-B7-026 | Does this contract have missing modifiers or a tx.origin phishing path? | access-control |  | clear | ok | |
| B-B7-027 | Could someone borrow a flash loan to swing a governance vote or inflate the rewards in this protocol? | flashloan | economic-attack | boundary | ok | |
| B-B7-028 | Check whether this lending pool is exposed to a stale oracle, a short TWAP or a donation attack. | economic-attack | flashloan | boundary | ok | |

## B8

Installed skills:

- **aave-v3-liquidation-watcher-teneo** (TeneoProtocolAI/teneo-skills): AI agent for Aave V3 Liquidation Watcher via Teneo Protocol. Use this skill when the user needs Aave V3 Liquidation Watcher via the bundled Teneo CLI and you need the live commands, arguments, or pricing before execution.
- **vc-attention-teneo** (TeneoProtocolAI/teneo-skills): AI agent for VC Attention via Teneo Protocol. Use this skill when the user needs VC Attention via the bundled Teneo CLI and you need the live commands, arguments, or pricing before execution.
- **squid-router-teneo** (TeneoProtocolAI/teneo-skills): AI agent for Squid Router via Teneo Protocol. Use this skill when the user needs Squid Router via the bundled Teneo CLI and you need the live commands, arguments, or pricing before execution.
- **predexon-prediction-market-agent-1-5-teneo** (TeneoProtocolAI/teneo-skills): AI agent for Predexon Prediction Market Agent 1.5 via Teneo Protocol. Use this skill when the user needs Predexon Prediction Market Agent 1.5 via the bundled Teneo CLI and you need the live commands, arguments, or pricing before execution.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B8-029 | Use the Teneo CLI to check which Aave V3 positions are close to liquidation, and tell me the price first. | aave-v3-liquidation-watcher-teneo |  | clear | ok | |
| B-B8-030 | Using Teneo, show me how much attention venture investors are giving to this project. | vc-attention-teneo |  | clear | ok | |
| B-B8-031 | Through the Teneo CLI, route a cross-chain swap using Squid Router. | squid-router-teneo |  | clear | ok | |
| B-B8-032 | Use Teneo to query the Predexon prediction market agent and show me its commands. | predexon-prediction-market-agent-1-5-teneo |  | clear | 4gram:predexon prediction market agent | |

## B9

Installed skills:

- **integration-python** (amplitude/wizard): Amplitude integration for any Python application using the amplitude-analytics package
- **integration-ruby** (amplitude/wizard): Amplitude integration for any Ruby application using the amplitude-api gem
- **integration-javascript_web** (amplitude/wizard): Amplitude integration for client-side web JavaScript applications using @amplitude/unified (or @amplitude/analytics-browser for existing projects)
- **integration-android** (amplitude/wizard): Amplitude integration for Android applications using the Kotlin SDK

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B9-033 | Add product analytics to my Flask app with Amplitude. | integration-python |  | clear | ok | |
| B-B9-034 | Instrument my Rails app with Amplitude events. | integration-ruby |  | clear | ok | |
| B-B9-035 | Add Amplitude tracking to our browser-based web client. | integration-javascript_web |  | clear | ok | |
| B-B9-036 | Wire Amplitude into our Android app written in Kotlin. | integration-android |  | clear | ok | |

## B10

Installed skills:

- **umbraco-granular-user-permissions** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement granular user permissions in Umbraco backoffice using official docs
- **umbraco-package-view** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement package views in Umbraco backoffice using official docs
- **umbraco-property-editor-schema** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement property editor schemas in Umbraco backoffice using official docs
- **umbraco-icons** (umbraco/Umbraco-CMS-Backoffice-Skills): Implement custom icons in Umbraco backoffice using official docs

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B10-037 | Implement fine-grained permissions for backoffice users in Umbraco. | umbraco-granular-user-permissions |  | clear | ok | |
| B-B10-038 | Add a custom package view to the Umbraco backoffice. | umbraco-package-view |  | clear | ok | |
| B-B10-039 | Define a schema for a new property editor in Umbraco's backoffice. | umbraco-property-editor-schema |  | clear | ok | |
| B-B10-040 | Register my own custom icons in the Umbraco backoffice. | umbraco-icons |  | clear | ok | |

## B11

Installed skills:

- **canopy-brand-icon** (Legal-and-General/canopy): Removal notice for the Canopy Brand Icon component. Trigger whenever lg-brand-icon, LgBrandIconComponent, or brand icon imports appear in an Angular project using Canopy.
- **canopy-carousel** (Legal-and-General/canopy): Deprecation notice for the Canopy Carousel component. Trigger whenever lg-carousel, LgCarouselComponent, LgCarouselItemComponent, or LgAutoplayComponent appear in an Angular project using Canopy.
- **canopy-link** (Legal-and-General/canopy): Best practices for Canopy link styles. Trigger when using anchor tags, links with icons, external links, or the lg-unstyled-link class in an Angular project using Canopy.
- **canopy-filter-container** (Legal-and-General/canopy): Best practices for the Canopy Filter Container pattern. Trigger when adding an expandable filter panel with a toggle button and filter controls in an Angular project using Canopy.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B11-041 | My Angular Canopy app still imports LgBrandIconComponent. What should happen to it? | canopy-brand-icon |  | clear | ok | |
| B-B11-042 | I'm using lg-carousel with LgAutoplayComponent in our Canopy app. Is that still okay? | canopy-carousel |  | clear | ok | |
| B-B11-043 | What's the recommended way to style external links with icons in our Canopy Angular app? | canopy-link |  | clear | ok | |
| B-B11-044 | I'm adding an expandable filter panel with a toggle button to our Canopy Angular app. How should I structure it? | canopy-filter-container |  | clear | 4gram:adding an expandable filter | |

## B12

Installed skills:

- **filter** (sdemyanov/retriever): This skill should be used when the user types "/filter", "/filter ...", or "/filter clear". It exposes Retriever's visible slash-command surface for SQL-like filter refinement.
- **from-run** (sdemyanov/retriever): This skill should be used when the user types "/from-run", "/from-run 42", or "/from-run clear". It exposes Retriever's visible slash-command surface for scoping results to a processing run.
- **sort** (sdemyanov/retriever): This skill should be used when the user types "/sort", "/sort list", "/sort date_created desc", "/sort date_created desc, file_name asc", or "/sort default". It exposes Retriever's visible slash-command surface for sort inspection and changes.
- **scope** (sdemyanov/retriever): This skill should be used when the user types "/scope", "/scope list", "/scope clear", "/scope save ...", or "/scope load ...". It exposes Retriever's visible slash-command surface for inspecting and managing the active scope.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| B-B12-045 | Narrow the retrieved documents down to only those where the file type is PDF. | filter |  | boundary | ok | |
| B-B12-046 | Limit the results to what came out of processing run 42. | from-run |  | boundary | ok | |
| B-B12-047 | Order the results by creation date, newest first, then by file name. | sort |  | boundary | ok | |
| B-B12-048 | Save my current scope under a name so I can load it again tomorrow. | scope | filter | boundary | name:scope | |

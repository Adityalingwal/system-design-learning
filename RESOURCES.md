# System Design Resources

Checked on 2026-10-12 (research gap-check: Claude + Codex, web-verified). Paid ko 💰 se mark kiya hai, baaki free.

## Books

- 💰 [_Designing Data-Intensive Applications_, 2nd ed. — Martin Kleppmann, Chris Riccomini (O'Reilly, 2026)](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
  "Andar se kyun aise chalta hai" wali book. Use for: Sections 2, 4, 5 ki depth. Chapters: 1-2 trade-offs + NFRs (Sec 7, 10, 12) · 3-4 data models + storage (Sec 2, 13) · 5 encoding & evolution (Sec 1) · 6 replication · 7 sharding · 8 transactions (Sec 2) · 9-10 distributed dikkatein, consistency, consensus (Sec 5) · 11-13 batch + stream (Sec 4, 11A). Ch 14 (ethics) skip.
- 💰 [_Understanding Distributed Systems_, 2nd ed. — Roberto Vitillo (2022)](https://understandingdistributed.systems/)
  DDIA se halki, practical. Use for: load balancing, timeouts, load shedding, microservices, observability. [Free sample](https://understandingdistributed.systems/sample.pdf).
- 💰 [_System Design Interview_ Vol 1 — Alex Xu (2020)](https://blog.bytebytego.com/p/system-design-interview-books-volume) · Vol 2 — Alex Xu, Sahn Lam (2022)
  HLD practice problems ke worked designs. Vol 1: rate limiter, consistent hashing, KV store, ID generator, URL shortener, crawler, notification, feed, chat, autocomplete, YouTube, Drive. Vol 2: proximity, nearby friends, maps, message queue, metrics, ad-click, hotel, S3, leaderboard, payment, wallet. Same content [ByteByteGo course](https://bytebytego.com/courses/system-design-interview) pe bhi hai.
- 💰 [_Object Oriented Design Interview_ — Desmond Zhou, Fawaz Bokhari, Alex Xu (2025)](https://www.shroffpublishers.com/books/9789368086154/)
  LLD problems ke worked designs: parking lot, movie booking, file search, vending machine, elevator, locker, ATM, restaurant. Use for: Section 15B.
- 💰 [_Head First Design Patterns_, 2nd ed. — Eric Freeman, Elisabeth Robson (O'Reilly, 2020)](https://www.oreilly.com/library/view/head-first-design/9781492077992/)
  Patterns ko kahaniyon se samjhati hai. Use for: Section 14A.
- 💰 [_Designing Machine Learning Systems_ — Chip Huyen (O'Reilly, 2022)](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)
  Use for: Section 11A. Ch 4 training data · 5 features/leakage · 6 evaluation · 7 deployment · 8 drift · 9 continual learning · 10 MLOps. [Free chapter summaries](https://github.com/chiphuyen/dmls-book/blob/main/summary.md).
- 💰 [_AI Engineering_ — Chip Huyen (O'Reilly, Dec 2024)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)
  Tumhare role ki sabse important book. Use for: Section 11B. Ch 3-4 evals + model selection · 5 prompting/context · 6 RAG + agents + memory · 7 fine-tuning · 9 inference optimization · 10 architecture (guardrails, gateway, cache, observability, feedback). [Free ToC + resources](https://github.com/chiphuyen/aie-book).
- 💰 [_Machine Learning System Design Interview_ — Ali Aminian, Alex Xu (2023)](https://www.aliaminian.com/books)
  ML practice problems: visual search, ad-click, video recsys, PYMK, harmful content. Use for: Section 15C (ML wale).
- 💰 [_Generative AI System Design Interview_ — Ali Aminian, Hao Sheng (2024)](https://www.aliaminian.com/books)
  Use for: Section 15C. Kaam ke chapters: 1 framework, 2 Smart Compose, 4 ChatGPT, 6 RAG. Baaki image/video generation, scope se bahar.
- [_Site Reliability Engineering_ — Google (online)](https://sre.google/sre-book/table-of-contents/)
  Use for: Section 7. Ch 4 SLOs · 6 monitoring · 10 alerting · 19-20 load balancing · 21 overload · 22 cascading failures.

## Platforms & free guides

- [Hello Interview](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) (kuch hissa 💰)
  Sabse kaam ka free source. [Delivery framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery) (Sec 12), [core concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts), [key technologies](https://www.hellointerview.com/learn/system-design/in-a-hurry/key-technologies), [common patterns](https://www.hellointerview.com/learn/system-design/in-a-hurry/patterns), [problem breakdowns](https://www.hellointerview.com/learn/system-design/in-a-hurry/problem-breakdowns), [ML system design](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction), [LLD](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/delivery), [ChatGPT breakdown](https://www.hellointerview.com/learn/system-design/problem-breakdowns/chatgpt).
- [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer)
  Poore HLD ka free map. Use for: Sections 1-3, 13 ka quick overview.
- [ByteByteGo System Design 101 (GitHub)](https://github.com/ByteByteGoHq/system-design-101)
  Ek-ek concept ke diagrams. Use for: kisi topic ki 2-minute visual revision.
- [awesome-low-level-design (GitHub)](https://github.com/ashishps1/awesome-low-level-design)
  LLD problems + concurrency. Use for: Sections 14B, 15B.
- [refactoring.guru: design patterns](https://refactoring.guru/design-patterns/catalog)
  Har pattern Python example ke saath. Use for: Section 14A.
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/schedule.html)
  Poora course nahi. Use for: Raft paper + lecture, linearizability, "Memcached at Facebook" paper (Sec 3, 5).
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
  Use for: Sections 6, 7, 9 (reliability, cost, security pillars).
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
  Use for: SLO/SLI/error budget (Sec 7).

## AI / LLM specific (Section 11B)

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
  Agent workflow patterns (chaining, routing, orchestrator-workers). Use for: agent orchestration.
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Use for: context window management.
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
  Use for: agent evals (tool traces, task success).
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
  Use for: guardrails + AI security.
- [AWS: Secure multi-tenant RAG](https://aws.amazon.com/blogs/architecture/secure-multi-tenant-rag-with-amazon-bedrock-and-verified-permissions/)
  Use for: permission-aware retrieval.
- [Eugene Yan: Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/)
  Use for: evals, caching, guardrails, feedback ka overview.
- [Model Context Protocol docs](https://modelcontextprotocol.io/docs/getting-started/intro)
  Use for: MCP (awareness).

## Voice AI (Section 11B voice rows, 15C voice problems)

Checked on 2026-10-12 (Claude + Codex). Docs free hain; API usage alag paid. Vendor blogs ke numbers "starting point" samjho, universal SLO nahi.

- [Voice AI & Voice Agents: An Illustrated Primer — Kwindla Hultman Kramer (Daily/Pipecat)](https://voiceaiandvoiceagents.com/)
  Poore voice stack ka free "book": latency breakdown, S2S vs cascaded, WebRTC vs WebSocket, edge routing, turn detection, interruptions, evals, telephony, hosting + per-minute cost. Use for: 11B ki saari voice rows ka pehla read.
- [Twilio: A Guide to Core Latency in AI Voice Agents](https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents)
  Mouth-to-ear vs platform turn gap, per-stage latency targets, colocation, audio format pitfalls, fixed vs smart endpointing. Vendor blog. Use for: latency budget + inference placement.
- [OpenAI: Voice agents guide](https://developers.openai.com/api/docs/guides/voice-agents)
  3 architectures (full-duplex, Realtime S2S, chained) kab kya + voice evals aur audible latency measure karna. Use for: architecture choice + evals.
- [LiveKit Agents docs](https://docs.livekit.io/agents/) — khaas kar [server lifecycle](https://docs.livekit.io/agents/server/lifecycle/) aur [self-hosted deployments](https://docs.livekit.io/deploy/custom/deployments/)
  Job dispatch, process isolation, load threshold, drain, sizing. Use for: voice scaling, 15C designs.
- [LiveKit: Turns (turn detection + interruptions)](https://docs.livekit.io/agents/logic/turns/)
  Detection modes, endpointing delay, adaptive interruption / backchannel. Use for: turn-taking + barge-in.
- [WebRTC for the Curious](https://webrtcforthecurious.com/)
  Vendor-neutral, free WebRTC book; ch.8 mein mesh vs SFU vs MCU. Use for: Section 1 real-time media transport.
- [LiveKit Telephony docs](https://docs.livekit.io/telephony/) + [LiveKit AMD blog](https://livekit.com/blog/answering-machine-detection)
  SIP trunks, dispatch rules, DTMF, cold vs warm transfer, voicemail detection. Use for: telephony call flow, 15C call-center.
- [Pipecat docs](https://docs.pipecat.ai/) — [Evals](https://docs.pipecat.ai/pipecat/evals/overview), [Metrics](https://docs.pipecat.ai/pipecat/fundamentals/metrics)
  Frame-pipeline model; simulated callers, text vs audio mode, barge-in tests; TTFB/TTFA metrics. Use for: evals + streaming.
- [OpenAI Cookbook: Realtime eval guide](https://developers.openai.com/cookbook/examples/realtime_eval_guide)
  Crawl / walk / run eval plan, layered graders, production failures → regression set. Use for: voice evals, 15C eval harness.
- [Hamming: How to Evaluate Voice Agents](https://hamming.ai/resources/how-to-evaluate-voice-agents)
  Task success, containment, barge-in recovery, P50/P95, WER + alert thresholds. Vendor content. Use for: voice evals + Section 7.

**Apna voice material:** `local/voice-material.md` (gitignored — sirf is Mac pe).

## Section → kahan se padhna (quick map)

| Section | Pehla resource | Depth ke liye |
|---|---|---|
| 1 Networking | Hello Interview core concepts | Vitillo Part I |
| 2 Databases | Hello Interview (data modeling, indexing, sharding) | DDIA ch 3-8 |
| 3 Caching | Hello Interview caching | DDIA, Memcached paper |
| 4 Queues | Hello Interview Kafka deep-dive | DDIA ch 11-13 |
| 5 Distributed core | Vitillo Part II + IV | DDIA ch 9-10, MIT Raft |
| 6 Architecture | Hello Interview patterns | Vitillo, AWS Well-Architected |
| 7 Reliability | Google SRE book (ch 4, 6, 21, 22) | AWS Well-Architected |
| 8 Security | OWASP LLM Top 10 (AI angle) | AWS multi-tenant RAG |
| 9 Cloud | AWS Well-Architected | — |
| 10 Performance | DDIA ch 2 (percentiles) | AI Engineering ch 9 |
| 11A ML | Hello Interview ML | Designing ML Systems |
| 11B LLM/AI | AI Engineering | Anthropic posts |
| 11B Voice AI | Voice AI primer | Twilio latency guide, LiveKit + Pipecat docs |
| 12 Design process | Hello Interview delivery | Alex Xu Vol 1 (framework chapter) |
| 13 Special storage | System Design Primer | Hello Interview deep-dives |
| 14 LLD | refactoring.guru, Head First | awesome-low-level-design |
| 15 Practice | Hello Interview breakdowns, Alex Xu | OOD Interview, GenAI SDI |

## Gaps

- Communities (Reddit, Discord, mock-interview groups) abhi research nahi kiye.
- Achhi YouTube videos/channels abhi nahi chuni — lesson banate waqt dhoondh ke `/teach-video` se padhenge.

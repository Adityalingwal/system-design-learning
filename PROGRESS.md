# Progress

Order: `system-design-list.md` → "Order" section. Update at the end of every session.

## Now
- **Weekday track:** P0 · Design Process (12) + back-of-envelope estimation — in progress. Lesson 0001 (standard flow + requirements) 12 Oct 2026: chat mein section-by-section padha, **recall pass** (6 steps, FR vs NFR, NFR ke 4 parts). Baaki: 🟢 practice, **role-play format** (Aditya ka idea): Claude non-technical business owner banta hai, Aditya senior engineer ban ke sawaal poochhta hai aur `designs/01-...md` (English) mein requirements likhta hai; beech mein Claude nayi constraint daalta hai; end mein Claude role se bahar aake review karta hai. **Timing (Aditya ka faisla, 12 Oct 2026):** pehle P0 ke saare 9 topics ki theory, phir end mein ek saath role-play + poora design doc. Beech mein har session ka recall quiz chalta rahega taaki purane topics na bhoolein. Agla theory topic: trade-off reasoning, phir baaki P0 (bottleneck, failure thinking, 10x, YAGNI, design doc, estimation lesson: Little's Law + peak-hour math step by step, verified "numbers to know").
- **Trade-off reasoning (🟢):** theory done 12 Oct 2026 16:55. Final format Aditya ne khud jod ke banaya: X over Y · because Z (saboot) · downside W · mitigation M · revisit trigger. Practice P0-end design doc mein.
- **Bottleneck pehchanna (🟢):** theory done 12 Oct 2026 (2 symptoms latency/capacity, kai causes; AI mein 4 lens: latency, capacity, cost, quality; bottleneck hilta hai; design time pe 3 sawaal).
- **Failure thinking (🟢):** theory done 12 Oct 2026 (3 sawaal: band/dheema/galat → blast radius → detect + respond; 6 tools; galat sabse khatarnaak; idempotency ka sirf naam).
- **10x + YAGNI (🟡🟡):** theory done 13 Oct 2026 (10x tak taiyaari, 100x pe redesign maan ke chalo; "baad mein kitna mehenga?" test; sasta darwaza abhi (wrapper), mehengi building baad mein (routing); revisit trigger limit se pehle).
- **Back-of-envelope estimation (🟢):** theory done 13 Oct 2026 (tools: din ≈ 1 lakh s, units ×1000, peak guna; Little's Law; storage: bitrate × s ÷ 8; audio basics: sample rate, codec, G.711 vs Opus; cost per call + LLM tokens + caching; latency numbers; QPS; bandwidth; ×10 check). Pehle overwhelm hua jab ek message mein 5 nayi cheezein thi → chhote tukde (A/B/C/D) se clear hua.
- **Design doc likhna (🟢):** theory done 13 Oct 2026 (kya/kyun, kab likhna: faisla bhaari ho tab — size nahi; 11 sections; achhe doc ke 6 rules; kamzori 3 jagah: downside, failure modes, open questions; open question = owner + blocker/non-blocker + default + recommendation). Template: `reference/design-doc-template.md`.
- **P0 theory: 9/9 complete (13 Oct 2026).** Practice baaki.
- **Next session (13 Oct ~8-9 PM, nayi chat):** (1) recall quiz — REVIEW.md ke saare due items, ek-ek karke; (2) role-play: Claude non-technical client/founder, Aditya senior engineer, requirements nikale; (3) Aditya `designs/01-<voice-system>.md` English mein template se likhe, Claude review kare (2-3 sabse badi gaps). Practice pass hone pe P0 ke 🟢 topics "Done" table mein jaayenge.
- **Note:** `lessons/0001-design-process-requirements.html` purana hai (chat se pehle ka, overwhelming laga tha); asli padhai chat mein hui. Baad mein ek short summary page se replace karna hai, Aditya se poochh ke.
- **Reference banaye:** `reference/quality-checklist.md` (ISO 25010 ke 9 groups + voice examples) · `reference/design-doc-template.md` (11 sections + submit checklist).
- **Sunday track:** 14A · OOP basics — not started
- **Next design-doc milestone:** after P2 → URL Shortener

## Session log (IST)
| Date | Time | Kya hua |
|---|---|---|
| 2026-10-12 (Mon) | start note nahi hua → 21:58 | Lesson 0001 chat mein section-by-section, recall pass, quality checklist bana, teaching style + model (Opus) lock; trade-off reasoning, bottleneck, failure thinking ki theory |
| 2026-10-13 (Tue) | subah (start note nahi hua) → 16:45 | 10x + YAGNI, estimation (poora), design doc theory → P0 theory 9/9. Recall quiz Aditya ke kehne pe raat 8-9 PM ki nayi chat tak taala |

## Done
| Date | Topic | Section | Tag | How proven |
|---|---|---|---|---|

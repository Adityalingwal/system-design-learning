# P0 hard mode: applies concepts well, definitions and memorised numbers still slip

In the hard-mode revision (all 21 P0 items, English definition + why + apply to a new voice case), Aditya applied concepts correctly on new scenarios far more often than he could state them cold. He found the capacity bottleneck and the next one after a fix, saw that one shared API key puts all clinics in the blast radius, chose `clinic_id` now via the YAGNI cost test, picked Little's Law vs QPS correctly, and fixed his old misconception (multi-turn LLM cost is driven by input tokens). Bare definitions, hooks and memorised numbers were weaker.

**Evidence:** chat quiz, 20 Oct 13:47 → 22 Oct 23:21 IST, 39 questions.

**Misconceptions corrected:**
- Bottleneck = single point of failure (fixed: bottleneck = slow, SPOF = stop / no backup).
- Wrote "functional requirement … how well" twice — FR/NFR labels swap under pressure.
- Wrote FRs and scopes as builder tasks ("build a dashboard") instead of actor capabilities.
- Bits → bytes by ×8 instead of ÷8.
- "Browser audio has no sample rate"; G.711 guessed as 16 kHz.
- Little's Law = "peak = average × 2-3" (mixed with peak factor).
- Copied the speed NFR's condition ("past bookings") onto a reliability NFR.
- Latency: RAM ~500 ns, same-DC ~300 ms (real: 100 ns, 0.5 ms).

**Implications:**
- He asks for notes-ready **model answers in Q/A form**, generic phrasing, no ambiguous words ("client" was ambiguous; repeated "how" bothered him) — precision of wording matters to him; review blocks before sending.
- Mental math stalls on multi-digit steps; give the order-of-operations trick (÷8 first, 1 day ≈ 1 lakh s) rather than the result.
- Next practice should be generative (role-play + design doc), where he is strongest; keep short daily recall for the slipping definitions and numbers.

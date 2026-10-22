# P0 recall: examples and methods stick, flat lists and names do not

First recall quiz on all 21 P0 items (14 Oct 2026, 1-2 days after learning) went poorly on lists and names but well on worked examples and methods. He could rebuild things he had *used* — the LLM-wrapper YAGNI example, LLM as the pipeline bottleneck, `128 × 60 ÷ 8` for storage, Little's Law from a concrete example (10 calls/min × 3 min → 30) — but blanked on enumerations: the 6 failure tools, the 3 requirement buckets, the 4 NFR parts, "revisit trigger", "evidence" in the trade-off format, the 3 bottleneck questions.

**Evidence:** quiz in chat, 14 Oct 2026 23:14 → 15 Oct 00:22 IST. Solid: estimation-only-when-it-changes-design, peak not average, 10x/100x, storage formula, bits vs bytes, G.711 64 kbps / Opus. Misconception: thought output tokens drive multi-turn LLM cost (it is input — prompt + history resent every turn).

**Implications:**
- Turn every list into a hook or a short story before quizzing it ("Slowest, Smallest, Single"; "Down, Slow, Wrong"; the 6 tools as one call-failure story). Let him pick the final hook.
- Quiz one thing per question; when he blanks, give a concrete example to compute from instead of the answer — that recovered Little's Law and the day-in-seconds fact.
- Always give the English term and an English sentence pattern next to the Hinglish hook; he has to explain these in English.
- Knowing the 4 NFR parts is not the same as writing one: "calls sometimes missing" was written as a latency NFR. Practise turning complaints into NFRs (pick the quality first).

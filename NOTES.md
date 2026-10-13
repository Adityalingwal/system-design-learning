# Notes

## Decisions

- GitHub repo: **public** rakhna hai (decided 12 Oct 2026). Publish tab, jab folder structure + seekhne ka tarika set ho jaye; push se pehle Aditya ki final haan.
- Order: Option A — Mon–Sat HLD, Sunday LLD coding (details: system-design-list.md).
- Research gap-check (Claude + Codex, 12 Oct 2026) apply ho chuka: gaps → `system-design-list.md` (🔍 marker), resources + books → `RESOURCES.md`, raw reports delete.

## Senior level pe kya expect hota hai (system design round)

Source: [Meta interview guide](https://d3no4ktch0fdq4.cloudfront.net/public/course/files/SWE_engineering_leadership_-_onsite_guide.pdf), [Hello Interview: expected at each level](https://www.hellointerview.com/blog/the-system-design-interview-what-is-expected-at-each-level), [Hello Interview delivery](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery), [PracHub rubric](https://prachub.com/resources/system-design-interview-rubric-by-level-mid-level-vs-senior-vs-staff). Koi ek universal L5 rubric public nahi hai; company ke hisaab se thoda badalta hai.

1. **Basics jaldi, depth deep-dives mein.** Fundamentals assume kiye jaate hain. Interviewer ke shabdon mein: ~2 jagah gehraai se jao.
2. **Deep-dive khud lead karo.** Interviewer ke ishaare ka wait mat karo. Apne design ki kamzori khud batao.
3. **Requirements → numbers.** Vague problem ko traffic, latency, SLO jaise numbers mein badlo. Math tabhi karo jab usse design badle.
4. **Trade-offs defend karo.** Sirf technology ke naam lena kaafi nahi. "X liya kyunki Z" bolna aana chahiye.
5. **Failure + observability + cost.** Kya tootega, kaise pata chalega (metrics, alerts), aur kitna mehenga padega.
6. **Safe rollout.** Phased rollout aur guardrails khud propose karo.
7. **Real specifics.** Jaise "DynamoDB mein ye partition key kyun chuni". Kitaabi jawab kaafi nahi.
8. **Nayi requirement aaye to design update karo.** Bina ghabraye.
9. **ML/AI round:** problem ko ML task mein khud frame karo. Tokens ko budget ki tarah treat karo. Evals aur guardrails bina pooche add karo.
10. **LLD round:** pehle scope aur entities clear karo, seedha code likhna red flag hai. Practical extensibility ko reward milta hai, faltu future-proofing ko nahi.

## Skill + mission (12 Oct 2026, draft — MISSION.md banate waqt yahan se lena)

- Skill: `teach-system-design`, teach-english ko base bana ke. Aditya slash command nahi chalata — natural baat ("chalo system design padhte hain", "aaj ka lesson") se main khud chalaunga.
- Mission = **B: asli kaam ki skill**, interview-first NAHI. Topics gehraai se dimaag mein, khud bana sake. Interview prep iska side-effect.
- Aditya ke interviews mostly **assignment-based** hain: assignment banao, phir explain karo ki kaise design kiya, kya choices kiye aur kyun. Koi interview deadline/time pressure se padhai nahi chalani.
- **Interview = last priority.** Pehle poora seekhna; interview prep alag phase, sab seekhne ke baad. Interviews kuch bhi ho sakte hain (catch-up call, normal baatcheet, assignment) — sirf assignment pe focus nahi.
- Target roles: **AI agent engineer, voice AI engineer, ML engineer, AI engineer.**
- HLD design practice = **design doc likh ke** (problem, requirements, design, choices + kyun, kya tootega), timer nahi. Weekend pe, jab ek theek-thaak topic block cover ho jaye. Docs GitHub portfolio mein jayenge.
- Folder structure LOCKED: MISSION.md, system-design-list.md, RESOURCES.md, NOTES.md, REVIEW.md, lessons/ (HTML), reference/ (cheat-sheets), learning-records/, designs/ (HLD design docs), lld/ (Sunday Python code, problem-wise), builds/ (🟢 topics ke chhote builds), .claude/skills/teach-system-design/. (Skill build ke time 2 aur jode: `PROGRESS.md` — kahan tak pahunche; `assets/` — lessons ka shared style/quiz, English-learning se copy.)
- Practice schedule: topic block poora hone wale Sunday — pehle LLD (~4-5 hr), phir 1 HLD design doc (~2-3 hr).
- Language LOCKED: samjhana (lessons, explanations, notes) = Hinglish. Likhna (designs/, lld/, builds/ — docs, README, code comments) = English, written-English practice bhi.
- Diagnostic SKIP (Aditya: voice AI ka kaam kiya hai, system design knowledge kam). Learning order LOCKED: P0→P6 dependency path (system-design-list.md ke "Order" section mein).
- **Teaching style LOCKED (12 Oct 2026, lesson 0001 ke baad):** chat mein ek chhota hissa + ek sawaal, ek baar mein. HTML page ek baar mein bada nahi; chat mein samajh aa jaane ke baad hi summary page. Examples sirf voice AI / AI agent (LiveKit, LangGraph-style pipelines) ke; WhatsApp/Twitter jaise generic apps nahi. Sabse accha example = Aditya ka apna production LiveKit voice codebase (`local/voice-material.md`), taaki wo "ye pipeline kaise banayi" ka poora design explain kar sake. Evals ke topic pe bhi isi codebase se example.
  - Pehle **theory**, phir design. Theory ke beech Aditya se apna system design mat karwao (sirf example ki tarah use karo). Lesson page ke sections shuru se, ek-ek karke, jaldi aage mat badho; har section ke baad "clear?" poochh ke hi agla.
- **Time tracking + recall (12 Oct 2026):** har naye message pe `date` chala ke date + time dekho (IST). `REVIEW.md` ke sirf **due** items (Next review date aa gayi ho) ka quiz, naye topic se pehle. Same din ke beech mein purana recall mat poochho (Aditya ne mana kiya). `PROGRESS.md` ke session log mein date + time likho.
- **Model (12 Oct 2026):** Aditya hamesha **Opus** pe padhna chahta hai (Sonnet cheezein miss kar raha tha aur bahut jaldi aage badh raha tha). Skill ki model table (P0 → Sonnet) ko override karta hai; Sonnet recommend mat karo.
- **Vision: "design partner" skill (12 Oct 2026).** Kisi bhi project / feature / assignment pe kaam shuru hote hi chale, aur senior engineer ki tarah saath mein requirements + `reference/quality-checklist.md` + trade-offs tay kare, bina Aditya ke bole.
  - **Goal:** duniya ki best system design skill: junior → senior, aur aage senior → staff/principal ke liye. Quality ka reference: [mattpocock/skills](https://github.com/mattpocock/skills) (banate waqt unka structure aur style padhna).
  - **Kaise banegi:** ek baar mein nahi. Jab tak poori system design seekh nahi lete, har phase ke baad usme naya content jodte jaate hain. Jo bhi cheez "skill mein jaani chahiye" lage (jaise `reference/quality-checklist.md`), yahan note karte jao.
  - **Design hum khud karenge:** skill ka structure bhi hum saath mein tay karenge, example dekh ke aur system design karte hue.
  - **Scope note:** staff/principal content skill ke liye hai. Aditya ka apna seekhna abhi senior level tak hai (`MISSION.md` "Out of scope" waisa hi).
  - **Pehla version:** P0 poora hone ke baad. Banate waqt confirm-gate + model poochho.
  - **Skill mein jaane wali cheezein (chalta hua list):** design process 6 steps · `reference/quality-checklist.md` · "box ke peeche requirement" rule · estimation sirf jab design badle · `reference/design-doc-template.md` · trade-off format (X over Y, because Z, downside W, mitigation, revisit trigger) · failure thinking (band/dheema/galat → blast radius → detect + respond) · open question format (owner, blocker, default, recommendation) · "doc kab likhna": faisla bhaari ho tab.
- `local/` folder gitignored hai: private cheezein (jaise apna voice material) yahin. Seekh khatam hone pe hata denge, ya unki **sanitized** seekh (bina private details) public files mein likh denge.

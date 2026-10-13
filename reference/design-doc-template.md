# Design doc template

Har HLD design doc (`designs/NN-system.md`) isi se shuru hota hai. Doc **English** mein likho; ye file sirf dhaancha hai. Mini doc (1-3 page) ke liye har section chhota rakho, par koi section skip mat karo; jo lagu nahi, uspe ek line likho "Not applicable because ...".

Sources: hamare P0 lessons (requirements, estimation, trade-offs, failure, 10x) + [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) (goals / non-goals, alternatives considered, length).

---

```md
# <System name>

## 1. Problem
<2-4 lines: who is it for, what pain does it solve, why now.>

## 2. Requirements
### Functional (core)
1. <Actor> should be able to <action>.
2. ...
### Later (not in v1)
- ...
### Non-goals
- <Something that could be a goal but we chose not to do.>
### Non-functional
1. <Quality>: <which part> <number or checkable rule> <condition>. (FR x)
2. ...

## 3. Assumptions and open questions
- Assumed: <value> — confirm with <who>.
- Open: <question> — owner: <who> — blocking / non-blocking — until answered we assume: <default> — my recommendation: <A, because Z>.

## 4. Estimation
<Only numbers that change the design. Show the steps, round, write assumptions.
End each calculation with "Decision: ...".>

## 5. API
<Main endpoints / events. Who is the caller is taken from auth, not from the request body.>

## 6. Data model
<Main entities and the fields that matter for the design.>

## 7. High-level design
<Diagram (ASCII or Mermaid) + walk one request through it, step by step.>

## 8. Deep dives
### 8.1 <hardest part 1>
### 8.2 <hardest part 2>

## 9. Trade-offs
- We chose X over Y because Z (evidence). The downside of X is W. Mitigation: M. Revisit when: T.

## 10. Failure modes
| Component | How it breaks (down / slow / wrong) | Blast radius | Detection | Response |
|---|---|---|---|---|

## 11. What changes at 10x
| Item | Today | 10x | Breaks? | Build now (cheap door) or later (trigger) |
|---|---|---|---|---|
```

---

## Submit karne se pehle checklist

- [ ] Har NFR mein number (ya check hone wala rule) hai, koi "fast / scalable" nahi.
- [ ] Har bade choice ke saath "because" + downside likha hai.
- [ ] Har bade choice ka chhoda hua option (Y) dikh raha hai.
- [ ] Saari assumptions section 3 mein hain.
- [ ] Har estimate ke end mein ek "Decision" hai.
- [ ] Kamzoriyan khud likhi hain (failure modes, open questions).
- [ ] Har short form pehli baar poora likha hai (jaise "non-functional requirement (NFR)").
- [ ] Headings, bullets, tables, ek diagram — lambe paragraph nahi.

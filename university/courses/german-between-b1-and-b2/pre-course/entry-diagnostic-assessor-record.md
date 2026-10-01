# Entry diagnostic: assessor record (assessor-only)

Assessor-only companion of `entry-diagnostic-part-a.md` and
`entry-diagnostic-part-b.md`. It must not be shown to the Student before or
during the diagnostic. It holds answer keys, audio scripts, the task-to-criterion
map, and judgement rules.

## 1. Identity and authority

- Contract 2 artifact for the Dean's Assessment Request (Contract 1) in
  `README.md`, section "Entry diagnostic: Dean frame".
- Author and accepting assessor: Learning Analyst Emma (Language Faculty).
  No code is submitted; no run/inspection method applies.
- Public and Student-independent. No Student data appears in any file. Results
  are recorded in the private Student workspace through `update-evidence` after
  administration; that is outside this artifact.
- Emma measures and reports. Placement, Module choice, skip/narrowing, bridge,
  and trajectory remain with the Dean (`README.md` decision map, which is not
  changed here).
- Independence: the administering Analyst must not have taught or coached this
  Student on the assessed scope (`policies/assessment-independence.md`).

## 2. Provenance and rights

- All learner texts, audio scripts, and items are original, authored for this
  artifact by the Analyst. No external text, audio, image, or exam item is
  copied or adapted. No external sources were used.
- Level calibration (A2/B1) is the Analyst's professional judgement against
  the Course's qualitative criteria. It is not validated against a corpus or
  piloted with learners (see section 9).
- Audio is not supplied as a file. Section 5 gives the scripts for live or
  self-recorded reading by a human. Delivery channel must be recorded.

## 3. Measured criteria (quoted from the Course; not changed)

Module 2 Entry Contract (A2 foundations), the Student can, in familiar
contexts:

- E1 form understandable basic statements and questions with controlled word
  order;
- E2 preserve meaning with essential articles, cases, pronouns, prepositions,
  and common verb forms;
- E3 refer to present, past, and future situations in a comprehensible way;
- E4 understand and use high-frequency vocabulary and functional phrases.

Module 2 Exit Contract (B1 performance), the Student can independently:

- X1 understand main points and relevant details of clear standard German on
  familiar everyday, study, and work-related topics;
- X2 read connected B1-level texts and identify main message, supporting
  information, and relevant vocabulary;
- X3 speak coherently about experiences, plans, opinions, and familiar
  problems, with enough interactional control to maintain a conversation;
- X4 write connected practical texts with an understandable structure and
  appropriate B1-level language;
- X5 use the B1 grammar and vocabulary needed for meaning, while identifying and
  correcting recurring personal errors;
- X6 transfer a recovered form or expression from controlled practice into a
  new but familiar communicative context;
- X7 notice uncertainty in a spoken or written attempt and request clarification
  or repair when communication breaks down.

## 4. Task-to-criterion map

Label mapping: this record keeps the internal labels A1-A4 and B1-B5, B3a/B3b.
The learner files use Aufgabe 1-4 (A1-A4) and Aufgabe 5-9 (B1 = 5 Lesen,
B2 = 6 Hören, B3a/B3b = 7a/7b, B4 = 8, B5a/B5b = 9a/9b); Z is "Extra-Aufgabe Z".
The renaming avoids confusion with CEFR level labels.

| Task | Part | Skill | Measures | Mode |
|---|---|---|---|---|
| A1 sentence order (items 1-3) and questions (items 4-6) | A | Schreiben (controlled) | E1 | NO_AI |
| A2 cloze, 12 items (articles 1, 2, 10; prepositions 3, 4; pronouns 8, 9; verb forms 5, 6, 7, 11, 12) | A | Schreiben (controlled) | E2 | NO_AI |
| A3 present / past / future, 2 sentences each | A | Schreiben (guided) | E3 | NO_AI |
| A4 situations (8) and words (6) | A | Schreiben / vocabulary | E4 | NO_AI |
| B1 reading, 9 items | B | Lesen | X2 | NO_AI |
| B2 listening, 6 items | B | Hören | X1 | NO_AI (notes on paper allowed) |
| B3a e-mail | B | Schreiben | X4, X5 (use of B1 grammar), X6 (free production side) | NO_AI |
| B3b mark and correct own text | B | Schreiben | X5 (identify/correct), X7 (noticing) | NO_AI |
| B4 two clarification questions | B | Schreiben | X7 | NO_AI |
| B5a monologue, B5b conversation | B | Sprechen | X3, X7 (spoken), X6 (free production side), X5 (spoken use) | NO_AI |
| Z optional revision | B | Schreiben | supplementary evidence for X5 and X7 only | AI_ASSISTED, disclosed, recorded separately |

X6 additionally uses the controlled-form results of Part A (see 6.X6).

## 5. Administration protocol

### 5.1 Common rules

- One attempt per part. No retake. A disrupted sitting is recorded with the
  disruption; any further measurement is a Dean decision (`README.md`
  decision map: "request a bounded further measurement").
- Part A at most 45 minutes, Part B at most 75 minutes (B1-B5), one sitting
  each. Per-task slots: A1 8, A2 10, A3 10, A4 12 (Part A); B1 20, B2 12, B3 20
  (15 + 5), B4 5, B5 12 (Part B). The learner is told to move on when a slot
  ends. B5 must keep its slot; if earlier tasks overrun, cut them, not B5.
  A short pause (at most 5 minutes) is allowed between tasks and is
  recommended before B5. Parts may be in separate sessions.
- Record per part: date, start/end, channel (typed / handwritten / spoken /
  audio), whether the sitting was unobserved, any tool use observed or
  disclosed, any technical disruption, items left blank, items cut by time.
- `NO_AI`, no dictionary, no translator, no autocorrect for every task except Z.
  If a violation is observed or disclosed, the affected items are reported
  `uncertain` and the violation recorded; they are never `demonstrated`.
- Instructions are A2 or lower. If an answer shows that the Student
  misunderstood the instruction (off-task answer), do not count that item
  against the criterion; mark it "instruction not understood" and treat as no
  evidence. The Analyst must not explain the task content or hint.
- The Analyst accepts any answer whose meaning is sufficiently clear, in
  another order or wording (`policies/interaction-format.md`). Spelling is
  ignored when meaning and form are recognisable. Missing umlauts count as
  correct. Do not request a correction for cosmetic differences.
- Part B is not administered if the stop rule (5.2) applies.

### 5.2 Stop rule after Part A (Dean's stop condition, operationalised)

The Dean's condition: stop when Part A shows A2 gaps that materially block B1
work. The Dean set no threshold. The Analyst proposes the following operational
reading, which the Dean may adjust. It changes no criterion and makes no
placement:

- Part B is **withheld** when E1 is `not demonstrated`, or when two or more of
  E1-E4 are `not demonstrated`. Reason: B1 tasks need basic sentence order and
  meaning-preserving forms to be interpretable at all.
- Part B is **administered** when all of E1-E4 are `demonstrated`, or
  `uncertain`, or when at most one of E2-E4 is `not demonstrated` and E1 is
  not `not demonstrated`. A Part B measurement is then interpreted with the A2
  gap in mind.
- When withheld: return the Part A evidence, state that X1-X7 were not
  measured, and do not infer B1 results.
- The Analyst announces only "Teil B ist sinnvoll / Teil B ist jetzt nicht
  sinnvoll" without placement advice.

### 5.3 Delivery of listening (B2)

- Preferred delivery: a person reads the scripts below aloud at natural
  pace, or plays a recording of a human reading, to the Student. Two plays per
  text, a 10-second pause between plays. Do not repeat further. Do not show the
  script.
- If the only available channel is text or a text-to-speech engine, record
  this. A text-to-speech recording is audio, but pronunciation may differ from
  human speech; record the channel. If no audio is possible, B2 is not
  administered and X1 is `uncertain` (never `demonstrated` from reading
  alone, because reading the script measures X2 not X1).
- Script H1 (everyday; about 85 words):
  "Guten Tag, hier ist die Praxis von Doktor Berger. Mein Name ist Anna
  Roth. Ich rufe wegen Ihres Termins am Donnerstag an. Leider ist die
  Ärztin an dem Tag krank. Wir müssen den Termin verschieben. Können Sie
  stattdessen am Freitag um halb elf kommen? Wenn das nicht geht, rufen
  Sie uns bitte bis morgen Mittag an. Bitte bringen Sie auch Ihre
  Versichertenkarte mit, wir brauchen sie neu. Vielen Dank und bis bald."
- Script H2 (study; about 95 words):
  "Liebe Kursteilnehmerinnen und Kursteilnehmer, eine Information für
  nächste Woche. Der Unterricht am Montag fällt aus, weil die Lehrerin an
  einer Fortbildung teilnimmt. Dafür gibt es am Samstag einen
  Zusatztermin, von neun bis zwölf Uhr, im Raum 204. Der Raum ist im
  zweiten Stock, neben der Bibliothek. Bitte bringen Sie die
  Hausaufgaben von Seite 45 mit. Wer am Samstag nicht kommen kann,
  schreibt bitte bis Mittwoch eine E-Mail an das Sekretariat. Dann
  bekommt er die Materialien online."

### 5.4 Delivery of speaking (B5)

- Channel: live voice with the Analyst or another human assessor; a
  synchronous voice or video call counts. Record the channel.
- B5a: 30 seconds thinking, no notes, about one minute of speech. Do not
  interrupt; one neutral prompt allowed after 20 seconds of silence.
- B5b scripted conversation. The partner follows this sequence, with natural
  adaptation to the Student's answers, and records the turns:
  1. "Wie lernen Sie im Moment Deutsch?" (familiar topic; gets the
     conversation going; follow up with "Warum?")
  2. "Was ist für Sie im Alltag ein Problem mit der deutschen Sprache?"
     (familiar problem)
  3. Planned repair trigger R1 (lexical): "Welche Hürden gibt es dabei?"
     (Hürden is deliberately unfamiliar; say it once at normal pace; do not
     explain unless the Student asks.)
  4. "Was denken Sie über Online-Kurse? Sind sie gut oder schlecht?"
     (opinion; follow up with "Warum?")
  5. Planned repair trigger R2 (referential vagueness): "Und wie war das
     dann mit der Sache?" said without a clear referent; do not clarify unless
     the Student asks.
  6. Invite: "Haben Sie auch eine Frage an mich?" (interaction; the Student
     may have already asked).
- Do not correct, teach, or help. If the Student requests clarification, give
  one brief, simpler rephrasing and record that the Student initiated it. Do not
  rescue silently; record how long the breakdown lasted.
- Record, per turn: Student initiated or responded; trigger R1/R2 reaction
  (clarification request / guess / silence / off-topic answer / answered
  appropriately); understandability.
- Optional: a recorded monologue only, without an exchange, may be collected
  as an observation. It cannot yield `demonstrated` for X3 (see section 7).

## 6. Judgement rules by criterion

General: judge each item as correct / partly correct / incorrect / blank /
no evidence (instruction not understood or AI/tool violation). A Part A item
is "correct" when meaning is preserved and the targeted form is correct.
Where items are counted, "blank" counts as not correct. If more than 25% of a
criterion's items are blank or cut by time, and the answered items alone would
give `demonstrated`, the result is `uncertain`; if the answered items alone would
give `not demonstrated`, the result stays `not demonstrated` only when at least
three items are answered; otherwise `uncertain`.

The count thresholds below are the Analyst's proposed measurement rules
(the Course leaves thresholds to the Analyst). They are not Dean thresholds and
are not converted into a score in the report. The three-way result is the only
reported result. Judging is by pattern; one-off slips do not decide.

### E1: word order (A1, 6 items)

Keys (any of the grammatically correct word orders accepted):
1 "Heute gehe ich zum Arzt." or "Ich gehe heute zum Arzt." (also "Zum Arzt
gehe ich heute.")
2 "Am Wochenende besucht er seine Eltern." or "Er besucht seine Eltern am
Wochenende."
3 "Morgen können wir nicht kommen." or "Wir können morgen nicht kommen."
4 e.g. "Wann fährt der Zug nach Köln?" / "Wann fährt der nächste Zug?" (W-question,
verb in 2nd position; "Wissen Sie, wann ...?" acceptable if the verb is final)
5 e.g. "Ist Herr Weber heute da?" (Ja/Nein question, verb in first position)
6 e.g. "Was ist dein Hobby?" / "Was machst du gern?" (any understandable
question with correct question order; addressed to Lisa)

- `demonstrated`: at least 5 of 6 correct, no item where word order changes
  meaning.
- `not demonstrated`: 3 or fewer correct, or word order changes or blocks meaning
  in at least 2 items.
- otherwise `uncertain`.

### E2: forms preserving meaning (A2, 12 items)

Accepted keys (all forms that fit the sentence and are correct):
1 meiner / einer / der / ihrer (dative feminine, after "bei").
2 eine (accusative feminine)
3 am (one gap before "Bahnhof"; "beim" also accepted)
4 mit (item says "mit der U-Bahn")
5 getroffen
6 heißt
7 spricht
8 ihn (hint "(Tom)" resolves the Tom/Eva ambiguity)
9 mir
10 die (accusative after "in", direction)
11 kann
12 fährt ... ab (both words; correct only if both are right)

- Record for each item both "form-correct" and "meaning-affecting error" (an
  error that changes the intended meaning or makes it unclear).
- `demonstrated`: at least 9 of 12 form-correct and at most 1 meaning-affecting
  error.
- `not demonstrated`: 6 or fewer form-correct, or at least 4 meaning-affecting
  errors.
- otherwise `uncertain`.
- Also record the error type pattern (article/case, preposition, pronoun,
  verb form) for the report and for X5/X6.

### E3: present, past, future reference (A3, three frames)

For each frame (a, b, c), judge whether a reader can identify the time
reference from verb form or time marker, and whether the verb form is
acceptable.

- Present (a): present tense or habitual present.
- Past (b): Perfekt, or Präteritum of sein/haben/modals/common verbs.
  Recognisable past reference using present tense with a time marker ("gestern
  gehe ich") is not accepted as past form but the reference is comprehensible;
  record "reference understood, form not controlled".
- Future (c): present tense with a future time marker (accepted) or "werden +
  infinitive".
- `demonstrated`: all three frames have comprehensible time reference with an
  acceptable form in at least 2 of 3 frames and no frame in which the reference
  is wrong or unclear.
- `not demonstrated`: at least 2 frames in which the time reference is wrong
  or not identifiable.
- otherwise `uncertain`.

### E4: vocabulary and functional phrases (A4, 14 items)

A4 Teil 1 (numbers 1-8; items 1 and 8 need two short utterances): acceptable when the phrase fits the situation, is
understandable, and is not inappropriate. Expected types: 1 "Guten Tag, ich
bin ... / Mein Name ist ..." (formal) 2 "Entschuldigung, wo finde ich Milch?" 3
"Können Sie das bitte wiederholen? / Wie bitte?" 4 "Ich möchte einen Kaffee, bitte."
5 "Entschuldigung, ich bin zu spät." 6 "Was kostet die Jacke?" 7 "Ich möchte einen
Termin machen." 8 "Danke, auf Wiedersehen / Tschüss."
Teil 2 keys (numbers 9-14 in the learner file): 9 c, 10 b, 11 c, 12 a, 13 b, 14 c.

- `demonstrated`: at least 11 of 14 acceptable.
- `not demonstrated`: 7 or fewer acceptable.
- otherwise `uncertain`.
- If a Student shows a clear guessing pattern in Teil 2 (for example the same
  letter throughout), treat Teil 2 as `no evidence` and judge E4 on Teil 1
  alone (at least 6 of 8 for `demonstrated`; 4 or fewer for
  `not demonstrated`; otherwise `uncertain`).

### X2: reading (B1, 9 items)

Keys:
1 (main message) A person has lived without a car for a year; changes from car
to bus/bike/train and gives advantages and disadvantages. Accept any sentence
that identifies the topic (living without a car) plus the evaluation or
change.
2 (a) the new flat is only 5 km from work, (b) parking in the city is very
expensive. Accept either as partial; both = correct.
3 Bus at 6:40, waiting in rain in winter, once the bus did not come. At least
one named difficulty = partial; two = correct.
4 rents a cargo bike from the city.
5 Two of: 20 minutes by bike, feels more awake, saves about 300 euros per month,
moves more, can read/listen to music on the train.
6 plans to buy an electric bike, so that the Student can ride in winter too.
7 a, 8 a, 9 b.

- `demonstrated`: main message (item 1) correct; at least 4 of items 2-6
  correct; at least 2 of items 7-9 correct.
- `not demonstrated`: at most 2 of items 2-6 correct, or the main message
  wrong and at most 3 of items 2-6 correct.
- otherwise `uncertain`.
- Production quality of the answers is ignored when meaning is clear. Items 1-6
  ask for German production but judge content only.
- Reading is NO_AI untimed apart from the 15-minute block; blank/time-out rules
  apply.

### X1: listening (B2, 6 items)

Keys: 1 a. 2 Friday, 10:30. 3 The insurance card (Versichertenkarte). 4 b. 5
Saturday, 9-12, room 204 (second floor, next to the library). Both time and
place needed; either alone is partial. 6 Write an e-mail to the secretariat
by Wednesday.

- `demonstrated`: items 1 and 4 correct and at least 3 of items 2, 3, 5, 6
  correct, and both texts show at least one correct detail.
- `not demonstrated`: at most 2 of the 6 items correct overall, or items 1 and 4
  both wrong.
- otherwise `uncertain`.
- Only if heard in audio (5.3). A reading delivery or no audio gives `uncertain`
  (not measured), never `demonstrated`.
- Note: items 1 and 4 are multiple choice (guessing chance 1 in 3). They
  count only together with the details.

### X4: connected writing (B3a)

Content points required: P1 problem and since when (Heizung kaputt, seit drei
Tagen); P2 what was already done (past); P3 reason why it matters (cold,
weil / denn / deshalb or another way); P4 request and deadline. Assessable
features: greeting and closing appropriate to an e-mail to a caretaker
(register: formal Sie, stated in the task; register choice is not measured), logical order, connectors, length 80-120 words (outside the range
is recorded, not penalised unless it prevents the points).

- `demonstrated`: all four content points present; text understandable at
  first reading; recognisable structure (greeting, ordered content, closing);
  and the language is of a B1 type in at least two of: subordinate clause,
  Perfekt/Präteritum for past events, modal verbs for request, connectors; the
  errors do not obstruct meaning.
- `not demonstrated`: two or more content points missing, or the text requires
  repeated interpretation to understand, or no recognisable structure.
- otherwise `uncertain`.
- B3a judged on the NO_AI text only; Z does not affect it.

### X5: B1 grammar and vocabulary for meaning; identifying and correcting recurring personal errors

Two components, both from NO_AI evidence only:

- (a) Use: across B3a, B5 (if available), and A-part items where relevant, the B1
  grammar and vocabulary needed for meaning is mostly controlled (main verb
  forms, word order in main and subordinate clauses, essential cases and
  connectors) and errors do not obstruct meaning.
- (b) Identifying and correcting recurring personal errors: an error type is
  "recurring" when the same type appears at least twice across Part A and Part B
  NO_AI texts. Evidence: B3b marks and corrections (unassisted). Count a
  recurring type as "identified and repaired" when the Student marks or corrects
  at least one instance of it correctly in B3b.

- `demonstrated`: (a) is met, and either no recurring error type exists, or at
  least half of the recurring error types are identified and repaired in B3b.
  If no recurring error type exists, record "(b) not applicable".
- `not demonstrated`: (a) is not met, i.e. grammar/vocabulary errors
  frequently obstruct meaning.
- `uncertain`: (a) is met but fewer than half of the recurring types are
  identified and repaired, or B3b was not done, or Part A was not administered so
  recurrence cannot be judged. Reason for this choice: B3b is a single, short
  check. A failure there is weaker evidence than a failure of use.
- Z (AI-assisted) is recorded separately in the report. It can add supporting
  observation, never `demonstrated` on its own.

### X6: transfer from controlled to free context

The diagnostic has no teaching phase, so there is no "recovered" form in the
strict sense. The Analyst reads the criterion as: forms that were correct in
the controlled Part A tasks are also correct in free, new-context Part B
production. This is a measurement reading, flagged for the Dean in section 9.

- Select up to five target forms that were correct in Part A (for example Perfekt,
  dative pronoun, preposition with accusative, V2 inversion, modal + infinitive,
  question order).
- Look for opportunities to use each form in B3a, B3b, B4, and B5 (NO_AI
  only). Count a form as "transferred" when it appears and is correct in at
  least one free context.
- `demonstrated`: at least three target forms found, and at least two
  transferred, and none of the forms that were controlled in Part A is
  repeatedly wrong in free production.
- `not demonstrated`: at least two target forms found in free production
  and wrong in them though controlled in Part A.
- `uncertain`: fewer than three target forms found with an opportunity in
  free production, Part A was not administered or Part B Sprechen/Schreiben
  evidence is incomplete.

### X3: speaking and interaction (B5)

Functions to observe: experience (B5a), plan (B5a), problem (B5b turn 2),
opinion (B5b turn 4). Interactional control: responds to follow-up, keeps the
exchange going, asks the Analyst at least one question, handles R1/R2.

- `demonstrated`: all four functions comprehensibly performed, with
  connected speech (linking, not only isolated words), the exchange
  is maintained, and the Student asks at least one question. At most one
  breakdown needs Analyst rescue.
- `not demonstrated`: at least two functions are not comprehensible, or the
  exchange cannot be maintained (repeated silence/off-task responses).
- otherwise `uncertain`.
- No spoken exchange possible: see section 7. Result is `uncertain`.

### X7: noticing uncertainty and requesting clarification or repair

Evidence sources: B4 (written), B3b (marks), B5 R1/R2 (spoken).

- Written: B4 contains two distinct requests; each names a specific missing
  or unknown piece (for example time, which documents, which Amt/where, what
  "Antrag"/"Sachbearbeiterin" means). "Ich verstehe nicht." alone is not
  specific. The message really lacks: time, location of the Amt, what Unterlagen
  exactly; the words "Antrag" and "Sachbearbeiterin" may be unknown.
- Noticing: at least one B3b line marked "Ich bin nicht sicher" (the list holds
  up to three entries; the Student does not edit the e-mail) that points at a
  real problem (a hit). A mark at a correct place counts as noticing without
  correctness of the repair; a hit is also evidence of noticing an error the
  Student could not fix.
- Spoken: Student requests clarification at R1 or R2, or uses paraphrase/repair
  moves of their own (self-correction, "Ich meine ...").
- `demonstrated`: B4 yields two specific, understandable requests, and at
  least one of (a hit in B3b, a spoken repair move).
- `not demonstrated`: B4 yields no specific request, and no hit in B3b, and no
  spoken repair move although a breakdown occurred. (If no spoken exchange
  occurred, spoken evidence is `no evidence`.)
- otherwise `uncertain`.
- Limitation: the written tasks cue the request. Uncued evidence exists only
  from spoken R1/R2 and from unprompted self-corrections. The record must
  state which evidence was cued.
- The spoken part is not scored if there is no spoken exchange. Without
  spoken evidence, the result can still be `demonstrated` for the written side,
  because the criterion says "spoken or written". Record that the spoken
  side was not measured.

## 7. Sprechen when no spoken exchange is possible

- If no live spoken exchange is possible, B5 is not administered as designed.
  X3 is reported `uncertain` (not measured in the available channel). It is never
  `demonstrated`.
- A recorded monologue (B5a) without interaction may be collected, but is only
  an observation. It does not change X3 from `uncertain`, because X3 requires
  interactional control. Record what the monologue showed (functions
  performed, comprehensibility) as an observation for the Dean.
- X7 spoken side, X5 spoken use, and X6 spoken free production are not
  measured. The report states which written evidence stands in for them and
  that this is partial.
- The report must say: "Sprechen was not measured as an exchange" and the Dean's
  map row "Criteria `uncertain`: request a bounded further measurement" applies.
  The Analyst does not decide that route.

## 8. AI-assisted revision step (Z): recording and handling

- Administered only after B5, never before an unassisted task is complete.
  Release the Z section to the Student only after B5 (the learner file contains
  it, so withhold that section or page until then). The unassisted B3a/B3b texts
  are collected and frozen first. Maximum 15 minutes, outside the Part B limit.
  The AI input is the unmarked B3a e-mail. Item 4 of Z (the Student's own
  account) is written without AI, in the form "Alt -> Neu -> Ich glaube".
- Record: tool name, the Student's prompt, the revised text, the Student's
  own account of up to three errors (what was wrong, correction, why).
- Report in a separate evidence row labelled `AI_ASSISTED`. Do not merge it into
  the criterion results of X4, X5, X6, X7 from NO_AI evidence.
- What it can show: whether the Student, after help, identifies errors
  and understands the correction. Use as supporting observation for X5 and X7. If
  the Student's account is not in own words or does not match the changes, record
  `uncertain` for that evidence.
- It cannot raise a criterion from `uncertain`/`not demonstrated` to
  `demonstrated` on its own.
- The step is optional and carries no penalty if skipped. Skipping is reported
  as "step not taken", not as a failure.

## 9. Limitations and open questions (for the Dean)

- L1 Public repository: this record contains keys and scripts and sits in a
  public path. The separation is organisational, not secrecy. If the Student can
  read it, independence is at risk. Request: decide whether keys should move to
  a restricted location before administration; the Analyst has not moved them.
- L2 Stop-rule thresholds (5.2) and all count thresholds (section 6) are the
  Analyst's proposals; no Dean or Course threshold exists. They are not
  validated or piloted.
- L3 X6 transfer reading (section 6, X6) is a diagnostic adaptation of the
  criterion's wording. The Dean may disagree with this reading.
- L4 Hören and Sprechen need channels (audio delivery, spoken exchange). Without
  them X1 and X3 are `uncertain`.
- L5 Written X7 evidence is cued by the task. Spoken evidence is the only
  uncued evidence.
- L6 One short text per skill. The evidence is a small sample; contradictory
  or thin evidence is reported `uncertain`, not smoothed.
- L7 The Z step is designed for Schreiben only. A Sprechen revision step would
  need a transcript or recording and is not designed here. The Dean's frame
  makes it optional.
- L8 Learner-facing text is German only; this record is English. Learner-text
  German and A2 level were written and checked by the Analyst alone, with the
  Contract 3 review below as the only external check.
- L9 Time limits (Part A 45 minutes, Part B 75 minutes) are proposed within
  the Dean's "single sitting" bound; not tested.

## 10. Report format to the Dean (Contract 4)

For each of E1-E4 and X1-X7: result (`demonstrated`, `not demonstrated`,
`uncertain`), the evidence items it rests on, the mode (`NO_AI`; `AI_ASSISTED`
only for Z), the channel, and any limitation. Do not report a score or
percentage. State explicitly that the Analyst did not choose placement or
trajectory.

## 11. Contract 3 review record

- Reviewer: Instructional Assistant Livia (`workers/livia/WORKER.md`), separate
  review call with the complete learner files, the Dean's request, the
  criteria, and the AI-use mode. Read-only. Scoring, independence, level
  calibration, and the audio scripts were not validated by the reviewer.
- Pedagogical readiness reported: `ready_with_changes`.
- Owner review (Analyst): findings applied or rejected below. The reviewed
  version was revised afterwards; the revised files were not re-reviewed.
  Status: reviewed once, changes applied, no second review.

| # | Finding | Disposition |
|---|---|---|
| H1 | A2 example `1 - meiner` leaks the key for gap 1 | Applied: example is `0 - wohne`; format for 2-word gap 12 shown |
| H2 | A1 items 4-6 copy the question or test pronoun change | Applied: situations rewritten without the question wording; E1 measured by free question formation; item 6 asks for Lisa's hobby |
| H3 | "andere Reihenfolge" rule conflicts with E1/E2 | Applied: "other words are fine"; order matters in Aufgabe 1; form matters in Aufgabe 2 |
| H4 | Labels A1/B1/B2 collide with CEFR levels | Applied: Aufgabe 1-9; mapping in section 4 |
| M5 | A4 format "one sentence" does not fit items 1 and 8 | Applied: one or two sentences |
| M5b | Item 5 speech act open | Rejected: open on purpose; any fitting apology counts |
| M6 | Item 1 address form not stated | Applied: "Sie" stated |
| M7 | A3 prompts model tense; heading a) "Jetzt" mismatch | Partly applied: heading a) now "Jeden Tag", meta-concept removed. Rejected: removing time cues, which are the task for E3 (comprehensible reference) |
| M8 | Numbering restarts in A4 and example | Applied: A4 numbers 1-14, example `0 - a` |
| M9 | A2 gaps 1/3/8 ambiguous | Applied: gap 8 changed to `(Tom)` hint; keys for gaps 1 and 3 widened in section 6 |
| M10 | B1 Q2 count hidden | Applied: "zwei Gründe"; Q3 "eine Sache" |
| M11 | "Vorteile" in instruction | Applied: "Was ist jetzt gut". Q8 "Nachteile" stays because it is the tested word (in the text) |
| M12 | Tasks cue noticing for X7 | Not changed (written evidence needs a cue); recorded as limitation L5 and in the X7 rule |
| M13 | B5 hint "mit anderen Wörtern sagen" | Applied: removed |
| L14 | "Prüfung/Prüferin" clash | Applied: "Gesprächspartner" |
| L15 | A "prüft nicht Lesen" wrong | Applied: "Hören und Sprechen" |
| L16 | A2 letter abrupt | Applied: connecting sentence added |
| L17 | 80-120 word count | Applied: "ungefähr 100 Wörter"; X4 keeps the range as a record only |
| L18 | Register hidden | Applied: "Sie" stated; not measured |
| L19 | B5a topic personal | Applied: "muss nicht wahr sein" |
| Lang | B1+ meta words (Antwortformat, Wir achten auf, Sitzung, Anrede, Betreff, kontrollieren, etc.) | Applied. "Hausmeister" replaced by a gloss. "Amt/Antrag/Unterlagen/Sachbearbeiterin" kept in Aufgabe 8: everyday words, and the unknown words are the point of X7 |
| Lang | B2 Q1 option unidiomatic | Applied |
| T1 | Sitting length and time per task | Applied: per-task time rule, Part B 75 minutes, reading 20 minutes, 1 minute question preview in Hören, pause before Sprechen |
| T2 | Who is "wir"; how to report problems | Applied: "die Person, die den Test begleitet"; the administrator and observation mode are not decided here |
| T3 | B3b inconsistent | Applied: single contract, list of up to three, no editing |
| T4 | Z under-specified | Applied: 15 minutes, unmarked e-mail version, item 4 without AI in lighter form, release only after B5. Not applied: a physically separate page (outside the allowed three files); handled by the release rule |
| T5 | Channel and delivery not told | Partly applied: Aufgabe 6 and 9 say who/how; typed or handwritten left open (5.1) |
| T6 | B5 asking questions optional vs measured | Applied: "Bitte stellen Sie auch Fragen" |
| Q7 | Audio scripts need language check | Not done: scripts use B1-level words (Versichertenkarte, Fortbildung, Zusatztermin, Sekretariat) by design as B1 listening content; not separately reviewed. Limitation L8 |
| Q8 | Danach silent about "Teil B nicht sinnvoll" | Applied: neutral "Dann sprechen wir über den nächsten Schritt" |

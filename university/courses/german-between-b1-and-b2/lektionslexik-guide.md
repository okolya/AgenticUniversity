# Lektionslexik — Leitfaden für Lecturer und Teacher / Гід з лексем уроку

- **Kurs:** Між B1 та B2 (nur dieser Kurs)
- **Detailregeln:** siehe `COURSE.md`, Abschnitt Lektionslexik
- **ADR:** `university/decisions/0013-formative-lexicon-track.md`
- **Rollout:** alle 51 Lessons (Module 1–4); Checkpoints = Theme-Pack Recycle
- **Pilot SQLite-Track:** Modul 1 Thema 2 (Karten + CLI-Schritte)
- **Workers:** Lecturer Ferdinand (Autor/Durchführung); Teacher Viktor (vocab gym bei Trigger)
- **Katalognachzug:** `scripts/apply_lektionslexik.py` (nur Wartung)

---

## Deutsch

### Was ist `Lektionslexik`?

Genau **3–5** Ziellexeme pro Lektion. Sie stehen im Kontext der Lektion und
werden spielerisch geprüft. Die große Liste „Wörter für diese Lektion“ bleibt
als Verständnisstütze — sie ist **nicht** der recycle-Pflichtsatz.

Pro Lemma kurz notieren:

| Spalte | Pflicht | Regel |
|---|---|---|
| Lemma | ja | Grundform wie im Unterricht |
| Artikel | ja | `der` / `die` / `das` für Nomen; `none` sonst |
| Kollokation | optional | eine Wortverbindung auf demselben Item |
| Merkhilfe | optional | nur Text (z. B. `der=blau`) |
| Kurz | ja | kurze Glosse / Bedeutung |

### Wiederholung vs Festigung

| Modus | Was | Store? |
|---|---|---|
| **Wiederholung** | `Lexik-Spiel`, `Recycle-Spiel`, Teacher gym | ja — `lexicon_item` in SQLite |
| **Festigung** | `Lexik-Schreiben` (Sätze in der Lektion) | **nein** — nur im Lesson-Text |

`Lexik-Schreiben` konsolidiert im Slot; es erzeugt keine `next_due` und keinen
Recycle-Eintrag.

### Spiele (v1)

Lecturer wählt **ein** Format pro Slot.

1. **Match-3** — Karte ↔ Bedeutung/Satz; 3 Leben; Ziel: alle Paare.
2. **Lücken-Duell** — Satz aus der Lektion mit Lücke; Zeitbox ~60–90 s pro Item.
3. **Rate-mich** — Agent beschreibt ohne das Wort; Student nennt die Lexik
   (1:1-Hot-Seat).

Immer sichtbar: Ziel, Regeln, was als Treffer zählt, was bei Niederlage passiert.

### Lexik-Schreiben (Produktion / Festigung)

Nach Erklären + Spiel: kurze **Satzproduktion** mit der `Lektionslexik`
(Sprachkurs-Muster: recognition → controlled use → freer use).

Pflicht, wenn die übrigen Aufgaben die Ziellexeme nicht ausdrücklich verlangen:

- **gesteuert:** ein kurzer Satz **pro Lemma** (bei Metasprache: eigenen Satz
  schreiben und Subjekt / Position 2 markieren);
- **etwas freier:** 3–5 Sätze, jedes Ziellemma mindestens einmal;
- Zeitbox ~5–8 Min.; formativ; Lektionsregeln (z. B. Verb Position 2) gelten.

Teacher vocab gym darf dieselben Satztypen als Drill wiederholen — ohne Store-
Schreiben für die Sätze selbst.

### Student-Track (SQLite, bei Student-ID)

Formativ, kein Mastery-Urteil, keine Exit-Evidence (ADR 0013).

| Feld | Werte |
|---|---|
| lemma | Zeichenkette |
| article | `der` \| `die` \| `das` \| `none` |
| collocation | optional |
| status | `new` \| `recycling` \| `weak` \| `stable` |
| introduced_lesson_ref | kanonische Lesson-Referenz |
| last_check / next_due | ISO-Datum |
| streak_ok | Zähler sauberer Recycles |
| mnemonic | optionaler Text |

**CLI** (aus `university-core/`, registrierter Student):

```text
python3 scripts/student_store.py list-lexicon-due <id> --course german-between-b1-and-b2
python3 scripts/student_store.py upsert-lexicon <id> --profession Lecturer --workflow lesson-preparation
  < JSON: lemma, article, course_id, introduced_lesson_ref, …
python3 scripts/student_store.py record-lexicon-check <id> <lemma> ok|fail \
  --course german-between-b1-and-b2 --profession Lecturer --workflow lesson-preparation
python3 scripts/student_store.py list-lexicon <id> --course german-between-b1-and-b2
```

Teacher nutzt dieselben Befehle mit `--profession Teacher` und dem aktiven
Reinforcement-Workflow.

**Spacing v1:** Spiel-`ok` → `recycling` / nächster Tag; `fail` → `weak` /
heute (gym); zwei saubere Recycle-`ok` → `stable` / +3 Tage; `fail` bei
`stable` → `weak`.

Ohne Student-ID: nur Session-Notiz der Statusfelder; kein Store-Schreiben.

### Ablauf

| Wann | Was | Wer | Store |
|---|---|---|---|
| Start Lektion | `list-lexicon-due` (+ Recycle-Spiel) | Lecturer | lesen |
| Nach Einführung | `upsert-lexicon` für neue Lemmata | Lecturer | schreiben |
| Ende Lektion N | `Lexik-Spiel` + `record-lexicon-check` | Lecturer | schreiben |
| Nach Spiel | `Lexik-Schreiben` | Lecturer | **nicht** |
| Nach Fail | vocab gym + Checks | Teacher | schreiben |
| Theme-Checkpoint | Theme-Pack Recycle | Lecturer | schreiben |

**Fail-Trigger → Teacher vocab gym:** im Recycle ≥2 Fehler im aktuellen Satz
**oder** dasselbe Lemma zwei Recycles hintereinander schwach. Contract-4-next:
`Teacher reinforcement (vocab gym)`, Scope = schwache Lemmata. Dauer ca.
10–15 Minuten Spiele/Drills, dann zurück in den Lecturer-Slot. Teacher
erweitert Theme/Module nicht.

### Nicht tun

- Lexik nicht zum Module-Exit-Kriterium machen.
- Learning Analyst / Examiner nicht für Routine-Spiele rufen.
- Keine 20-Wort-Pflichtlisten als `Lektionslexik`.
- `Lexik-Schreiben` nicht in SQLite speichern.
- Nomen nicht ohne Artikel als Track-Item anlegen.

---

## Українською

`Lektionslexik` = 3–5 лексем (іменник **з артиклем**) + гра (**Wiederholung**
→ SQLite) + **Lexik-Schreiben** (**Festigung** лише в уроці). Recycle на старті
наступного уроку; Teacher — лише за fail. CLI: `list-lexicon-due` /
`upsert-lexicon` / `record-lexicon-check`. Деталі — у німецькій секції,
`COURSE.md` і ADR 0013.

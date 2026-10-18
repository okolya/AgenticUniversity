# Vorbereitungsprotokoll Thema 1 / Протокол підготовки Теми 1

- **Kurs / Modul / Thema:** Між B1 та B2 / Modul 1 — A2-Wiederherstellung / Thema 1 — Wortstellung, Fragen und Verneinung
- **Status:** ahead-of-student `ready` (Dean 2026-10-18; reconciled 2026-10-18); vier Lessons `unpiloted` (`unpiloted` blockiert die Durchführung nicht); per-Student delivery confirmation erfolgt bei der Durchführung

---

## Deutsch

### 1. Identifikation

- Kurs: Між B1 та B2; Modul 1 — A2-Wiederherstellung; Thema 1 — Wortstellung, Fragen und Verneinung.
- Dialogsprache und Sprache des Materials: Deutsch als Quelle mit vollständiger ukrainischer Übersetzung in derselben Datei (verbindliche Regel des Nutzers über den Dekan; nichts auf Englisch, außer technischen Bezeichnern).
- Verantwortliche Profession: Lecturer. Aufgelöster Worker: `university/workers/ferdinand/WORKER.md` (Lecturer, Language Faculty, active, Scope Language Faculty). Aktivierung: Profession + Worker; Fähigkeiten = Basis-Skills des Lecturers (Worker hat keine zusätzlichen Skills); benutzt wurden `research-materials` und `author-material` als Werkzeuge.
- Git-Root vor der Arbeit geprüft: `university-core`.

### 2. Contract 1 — Dean → Lecturer

- **Eingang:** begrenzter Lehrauftrag für Thema 1 (4 Plätze, Plätze verbleibend 4), ohne Studenten-Kontext; Vorbereitung vor einem Studenten (`theme-design.md`, `lesson-preparation.md`, „Preparing ahead of a Student“).
- **Ausgang:** `lesson-01-verb-position-2-statements.md`, `lesson-02-questions.md`, `lesson-03-negation-and-connectors.md`, `lesson-04-theme-checkpoint.md`; das Dozenten-Material `lecturer-evidence-guide.md` (Lösungen der Nachweis-Aufgaben, Checkpoint-Aufgabenpaket, Beobachtungsraster, Contract-6-Gerüst; **zusätzliche Datei**, keine zusätzliche Lektion); `material-review.md`; dieses Protokoll.
- **Grenze:** keine neuen Plätze, keine Änderung von Kriterien, Reihenfolge, Stoppbedingung; THEME.md, MODULE.md, COURSE.md unverändert; kein Studenten-Zustand gelesen.
- **Dean-Entscheidungen angewendet:** Hören/Sprechen nur `attested` (dieses Thema beansprucht nichts); Checkpoint-Versuch `NO_AI`, kein Wörterbuch; Überarbeitung `AI_ASSISTED` nur wenn angegeben; Provenienz je Quelle.
- **Bereitschaftsentscheidung (Dekan):** ahead-of-student `ready` (2026-10-18). Das öffentliche Paket ist lieferfähig; `unpiloted` blockiert die Durchführung nicht (ADR 0010, `curriculum-authority.md`). Die per-Student confirmation (Nachweise, ausgelassene Kriterien, Duplikat-Test gegen vorherige Nachweise) ist kein öffentlicher Blocker, sondern ein Schritt bei der Durchführung für jeden Studenten. Entscheidung zu N10: Kriterium 5 verlangt einen gefundenen und korrigierten Fehler; „nur einer von mehreren Fehlern gefunden“ erfüllt Kriterium 5 und darf in Rasterzeile 5 nicht schwächer bewertet werden. Rasterzeile 5 wird entsprechend angeglichen (kleine Korrektur der Dozentin bzw. des Dozenten). Nicht überprüfte Beispielsätze (siehe `unverified`) bleiben Beispiele, keine Regeln.

### 3. Genehmigter Rahmen (Quelle: THEME.md, nicht kopiert)

Ergebnis, 5 Erfolgskriterien, Ausschlüsse (Nebensätze, Relativsätze, B2-Satzbau, Grammatiküberblick, Artikel/Kasus, Zeitformen), endliche Lektionskarte (4 Plätze), Checkpoint und Stoppbedingung stehen in `THEME.md`. Die vorbereitete Reihenfolge entspricht der Karte unverändert.

Anpassungen innerhalb der Plätze (nach `learning-content-authority.md`, form- und beispielneutral): kurze Verwendung von *möchten/können/müssen* mit Verb am Ende als reine Wortstellung (Formen aus der Wortbox); `kein-`-Formen als Wortbox-Chunks (Endungen gehören zu Thema 2); der Fall „eigener Text ohne Wortstellungsfehler“ im Checkpoint wird mit einem Ersatztext innerhalb von Platz 4 gelöst (siehe **Dekan-Entscheidung zu Kriterium 5** unten).

**Dekan-Entscheidung zu Kriterium 5 (in `THEME.md` eingetragen):** Ein eigener Wortstellungsfehler wird gefunden und korrigiert. Enthält der eigene Text keinen solchen Fehler, findet und korrigiert der Student stattdessen den Wortstellungsfehler in einem vorgegebenen kurzen Text. Umsetzung durch die Lehrperson: Lektion 4 (Teil 3, Schritt 5, Zeitplan, Rückgabe) und `lecturer-evidence-guide.md` (Ersatztexte mit Schlüssel, Auslöser = Befund der Lehrperson, Vorrangregel, Rasterzeile 5, Contract-6-Gerüst); innerhalb von Platz 4, keine zusätzliche Lektion; der Ersatztext ist eine Ersatzbeobachtung, kein Nachweis am eigenen Text.

### 4. Rückverfolgbarkeit: Modul-Kriterium → Thema-Kriterium → Lektion (Delta) → nächstes Ergebnis

| Modul 1 Exit | Thema-Kriterium | Lektion und Evidence Delta (relativ zur Lektionskarte) | Baut auf | Ermöglicht |
|---|---|---|---|---|
| 1 | 1 | **L1** — Aussagesätze mit Verb an Position 2, auch nach Zeit/Ort; Erkennen falscher Verbstellung | Nachweis aus Course Entry (zur Durchführung zu prüfen) | L2 (Fragen mit Verb an Position 1/2) |
| 1 | 2 | **L2** — aus Aussagen richtige Ja/Nein- und W-Fragen bilden; Fragen zu einer Situation schreiben | L1 | L3 (Verneinung/Konjunktionen in Sätzen, Fragen, Antworten) |
| 1 | 3, 4 | **L3** — `nicht`/`kein-` mit richtiger Bedeutung; zwei Sätze mit `und/aber/oder/denn` verbinden | L1, L2 | L4 (integrierter Checkpoint) |
| 1; 5 (teilweise); 6 (teilweise: Lesen, Schreiben) | 1–5 | **L4** — ohne Hilfe, neue Situation, alle Kriterien zusammen; Leseaufgabe; eigener Fehler erkannt und korrigiert | L1–L3 | Contract 6 an den Dekan |

Hinweise: Kriterium 5 hat nur einen Pflichtnachweis (L4: eigener Fehler oder, wenn der eigene Text keinen hat, Ersatztext) plus freiwillige Zusatzbeobachtungen in L2/L3. Hören und Sprechen: nicht beansprucht. Exit-Kriterien 2, 3, 4 gehören zu den Themen 2–4.

### 5. Ausgelassene / bereits nachgewiesene Kriterien; Studenten-Kontext

Es gibt keinen Studenten und keinen Studenten-Zustand. **Aufgeschoben auf die Durchführung:** Laden des echten Nachweises und ausgelassener Kriterien; Duplikat-Test gegen den echten Nachweis (insbesondere gegen den öffentlichen Eingangstest Teil A Aufgaben 1, 2, 4 und Teil B Aufgaben 7, 8, und gegen frühere Arbeiten); Frage an den Studenten nach eigenem Material; Entscheidung des Dekans über Überspringen eines Platzes; Passung nach Contract 2. Öffentliches Material (Lektionskarte, Eingangstest-Text) wurde bei der Vorbereitung benutzt, um Wiederholungen zu vermeiden.

### 6. Contract 5 — Lecturer → Instructional Assistant

- **Eingabe:** vollständiges Paket (4 Lektionen, Dozenten-Material, Rahmen, öffentlicher Eingangstest), Ziel, Kriterien, Lernerkontext, Evidence Delta je Lektion, KI-Modus, Beweislast, Ausschlüsse, Provenienz; Studenten-Duplikat-Test ausdrücklich aufgeschoben.
- **Ausgabe Stufe 1:** `ready_with_changes`, 20 Befunde; **Stufe 2 (gezielt):** `ready_with_changes`, 10 neue Befunde; **Stufe 3 (gezielt, nach Dekan-Entscheidung zu Kriterium 5):** `ready_with_changes`, N1–N9 und B5e `gelöst`, 9 neue Befunde T1–T9 (T1–T8 bearbeitet, T9 Rahmenhinweis). Frühere Formulierung „delivery `not_ready` ohne Duplikat-Test“ meint den per-Student Schritt bei der Durchführung, nicht einen öffentlichen Blocker (Dean 2026-10-18 / ADR 0010).
- **Dispositionen:** siehe `material-review.md` (Abschnitte 5, 6 und 6a). Offen/aufgeschoben: nicht verifizierte Aussagen (T9 und Ablageort sind vom Dekan geschlossen) (Abschnitt 11), Überschneidung mit dem Eingangstest bei der Durchführung, Wortschatz-Feinschliff beim Pilotdurchlauf.
- **Bereitschaftssignal:** `ready_with_changes`, danach N1–N9 bearbeitet. Die kleinen Korrekturen T1–T8 wurden vom Instructional Assistant nicht erneut geprüft; die Lehrperson hat sie in beiden Sprachen kontrolliert.

### 7. Translator-Übergabe und semantische Äquivalenz

- Übergabe an die Translator Profession (Worker laut `university/workers/maria/WORKER.md`) nach der Quellkontrolle; zwei Läufe: L1–L2 und L3–L4 mit Dozenten-Material. Signale: alle fünf Dateien `localized_with_questions`; deutsche Teile unverändert; Terminologie einheitlich (Урок, Тема, Лектор, позиція 1/2, розповідне речення, самостійне речення, W-питання, питання «так/ні», сполучник, Вправа/Свідчення).
- **Lehrperson-Prüfung der Äquivalenz (vollständige Lektüre):** Die ukrainischen Abschnitte aller Dateien (`lesson-01` bis `lesson-04`, `lecturer-evidence-guide.md`; `THEME.md` und die Records auf Strukturgleichheit) wurden Abschnitt für Abschnitt mit dem deutschen Text verglichen, einschließlich Tabellen, Aufgaben, Lösungen, Rückgabe, `NO_AI`, Evidenzklassen und der Ersatztexte. Ergebnis: keine Bedeutungsabweichung; Strukturzählung gleich; kein englischer Fließtext (Bezeichner ausgenommen). Gefundene Abweichungen und Maßnahmen: (a) Wort „німецькою“ in Schreibanweisungen und Glossen sind bewusste Zusätze der Lokalisierung (Beweislast unverändert); (b) die Zeitplanformulierung zu Teil 3 in `lesson-04` war in beiden Sprachen gleich ungenau (T1) und wurde in beiden korrigiert; (c) die ukrainischen Stellen nach den Korrekturen N1–N9 und T1–T8 hat die Lehrperson selbst nachgezogen, nicht der Translator.
- **Fragen des Translators und Dispositionen:**
  - L1/L2: Q1 englische Modulbezeichnung — `accepted` (Dekan-Entscheidung: Modulnamen deutsch und ukrainisch; in allen Dateien dieses Themas umgesetzt); Q2 Wort „німецькою“ in Anweisungen — `accepted`; Q3 „alle Wörter in der Box“ — `accepted`, Quelle in L1 geändert; Q4 Reihenfolge in Lösungen — `deferred` (Beobachtung beim Pilotdurchlauf); Q5 *heute Abend* — `deferred`; Q6 Beispiel mit Lena — `accepted`, geändert; Q7 *wie viel/wie viele* — `deferred` (keine neue Regel); Q8 *Karte* — `accepted` (*Eintrittskarte*); Q9 Beispiel zu Aufg. 1 — `deferred`.
  - L3/L4/Dozenten-Material: Q1 Textlänge — `accepted` (Vorgabe auf „etwa 6 bis 8 Sätze“); Q2 Lese-Item 4 — `accepted` (Beobachtungstext korrigiert); Q3 Wortbox „nach haben, brauchen, kaufen“ vs. *trinken* — `deferred`; Q4 „jedes Thema“ Kleinschreibung — `deferred`; Q5 Klammer zu „Denn …“ — `deferred`; Q6 Abgleich der Begriffe L1–L4 — `accepted` (Terminologie einheitlich).
  - Vorschlag des Translators, in L3 einen Hinweis auf „не/немає“ für beide Wörter zu geben: `deferred` (neuer Lehrinhalt; Entscheidung beim Pilotdurchlauf).
- **Zweite Instructional-Assistant-Prüfung nach der Lokalisierung:** nicht verlangt; Lernweg unverändert.

### 8. Teacher, Laboratory Specialist, Learning Analyst, Examiner

- Teacher: nicht nötig (kein konkreter Verstärkungsbedarf ohne Student).
- Laboratory Specialist: nicht nötig (keine praktische Lücke außerhalb der Lektionsaufgaben).
- Learning Analyst: nicht nötig (keine Dekan-Bewertungsanfrage); mögliche Messbarkeitsberatung erst auf Anfrage des Dekans.
- Examiner: nicht nötig (keine Modulprüfung).
- Der Instructional Assistant und der Translator wurden als Professions angefragt, nicht als benannte Worker.

### 9. Abschließende Kontrolle der Lehrperson und Entscheidung des Dekans

- **Kontrolle aus Lernersicht** (nach Stufe 1, nach Stufe 2 und nach den Korrekturen N1–N9): Ziel, Voraussetzungen, Wortschatz, Erklärungen, Beispiele, Aufgaben, Rückgabe, Provenienz, KI-Modus und Grenzen der Evidenzklasse wurden in allen vier Lektionen und im Dozenten-Material gelesen; Widersprüche zwischen Regeln und Schlüsseln (N1, N2) wurden behoben. Die ukrainischen Abschnitte wurden nach der Lokalisierung vollständig gelesen (Abschnitt 7).
- **Lehrperson-Signal:** kein eigenes `ready` (Bereitschaft liegt beim Dekan). Empfehlung an den Dekan: Sichtkontrolle der Änderungen T1–T8 (laut Instructional Assistant genügt das); Kenntnisnahme der nicht verifizierten Aussagen (Abschnitt 11).
- **Entscheidung des Dekans:** ahead-of-student `ready` (2026-10-18); Statuszeilen und dieses Protokoll am 2026-10-18 mit ADR 0010 abgeglichen (`unpiloted` ≠ Blocker; per-Student confirmation bei der Durchführung).

### 10. Contract 6 und Stopp-/Nächste-Entscheidung

Nach Abschluss des Themas mit einem Studenten übergibt die Lehrperson Contract 6 an den Dekan (Gerüst im Dozenten-Material, Abschnitt 7): Sequence ID Thema 1, Plätze 1–4; Kriterien 1–5; formativer Lernnachweis in Lesen und Schreiben, **kein** Nachweis in Hören/Sprechen, keine unabhängige Messung; Lücken, Material-Kritik getrennt vom Nachweis; Empfehlung im Rahmen der Befugnis. Stoppbedingung laut THEME.md: Das Thema endet nach Lektion 4 oder wenn der Nachweis zeigt, dass das Kriterium stabil ist. Ungelöste Lücken gehen als begrenzte Entscheidung an den Dekan, es gibt keine zusätzliche Lektion. Der Fall „kein eigener Fehler im Checkpoint-Text“ ist als offene Dekan-Entscheidung vorgesehen. Nächste Entscheidung: Thema bestätigen, nächstes Thema öffnen, begrenzte Korrektur oder unabhängige Messung.

### 11. Provenienz (je Quelle: URL oder Pfad, Rolle, benutzte Abschnitte, Art)

| Quelle | Rolle | Benutzte Abschnitte | Art |
|---|---|---|---|
| Goethe Rahmencurriculum A2–B1, https://www.goethe.de/resources/files/pdf209/rahmencurriculum-integrationskurs_20171.pdf | ergänzend (Einordnung der Kommunikationsziele) | Beschreibungen sprachlicher Handlungen zu Konnektoren und Satzmustern (Abschnitte der Lernziel-Kataloge); kein Grammatikregelwerk; Text per PDF-Extraktion gelesen | `reference-only`, nichts kopiert |
| https://de.wikipedia.org/wiki/Verbzweitstellung | ergänzend (Kontrolle der V2-Regel und der Position-0-Konjunktionen) | Abschnitte zu Verbzweitstellung, Vorfeld, Konjunktionen | `reference-only` |
| https://de.wikipedia.org/wiki/Satzklammer | ergänzend (Kontrolle: finites Verb an Position 2, Infinitiv am Ende) | Einleitung und Beispiele | `reference-only` |
| https://mein-deutschbuch.de/files/grammatik/negation/negation.pdf (Arbeitsblatt „Negation (Verneinung)“, Online-Grammatik) | ergänzend, **geöffnet und gelesen** | Abschnitt 2 „Satznegation und Satzstellung von nicht“, Abschnitt 4 „Negation mit kein“ | `reference-only`, nichts kopiert; Urheberrecht des Arbeitsblattes beachtet |
| https://www.duden.de/sprachwissen/sprachratgeber/Das-Komma-zwischen-gleichrangigen-S%C3%A4tzen | ergänzend, **geöffnet und gelesen** | Regel zum Komma zwischen gleichrangigen Sätzen (und/oder: in der Regel kein Komma; aber/denn: Komma) | `reference-only` |
| https://en.wikipedia.org/wiki/German_grammar | geprüft und nicht benutzt | allgemeiner Abschnitt zur V2-Stellung; zu allgemein | ausgeschlossen |
| `university/courses/german-between-b1-and-b2/pre-course/entry-diagnostic-part-a.md`, `entry-diagnostic-part-b.md` (öffentliche Repository-Dateien) | geprüft, um Wiederholungen zu vermeiden | Aufgaben zu Satzbau, Fragen, Verneinung, Korrektur | nicht kopiert; Überschneidungen bei der Durchführung zu prüfen |
| `.../themes/theme-01-word-order-and-questions/THEME.md`, MODULE.md, COURSE.md | primärer Rahmen | Ergebnis, Kriterien, Karte, Evidence-Klassen | Rahmen, unverändert |
| Erklärungen, Beispiele, Aufgaben, Checkpoint-Aufgabenpaket in Lektionen 1–4 und Dozenten-Material | — | — | `original` (neu geschrieben) |

**Prüfung der Grammatikaussagen gegen geöffnete Quellen (zweiter Durchgang auf Auftrag des Dekans):**

- **verifiziert** (Quelle geöffnet und gelesen): (1) `kein-` bei Nomen mit unbestimmtem Artikel oder Nullartikel, `nicht` bei bestimmtem Artikel und bei Verb/Adjektiv/Ort; (2) Stellung von `nicht` (Satzende; vor dem Verb am Ende; vor Präpositional-/Richtungs-/Ortsergänzung; vor Adjektiv; nicht auf Position 1 bei Satznegation; Wortnegation mit Betonung); (3) `kein`/`keine`/`keinen` (Akkusativ Maskulinum *keinen*) — alle drei in mein-deutschbuch (Abschnitte 2 bis 4); (4) Komma: kein Komma vor `und`/`oder` zwischen Hauptsätzen in der Regel, Komma vor `aber`/`denn` — Duden-Sprachratgeber; (5) finites Verb an Position 2 im Hauptsatz, Infinitiv am Satzende, Konjunktionen außerhalb des Vorfelds — de.wikipedia Verbzweitstellung und Satzklammer; (6) **Ja/Nein-Frage mit Verb an erster Stelle (V1)** — de.wikipedia Fragesatz („durch ein Verb in Anfangsstellung … V1-Stellung“) und easy-deutsch.de/satzbau/fragen („Bei Ja/Nein-Fragen steht das Verb auf Position 1“); (7) **W-Frage**: Fragewort am Satzanfang, finites Verb an zweiter Stelle, auch *Wer hat das getan?* (Fragewort ist Subjekt) — de.wikipedia Fragewort (Interrogativpronomen), Beispiele *Was hast du nur getan?*, *Wer hat das getan?*; (8) **`denn` nebenordnend, `weil` unterordnend mit Verb am Ende** — de.wikipedia Konjunktion (Wortart) (nebenordnend: und, oder, aber, denn, sondern; unterordnend mit Verb am Ende: weil, dass, ob) und Duden-Eintrag *denn* (Begründung, Beispielsatz mit Hauptsatz-Stellung *wir blieben zu Hause, denn das Wetter war schlecht*), Satzklammer (Beispiel *weil … nicht sehen konnte*).
- **teilweise verifiziert / `unverified` (Idiomatik einzelner Beispielsätze, keine Regeln):** (a) *Ist das Schwimmbad am Sonntag offen?* und *Wann ist die Bank offen?*: Duden *offen* bestätigt nur die Bedeutung „nicht geschlossen; geöffnet“, nicht ausdrücklich die Verwendung für Geschäfte/Bank/Schwimmbad (`unverified`; als Beispielsatz in Lektion 2 beibehalten, im Dozenten-Material mit Alternativen *geöffnet/öffnet*); (b) *Was machst du beruflich?*: Duden *beruflich* bestätigt die Bedeutung („den Beruf betreffend“) und führt die Wendung nach dem Prüfergebnis als üblich auf (nur Hinweis der Seitenzusammenfassung; als `teilweise verifiziert` eingestuft); (c) *Ab wann ist das Schwimmbad am Morgen offen?* (nur im Dozenten-Material als Beispielantwort, nicht im Lerntext): `unverified`; (d) die Auswahl von *haben/brauchen/kaufen* in der Wortbox von Lektion 3 (die Akkusativ-Formen sind verifiziert, die Verbauswahl ist didaktisch).
- Nicht abrufbar: https://de.wikipedia.org/wiki/Komma_(Rechtschreibung), https://de.wikipedia.org/wiki/Negation_(Linguistik), https://de.wikipedia.org/wiki/Feldermodell_(Syntax), https://www.duden.de/sprachwissen/sprachratgeber/weil-oder-denn (HTTP 404); https://resources.german.lsa.umich.edu/grammatik/wortstellung (HTTP 403). Die geöffneten Seiten sind Online-Grammatiken und Wörterbücher (kein Universitätswerk); die Verifizierung ist durch die Zusammenfassung des Abrufwerkzeugs vermittelt, die Seiten wurden nicht in voller Länge von der Lehrperson gelesen. Eine unabhängige Zweitquelle bleibt für die Sprachfakultät offen.
- Lerntexte: Keine der unter `unverified` geführten Aussagen steht in einem Lerntext als Regel; es sind Beispielsätze.

### 12. Weitere Hinweise

- Im Repository `university-core` waren zum Zeitpunkt der Prüfung auch andere Dateien geändert (COURSE.md, MODULE.md aller Module, pre-course README und Assessor-Record). Diese Änderungen stammen nicht aus dieser Arbeit; sie wurden nicht angefasst.
- Es wurde nichts committet.

### 13. Dekan-Entscheidungen nach der Vorbereitung und eigene Endkontrolle der Befunde T1–T8

**Dekan-Entscheidungen (alle in den Dateien umgesetzt oder vom Dekan selbst eingetragen):**
1. Kriterium 5 mit Ersatztext (siehe Abschnitt 3); `THEME.md` vom Dekan angeglichen (Ergebnis, Checkpoint-Absatz, Lektionskarte Zeile 4; Befund T9 geschlossen).
2. Modulnamen auf Deutsch und Ukrainisch; in allen Dateien dieses Themas umgesetzt.
3. **Ablageort der Checkpoint-Aufgaben und der Lösungen: öffentlich in diesem Repository akzeptiert** (gleiche Entscheidung wie beim Eingangstest; das Modell der Universität kennt keinen geschützten Ort; ein Student kann Schlüssel lesen; nicht beobachtete Durchführung ist ein schwächerer Nachweis). Der aufgeschobene Punkt „Ablageort“ ist damit **geschlossen**. Praxis: frische Aufgaben mit denselben Merkmalen sind bei der Durchführung möglich, aber nicht verlangt.
4. Trennbare Verben werden in Thema 3 eingeführt (B11 geschlossen); Status und Tippfehler in `THEME.md` vom Dekan korrigiert (B20 geschlossen).

**Endkontrolle der Lehrperson zu den Befunden des Instructional Assistant (Stufe 3), selbst an den Zeilen geprüft; kein neuer Assistant-Aufruf, weil sich der Lernweg nicht ändert:**

| # | Prüfergebnis der Lehrperson |
|---|---|
| T1 | `lesson-04`: Zeitplan (45/50 Minuten), Tabelle Teil 3 und Schritt 5 nennen als Auslöser „Ihr Text hat keinen Fehler in der Wortstellung“ bzw. die Prüfung durch die Lehrperson; ukrainischer Text gleich. Erledigt. |
| T2 | Dozenten-Material, Abschnitt „Ersatztext“: Auslöser ist der Befund der Lehrperson; falsche „Korrekturen“ und falsche Wahl `nicht`/`kein-` als Zusatzbeobachtung. Erledigt. |
| T3 | Vorrangregel (nicht gefunden → `nicht gezeigt`; falsch korrigiert oder zusätzlich falsche „Korrektur“ → `unsicher`; richtig und ohne falsche Korrektur → `gezeigt`) im Dozenten-Material; Rasterzeile 5 verweist darauf. Erledigt. |
| T4 | Prüfung des eigenen Textes während der Pause; Ersatztext vor Teil 3 bereit. Erledigt. |
| T5 | Text 3 neu (*morgen ich arbeite bis 18 Uhr …*), voller Schlüssel; keine Nähe mehr zu L1 Aufg. 3 Nr. 1 und zum Lesetext. Erledigt. |
| T6 | Text 2 neu (Leipzig, *wohne bei Oma*); *bei Oma* steht in der Wortliste von L1. Erledigt. |
| T7 | Merkmale eines Ersatztextes im Dozenten-Material (3 bis 4 Sätze, genau ein Wortstellungsfehler, nur Stoff aus L1 bis L3, sonst fehlerfrei). Erledigt. |
| T8 | `lesson-04`, „Das geben Sie zurück“: Rückgabe des Ersatztextes mit *Korrektur: …* ergänzt (beide Sprachen). Erledigt. |

Diese Endkontrolle ist keine Bereitschaftserklärung; die Entscheidung liegt beim Dekan.

---

## Українською (переклад)

### 1. Ідентифікація

- Курс: Між B1 та B2; Модуль 1 — Відновлення A2; Тема 1 — Порядок слів, питання і заперечення.
- Мова діалогу й матеріалу: німецька як джерело з повним українським перекладом у тому самому файлі (обов'язкове правило від користувача через Декана; нічого англійською, крім технічних позначень).
- Відповідальна Професія: Lecturer. Визначений Worker: `university/workers/ferdinand/WORKER.md` (Lecturer, Language Faculty, active, scope Language Faculty). Активація: Професія + Worker; можливості = базові Skills Лектора (додаткових Skills у Worker немає); використано `research-materials` і `author-material` як інструменти.
- Корінь Git перевірено до роботи: `university-core`.

### 2. Contract 1 — Декан → Лектор

- **Вхід:** обмежене навчальне доручення для Теми 1 (4 слоти, залишилося 4), без контексту Студента; підготовка до появи Студента (`theme-design.md`, `lesson-preparation.md`, «Preparing ahead of a Student»).
- **Вихід:** `lesson-01-verb-position-2-statements.md`, `lesson-02-questions.md`, `lesson-03-negation-and-connectors.md`, `lesson-04-theme-checkpoint.md`; матеріал для Лектора `lecturer-evidence-guide.md` (розв'язки до свідчень, пакет завдань чекпойнту, таблиця спостережень, каркас Contract 6; **додатковий файл**, не додатковий Урок); `material-review.md`; цей протокол.
- **Межа:** нових слотів немає, критерії, порядок і умова зупинки не змінені; THEME.md, MODULE.md, COURSE.md не змінені; стан Студента не читався.
- **Застосовані рішення Декана:** Hören/Sprechen лише `attested` (ця Тема нічого не заявляє); спроба чекпойнту `NO_AI`, без словника; виправлення `AI_ASSISTED` лише коли оголошено; походження за кожним джерелом.
- **Рішення про готовність (Декан):** ahead-of-student `ready` (2026-10-18). Публічний пакет готовий до проведення; `unpiloted` не блокує проведення (ADR 0010, `curriculum-authority.md`). Підтвердження для кожного Студента (свідчення, пропущені критерії, тест на дублювання) — крок під час проведення, а не блокер публічної готовності. Рішення щодо N10: критерій 5 вимагає одну знайдену й виправлену помилку; «знайдено лише одну з кількох помилок» виконує критерій 5 і не може оцінюватися слабше в рядку 5 таблиці. Рядок 5 узгоджується відповідно (невелика корекція Лектора). Неперевірені приклади речень (див. `unverified`) лишаються прикладами, а не правилами.

### 3. Затверджена рамка (джерело: THEME.md, не скопійовано)

Результат, 5 критеріїв успіху, виключення (підрядні, означальні підрядні, синтаксис B2, огляд граматики, артиклі/відмінки, часові форми), скінченна карта Уроків (4 слоти), чекпойнт і умова зупинки — у `THEME.md`. Підготовлений порядок точно відповідає карті.

Пристосування в межах слотів (за `learning-content-authority.md`, форма й приклади вільні): коротке вживання *möchten/können/müssen* з дієсловом у кінці лише як порядок слів (форми з блоку слів); форми `kein-` як готові фрагменти з блоку слів (закінчення належать до Теми 2); випадок «власний текст без помилки порядку слів» у чекпойнті розв'язується замінним текстом у межах слота 4 (див. **рішення Декана щодо критерію 5** нижче).

**Рішення Декана щодо критерію 5 (внесено в `THEME.md`):** власну помилку порядку слів знаходять і виправляють. Якщо у власному тексті такої помилки немає, Студент натомість знаходить і виправляє помилку порядку слів у заданому короткому тексті. Реалізація Лектором: Урок 4 (частина 3, крок 5, план часу, повернення) і `lecturer-evidence-guide.md` (замінні тексти з ключем, підстава = висновок Лектора, правило пріоритету, рядок 5 таблиці, каркас Contract 6); у межах слота 4, додаткового Уроку немає; замінний текст є замінним спостереженням, а не свідченням на власному тексті.

### 4. Простежуваність: критерій Модуля → критерій Теми → Урок (приріст) → наступний результат

| Exit Модуля 1 | Критерій Теми | Урок і Evidence Delta (щодо карти Уроків) | Спирається на | Уможливлює |
|---|---|---|---|---|
| 1 | 1 | **У1** — розповідні речення з дієсловом на позиції 2, зокрема після часу/місця; розпізнавання хибного місця дієслова | свідчення Course Entry (перевірити під час проведення) | У2 (питання з дієсловом на позиції 1/2) |
| 1 | 2 | **У2** — утворення правильних питань «так/ні» та W-питань із тверджень; питання до ситуації | У1 | У3 (заперечення/сполучники в реченнях, питаннях, відповідях) |
| 1 | 3, 4 | **У3** — `nicht`/`kein-` із правильним змістом; поєднання двох речень через `und/aber/oder/denn` | У1, У2 | У4 (інтегрований чекпойнт) |
| 1; 5 (частково); 6 (частково: Lesen, Schreiben) | 1–5 | **У4** — без допомоги, нова ситуація, усі критерії разом; завдання на читання; виявлення й виправлення власної помилки | У1–У3 | Contract 6 Декану |

Примітки: критерій 5 має лише один обов'язковий доказ (У4: власна помилка або, якщо у власному тексті її немає, замінний текст) і необов'язкові додаткові спостереження в У2/У3. Hören і Sprechen не заявлено. Exit-критерії 2, 3, 4 належать Темам 2–4.

### 5. Пропущені / уже підтверджені критерії; контекст Студента

Студента й стану Студента немає. **Відкладено до проведення:** завантаження справжнього свідчення й пропущених критеріїв; тест на дублювання зі справжнім свідченням (зокрема з публічним вхідним тестом, частина A завдання 1, 2, 4 і частина B завдання 7, 8, та з попередніми роботами); запитання Студентові про власні матеріали; рішення Декана про пропуск слота; відповідність Contract 2. Під час підготовки використано публічні матеріали (карту Уроків, текст вхідного тесту), щоб уникнути повторів.

### 6. Contract 5 — Лектор → Instructional Assistant

- **Вхід:** повний пакет (4 Уроки, матеріал для Лектора, рамка, публічний вхідний тест), мета, критерії, контекст Студента, Evidence Delta кожного Уроку, режим ШІ, обсяг свідчень, виключення, походження; тест на дублювання для Студента прямо відкладено.
- **Вихід етапу 1:** `ready_with_changes`, 20 знахідок; **етап 2 (цільовий):** `ready_with_changes`, 10 нових знахідок; **етап 3 (цільовий, після рішення Декана щодо критерію 5):** `ready_with_changes`, N1–N9 і B5e розв'язано, 9 нових знахідок T1–T9 (T1–T8 опрацьовано, T9 — рамкова примітка). Раніше «delivery `not_ready` без тесту на дублювання» означає per-Student крок під час проведення, а не публічний блокер (Декан 2026-10-18 / ADR 0010).
- **Рішення:** див. `material-review.md` (розділи 5, 6 і 6a). Відкрито/відкладено: неперевірені твердження (T9 і місце зберігання закрито Деканом) (розділ 11), збіги з вхідним тестом під час проведення, доведення лексики під час пілотного проходження.
- **Сигнал готовності:** `ready_with_changes`, потім опрацьовано N1–N9. Дрібні виправлення T1–T8 Instructional Assistant повторно не перевіряв; Лектор перевірив їх в обох мовах.

### 7. Передача Translator і семантична еквівалентність

- Передача Професії Translator (Worker за `university/workers/maria/WORKER.md`) після контролю джерела; два запуски: У1–У2 і У3–У4 з матеріалом для Лектора. Сигнали: усі п'ять файлів `localized_with_questions`; німецькі частини не змінені; термінологія однакова (Урок, Тема, Лектор, позиція 1/2, розповідне речення, самостійне речення, W-питання, питання «так/ні», сполучник, Вправа/Свідчення).
- **Перевірка еквівалентності Лектором (повне читання):** українські розділи всіх файлів (`lesson-01`–`lesson-04`, `lecturer-evidence-guide.md`; `THEME.md` і записи — на однакову структуру) порівняно розділ за розділом із німецьким текстом, зокрема таблиці, завдання, розв'язки, повернення, `NO_AI`, класи свідчень і замінні тексти. Результат: відхилень у змісті немає; підрахунок структури однаковий; англійського прозового тексту немає (крім позначень). Знайдені відхилення й дії: (а) слово «німецькою» в інструкціях до письма та глоси — свідомі доповнення локалізації (обсяг свідчень не змінено); (б) формулювання плану часу для частини 3 в `lesson-04` було однаково неточним в обох мовах (T1) і виправлене в обох; (в) українські місця після виправлень N1–N9 і T1–T8 Лектор виправляв сам, а не Translator.
- **Питання Translator і рішення:**
  - У1/У2: Q1 англійська назва Модуля — `accepted` (рішення Декана: назви Модулів німецькою й українською; застосовано в усіх файлах цієї Теми); Q2 слово «німецькою» в інструкціях — `accepted`; Q3 «alle Wörter in der Box» — `accepted`, джерело в У1 змінено; Q4 порядок у розв'язках — `deferred` (спостереження під час пілотного проходження); Q5 *heute Abend* — `deferred`; Q6 приклад із Lena — `accepted`, змінено; Q7 *wie viel/wie viele* — `deferred` (нового правила немає); Q8 *Karte* — `accepted` (*Eintrittskarte*); Q9 приклад до завд. 1 — `deferred`.
  - У3/У4/матеріал для Лектора: Q1 довжина тексту — `accepted` (вимога «близько 6–8 речень»); Q2 пункт 4 для читання — `accepted` (текст спостереження виправлено); Q3 блок слів «nach haben, brauchen, kaufen» і *trinken* — `deferred`; Q4 «jedes Thema» з малої літери — `deferred`; Q5 дужки до «Denn …» — `deferred`; Q6 узгодження термінів У1–У4 — `accepted` (термінологія однакова).
  - Пропозиція Translator додати в У3 примітку про «не/немає» для обох слів: `deferred` (новий навчальний зміст; рішення під час пілотного проходження).
- **Друга перевірка Instructional Assistant після локалізації:** не вимагалася; шлях Студента не змінився.

### 8. Teacher, Laboratory Specialist, Learning Analyst, Examiner

- Teacher: не потрібно (конкретної потреби в закріпленні без Студента немає).
- Laboratory Specialist: не потрібно (практичної прогалини поза завданнями Уроків немає).
- Learning Analyst: не потрібно (запиту Декана на оцінювання немає); поради щодо вимірюваності — лише на запит Декана.
- Examiner: не потрібно (іспиту Модуля немає).
- Instructional Assistant і Translator запитано як Професії, а не як іменованих Worker.

### 9. Остаточний контроль Лектора і рішення Декана

- **Контроль із погляду Студента** (після етапу 1, після етапу 2 і після виправлень N1–N9): мету, передумови, лексику, пояснення, приклади, завдання, повернення, походження, режим ШІ та межі класу свідчень прочитано в усіх чотирьох Уроках і в матеріалі для Лектора; суперечності між правилами й ключами (N1, N2) усунуто. Українські розділи після локалізації прочитано повністю (розділ 7).
- **Сигнал Лектора:** власного `ready` немає (готовність за Деканом). Рекомендація Декану: оглянути зміни T1–T8 (за оцінкою Instructional Assistant цього достатньо); прийняти до відома неперевірені твердження (розділ 11).
- **Рішення Декана:** ahead-of-student `ready` (2026-10-18); рядки статусу й цей протокол узгоджено 2026-10-18 з ADR 0010 (`unpiloted` ≠ блокер; per-Student confirmation під час проведення).

### 10. Contract 6 і межа зупинки / наступного рішення

Після завершення Теми зі Студентом Лектор передає Декану Contract 6 (каркас — у матеріалі для Лектора, розділ 7): sequence ID Тема 1, слоти 1–4; критерії 1–5; формувальне навчальне свідчення з Lesen і Schreiben, **жодного** свідчення з Hören/Sprechen, незалежного вимірювання немає; прогалини, критика матеріалу окремо від свідчення; рекомендація в межах повноважень. Умова зупинки за THEME.md: Тема завершується після Уроку 4 або коли свідчення показує, що критерій стабільний. Нерозв'язані прогалини повертаються Декану як обмежене рішення, додаткового Уроку немає. Випадок «у тексті чекпойнту немає власної помилки» передбачено як відкрите рішення Декана. Наступне рішення: підтвердити Тему, відкрити наступну, обмежене виправлення або незалежне вимірювання.

### 11. Походження (за кожним джерелом: URL або шлях, роль, використані розділи, вид)

| Джерело | Роль | Використані розділи | Вид |
|---|---|---|---|
| Goethe Rahmencurriculum A2–B1, https://www.goethe.de/resources/files/pdf209/rahmencurriculum-integrationskurs_20171.pdf | допоміжне (співвіднесення комунікативних цілей) | описи мовних дій щодо сполучників і мовних моделей (розділи каталогів цілей); не є зводом граматичних правил; текст прочитано через витяг з PDF | `reference-only`, нічого не скопійовано |
| https://de.wikipedia.org/wiki/Verbzweitstellung | допоміжне (перевірка правила V2 і сполучників на позиції 0) | розділи про Verbzweitstellung, Vorfeld, Konjunktionen | `reference-only` |
| https://de.wikipedia.org/wiki/Satzklammer | допоміжне (перевірка: відмінюване дієслово на позиції 2, інфінітив у кінці) | вступ і приклади | `reference-only` |
| https://mein-deutschbuch.de/files/grammatik/negation/negation.pdf (аркуш «Negation (Verneinung)», онлайн-граматика) | допоміжне, **відкрито й прочитано** | розділ 2 «Satznegation und Satzstellung von nicht», розділ 4 «Negation mit kein» | `reference-only`, нічого не скопійовано; авторське право аркуша враховано |
| https://www.duden.de/sprachwissen/sprachratgeber/Das-Komma-zwischen-gleichrangigen-S%C3%A4tzen | допоміжне, **відкрито й прочитано** | правило про кому між рівноправними реченнями (und/oder: як правило без коми; aber/denn: кома) | `reference-only` |
| https://en.wikipedia.org/wiki/German_grammar | переглянуто й не використано | загальний розділ про V2; надто загальне | виключено |
| `university/courses/german-between-b1-and-b2/pre-course/entry-diagnostic-part-a.md`, `entry-diagnostic-part-b.md` (публічні файли репозиторію) | переглянуто, щоб уникнути повторів | завдання про будову речення, питання, заперечення, виправлення | не скопійовано; збіги перевірити під час проведення |
| `.../themes/theme-01-word-order-and-questions/THEME.md`, MODULE.md, COURSE.md | основна рамка | результат, критерії, карта, класи свідчень | рамка, без змін |
| Пояснення, приклади, завдання, пакет завдань чекпойнту в Уроках 1–4 і матеріалі для Лектора | — | — | `original` (написано заново) |

**Перевірка граматичних тверджень за відкритими джерелами (другий прохід за дорученням Декана):**

- **перевірено** (джерело відкрито й прочитано): (1) `kein-` з іменником із неозначеним артиклем або без артикля, `nicht` із означеним артиклем та з дієсловом/прикметником/місцем; (2) місце `nicht` (кінець речення; перед дієсловом у кінці; перед прийменниковою/напрямною/місцевою доповнювальною частиною; перед прикметником; не на позиції 1 при запереченні всього речення; заперечення частини речення з наголосом); (3) `kein`/`keine`/`keinen` (знахідний відмінок чол. роду *keinen*) — усе три в mein-deutschbuch (розділи 2–4); (4) кома: перед `und`/`oder` між головними реченнями, як правило, коми немає, перед `aber`/`denn` кома — Duden-Sprachratgeber; (5) відмінюване дієслово на позиції 2 в головному реченні, інфінітив у кінці, сполучники поза Vorfeld — de.wikipedia Verbzweitstellung і Satzklammer; (6) **питання «так/ні» з дієсловом на першому місці (V1)** — de.wikipedia Fragesatz («durch ein Verb in Anfangsstellung … V1-Stellung») і easy-deutsch.de/satzbau/fragen («Bei Ja/Nein-Fragen steht das Verb auf Position 1»); (7) **W-питання**: питальне слово на початку речення, відмінюване дієслово на другому місці, зокрема *Wer hat das getan?* (питальне слово є підметом) — de.wikipedia Fragewort (Interrogativpronomen), приклади *Was hast du nur getan?*, *Wer hat das getan?*; (8) **`denn` — сурядний, `weil` — підрядний із дієсловом у кінці** — de.wikipedia Konjunktion (Wortart) (сурядні: und, oder, aber, denn, sondern; підрядні з дієсловом у кінці: weil, dass, ob) і стаття Duden *denn* (причина, приклад із порядком слів головного речення *wir blieben zu Hause, denn das Wetter war schlecht*), Satzklammer (приклад *weil … nicht sehen konnte*).
- **частково перевірено / `unverified` (ідіоматичність окремих прикладів, не правила):** (а) *Ist das Schwimmbad am Sonntag offen?* і *Wann ist die Bank offen?*: Duden *offen* підтверджує лише значення «не зачинено; відчинено», але не прямо вживання для крамниць/банку/басейну (`unverified`; залишено як приклад в Уроці 2, у матеріалі для Лектора подано альтернативи *geöffnet/öffnet*); (б) *Was machst du beruflich?*: Duden *beruflich* підтверджує значення («den Beruf betreffend») і, за результатом перевірки, подає звороти як звичні (лише вказівка зі стислого викладу сторінки; оцінено як `частково перевірено`); (в) *Ab wann ist das Schwimmbad am Morgen offen?* (лише в матеріалі для Лектора як приклад відповіді, не в тексті для Студента): `unverified`; (г) добір *haben/brauchen/kaufen* у блоці слів Уроку 3 (форми знахідного відмінка перевірено, добір дієслів — дидактичний).
- Недоступні: https://de.wikipedia.org/wiki/Komma_(Rechtschreibung), https://de.wikipedia.org/wiki/Negation_(Linguistik), https://de.wikipedia.org/wiki/Feldermodell_(Syntax), https://www.duden.de/sprachwissen/sprachratgeber/weil-oder-denn (HTTP 404); https://resources.german.lsa.umich.edu/grammatik/wortstellung (HTTP 403). Відкриті сторінки — онлайн-граматики й словники (не університетські видання); перевірка опосередкована стислим викладом інструмента завантаження, сторінки Лектор повністю не читав. Незалежне друге джерело лишається відкритим для Мовного факультету.
- Тексти для Студента: жодне з тверджень `unverified` не подано в тексті для Студента як правило; це приклади речень.

### 12. Інші примітки

- У репозиторії `university-core` під час перевірки були змінені й інші файли (COURSE.md, MODULE.md усіх Модулів, README і assessor-record у pre-course). Ці зміни не походять з цієї роботи; їх не чіпали.
- Нічого не закомічено.

### 13. Рішення Декана після підготовки й власний остаточний контроль знахідок T1–T8

**Рішення Декана (усі реалізовані у файлах або внесені Деканом самим):**
1. Критерій 5 із замінним текстом (див. розділ 3); `THEME.md` Декан узгодив (результат, абзац про чекпойнт, рядок 4 карти Уроків; знахідка T9 закрита).
2. Назви Модулів німецькою й українською; застосовано в усіх файлах цієї Теми.
3. **Місце зберігання завдань чекпойнту й розв'язків: публічне в цьому репозиторії прийнято** (те саме рішення, що й для вхідного тесту; модель Університету не має захищеного місця; Студент може прочитати ключі; непідконтрольне проведення дає слабше свідчення). Відкладений пункт «місце зберігання» цим **закрито**. Практика: свіжі завдання з тими самими ознаками під час проведення можливі, але не вимагаються.
4. Відокремлювані дієслова вводяться в Темі 3 (B11 закрито); статус і одруківку в `THEME.md` Декан виправив (B20 закрито).

**Остаточний контроль Лектора щодо знахідок Instructional Assistant (етап 3), перевірено самостійно за рядками; нового виклику Assistant немає, бо шлях Студента не змінюється:**

| # | Результат перевірки Лектором |
|---|---|
| T1 | `lesson-04`: план часу (45/50 хвилин), таблиця частини 3 і крок 5 називають умовою «ваш текст не містить помилки порядку слів» або перевірку Лектором; український текст такий самий. Виконано. |
| T2 | Матеріал для Лектора, розділ «замінний текст»: підстава — висновок Лектора; хибні «виправлення» і хибний вибір `nicht`/`kein-` — додаткове спостереження. Виконано. |
| T3 | Правило пріоритету (не знайдено → `nicht gezeigt`; виправлено неправильно або додатково хибне «виправлення» → `unsicher`; правильно й без хибного виправлення → `gezeigt`) є в матеріалі для Лектора; рядок 5 таблиці посилається на нього. Виконано. |
| T4 | Перевірка власного тексту під час перерви; замінний текст напоготові до частини 3. Виконано. |
| T5 | Text 3 новий (*morgen ich arbeite bis 18 Uhr …*), повний ключ; близькості до У1 завд. 3 № 1 і до тексту для читання більше немає. Виконано. |
| T6 | Text 2 новий (Leipzig, *wohne bei Oma*); *bei Oma* є у словнику У1. Виконано. |
| T7 | Ознаки замінного тексту в матеріалі для Лектора (3–4 речення, рівно одна помилка порядку слів, лише матеріал У1–У3, інших помилок немає). Виконано. |
| T8 | `lesson-04`, «Das geben Sie zurück»: повернення замінного тексту з *Korrektur: …* додано (обома мовами). Виконано. |

Цей остаточний контроль не є заявою про готовність; рішення за Деканом.

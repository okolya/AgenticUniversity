#!/usr/bin/env python3
"""Apply Lektionslexik / Spiel / Schreiben / Recycle blocks to course lessons."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "modules"

# path relative to modules/ -> (checkpoint?, lemmas[(de, gloss)], game, schreiben_hint, recycle_from)
# game: match | luecken | rate
CATALOG: dict[str, dict] = {
    # Module 1 Theme 2
    "01-a2-recovery/themes/theme-02-articles-cases-pronouns/lesson-01-articles-gender-accusative.md": {
        "lemmas": [
            ("der Artikel", "артикль"),
            ("das Genus", "рід"),
            ("der Akkusativ", "знахідний"),
            ("ein/eine", "неозначений артикль"),
            ("das Objekt", "додаток"),
        ],
        "game": "match",
        "schreiben": "Schreiben Sie fünf kurze Sätze: benutzen Sie jeden Lemma-Begriff einmal (oder markieren Sie Artikel + Akkusativobjekt in eigenen Sätzen).",
    },
    "01-a2-recovery/themes/theme-02-articles-cases-pronouns/lesson-02-dative-prepositions-indirect-object.md": {
        "recycle": "Artikel, Genus, Akkusativ, ein/eine, Objekt",
        "lemmas": [
            ("der Dativ", "давальний"),
            ("mit", "з (Dativ)"),
            ("zu", "до (Dativ)"),
            ("von", "від (Dativ)"),
            ("das indirekte Objekt", "непрямий додаток"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze: je einmal Dativ, mit, zu, von, indirektes Objekt (oder Markierung im Satz).",
    },
    "01-a2-recovery/themes/theme-02-articles-cases-pronouns/lesson-03-pronouns-possessives-two-way-prepositions.md": {
        "recycle": "Dativ, mit, zu, von, indirektes Objekt",
        "lemmas": [
            ("das Pronomen", "займенник"),
            ("mein/dein", "присвійний"),
            ("in", "в (Wechsel)"),
            ("auf", "на (Wechsel)"),
            ("an", "біля/на (Wechsel)"),
        ],
        "game": "rate",
        "schreiben": "Fünf Sätze mit Pronomen/Possessiv und je einer Wechselpräposition wo sinnvoll.",
    },
    "01-a2-recovery/themes/theme-02-articles-cases-pronouns/lesson-04-theme-checkpoint.md": {
        "checkpoint": True,
        "recycle_pack": "Artikel, Akkusativ, Dativ, Pronomen, mein/dein, in/auf/an",
    },
    # Module 1 Theme 3
    "01-a2-recovery/themes/theme-03-time-reference-and-verb-forms/lesson-01-present-separable-modal-verbs.md": {
        "lemmas": [
            ("das Präsens", "теперішній час"),
            ("trennbar", "віддільне дієслово"),
            ("aufstehen", "вставати"),
            ("können", "могти"),
            ("müssen", "мусити"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze: Präsens; ein trennbares Verb; aufstehen; können; müssen.",
    },
    "01-a2-recovery/themes/theme-03-time-reference-and-verb-forms/lesson-02-perfekt-haben-sein.md": {
        "recycle": "Präsens, trennbar, aufstehen, können, müssen",
        "lemmas": [
            ("das Perfekt", "перфект"),
            ("haben", "допоміжне haben"),
            ("sein", "допоміжне sein"),
            ("gemacht", "Partizip II machen"),
            ("gegangen", "Partizip II gehen"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Perfekt-Sätze: haben/sein + passende Partizipien inkl. gemacht/gegangen.",
    },
    "01-a2-recovery/themes/theme-03-time-reference-and-verb-forms/lesson-03-past-modal-future-reference.md": {
        "recycle": "Perfekt, haben, sein, gemacht, gegangen",
        "lemmas": [
            ("war", "був/була"),
            ("hatte", "мав/мала"),
            ("wollte", "хотів (Präteritum)"),
            ("werden", "майбутнє/werden"),
            ("morgen", "завтра"),
        ],
        "game": "rate",
        "schreiben": "Fünf Sätze: war, hatte, wollte, werden+Infinitiv, morgen.",
    },
    "01-a2-recovery/themes/theme-03-time-reference-and-verb-forms/lesson-04-theme-checkpoint.md": {
        "checkpoint": True,
        "recycle_pack": "Präsens, Perfekt, haben/sein, war/hatte, werden/morgen",
    },
    # Module 1 Theme 4
    "01-a2-recovery/themes/theme-04-functional-vocabulary-and-integration/lesson-01-functional-situations.md": {
        "lemmas": [
            ("Entschuldigung", "перепрошую"),
            ("Können Sie …?", "чи можете ви…"),
            ("Ich hätte gern …", "я б хотів…"),
            ("Wie komme ich …?", "як пройти…"),
            ("Vielen Dank", "дякую"),
        ],
        "game": "match",
        "schreiben": "Fünf kurze Äußerungen/Sätze — jedes Lemma einmal in einer Alltagssituation.",
    },
    "01-a2-recovery/themes/theme-04-functional-vocabulary-and-integration/lesson-02-integrated-four-skills-cycle.md": {
        "recycle": "Entschuldigung, Können Sie, Ich hätte gern, Wie komme ich, Vielen Dank",
        "lemmas": [
            ("verstehen", "розуміти"),
            ("wiederholen", "повторити"),
            ("notieren", "занотувати"),
            ("antworten", "відповідати"),
            ("zusammenfassen", "стисло сказати"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze über Ihren Lernzyklus mit je einem Lemma.",
    },
    "01-a2-recovery/themes/theme-04-functional-vocabulary-and-integration/lesson-03-module-checkpoint-entry-gap.md": {
        "checkpoint": True,
        "recycle_pack": "Entschuldigung, Ich hätte gern, verstehen, wiederholen, antworten",
    },
    # Module 2 Theme 1
    "02-b1-recovery/themes/theme-01-connected-reading-and-information/lesson-01-main-idea-and-structure.md": {
        "lemmas": [
            ("die Hauptaussage", "головна думка"),
            ("der Abschnitt", "абзац"),
            ("zuerst", "спочатку"),
            ("dann", "потім"),
            ("schließlich", "нарешті"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze über einen Text: Hauptaussage, Abschnitt, zuerst/dann/schließlich.",
    },
    "02-b1-recovery/themes/theme-01-connected-reading-and-information/lesson-02-relevant-details.md": {
        "recycle": "Hauptaussage, Abschnitt, zuerst, dann, schließlich",
        "lemmas": [
            ("das Detail", "деталь"),
            ("die Textstelle", "місце в тексті"),
            ("belegen", "підтвердити цитатою"),
            ("relevant", "релевантний"),
            ("übersehen", "пропустити"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze: Detail + Textstelle nennen; belegen; relevant/übersehen erklären.",
    },
    "02-b1-recovery/themes/theme-01-connected-reading-and-information/lesson-03-context-vocabulary-and-summary.md": {
        "recycle": "Detail, Textstelle, belegen, relevant, übersehen",
        "lemmas": [
            ("der Kontext", "контекст"),
            ("schätzen", "здогадуватись за сенсом"),
            ("die Zusammenfassung", "стислий виклад"),
            ("mit eigenen Worten", "своїми словами"),
            ("unklar", "неясно"),
        ],
        "game": "rate",
        "schreiben": "Kurze Zusammenfassung (4–5 Sätze) mit jedem Lemma mindestens einmal sinngemäß.",
    },
    "02-b1-recovery/themes/theme-01-connected-reading-and-information/lesson-04-theme-checkpoint-unfamiliar-text.md": {
        "checkpoint": True,
        "recycle_pack": "Hauptaussage, Detail, Textstelle, Kontext, Zusammenfassung",
    },
    # Module 2 Theme 2
    "02-b1-recovery/themes/theme-02-experience-plans-opinions/lesson-01-experiences-in-sequence.md": {
        "lemmas": [
            ("die Erfahrung", "досвід"),
            ("zuerst", "спочатку"),
            ("danach", "після того"),
            ("plötzlich", "раптом"),
            ("am Ende", "наприкінці"),
        ],
        "game": "match",
        "schreiben": "Kurze Erzählung: fünf Sätze, jedes Lemma einmal.",
    },
    "02-b1-recovery/themes/theme-02-experience-plans-opinions/lesson-02-plans-reasons-consequences.md": {
        "recycle": "Erfahrung, zuerst, danach, plötzlich, am Ende",
        "lemmas": [
            ("der Plan", "план"),
            ("deshalb", "тому"),
            ("weil", "тому що"),
            ("die Folge", "наслідок"),
            ("beabsichtigen", "мати намір"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze zu einem Plan mit deshalb/weil/Folge/beabsichtigen.",
    },
    "02-b1-recovery/themes/theme-02-experience-plans-opinions/lesson-03-opinion-reason-counterpoint.md": {
        "recycle": "Plan, deshalb, weil, Folge, beabsichtigen",
        "lemmas": [
            ("die Meinung", "думка"),
            ("ich finde", "я вважаю"),
            ("der Grund", "причина"),
            ("andererseits", "з іншого боку"),
            ("trotzdem", "попри це"),
        ],
        "game": "rate",
        "schreiben": "Meinung + Grund + Gegenpunkt: fünf Sätze mit allen Lemmata.",
    },
    "02-b1-recovery/themes/theme-02-experience-plans-opinions/lesson-04-theme-checkpoint-integrated-contribution.md": {
        "checkpoint": True,
        "recycle_pack": "Erfahrung, Plan, deshalb, Meinung, andererseits",
    },
    # Module 2 Theme 3
    "02-b1-recovery/themes/theme-03-practical-writing-and-register/lesson-01-purpose-structure-and-details.md": {
        "lemmas": [
            ("der Zweck", "мета тексту"),
            ("die Anrede", "звертання"),
            ("der Schluss", "закінчення"),
            ("das Detail", "деталь"),
            ("klar", "зрозуміло"),
        ],
        "game": "match",
        "schreiben": "Skizzieren Sie Zweck/Anrede/Schluss in fünf kurzen Sätzen mit den Lemmata.",
    },
    "02-b1-recovery/themes/theme-03-practical-writing-and-register/lesson-02-anrede-register-and-request.md": {
        "recycle": "Zweck, Anrede, Schluss, Detail, klar",
        "lemmas": [
            ("Sie", "ввічливе ви"),
            ("du", "неформальне ти"),
            ("die Bitte", "прохання"),
            ("höflich", "ввічливо"),
            ("formell", "офіційно"),
        ],
        "game": "luecken",
        "schreiben": "Zwei Bitten: eine formell (Sie), eine mit du; fünf Sätze insgesamt mit allen Lemmata.",
    },
    "02-b1-recovery/themes/theme-03-practical-writing-and-register/lesson-03-revision-control-raster.md": {
        "recycle": "Sie, du, Bitte, höflich, formell",
        "lemmas": [
            ("überarbeiten", "переробити"),
            ("das Raster", "контрольна сітка"),
            ("prüfen", "перевірити"),
            ("korrigieren", "виправити"),
            ("klarer", "зрозуміліше"),
        ],
        "game": "rate",
        "schreiben": "Fünf Sätze: was Sie im Raster prüfen/überarbeiten/korrigieren.",
    },
    "02-b1-recovery/themes/theme-03-practical-writing-and-register/lesson-04-theme-checkpoint-practical-text.md": {
        "checkpoint": True,
        "recycle_pack": "Zweck, Anrede, Bitte, höflich, überarbeiten",
    },
    # Module 2 Theme 4
    "02-b1-recovery/themes/theme-04-interaction-repair-and-transfer/lesson-01-asking-and-confirming.md": {
        "lemmas": [
            ("Wie bitte?", "прошу повторити"),
            ("Meinen Sie …?", "ви маєте на увазі…"),
            ("Verstehe ich richtig …?", "чи правильно я розумію…"),
            ("genau", "саме так"),
            ("noch einmal", "ще раз"),
        ],
        "game": "match",
        "schreiben": "Fünf kurze Klärungsäußerungen — jedes Lemma einmal.",
    },
    "02-b1-recovery/themes/theme-04-interaction-repair-and-transfer/lesson-02-repairing-a-misunderstanding.md": {
        "recycle": "Wie bitte, Meinen Sie, Verstehe ich richtig, genau, noch einmal",
        "lemmas": [
            ("das Missverständnis", "непорозуміння"),
            ("entschuldigen", "перепрошувати"),
            ("klären", "зʼясувати"),
            ("ich meinte", "я мав на увазі"),
            ("jetzt ist klar", "тепер зрозуміло"),
        ],
        "game": "luecken",
        "schreiben": "Mini-Dialog (5 Zeilen) mit allen Lemmata.",
    },
    "02-b1-recovery/themes/theme-04-interaction-repair-and-transfer/lesson-03-transfer-and-self-correction.md": {
        "recycle": "Missverständnis, entschuldigen, klären, ich meinte, jetzt ist klar",
        "lemmas": [
            ("übertragen", "перенести"),
            ("die Situation", "ситуація"),
            ("selbst korrigieren", "самовиправлення"),
            ("unsicher", "невпевнено"),
            ("trotzdem", "попри це"),
        ],
        "game": "rate",
        "schreiben": "Fünf Sätze: Transfer in neue Situation + Selbstkorrektur.",
    },
    "02-b1-recovery/themes/theme-04-interaction-repair-and-transfer/lesson-04-module-checkpoint.md": {
        "checkpoint": True,
        "recycle_pack": "Wie bitte, klären, Missverständnis, übertragen, selbst korrigieren",
    },
    # Module 3 Theme 1
    "03-practice-and-readiness-check/themes/theme-01-transfer-reading-and-writing/lesson-01-reading-in-a-new-bounded-context.md": {
        "lemmas": [
            ("der Kontext", "контекст"),
            ("die Hauptaussage", "головна думка"),
            ("das Detail", "деталь"),
            ("die Textstelle", "місце з тексту"),
            ("unbekannt", "незнайомий"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze zum gelesenen Text mit allen Lemmata.",
    },
    "03-practice-and-readiness-check/themes/theme-01-transfer-reading-and-writing/lesson-02-writing-in-a-new-bounded-context.md": {
        "recycle": "Kontext, Hauptaussage, Detail, Textstelle, unbekannt",
        "lemmas": [
            ("zusammenhängend", "звʼязно"),
            ("die Struktur", "структура"),
            ("die Situation", "ситуація"),
            ("höflich", "ввічливо"),
            ("der Schluss", "закінчення"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze/Zeilen Ihrer Nachricht bewusst mit jedem Lemma markiert.",
    },
    "03-practice-and-readiness-check/themes/theme-01-transfer-reading-and-writing/lesson-03-theme-checkpoint-combined-rw.md": {
        "checkpoint": True,
        "recycle_pack": "Hauptaussage, Detail, zusammenhängend, Struktur, höflich",
    },
    # Module 3 Theme 2
    "03-practice-and-readiness-check/themes/theme-02-integrated-listening-speaking-practice/lesson-01-prescribed-listening-practice.md": {
        "lemmas": [
            ("zuhören", "слухати уважно"),
            ("notieren", "занотувати"),
            ("der Hauptpunkt", "головний пункт"),
            ("attested", "лише засвідчена практика"),
            ("kein Urteil", "без оцінки рівня"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze: was Sie gehört/notiert haben; attested/kein Urteil erklären.",
    },
    "03-practice-and-readiness-check/themes/theme-02-integrated-listening-speaking-practice/lesson-02-prescribed-speaking-practice.md": {
        "recycle": "zuhören, notieren, Hauptpunkt, attested, kein Urteil",
        "lemmas": [
            ("sprechen", "говорити"),
            ("die Antwort", "відповідь"),
            ("nachfragen", "уточнити"),
            ("verständlich", "зрозуміло"),
            ("kurz", "коротко"),
        ],
        "game": "rate",
        "schreiben": "Schreiben Sie fünf geplante Sprechzeilen mit allen Lemmata (vor dem Sprechen).",
    },
    "03-practice-and-readiness-check/themes/theme-02-integrated-listening-speaking-practice/lesson-03-theme-checkpoint-integrated-hs.md": {
        "checkpoint": True,
        "recycle_pack": "zuhören, notieren, sprechen, nachfragen, attested",
    },
    # Module 3 Theme 3
    "03-practice-and-readiness-check/themes/theme-03-revision-after-feedback/lesson-01-read-feedback-and-mark-target.md": {
        "lemmas": [
            ("das Feedback", "зворотний звʼязок"),
            ("markieren", "позначити"),
            ("die Zielstelle", "місце для правки"),
            ("das Kriterium", "критерій"),
            ("verstehen", "зрозуміти коментар"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze: was das Feedback sagt; welche Zielstelle; welches Kriterium.",
    },
    "03-practice-and-readiness-check/themes/theme-03-revision-after-feedback/lesson-02-targeted-revision.md": {
        "recycle": "Feedback, markieren, Zielstelle, Kriterium, verstehen",
        "lemmas": [
            ("überarbeiten", "переробити"),
            ("verbessern", "покращити"),
            ("derselbe Fokus", "той самий фокус"),
            ("die neue Version", "нова версія"),
            ("vergleichen", "порівняти"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze: was Sie überarbeiten/verbessern und wie Sie vergleichen.",
    },
    "03-practice-and-readiness-check/themes/theme-03-revision-after-feedback/lesson-03-theme-checkpoint-revision-cycle.md": {
        "checkpoint": True,
        "recycle_pack": "Feedback, Zielstelle, überarbeiten, verbessern, vergleichen",
    },
    # Module 3 Theme 4
    "03-practice-and-readiness-check/themes/theme-04-self-limits-checkpoint-and-measurement-handoff/lesson-01-name-remaining-limits.md": {
        "lemmas": [
            ("die Einschränkung", "обмеження"),
            ("gegenüber B1", "відносно B1"),
            ("konkret", "конкретно"),
            ("kein B2-Urteil", "без вердикту B2"),
            ("ehrlich", "чесно"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze Selbstlimits mit allen Lemmata.",
    },
    "03-practice-and-readiness-check/themes/theme-04-self-limits-checkpoint-and-measurement-handoff/lesson-02-bundle-module-evidence.md": {
        "recycle": "Einschränkung, gegenüber B1, konkret, kein B2-Urteil, ehrlich",
        "lemmas": [
            ("der Nachweis", "свідчення"),
            ("bündeln", "зібрати докупи"),
            ("demonstrated", "виміряно"),
            ("attested", "лише практика"),
            ("fehlt", "бракує"),
        ],
        "game": "luecken",
        "schreiben": "Fünf Sätze: was Sie bündeln; demonstrated vs attested; was fehlt.",
    },
    "03-practice-and-readiness-check/themes/theme-04-self-limits-checkpoint-and-measurement-handoff/lesson-03-module-checkpoint-and-measurement-handoff.md": {
        "checkpoint": True,
        "recycle_pack": "Einschränkung, Nachweis, bündeln, demonstrated, attested",
    },
    # Module 4 Theme 1
    "04-b2-entry-readiness/themes/theme-01-b1-b2-boundary-orientation/lesson-01-what-this-course-means-as-b1-readiness.md": {
        "lemmas": [
            ("demonstrated", "виміряно"),
            ("attested", "лише засвідчено"),
            ("die Bereitschaft", "готовність"),
            ("der B2-Kurs", "окремий курс B2"),
            ("nicht unterrichtet", "тут не викладається"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze: Evidence classes und Grenze zum B2-Kurs.",
    },
    "04-b2-entry-readiness/themes/theme-01-b1-b2-boundary-orientation/lesson-02-theme-checkpoint-boundary-in-own-words.md": {
        "checkpoint": True,
        "recycle_pack": "demonstrated, attested, Bereitschaft, B2-Kurs, nicht unterrichtet",
        "lemmas": [
            ("die Grenze", "межа"),
            ("in eigenen Worten", "своїми словами"),
            ("mindestens drei", "щонайменше три"),
            ("keine Beherrschung", "не опанування B2"),
            ("dieser Kurs", "цей курс"),
        ],
        "game": "rate",
        "schreiben": "Checkpoint-Text nutzen: fünf Mini-Sätze mit Lemmata (formativ vor/neben dem Grenztext).",
        "checkpoint_with_lexik": True,
    },
    # Module 4 Theme 2
    "04-b2-entry-readiness/themes/theme-02-light-novelty-b1-transfer/lesson-01-light-novelty-reading-and-hs-practice.md": {
        "lemmas": [
            ("die Neuheit", "новизна"),
            ("das Zeitfenster", "часове вікно"),
            ("buchen", "забронювати"),
            ("der Treffpunkt", "місце зустрічі"),
            ("attested", "HS лише attested"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze zum Aushang mit allen Lemmata.",
    },
    "04-b2-entry-readiness/themes/theme-02-light-novelty-b1-transfer/lesson-02-integrated-b1-response-light-novelty.md": {
        "recycle": "Neuheit, Zeitfenster, buchen, Treffpunkt, attested",
        "lemmas": [
            ("die Nachricht", "повідомлення"),
            ("der Alternativtermin", "альтернативний час"),
            ("die Warteliste", "лист очікування"),
            ("erreichen", "звʼязатися"),
            ("zusammenhängend", "звʼязно"),
        ],
        "game": "luecken",
        "schreiben": "Markieren Sie in Ihrer Mail fünf Stellen mit den Lemmata (oder fünf Extra-Sätze).",
    },
    "04-b2-entry-readiness/themes/theme-02-light-novelty-b1-transfer/lesson-03-theme-checkpoint.md": {
        "checkpoint": True,
        "recycle_pack": "Zeitfenster, buchen, Nachricht, Alternativtermin, zusammenhängend",
    },
    # Module 4 Theme 3
    "04-b2-entry-readiness/themes/theme-03-evidence-self-portrait-and-exam-handoff/lesson-01-order-evidence-measured-vs-attested.md": {
        "lemmas": [
            ("die Evidenzlage", "картина свідчень"),
            ("ordnen", "упорядкувати"),
            ("measured", "виміряно"),
            ("attested", "attested"),
            ("unsicher", "непевно"),
        ],
        "game": "match",
        "schreiben": "Fünf Sätze zu Ihrer Tabelle measured/attested/unsicher.",
    },
    "04-b2-entry-readiness/themes/theme-03-evidence-self-portrait-and-exam-handoff/lesson-02-self-portrait-and-next-step.md": {
        "recycle": "Evidenzlage, ordnen, measured, attested, unsicher",
        "lemmas": [
            ("das Selbstbild", "самооцінка"),
            ("der nächste Schritt", "наступний крок"),
            ("der Vorschlag", "пропозиція Декану"),
            ("die Einschränkung", "обмеження"),
            ("keine Entscheidung", "не placement-рішення"),
        ],
        "game": "rate",
        "schreiben": "Fünf Sätze Selbstbild mit allen Lemmata.",
    },
    "04-b2-entry-readiness/themes/theme-03-evidence-self-portrait-and-exam-handoff/lesson-03-module-checkpoint-and-exam-handoff.md": {
        "checkpoint": True,
        "recycle_pack": "Evidenzlage, Selbstbild, nächster Schritt, Einschränkung, attested",
    },
}


def lemma_table(lemmas: list[tuple[str, str]]) -> str:
    lines = [
        f"### Lektionslexik (Ziel: {len(lemmas)})",
        "",
        "| Lemma | Kurz |",
        "|---|---|",
    ]
    for de, uk in lemmas:
        lines.append(f"| {de} | {uk} |")
    return "\n".join(lines)


def game_block(game: str, lemmas: list[tuple[str, str]]) -> str:
    names = " · ".join(de for de, _ in lemmas)
    if game == "match":
        body = (
            "### Lexik-Spiel — Match-3 (~5 Min.)\n\n"
            "**Regeln:** 3 Leben. Paare Lemma ↔ Kurzbedeutung. Formativ.\n\n"
            f"Karten: {names}\n"
        )
    elif game == "luecken":
        body = (
            "### Lexik-Spiel — Lücken-Duell (~5 Min.)\n\n"
            "**Regeln:** 3 Leben. Kurze Lückensätze mit den Lemmata (Zeitbox ~60 s). Formativ.\n\n"
            f"Lemmata: {names}\n"
        )
    else:
        body = (
            "### Lexik-Spiel — Rate-mich (~5 Min.)\n\n"
            "**Regeln:** 3 Leben. Agent umschreibt ohne das Wort; Sie nennen es. Formativ.\n\n"
            f"Lemmata: {names}\n"
        )
    body += "\nBei ≥2 Fehlern: Lemma als `weak` notieren (`lektionslexik-guide.md`).\n"
    return body


def schreiben_block(hint: str) -> str:
    return (
        "### Lexik-Schreiben (Üben, ~5–8 Min.)\n\n"
        f"{hint}\n\n"
        "Formativ. Siehe `lektionslexik-guide.md`.\n"
    )


def recycle_block(source: str) -> str:
    return (
        "### Recycle-Spiel (Start, ~5 Min.)\n\n"
        f"Aus vorheriger Lektion / schwachen Lemmata: {source}. "
        "Format: Match-3 oder Rate-mich. "
        "Fail-Trigger (≥2 Fehler) → Teacher vocab gym (`lektionslexik-guide.md`).\n"
    )


def checkpoint_block(pack: str) -> str:
    return (
        "### Recycle-Spiel — Theme-Pack (vor dem Nachweis, ~5–8 Min.)\n\n"
        f"Formatives Sammelspiel (nicht Teil eines `NO_AI`-Nachweises, falls getrennt): {pack}. "
        "Match-3 oder Lücken-Duell. Fail → Teacher vocab gym vor dem Nachweis. "
        "Keine neue Pflicht-`Lektionslexik`, außer unten zusätzlich genannt.\n\n"
        "**Optional:** ein Satz mit einem schwachen Lemma (formativ).\n"
    )


def uk_pointer(checkpoint: bool) -> str:
    if checkpoint:
        return (
            "\n### Recycle / Lektionslexik\n\n"
            "Theme-Pack / recycle — див. німецьку секцію (`lektionslexik-guide.md`).\n"
        )
    return (
        "\n### Lektionslexik / Lexik-Spiel / Lexik-Schreiben\n\n"
        "Цільові лексеми, гра й речення — у німецькій секції "
        "(`lektionslexik-guide.md`).\n"
    )


INSERT_BEFORE = [
    r"^### Aufgaben\s*$",
    r"^### Nachweis\s*$",
    r"^### Leitfragen\s*$",
    r"^### Formativer Checkpoint",
    r"^### Checkpoint-Aufgabe",
    r"^### So läuft",
    r"^### Übung\s*$",
    r"^### Situation\s*$",
    r"^### Lesetext",
    r"^### Kurze Orientierung",
    r"^### Leitgitter",
    r"^## Ukrainisch",
    r"^## Українською",
]


def find_insert_pos(text: str) -> int | None:
    for pat in INSERT_BEFORE:
        m = re.search(pat, text, flags=re.M)
        if m:
            return m.start()
    return None


def build_insertion(spec: dict) -> str:
    parts: list[str] = []
    if spec.get("checkpoint") and not spec.get("checkpoint_with_lexik"):
        parts.append(checkpoint_block(spec["recycle_pack"]))
        return "\n".join(parts) + "\n"
    if spec.get("recycle"):
        parts.append(recycle_block(spec["recycle"]))
    if spec.get("checkpoint") and spec.get("checkpoint_with_lexik"):
        parts.append(checkpoint_block(spec["recycle_pack"]))
    lemmas = spec.get("lemmas") or []
    if lemmas:
        parts.append(lemma_table(lemmas))
        parts.append(game_block(spec.get("game", "match"), lemmas))
        parts.append(schreiben_block(spec.get("schreiben", "Schreiben Sie einen kurzen Satz pro Lemma.")))
    return "\n".join(parts) + "\n"


def apply_one(rel: str, spec: dict) -> str:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if "### Lektionslexik" in text or "### Recycle-Spiel — Theme-Pack" in text:
        return "skip"
    block = build_insertion(spec)
    pos = find_insert_pos(text)
    if pos is None:
        return "no-anchor"
    text = text[:pos] + block + text[pos:]
    # UK pointer once
    uk = re.search(r"^## Українською.*$", text, flags=re.M)
    if uk and "### Lektionslexik / Lexik-Spiel" not in text[uk.start() : uk.start() + 800]:
        # insert after first UK heading line
        end = text.find("\n", uk.end())
        if end != -1:
            ptr = uk_pointer(bool(spec.get("checkpoint") and not spec.get("checkpoint_with_lexik")))
            text = text[: end + 1] + ptr + text[end + 1 :]
    path.write_text(text, encoding="utf-8")
    return "ok"


def main() -> None:
    ok = skip = bad = 0
    for rel, spec in CATALOG.items():
        status = apply_one(rel, spec)
        if status == "ok":
            ok += 1
            print("OK", rel)
        elif status == "skip":
            skip += 1
            print("SKIP", rel)
        else:
            bad += 1
            print("FAIL", status, rel)
    # verify remaining
    missing = []
    for p in sorted(ROOT.rglob("lesson-*.md")):
        t = p.read_text(encoding="utf-8")
        if "### Lektionslexik" not in t and "Recycle-Spiel" not in t:
            missing.append(str(p.relative_to(ROOT)))
    print(f"done ok={ok} skip={skip} fail={bad} still_missing={len(missing)}")
    for m in missing:
        print("MISSING", m)


if __name__ == "__main__":
    main()

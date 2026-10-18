# Між B1 та B2 — Pre-course / Між B1 та B2 — Pre-course

---

## Deutsch

### Zweck

Der Pre-course ist die öffentliche Eingangsschicht vor dem Eintritt des Studenten in den Kurs. Er misst den Entry Contract des Kurses und der Module und gibt dem Dekan den unabhängigen Nachweis für die Course-Entry-Entscheidung und die erste Modulplatzierung.

Die Eingangsdiagnostik ist ein Platzierungsinstrument, keine Zulassungsschranke: Ihr Ergebnis entscheidet, wo der Student in der Kursroute beginnt, nicht ob er lernen darf.

Der Pre-course ist kein Modul und zählt nicht als Kursdurchführung. Er ändert die Modularchitektur des Kurses nicht. Seine Artefakte sind öffentliches Universitätsmaterial; Antworten, Nachweise und Entscheidungen des Studenten bleiben im privaten Student-Workspace.

### Lebenszyklus

```text
unabhängige Eingangsdiagnostik → Course-Entry-Entscheidung des Dekans → erste Modulroute
```

Eine begrenzte Brücke darf nur für eine bekannte Entry-Lücke und nur durch eine vom Dekan erteilte Sequenz hinzugefügt werden (siehe `course-entry.md`). Bisher existiert keine Brücke.

### Eingangsdiagnostik: Rahmen des Dekans (Assessment Request, Contract 1)

Dieser Abschnitt ist die Anfrage des Dekans an den ernannten Learning Analyst. Er legt fest, was gemessen werden muss. Er schreibt weder die Aufgaben noch die Umsetzung der Prüfung noch den Lehrweg vor.

#### Zweck und Unsicherheit

- Zweck: Course Entry und erste Modulplatzierung.
- Fehlender Nachweis: Die aktuelle Deutschleistung des Studenten in Bezug auf die A2-Grundlagen und die Kriterien von B1-Wiederherstellung ist nach einer Unterbrechung unbekannt.

#### Zu messende Kriterien

1. **A2-Grundlagen** — die vier Entry-Kriterien von Modul 2 (B1-Wiederherstellung): kontrollierte einfache Aussagen und Fragen; wesentliche Artikel, Kasus, Pronomen, Präpositionen und Verbformen, die die Bedeutung erhalten; Bezug auf Gegenwart, Vergangenheit und Zukunft; häufiger Wortschatz und funktionale Wendungen.
2. **B1-Leistung** — die Exit-Kriterien 1–7 von Modul 2. Gemessen werden Lesen, Schreiben und die schriftlichen Teile von Unsicherheit bemerken und Klärung oder Reparatur erbitten. Hören und Sprechen (Kriterien 1, 3 und der gesprochene Teil von 7) werden nur attestiert (siehe unten).

Die Ergebnisse werden pro Kriterium als `demonstrated`, `not demonstrated` oder `uncertain` berichtet. Ein messbares Kriterium (Lesen, Schreiben, schriftliche Teile), das im verfügbaren Kanal nicht gemessen werden kann, wird als `uncertain` berichtet, nie als `demonstrated`. Hören und Sprechen folgen stattdessen der Regel unten.

Entscheidung des Dekans: Hören und Sprechen werden in diesem Kurs nie gemessen. Die Diagnostik hält nur fest, dass die Aufgaben zu Hören und Sprechen erledigt wurden (`attested`, siehe `COURSE.md`, Evidence classes für Hören und Sprechen). Diese Kriterien werden nicht als `uncertain` bis zur Messung berichtet, und Attestation wird nie als `demonstrated` berichtet. Der Analyst misst Lesen, Schreiben und die schriftlichen Teile der übrigen Kriterien.

#### Umfang und Grenzen

- Zwei Teile: Teil A misst die A2-Grundlagen; Teil B misst die B1-Leistung. Teil B wird nur durchgeführt, wenn Teil A keine A2-Lücken zeigt, die die B1-Arbeit wesentlich blockieren (siehe Stoppbedingung).
- Ein Versuch pro Teil. Der Student darf die Teile in getrennten Sitzungen bearbeiten. Jeder Teil ist auf eine Sitzung begrenzt; der Analyst schlägt die genaue Länge innerhalb dieser Grenze vor.
- Die Diagnostik unterrichtet nicht, prüft keine B2-Kompetenzen und ist keine Simulation eines Prüfungsformats.

#### Stoppbedingung

Der Analyst hört auf, wenn jedes gemessene Kriterium im Umfang ein Ergebnis hat (Hören und Sprechen brauchen nur einen Eintrag `attested` oder `not attested`) oder wenn Teil A zeigt, dass A2-Lücken die B1-Arbeit wesentlich blockieren. Im zweiten Fall gibt der Analyst die Nachweise zurück, ohne Teil B durchzuführen, und nennt, welche Kriterien nicht gemessen wurden.

#### Sprache des Artefakts

Aller Lernertext ist auf Deutsch. Aufgabenanweisungen verwenden einfaches Deutsch auf A2-Niveau oder darunter, damit ein Missverständnis der Anweisung nicht mit einer Lücke im gemessenen Kriterium verwechselt wird. Kriterien nur für Prüfer werden vom Lernertext getrennt gehalten.

#### KI- und Werkzeugmodus

Der Modus unterscheidet sich je Schritt und wird mit dem Nachweis festgehalten, weil er beeinflusst, was der Nachweis belegt (`policies/ai-usage.md`):

- gemessene Versuche in Teil A und B (Leseverstehen, Form, Wortschatz, Schreiben): `NO_AI`, kein Wörterbuch; Hören und Sprechen werden nur attestiert;
- ein optionaler, klar getrennter Überarbeitungsschritt nach einem gemessenen Schreibversuch: `AI_ASSISTED` mit offengelegter Nutzung, um Nachweis für das Bemerken und Reparieren eines Fehlers zu liefern. Sein Ergebnis wird getrennt festgehalten und ersetzt die unassistierte Messung nicht.

Der Analyst darf das Aufgabendesign innerhalb dieses Modus verfeinern, aber die `NO_AI`-Regel für die gemessenen Versuche nicht abschwächen.

#### Zulässiger Studentenkontext

Das Artefakt ist öffentlich und studentenunabhängig. Es darf keine privaten Studenteninformationen enthalten. Studentenspezifische Ergebnisse hält der Analyst nach der Durchführung über `update-evidence` im privaten Student-Workspace fest.

#### Übergabestufe

Vor der Veröffentlichung ruft der Analyst den Instructional Assistant zur Prüfung auf (Contract 5), wendet den Bericht an und gibt Artefaktpfad und Prüfprotokoll an den Dekan zurück. Platzierung und Verlauf bleiben beim Dekan.

### Entscheidungskarte des Dekans zum Course Entry

Nach dem unabhängigen Nachweis (Contract 4) entscheidet der Dekan nach Ergebnissen pro Kriterium, nicht nach einer Punktzahl. Die Entscheidung trifft der Dekan gemeinsam mit dem Studenten.

| Nachweis | Entscheidung des Dekans |
|---|---|
| A2-Kriterien `demonstrated`; B1-Kriterien gemischt oder noch nicht gezeigt | Modul 1 überspringen; Modul 2 auf die noch nicht nachgewiesenen B1-Kriterien verkürzt beginnen |
| Ein oder mehrere A2-Kriterien `not demonstrated` | Course Entry bestätigen; Modul 1 nur auf diese Kriterien verkürzt beginnen |
| A2- und B1-Kriterien in allen vier Fertigkeiten `demonstrated` | Eintritt in Modul 3 erwägen; mit einem Entry-Check für Modul 3 verifizieren, wenn der Nachweis veraltet oder unsicher ist |
| Kriterien `uncertain` oder widersprüchlich (Lesen, Schreiben) | begrenzte weitere Messung für diese Kriterien anfordern; Eintritt aufschieben |
| Hören und Sprechen nur `attested` | keine weitere Messung; Hör- oder Sprechpraxis nicht allein aufgrund von Attestation überspringen oder verkürzen |
| Student erfüllt den Course Entry Contract nicht | andere Route oder Fakultäts-/Kurswahl (`course-entry.md`) |

Es sind keine Schwellen oder Prozentsätze festgelegt. Verkürzung entfernt nie ein Kriterium aus den Kurs-Erfolgskriterien; sie entscheidet nur, welche Kriterien für diesen Studenten unterrichtet und geprüft werden.

### Aktueller Stand

Das Diagnostikartefakt (`entry-diagnostic-part-a.md`, `entry-diagnostic-part-b.md` und der nur für Prüfer bestimmte `entry-diagnostic-assessor-record.md`) wurde vom Learning Analyst unter Contract 2 erstellt. Es wurde sechsmal vom Instructional Assistant geprüft (letztes Ergebnis `ready_with_changes`, Protokoll in Abschnitt 11.6 des Assessor-Records; die sechste Prüfung betraf nur die Sprachumstellung auf Deutsch mit ukrainischer Übersetzung); die letzte Überarbeitung wurde nicht erneut geprüft und noch keinem Studenten übergeben. Es existieren noch keine Brücke, kein Thema und keine Lektion.

#### Vorläufige Parameter (Entscheidung des Dekans bis zu einem Pilot)

Diese Werte wurden vom Analysten vorgeschlagen und vom Dekan als vorläufig akzeptiert. Sie sind unpiloted und können sich nach der ersten Durchführung ändern:

- Stoppregel: Teil B wird zurückgehalten, wenn E1 nicht `demonstrated` ist oder wenn zwei oder mehr der Kriterien E1–E4 nicht `demonstrated` sind;
- Kriterium X6 wird gelesen als: In Teil A richtige Formen erscheinen in der freien Produktion in Teil B wieder richtig;
- der Überarbeitungsschritt (Z) gilt nur für Schreiben;
- Zeitlimits von 45 Minuten (Teil A) und 75 Minuten (Teil B) sowie die A2/B1-Niveaukalibrierung der Aufgaben.

#### Entschieden

- Nur für Prüfer bestimmtes Material (Lösungen, Hörskripte) bleibt in diesem Repository öffentlich, wie im Pre-course von AI Engineering. Das Universitätsmodell hat keinen geschützten Ort dafür, und ein Student kann die Lösungen lesen; eine Durchführung ohne Beobachter ist daher ein schwächerer Nachweis.

- Attestation von Hören und Sprechen (Entscheidung des Dekans, die den Vorschlag des Analysten in Einschränkung L11 des Assessor-Records annimmt):
  - die Bezeichnung für eine fehlende Attestation ist `not attested`;
  - Hören ist `attested`, wenn beide Texte gehört wurden (eine live vorlesende Person ist erlaubt) und für jeden Text ein Antwortversuch vorliegt; Sprechen ist `attested`, wenn irgendeine gesprochene Sprache produziert und der Austausch geführt wurde;
  - ein Verstoß gegen `no-AI` / keine Hilfe bei Hören oder Sprechen wird nur festgehalten und ändert `attested` nicht;
  - wurde Hören oder Sprechen übersprungen oder Teil B zurückgehalten, ist eine eigene Sitzung nur für die Attestation erlaubt;
  - der Zeitschutz der Sprechaufgabe in Abschnitt 5.1 des Assessor-Records gilt gleichermaßen für die Höraufgabe; andere Aufgaben werden zuerst gekürzt;
  - der Lernersatz „Hören und Sprechen üben Sie auch im Kurs“ bleibt;
  - eine Aufgabe, die gemacht wurde, aber `not attested` endete (kein Antwortversuch, ein Text nicht abgespielt), darf ebenfalls in einer eigenen Attestationssitzung wiederholt werden;
  - der Lernertext von Aufgabe 9 erhält den Satz „Wenn das nicht geht, machen wir die Aufgabe an einem anderen Termin“, und „nur einmal“ / „an einem Termin“ wird nur auf die gemessenen Aufgaben bezogen gelesen;
  - der A2-Wortlaut des Lernertextes in Teil B wird vereinfacht (Gesprächspartner, Aussprache, die Bezeichnung „B2“, „prüft“);
  - eine verschobene Aufgabe 6 oder 9 bleibt außerhalb der 75 Minuten (eigener 12-Minuten-Slot), und nach einer verschobenen Aufgabe 9 wird kein Z angeboten;
  - Sprechen darf telefonisch, per Video oder persönlich stattfinden, sofern ein echter Austausch geführt wird;
  - die Hörantworten werden nach jedem Text geschrieben.

#### Offene Entscheidungen

- wer die Sitzung durchführt und beobachtet, sowie der Kanal getippt oder handschriftlich (betrifft jetzt nur Lesen und Schreiben);
- wer die reine Attestationssitzung durchführt, ob Hörantwortbögen aufbewahrt werden und ob die Zahl der Wiederholungen begrenzt wird (bis zu einem Pilot aufgeschoben).

#### Ausstehende Überarbeitung durch den Analysten

Da Hören und Sprechen nur attestiert werden, muss der Learning Analyst `entry-diagnostic-part-b.md` und `entry-diagnostic-assessor-record.md` (Kriterien X1, X3, X7 und die Sprechabschnitte) so überarbeiten, dass der Abschluss festgehalten statt die Leistung beurteilt wird, und dann die Prüfung durch den Instructional Assistant wiederholen. Der Dekan verfasst diese Artefakte nicht.

Erledigt: das Umschreiben auf reine Attestation, gleicher Zeitschutz für Hören, die eigene Attestationssitzung und drei Prüfungen durch den Instructional Assistant. Für den Analysten steht nichts aus außer den Entscheidungen des Dekans in den offenen Punkten.

---

## Українською (переклад)

### Мета

Pre-course — це публічний вхідний шар перед вступом Студента до курсу. Він вимірює Entry Contract курсу й Модулів і дає Декану незалежне свідчення для рішення про Course Entry та першого розміщення в Модулі.

Вхідна діагностика — інструмент розміщення, а не бар'єр допуску: її результат визначає, з якого місця маршруту курсу Студент починає, а не чи може він навчатися.

Pre-course не є Модулем і не рахується як проведення курсу. Він не змінює архітектури Модулів курсу. Його артефакти — публічні матеріали Університету; відповіді, свідчення й рішення Студента лишаються в приватному просторі Студента.

### Життєвий цикл

```text
незалежна вхідна діагностика → рішення Декана про Course Entry → перший маршрут Модулем
```

Обмежений міст можна додати лише для відомої прогалини Entry і лише через послідовність, видану Деканом (див. `course-entry.md`). Мосту поки не існує.

### Вхідна діагностика: рамка Декана (Assessment Request, Contract 1)

Цей розділ — запит Декана до призначеного Learning Analyst. Він визначає, що треба виміряти. Він не приписує ні завдань, ні реалізації оцінювання, ні навчального шляху.

#### Мета і невизначеність

- Мета: Course Entry і перше розміщення в Модулі.
- Бракує свідчення: поточне володіння Студентом німецькою щодо основ A2 і критеріїв Відновлення B1 після перерви невідоме.

#### Критерії для вимірювання

1. **Основи A2** — чотири Entry-критерії Модуля 2 (Відновлення B1): контрольовані прості твердження й питання; основні артиклі, відмінки, займенники, прийменники й дієслівні форми, що зберігають зміст; відсилання до теперішнього, минулого й майбутнього; частотна лексика й функціональні звороти.
2. **Результат B1** — Exit-критерії 1–7 Модуля 2. Вимірюються Lesen, Schreiben і письмові частини «помічати невпевненість та просити уточнення чи виправлення». Hören і Sprechen (критерії 1, 3 і усна частина 7) лише attested (див. нижче).

Результати звітуються за кожним критерієм як `demonstrated`, `not demonstrated` або `uncertain`. Вимірюваний критерій (Lesen, Schreiben, письмові частини), який неможливо виміряти в доступному каналі, звітується як `uncertain`, ніколи як `demonstrated`. Hören і Sprechen натомість підпорядковані правилу нижче.

Рішення Декана: Hören і Sprechen у цьому курсі ніколи не вимірюються. Діагностика фіксує лише те, що завдання з Hören і Sprechen виконано (`attested`, див. `COURSE.md`, Evidence classes для Hören і Sprechen). Ці критерії не звітуються як `uncertain` до вимірювання, а attestation ніколи не звітується як `demonstrated`. Аналітик вимірює Lesen, Schreiben і письмові частини решти критеріїв.

#### Обсяг і межі

- Дві частини: Частина A вимірює основи A2; Частина B вимірює результат B1. Частину B проводять лише тоді, коли Частина A не показує прогалин A2, що суттєво блокують роботу на B1 (див. умову зупинки).
- Одна спроба на частину. Студент може проходити частини в окремих сесіях. Кожна частина обмежена однією сесією; точну тривалість у цих межах пропонує Аналітик.
- Діагностика не навчає, не оцінює компетенцій B2 і не є симуляцією екзаменаційного формату.

#### Умова зупинки

Аналітик зупиняється, коли кожен вимірюваний критерій в обсязі має результат (для Hören і Sprechen досить запису `attested` або `not attested`) або коли Частина A показує, що прогалини A2 суттєво блокують роботу на B1. У другому випадку Аналітик повертає свідчення без проведення Частини B і вказує, які критерії не виміряно.

#### Мова артефакту

Увесь текст для Студента — німецькою. Інструкції до завдань використовують просту німецьку рівня A2 або нижче, щоб нерозуміння інструкції не сплутали з прогалиною у вимірюваному критерії. Критерії лише для оцінювача відокремлені від тексту для Студента.

#### Режим ШІ та інструментів

Режим відрізняється за кроком і фіксується разом зі свідченням, бо впливає на те, що воно доводить (`policies/ai-usage.md`):

- виміряні спроби Частин A і B (розуміння прочитаного, форма, лексика, Schreiben): `NO_AI`, без словника; Hören і Sprechen лише attested;
- необов'язковий, чітко відокремлений крок виправлення після виміряної спроби Schreiben: `AI_ASSISTED` із розкритим використанням, щоб дати свідчення про помічання й виправлення помилки. Його результат фіксується окремо й не замінює вимірювання без допомоги.

Аналітик може уточнювати дизайн завдань у межах цього режиму, але не послаблювати правило `NO_AI` для виміряних спроб.

#### Допустимий контекст Студента

Артефакт публічний і не залежить від Студента. Він не повинен містити приватної інформації про Студента. Результати конкретного Студента Аналітик записує в приватний простір Студента через `update-evidence` після проведення діагностики.

#### Етап передачі

Перед публікацією Аналітик викликає Instructional Assistant на перевірку (Contract 5), застосовує звіт і повертає Декану шлях до артефакту й запис перевірки. Розміщення й траєкторія лишаються за Деканом.

### Карта рішень Декана щодо Course Entry

Після незалежного свідчення (Contract 4) Декан вирішує за результатами за критеріями, а не за числовим балом. Рішення належить Декану й ухвалюється разом зі Студентом.

| Свідчення | Рішення Декана |
|---|---|
| Критерії A2 `demonstrated`; критерії B1 змішані або ще не показані | Пропустити Модуль 1; вступити до Модуля 2, звуженого до ще не підтверджених критеріїв B1 |
| Один чи більше критеріїв A2 `not demonstrated` | Підтвердити Course Entry; вступити до Модуля 1, звуженого лише до цих критеріїв |
| Критерії A2 і B1 `demonstrated` у всіх чотирьох навичках | Розглянути вступ до Модуля 3; верифікувати перевіркою Entry Модуля 3, якщо свідчення застаріле чи невпевнене |
| Критерії `uncertain` або суперечливі (Lesen, Schreiben) | Запросити обмежене додаткове вимірювання цих критеріїв; відкласти вступ |
| Hören і Sprechen лише `attested` | Подальшого вимірювання немає; не пропускати й не скорочувати практику Hören чи Sprechen лише на підставі attestation |
| Студент не відповідає Entry Contract курсу | Інший маршрут або вибір факультету/курсу (`course-entry.md`) |

Порогів чи відсотків не встановлено. Звуження ніколи не прибирає критерій із Критеріїв успіху курсу; воно лише вирішує, які критерії викладають і перевіряють для цього Студента.

### Поточний стан

Артефакт діагностики (`entry-diagnostic-part-a.md`, `entry-diagnostic-part-b.md` і призначений лише для оцінювача `entry-diagnostic-assessor-record.md`) створив Learning Analyst за Contract 2. Його шість разів перевірив Instructional Assistant (останній результат `ready_with_changes`, запис у розділі 11.6 assessor-record; шоста перевірка стосувалася лише переходу на німецьку з українським перекладом); остання редакція не перевірялася повторно й ще не передана жодному Студенту. Мосту, Теми чи Уроку поки не існує.

#### Попередні параметри (рішення Декана до пілоту)

Ці значення запропонував Аналітик, а Декан прийняв як попередні. Вони unpiloted і можуть змінитися після першого проведення:

- правило зупинки: Частину B стримують, якщо E1 не `demonstrated` або якщо два чи більше з E1–E4 не `demonstrated`;
- критерій X6 читається так: форми, правильні в Частині A, правильно з'являються у вільному продукуванні в Частині B;
- крок виправлення (Z) стосується лише Schreiben;
- ліміти часу 45 хвилин (Частина A) і 75 хвилин (Частина B) та калібрування рівня завдань A2/B1.

#### Вирішено

- Матеріал лише для оцінювача (ключі, сценарії аудіювання) лишається публічним у цьому репозиторії, як у pre-course AI Engineering. Модель Університету не має для цього закритого місця, а Студент може прочитати ключі, тож проведення без спостерігача — слабше свідчення.

- Attestation Hören і Sprechen (рішення Декана, що приймає пропозицію Аналітика в обмеженні L11 assessor-record):
  - позначка відсутньої attestation — `not attested`;
  - Hören — `attested`, коли обидва тексти почуто (живий читець дозволений) і для кожного тексту є спроба відповіді; Sprechen — `attested`, коли вироблено будь-яке усне мовлення й відбувся обмін;
  - порушення `no-AI` / заборони допомоги в Hören чи Sprechen лише фіксується й не змінює `attested`;
  - якщо Hören чи Sprechen пропущено або Частину B стримано, окрема сесія лише для attestation дозволена;
  - захист часу завдання Sprechen у розділі 5.1 assessor-record так само діє для завдання Hören; спершу скорочують інші завдання;
  - речення для Студента «Hören und Sprechen üben Sie auch im Kurs» лишається;
  - завдання, яке було виконане, але закінчилося `not attested` (немає спроби відповіді, текст не відтворено), також можна повторити в окремій сесії attestation;
  - у тексті для Студента до Завдання 9 з'являється речення «Wenn das nicht geht, machen wir die Aufgabe an einem anderen Termin», а «nur einmal» / «an einem Termin» читається як таке, що стосується лише виміряних завдань;
  - формулювання A2 у тексті для Студента в Частині B спрощується (Gesprächspartner, Aussprache, позначка «B2», «prüft»);
  - перенесене Завдання 6 чи 9 лишається поза 75 хвилинами (окремий 12-хвилинний слот), а після перенесеного Завдання 9 Z не пропонується;
  - Sprechen може відбуватися телефоном, відео чи наживо, якщо проведено справжній обмін;
  - відповіді Hören записують після кожного тексту.

#### Відкриті рішення

- хто проводить сесію й спостерігає, та канал — набір чи рукопис (тепер стосується лише Lesen і Schreiben);
- хто проводить сесію лише для attestation, чи зберігати аркуші відповідей Hören і чи обмежувати кількість повторів (відкладено до пілоту).

#### Очікувана доробка Аналітика

Оскільки Hören і Sprechen лише attested, Learning Analyst має переробити `entry-diagnostic-part-b.md` та `entry-diagnostic-assessor-record.md` (критерії X1, X3, X7 і розділи Sprechen) так, щоб фіксувати завершення, а не оцінювати результат, а потім повторити перевірку Instructional Assistant. Декан цих артефактів не пише.

Зроблено: переписування на лише attestation, однаковий захист часу для Hören, окрема сесія attestation і три перевірки Instructional Assistant. Для Аналітика нічого не лишається, крім рішень Декана у відкритих пунктах.

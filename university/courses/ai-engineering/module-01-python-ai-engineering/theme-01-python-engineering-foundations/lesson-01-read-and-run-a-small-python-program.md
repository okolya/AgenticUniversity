# Урок 01 — Читання та запуск малої Python-програми

## Мета уроку

Цей перший урок створює практичний міст до Python. Ти прочитаєш коротку
програму, поясниш її inputs та outputs, запустиш її у development environment,
зробиш одну контрольовану зміну й перевіриш звичайний output та одну помилку
через invalid input.

Це вступ до читання та виконання Python-коду, а не повний Python-курс і не
фінальне assessment.

## Критерії успіху

Після цього уроку ти маєш уміти:

1. Визначити input, output, data values, named functions і рішення
   control flow програми.
2. Простими словами пояснити призначення малої Python-функції.
3. Зберегти приклад у `.py`-файлі та запустити його у development environment.
4. Зробити одну навмисну локальну зміну й до запуску описати її очікуваний
   ефект.
5. Зафіксувати звичайний output і визначити загальну причину помилки через
   invalid input, не приховуючи та не підміняючи diagnostic.

Ці критерії дають formative evidence для bridge із general-purpose programming
та development environment. Вони не підтверджують Module Entry або mastery.

## Основні ідеї

### Inputs та outputs

**Input** — це інформація, яку отримує програма. Вона може надходити від
користувача, з файла, command-line argument або іншого компонента. **Output** —
це інформація, яку програма повертає, друкує, записує або передає іншому
компоненту.

Для малої command-line програми `input()` є одним із можливих input boundaries,
а `print()` — одним із можливих output boundaries.

### Data values та types

Python values мають types, які впливають на значення операцій. У прикладі
`"72"` — це text, прочитаний із terminal, а `72` — integer після conversion.
Conversion може завершитися помилкою, якщо text не є коректним integer.

### Named functions

Function надає групі кроків name та boundary. Її parameters — це inputs
функції, а return value — її output. Корисна function зазвичай виконує одну
зрозумілу задачу.

### Control flow

Control flow визначає, які statements виконуються і в якому порядку. `if`,
`elif` та `else` обирають між cases. Нижче function спочатку перевіряє range,
а потім обирає label на основі threshold.

### Transfer boundary із PHP

Якщо ти працював із PHP, використовуй цей досвід як допомогу для читання, а не
як доказ, що Python уже відомий. Урок навмисно використовує знайомі engineering
ideas — named functions, parameters, return values, conditionals, input та
output — але Python має власні syntax, indentation rules, value conversions і
runtime behavior. Перевіряй кожен Python statement та observed result, а не
перекладай код механічно з PHP.

## Малий оригінальний приклад

Створи файл `lesson01_score.py` і введи цей код:

```python
def describe_score(score):
    """Return a label for a score on a 0–100 scale."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 70:
        return "ready"
    return "keep practicing"


def main():
    raw_score = input("Enter a sample score from 0 to 100: ")
    score = int(raw_score)
    label = describe_score(score)
    print(f"Score {score}: {label}")


if __name__ == "__main__":
    main()
```

Дані навмисно вигадані й не містять account, customer або production
information.

### Очікуваний output

Після запуску програми prompt попросить ввести score. Для input `72` очікуй:

```text
Enter a sample score from 0 to 100: 72
Score 72: ready
```

Для input `55` очікуй:

```text
Enter a sample score from 0 to 100: 55
Score 55: keep practicing
```

Для input `seventy` виникне conversion error під час `int(raw_score)`.
Для input `120` виникне `ValueError` усередині `describe_score`. Це очікувана
поведінка прикладу, яку потрібно побачити та пояснити.

Прочитай програму зверху вниз:

1. `describe_score` — named function. Вона отримує `score` і повертає `label`.
2. Range check — це guard. Values поза заявленим contract викликають
   `ValueError`.
3. Другий `if` — decision: scores від `70` повертають `"ready"`, інші
   коректні scores — `"keep practicing"`.
4. `main` читає text, перетворює його на integer, викликає named function і
   друкує result.
5. Фінальний conditional запускає `main()`, коли файл виконується напряму.
   Він не запускається лише через import файла.

Перед запуском файла спрогнозуй:

- Який input дасть `Score 72: ready`?
- Який input дасть `Score 55: keep practicing`?
- Яка operation може завершитися помилкою для input `seventy`?
- Яка operation відхиляє `120`?

## Запуск і перевірка

Із directory, що містить файл, запусти:

```text
python lesson01_score.py
```

Якщо твоє environment використовує `python3`, запусти:

```text
python3 lesson01_score.py
```

Виконай ці окремі runs:

1. Введи `72` і зафіксуй normal output.
2. Введи `55` і зафіксуй іншу valid branch.
3. Введи `seventy`. Перевір traceback і визнач, що `int(raw_score)` не може
   перетворити цей text на integer.
4. Введи `120`. Перевір traceback і визнач, що `describe_score` відхиляє value
   поза своїм declared range.

Traceback — це diagnostic information. Для цього уроку не приховуй його, не
замінюй вигаданим повідомленням і не вставляй sensitive environment details у
своє evidence.

## Керована C0-практика — напиши зміну самостійно

Зроби одну controlled change у своїй local copy:

> Зміни readiness threshold із `70` на `80`.

Перед редагуванням запиши:

- exact line або value, який плануєш змінити;
- один input, чий label має змінитися після edit;
- один input, чий label має залишитися незмінним;
- один invalid input, який усе ще має завершитися помилкою.

Потім зміни лише threshold, запусти програму з цими inputs і порівняй
observed output зі своїм prediction. Після фіксації evidence віднови початковий
threshold, якщо немає причини залишати змінену copy.

### AI та tooling boundary для цієї практики

Ти можеш використовувати editor, Python interpreter та official Python
documentation, щоб зрозуміти syntax, `ValueError`, `input`, `int`, `if` і
`return`. Можна попросити AI пояснити error message, перевірити твоє
розуміння Python concept або запропонувати питання для investigation.

AI не має писати requested threshold change, створювати completed replacement
solution або генерувати evidence за тебе. Введи change самостійно й повідом
commands та observations, які ти справді отримав. Не використовуй цю практику
як final mastery verdict.

## Формат очікуваного evidence

Відповідай за цією структурою:

```text
Evidence уроку 01

1. Program map
   - Input:
   - Outputs:
   - Data values/types:
   - Named functions and purpose:
   - Control flow:

2. Prediction
   - Valid input and expected result:
   - Invalid input and expected failure:

3. Execution
   - Environment/command:
   - Normal output for 72:
   - Other valid output for 55:
   - Invalid-input failure:

4. Controlled change
   - Change made:
   - Expected changed behavior:
   - Expected unchanged behavior:
   - Observed behavior:

5. One remaining uncertainty
   - ...
```

Додавай короткі output excerpts, а не весь terminal transcript. Для failure
вкажи exception type і relevant final message або поясни, що саме він означав.
Якщо не зміг запустити файл, вкажи exact blocker і все одно надай program map
та prediction.

## Додаткові матеріали та точні посилання

### Student-provided: Python for Beginners

Для цього уроку релевантний наданий тобою курс:

**Python for Beginners:**
https://www.udemy.com/course/pythonforbeginnersintro/learn/lecture/2493870?start=0#overview

У ньому можна використати теми, що відповідають цьому уроку:

- `Getting Started with Python`;
- `Variables and Multiple Assignment`;
- `Arithmetic Operators and Strings`;
- `Conditional Statements`;
- `Creating and Using Functions`.

Це supplementary material, а не обов’язкова вимога. Не потрібно проходити
весь курс або копіювати його ordering. Перегляд lesson не є evidence of
mastery — evidence формується через виконання цього уроку та власні
спостереження.

### Student-provided: Django course

Другий наданий курс:

**The Ultimate Beginners Guide to Django:**
https://www.udemy.com/course/the-ultimate-beginners-guide-to-django-django-2-python-web-dev-website

У Lesson 01 він **не використовується**, оскільки Django та web-framework
topics не потрібні для поточної цілі — читання й запуску малої Python-програми.
Його можна буде розглянути пізніше, якщо він буде релевантним для окремої
Theme або product application.

### Власний матеріал University

Цей Lesson написаний University спеціально для затвердженого Theme frame.
Він не є копією Udemy-матеріалів. Student-provided курси є лише джерелами
для курації; Adam самостійно вирішує, що включати, адаптувати або не
використовувати.

## Примітка з безпеки

Використовуй лише вигадані placeholder values, наприклад `72` і `55`. Не
розміщуй passwords, API keys, access tokens, customer data, private files або
інші secrets у source file, terminal input, screenshots чи response. Якщо
development tool показує environment variables або credentials, зупинись і
видали їх із evidence перед передачею.

# Dialogue language

The runtime follows the language of the first substantive Student message in
the session.

## Rules

1. Detect the dominant natural language of the first substantive user request.
2. Use that language for subsequent explanations, navigation, questions, and
   learning feedback.
3. Treat an explicit switch by the Student as a new dialogue-language choice
   and continue in the newly selected language.
4. If the first request is genuinely mixed, use the language carrying the
   main intent; if that is ambiguous, ask one concise language question.
5. Preserve code, file paths, command names, Skill names, Worker names, and
   other technical identifiers exactly as written.
6. Do not infer academic placement, Student state, or authority from language
   detection; this policy controls presentation only.

For the current session, the detected dialogue language is Ukrainian.

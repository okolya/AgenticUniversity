---
name: student-initialization
class: learning
---
# Student initialization

Owner: Rector.

1. The private Student state is created (`initialize-student` in
   `protocols/student-state-contract.md`). In the CLI host the Student document is created in the
   Student state store from the public Student template/instructions; in
   another host the Student's own sign-up request creates the Student record.
   The CLI host creates `homeworks/<student-id>/` together with the Student;
   it contains only private Student artifacts and is ignored by Git.
2. Rector verifies only the minimum Student state required for interaction.
3. Rector helps establish high-level learning goals through a focused choice
   question using the interaction format policy, and initializes the minimum
   University-facing relationship.
4. Rector routes the Student toward an appropriate Faculty when requested.

Do not create a Faculty, worker, or curriculum merely to complete this workflow.

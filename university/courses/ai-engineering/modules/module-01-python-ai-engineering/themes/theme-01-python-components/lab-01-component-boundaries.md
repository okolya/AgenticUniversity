# Theme 1 — Lab: component boundaries

**Owner:** Sara, Laboratory Specialist, Engineering Faculty

**Use:** optional practical support for Lesson 4 only; this Lab does not add a
Lesson to Theme 1.

## Purpose

Consolidate the ability to deliver one small Python component with separate
logic and entry-point files.

## Lab task

Create a bounded score component with:

- `score_logic.py` containing parsing, classification, and formatting logic;
- `score_app.py` containing input, calls, output, and the entry point.

The component must handle an ordinary score, a boundary score, text input, and
an out-of-range score. The Student makes one small controlled threshold change,
runs the affected case, and restores the required behavior.

## Run contract

The Student returns the artifact path and command. Sara or the accepting Worker
inspects both files and runs all required cases. A pasted output without the
files is insufficient.

## Minimum evidence

- compact results for the four required cases;
- one sentence describing the data flow between files;
- the controlled-change result;
- one short explanation of what the checks do not prove.

No full terminal transcript or program map is required.

## AI/tool mode

Documentation and ordinary command reference are allowed. The Student must
briefly disclose any AI assistance. The artifact and understanding check
remain required.

## Stop condition

The Lab ends after the bounded component and one understanding check. Sara
returns practical observations to Adam; she does not issue a Theme or Module
verdict.

# Python Education Docs Writing Guide

## 0. Purpose

This guide standardizes how we write Python learning materials for a GitHub repository.

Goals:

* Keep terminology consistent across all documents
* Make docs easy to read directly on GitHub
* Make each topic self-contained, with runnable example code in a separate file
* Ensure consistent structure, tone, and linking

---

## 1. Information Architecture

### 1.1 Terminology (Fixed)

We use the following hierarchy:

* **Section**: e.g., `Basics`, `OOP`, `Practical`, `Algorithms`
* **Chapter**: e.g., `Variables`, `Control Flow`, `Functions`
* **Topic (or Lesson)**: e.g., `Creating Variables`, `Naming Rules`

Rules:

* A Section contains multiple Chapters
* A Chapter contains multiple Topics
* Topic documents must not refer to themselves as chapters

---

### 1.2 Directory Structure (Fixed)

Each chapter follows this structure:

```text
basics/
  README.md
  variables/
    README.md
    docs/
      01_creating_variables.md
      02_naming_rules.md
      ...
    examples/
      01_creating_variables.py
      02_naming_rules.py
      ...
```

---

## 2. File Naming Rules

### 2.1 Topic Document Filenames

* Use a two-digit numeric prefix: `01_`, `02_`, ...
* Use `snake_case`
* One topic per file

Examples:

* `01_creating_variables.md`
* `02_naming_rules.md`

---

### 2.2 Example Code Filenames

* Must exactly match the topic numbering and slug
* One topic corresponds to one `.py` file

Example:

* `01_creating_variables.py` ↔ `01_creating_variables.md`

---

## 3. Linking Rules (Critical)

### 3.1 Chapter Index Links

In `Chapter/README.md`:

```md
1. [Creating Variables](./docs/01_creating_variables.md)
```

---

### 3.2 Topic-to-Example Links

In each topic document:

```md
- [`01_creating_variables.py`](../examples/01_creating_variables.py)
```

Topic documents live in `docs/`, so relative paths must use `../examples/`.

---

### 3.3 No Broken Links Rule

Before merging:

* Verify every topic doc links to its example file
* Verify chapter README lists all topics in order
* Verify filenames match exactly (case-sensitive)

---

## 4. Writing Style Rules

### 4.1 Language

* All explanations and examples must be written in **English**
* Use clear, instructional sentences
* Avoid slang or conversational filler

---

### 4.2 Tone

* Neutral, instructional tone
* Explanation-focused
* Avoid motivational or playful language

Good:

* "A variable is created when you assign a value to a name."

Avoid:

* "Let’s have fun creating magical variables!"

---

### 4.3 Audience Assumption

* Beginner-friendly by default
* Concepts explained step by step
* Avoid deep theory unless explicitly stated as a conceptual overview

---

## 5. Document Structure Standards

### 5.1 Chapter README Standard

Required sections (in order):

1. `# <Chapter Name>`
2. Short chapter description (2–4 sentences)
3. Explicit hierarchy mention:

   * "This chapter belongs to the **Basics** section …"
4. `## Learning Objectives`
5. `## Contents`
6. `## How to use this chapter`

---

### 5.2 Topic Document Standard

Required structure:

1. Single H1 title
2. Explanation paragraphs
3. Inline Python code examples
4. Use `---` to separate major sections
5. End with `## Example file`

Guidelines:

* Blend explanation and code naturally
* Avoid keyword-only bullet lists
* Keep examples runnable and focused

---

## 6. Code Example Standards

### 6.1 Code Blocks

* Always use fenced code blocks with `python`
* Prefer multiple small examples
* Avoid overly long scripts

---

### 6.2 Consistency With Example Files

* All code shown in the topic doc must be runnable
* Code should later be copied directly into the matching example file
* Do not include pseudo-code

---

### 6.3 Comments

* Use comments only when they add clarity
* Avoid commenting obvious lines

---

## 7. Variables Chapter Specific Rules

Topic order is fixed:

1. Creating Variables
2. Naming Rules and Best Practices
3. Data Types (Overview)
4. Variables as References
5. Variable Reassignment
6. Multiple Assignment
7. Common Beginner Mistakes

Additional guidance:

* Data Types is a light overview only
* Variables as References must remain conceptual (no memory internals)

---

## 8. Quality Checklist

### Chapter README

* Uses explicit Section reference
* Contains learning objectives
* Contents links are correct
* Mentions example usage

### Topic Document

* English only
* One H1 title
* Explanation and code blended
* Runnable examples
* Correct example file link

### Filenames

* Topic `.md` and example `.py` match
* Numbering is sequential

---

## 9. Contributor Handoff Instructions

When assigning work, provide:

* Topic title
* Topic number and slug
* Target paths for docs and examples
* Instruction to follow this guide

Example:

> Write `docs/02_naming_rules.md` for the Variables chapter.
> Follow the standard Topic document structure.
> Include inline Python examples.
> Link to `../examples/02_naming_rules.py` at the end.

---

## 10. Reference Documents

Use these as canonical references:

* `/basics/03_variables/README.md`
* `/basics/03_variables/docs/01_creating_variables.md`

# Agent Task Instruction Template

This template is used to assign writing tasks to agents or team members.

All work must follow the **Python Education Docs Writing Guide (Universal)**.

---

## 1. Task Overview

You are assigned to write **one Topic document** for a Python education repository.

This task focuses on **documentation only**. Example code files will be created later, but your document must include code examples that can be copied directly into the example file.

---

## 2. Scope Definition (Fill in Before Assigning)

* **Section**: Basics / OOP / Practical / Algorithms
* **Chapter**: <Chapter Name>
* **Topic Title**: <Topic Title>
* **Topic Number & Slug**: NN_<topic_slug>

Example:

* Section: Basics
* Chapter: Variables
* Topic Title: Naming Rules and Best Practices
* Topic Number & Slug: 02_naming_rules

---

## 3. Target Files

You will create or edit the following file:

* `docs/NN_topic_slug.md`

A corresponding example file will exist later at:

* `examples/NN_topic_slug.py`

Your document **must include code examples** that can be copied directly into this file later.

---

## 4. Writing Requirements (Strict)

### Language & Tone

* Write **everything in English**
* Use a neutral, instructional tone
* Do not use conversational, playful, or motivational language

---

### Document Structure

Your topic document must:

1. Have **exactly one H1 title** (the topic title)
2. Begin with a **concept-driven opening paragraph**

   * Describe the concept itself, not the document
   * Do **not** start with meta phrases such as "This document explains..." or "This section describes..."
3. Blend explanation and code examples naturally
4. Use multiple **short, focused Python examples**
5. Use `---` to separate major sections
6. End with a section titled `## Example file`

---

### Code Example Rules

* All code must be valid, runnable Python
* Do not include pseudo-code
* Prefer several small examples over one long script
* Use comments only when they add clarity

All code shown in the document should be suitable for direct copy-paste into the example file.

---

## 5. Linking Rules

At the end of the document, include an example file link using this exact format:

```md
- [`NN_topic_slug.py`](../examples/NN_topic_slug.py)
```

Do not modify the relative path.

---

## 6. Content Boundaries

* Focus **only** on the assigned topic
* Do not introduce future topics unless explicitly instructed
* Do not include chapter-level overviews
* Do not define curriculum-wide rules

If you are unsure whether something belongs in this topic, keep it out and flag it for review.

---

## 7. Quality Checklist (Before Submitting)

Confirm all items below:

* [ ] Written entirely in English
* [ ] Exactly one H1 title
* [ ] Concept-driven opening paragraph
* [ ] Explanation and code are interleaved
* [ ] Python examples are runnable
* [ ] No references to other topics or chapters
* [ ] Ends with `## Example file` and correct link
* [ ] Fully follows the Writing Guide

---

## 8. Submission Notes

* Do not create or modify example `.py` files unless explicitly instructed
* Do not rename files or change directory structure
* Ask questions **before** making assumptions

This task is complete when the topic document meets all requirements above.

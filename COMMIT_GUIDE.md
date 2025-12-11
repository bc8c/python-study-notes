# Commit Message Guide

This document defines the commit message conventions used in the `python-study-notes` repository.  
The goal is to create clean, readable commit history and make it easy to understand what changed and why.

---

## 1. Basic Format

Commit messages follow this structure:

```text
<type>(<scope>): <summary>
```

- **type** (required): the nature of the change
- **scope** (optional): the area or folder affected
- **summary** (required): a short, clear description

Examples:

```text
feat(basics): add list and tuple basic examples
docs(oop): add notes on classes and instances
fix(practical): correct wrong file path
```

`scope` can be omitted:

```text
feat: add list and tuple basic examples
```

---

## 2. Commit Types

This repository uses the following six commit types:

### 2.1 feat

For adding new code, examples, features, or files.

```text
feat(basics): add list basic examples
feat(oop): add inheritance practice code
feat(practical): add simple CLI calculator example
```

### 2.2 docs

For documentation changes: notes, README, explanations, comments, etc.

```text
docs(basics): add notes for integer and float types
docs(oop): improve class/instance explanation
docs: update folder structure section in README
```

### 2.3 refactor

For structural improvements without changing behavior.  
Includes renaming files, reorganizing code, splitting functions, etc.

```text
refactor(basics): refactor loop examples for clarity
refactor(algorithms): rename sorting functions
```

### 2.4 fix

For correcting bugs, typos, incorrect examples, or mistakes.

```text
fix(basics): fix comparison operator in conditional example
fix(docs): correct typo in list explanation
```

### 2.5 test

For adding or updating test files (e.g., pytest in the future).

```text
test(algorithms): add tests for binary search implementation
```

### 2.6 chore

For maintenance tasks: environment setup, folder restructuring, configuration updates, etc.

```text
chore: add Python/.venv .gitignore rules
chore: reorganize basics folder structure
```

---

## 3. Writing Rules

1. **Keep each commit focused on a single logical change.**

   - Example: adding list examples and updating README should be separate commits.

2. **Write clear one-line summaries.**  
   Good:

   ```text
   feat(basics): add list slicing examples
   ```

   Bad:

   ```text
   update
   ```

3. Summaries may be written in English or Korean, but clarity is required.

4. If needed, write additional details in the commit body:

```text
feat(basics): add list slicing examples

- basic slicing
- negative index slicing
- step slicing
```

---

## 4. When a Topic Requires Multiple Commits

Even if you're working on the same topic across multiple sessions,  
use `feat` every time **new examples, files, or content are added.**

Examples:

```text
feat(basics): add list basic examples
feat(basics): add additional list practice problems
feat(basics): add tuple basic examples
docs(basics): add notes for list and tuple usage
```

Types are selected based on **the nature of the work**, not on the topic.

---

## 5. Recommended Scopes

Using scopes is optional, but helpful.  
Typical scopes match folder names:

- basics
- intermediate
- oop
- practical
- algorithms
- web
- advanced

Examples:

```text
feat(basics): add nested list examples
refactor(algorithms): restructure sorting examples
```

---

This guide may be updated as the repository grows.

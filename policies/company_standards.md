# Company Coding Standards

All pull requests must follow these guidelines.

---

## 1. Code Structure

- Functions must be small and focused.
- Avoid deeply nested logic (>3 levels).
- Follow single responsibility principle.
- Avoid duplicated logic across files.

---

## 2. Naming Conventions

- Use meaningful variable names.
- Avoid single-letter variable names (except loop counters).
- Use snake_case for Python functions and variables.
- Class names must be PascalCase.

---

## 3. Performance Guidelines

- Avoid unnecessary loops.
- Prefer list comprehensions over manual loops (when readable).
- Avoid repeated database/API calls inside loops.
- Use built-in optimized functions where possible.

---

## 4. Error Handling

- Do not use bare `except:`
- Catch specific exceptions.
- Log errors properly.

---

## 5. Code Duplication

- Do not reimplement logic that already exists in the repository.
- Reuse utilities and helpers.
- Abstract repeated patterns.

---

## 6. Documentation

- All public functions must have docstrings.
- Complex logic must include comments.
- PR description must clearly explain:
  - What changed
  - Why it changed

---

## 7. Testing

- New features must include tests.
- No breaking changes without justification.

---

# Review Instructions

If violations exist:
- Mark FAILED
- Provide:
  - File name
  - Standard violated
  - Suggested fix

If fully compliant:
- Mark PASSED
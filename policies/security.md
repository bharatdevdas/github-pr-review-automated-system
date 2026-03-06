# Security Review Policy

This document defines mandatory security standards for all pull requests.

---

## 1. Input Validation

- All external inputs (API requests, query params, form data, CLI args) must be validated.
- Use strict typing where possible.
- Never trust client-side validation alone.
- Use parameterized queries for database operations.

❌ Forbidden:
- Direct string interpolation in SQL queries
- eval(), exec(), or dynamic code execution
- Blind JSON parsing without schema validation

---

## 2. Authentication & Authorization

- All protected endpoints must require authentication.
- Role-based access control (RBAC) must be enforced.
- Never expose admin functionality publicly.
- Avoid hardcoded credentials or API keys.

---

## 3. Secrets Handling

- Secrets must not be stored in source code.
- Use environment variables or secret managers.
- .env files must not be committed.

❌ Reject PR if:
- API keys appear in code
- Tokens are logged

---

## 4. Logging & Sensitive Data

- Do not log:
  - Passwords
  - Tokens
  - Personal identifiable information (PII)
- Errors should not expose stack traces to end users.

---

## 5. Dependency Safety

- Avoid outdated or vulnerable packages.
- No unknown third-party scripts.
- Prefer well-maintained libraries.

---

## 6. Injection Vulnerabilities

The PR must not introduce:
- SQL Injection
- Command Injection
- XSS
- Path Traversal

---

## 7. File Handling

- Validate file types and size before processing uploads.
- Sanitize file paths.

---

# Review Instructions

If violations exist:
- Mark the PR as FAILED
- Clearly explain:
  - The file
  - The vulnerability type
  - Why it is dangerous
  - How to fix it

If no violations:
- Mark PASSED
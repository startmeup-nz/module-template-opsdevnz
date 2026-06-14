# Non-Functional Requirements

**Module:** <module-name>
**Spec Last Updated:** <date>
**Status:** Draft

---

> Replace this section with the module's non-functional requirements.
> See [SRS Template Section 3.3 (Quality of
> Service)](https://github.com/john-opsdevnz/SRS-Template/blob/master/srs-template.md#33-quality-of-service)
> for guidance on NFR areas: performance, security, reliability, availability,
> observability, maintainability.

## NFR-1: Security

### NFR-1.1: <Requirement>

**Requirement:** <Statement>

**Rationale:** <Why this matters>

---

## NFR-2: Reliability

### NFR-2.1: <Requirement>

**Requirement:** <Statement>

**Rationale:** <Why this matters>

---

## NFR-3: Compatibility

### NFR-3.1: Python Version Support

**Requirement:** The module MUST support Python 3.10 through 3.14.

**Rationale:** Python 3.10 is the minimum for modern type syntax. Python 3.14
is the current latest. CI should test the full supported range.

---

## NFR-4: Code Quality

### NFR-4.1: Linting

**Requirement:** All code MUST pass `ruff check` with no errors.

### NFR-4.2: Testing

**Requirement:** All public API functions and CLI commands MUST have test coverage.

### NFR-4.3: Dependency Hygiene

**Requirement:** Dependencies MUST be declared with minimum viable version pins.

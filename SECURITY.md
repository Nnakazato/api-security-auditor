# Security Invariants

1. The scanner only targets the local Docker API by default.
2. The intentionally vulnerable endpoint is for synthetic lab testing only.
3. Passwords in the secure endpoint are stored as password hashes, not plaintext.
4. The scanner validates the base URL before sending requests.
5. Requests use network timeouts to avoid hanging indefinitely.
6. Evidence artifacts contain request outcomes and security findings, not real user data.
7. Docker runs the app as a non-root user with `no-new-privileges` enabled.

## What the System Detects

- SQL-injection-style authentication bypass behavior
- implementation detail leakage in error messages
- missing or ineffective rate limiting behavior

## What the System Does Not Do

- It is not a full penetration testing suite.
- It does not fuzz every possible input.
- It does not test real external APIs.
- It does not prove an API is fully secure.

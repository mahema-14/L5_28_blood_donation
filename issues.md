
## 4. Document the Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution (`os.system`) | Security | 65 | Executing shell commands can expose the program to command injection. | Removed shell execution and validated phone numbers without invoking a shell. |
| Unsafe temporary file creation (`tempfile.mktemp`) | Security | 60 | `mktemp` can introduce a race condition because it does not securely create the file. | Replaced it with `tempfile.mkstemp` and closed the returned file descriptor. |
| Assertion used for validation | Robustness | 18 | Assertions can be disabled when Python runs in optimized mode. | Replaced the assertion with explicit input validation. |
| Mutable default argument (`notes=[]`) | Code quality | 17 | A mutable default list can be shared between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Broad exception handling | Code quality | 43–47 | Catching a general exception can hide unexpected errors. | Narrowed exception handling to the expected exception. |
| Naming convention violations | Style | Multiple | CamelCase names do not follow Python's snake_case convention. | Renamed functions and parameters to snake_case. |
| Long lines and whitespace issues | Style | Flake8 findings | Long lines and excess blank lines reduce readability. | Wrapped long expressions and corrected whitespace and blank-line formatting. |


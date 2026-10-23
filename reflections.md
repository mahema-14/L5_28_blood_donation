
## 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and coding-style issues before the program is deployed.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks code quality, naming conventions, documentation, and potential programming errors. Bandit identifies common security risks in Python code. Flake8 checks formatting and style, including line length, whitespace, and blank lines.

## 3. What issues did you identify and fix?

The issues included unsafe temporary-file creation, shell command execution, assertion-based validation, mutable default arguments, broad exception handling, naming violations, and formatting problems. Fixing these issues improved the code's security, readability, and maintainability.

## 4. How did you verify your fixes?

I reran the static analysis tools after modifying the source code. Pylint reported a final score of 10.00/10, and Bandit reported no issues identified. Flake8 must also be run on the final saved source file to verify that the formatting issues have been resolved.

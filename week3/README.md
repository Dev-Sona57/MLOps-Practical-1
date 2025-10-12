# Week 3 - Testing, Debugging & OOP

## 🛠️ What I Built
This week, I focused on creating a simple Python project using object-oriented design. I implemented a `DataProcessor` class in `processor.py` that can calculate basic statistics like `mean` and `variance`. I added docstrings to document functionality and help with reproducibility. To practice testing and debugging, I wrote `pytest` tests in `test_processor.py`, intentionally introduced a bug in `mean()` to see the tests fail, and then debugged it to fix the error. I also created a Makefile to standardize running tests and cleaning temporary files.  

- **Tools Used:** Python, VSCode, Pytest, Makefile, Git  
- **Artifacts:** `src/processor.py`, `test/test_processor.py`, `Makefile`  
- **How to Run:**
  
  # Run tests (verbose)
pytest -v

# Run tests (quiet)
pytest -q

# Or using Makefile targets
make test
make clean

# Exploration
OOP and reproducibility: Implementing the DataProcessor class helped me understand why OOP is useful for reproducible projects. Encapsulating data and operations in a class keeps code modular, easier to test, and easier to extend later.
Debugging: Breaking mean() on purpose and using breakpoints in VSCode taught me how to inspect variables and control flow. This hands-on debugging clarified why tests fail and how to systematically find logic errors.
Testing with Pytest: Writing tests for normal cases and edge cases (empty list, single value) reinforced the importance of validating code thoroughly. It showed me that even simple calculations can produce unexpected results if edge cases aren’t handled.. I learned how pytest can quickly confirm correctness, and how the -v flag gives detailed information about each test versus the concise summary with -q.  Documentation: Adding docstrings in Google style helped me see how documenting parameters, return values, and exceptions supports reproducibility. Using help(p.mean) confirmed that future users or collaborators could understand the code without reading the full implementation.

# Evidence of work
Terminal outputs: Screenshots and logs show the script execution, test results. Icsaved pytest results to evidence/pytest_results.txt using: pytest -v > evidence/pytest_results.txt
GitHub Repository: All files (src/processor.py, test/test_processor.py, Makefile) are committed and versioned.
Tests passing/failing: Screenshots of failing tests after introducing a bug and passing tests after fixing it.

# Reflection
This week taught me the value of combining OOP, testing, and debugging for reliable, reproducible projects. Seeing the difference between verbose (-v) and quiet (-q) pytest output clarified how to quickly check overall results versus inspect each individual test. Including logs, screenshots, and a structured workflow ensures that anyone can follow my process and reproduce the results exactly.

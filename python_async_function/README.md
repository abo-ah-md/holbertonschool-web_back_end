# Python Async Function Project

## Overview

This project covers the fundamentals and practice of *asynchronous programming in Python*, focusing on concepts such as `async` and `await`, running concurrent coroutines, creating asyncio tasks, and using the `random` module for generating delays.

You will structure your code to be *pycodestyle-compliant*, fully type-annotated, and well-documented according to project and Holberton School requirements.

---

## Concepts

You are expected to understand and apply the following concepts:

- [Python - Asynchronous execution](https://intranet.hbtn.io/concepts/1173)
- [Python - Asynchronous Programming](https://intranet.hbtn.io/concepts/1174)

## Resources

Recommended readings before starting:

- [Async IO in Python: A Complete Walkthrough](https://intranet.hbtn.io/rltoken/IDv2YZ5p7QHF5SxYZBMGdQ)
- [asyncio - Asynchronous I/O](https://intranet.hbtn.io/rltoken/1neoNd8gRS_mn52IQd5WTQ)
- [random.uniform](https://intranet.hbtn.io/rltoken/XTxPUx9tDxZ51zhIUrSvPw)

---

## Learning Objectives

Upon completion, you should be able to explain:

- The purpose and usage of `async` and `await` syntax.
- How to execute an async program using `asyncio`.
- How to run concurrent coroutines effectively.
- How to create and manage `asyncio.Task` objects.
- How to utilize the `random` module for timing.

---

## Project Requirements

- All code must be *type-annotated* and *well-documented* (module and function docstrings as full sentences).
- Only use approved editors: `vi`, `vim`, `emacs`.
- All scripts must run on Ubuntu 20.04 LTS, using Python 3.9.
- Every file should end with a new line and be executable.
- File length will be checked via `wc`.
- The shebang line in every Python file must be:  
  `#!/usr/bin/env python3`
- Code style compliance: *pycodestyle 2.5.x*
- Project must include this README.md at the root directory.

---

## Directory Structure

```
holbertonschool-web_back_end/
└── python_async_function/
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
├── 4-tasks.py
└── README.md
```

---

## Tasks & Brief Explanations

### 0. The basics of async

- **File:** `0-basic_async_syntax.py`
- **Goal:** Create an asynchronous coroutine `wait_random` that waits for a random delay (between 0 and `max_delay`) using `random.uniform`, then returns the delay.

### 1. Execute multiple coroutines concurrently

- **File:** `1-concurrent_coroutines.py`
- **Goal:** Implement `wait_n`, which spawns `wait_random` n times and returns the delays as a sorted list (ascending order) without using `sort()`.

### 2. Measure the runtime

- **File:** `2-measure_runtime.py`
- **Goal:** Write `measure_time`, which measures the average execution time for running `wait_n(n, max_delay)` using the `time` module.

### 3. Tasks with asyncio

- **File:** `3-tasks.py`
- **Goal:** Implement `task_wait_random(max_delay)`: returns an `asyncio.Task` running `wait_random`.

### 4. Tasks with asyncio (extended)

- **File:** `4-tasks.py`
- **Goal:** Adapt `wait_n` as `task_wait_n`: spawns n `task_wait_random` tasks, collects delays, and returns them sorted as before.

---

## Style & Documentation Checklist

- **Type Annotations:** All functions and coroutines must include type hints.
- **Documentation:** Each module and function must have meaningful, complete docstrings.
- **Executable Files:** Scripts should have correct permissions and the specified shebang.
- **Coding Style:** Code checked with `pycodestyle` version 2.5.x.
- **Comprehensive README:** This file explains the purpose, structure, requirements, and usage.

---

## Example Usage

Here are example main files for task testing:

```
0-main.py
import asyncio
wait_random = import('0-basic_async_syntax').wait_random
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```
Output will be three random delays as floats.
```
1-main.py
import asyncio
wait_n = import('1-concurrent_coroutines').wait_n
print(asyncio.run(wait_n(5, 5)))
```
Output: list of 5 delays, in ascending order.

---

## GitHub Repo

- **Repository:** [`holbertonschool-web_back_end`](https://github.com/abo-ah-md/holbertonschool-web_back_end)
- **Directory:** `python_async_function/`

---

## License

This project is submitted for academic purposes at Holberton School.  
Usage, copying, and distribution are subject to the policies of the institution.

---

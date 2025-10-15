# Python Async Comprehension Project

This project covers advanced concepts in Python asynchronous programming, focusing on async generators, async comprehensions, and proper type annotations in coroutine-based workflows.

## Concepts

You are expected to be familiar with:
- [Python - Asynchronous execution](https://intranet.hbtn.io/concepts/1173)
- [Python - Asynchronous Programming](https://intranet.hbtn.io/concepts/1174)

## Resources

Recommended reading before starting:
- [PEP 530 – Asynchronous Comprehensions](https://intranet.hbtn.io/rltoken/UFCR8qW3nHmEDZZaHqXL7Q)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://intranet.hbtn.io/rltoken/PAGwxZUyVGBR8EMFGGNnGg)
- [Type-hints for generators](https://intranet.hbtn.io/rltoken/SAxOMI925qJrJVGmZ0JBNw)

## Learning Objectives

By completing this project, you will be able to **explain**:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators and coroutines

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Python: Ubuntu 20.04 LTS, version 3.9
- All files must end with a new line
- First line of all files: `#!/usr/bin/env python3`
- A `README.md` file at the root of the project is **mandatory**
- Code style: `pycodestyle` (version 2.5.x)
- File lengths are checked with `wc`
- All modules and functions must have a **full-sentence docstring** (checked with `python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions/coroutines must have **type annotations**

## Directory Structure

```
python_async_comprehension/
├── 0-async_generator.py
├── 1-async_comprehension.py
├── 2-measure_runtime.py
└── README.md
```

## Tasks

### 0. Async Generator

- Implement `async_generator` coroutine (no arguments).
- Loop 10 times, each time:
    - Asynchronously wait 1 second.
    - Yield a random float between 0 and 10 (`random.uniform` recommended).
- Example output:
```
[4.40, 6.91, 6.29, 4.55, 4.13, 9.99, 6.73, 9.84, 1.01, 1.38]
```

### 1. Async Comprehension

- Import `async_generator`.
- Implement `async_comprehension` coroutine (no arguments).
- Collect 10 random numbers **using async comprehension** over `async_generator`.
- Return the resulting list.

### 2. Run Time for Four Parallel Comprehensions

- Import `async_comprehension`.
- Implement `measure_runtime` coroutine.
- Execute `async_comprehension` four times in parallel with `asyncio.gather`.
- Measure the total runtime and return it.
- Expected: **~10 seconds**, since the 10x1s waits in each comprehension overlap in parallel.

## Usage Examples

```
0-main.py
import asyncio
async_generator = import('0-async_generator').async_generator

async def print_yielded_values():
result = []
async for i in async_generator():
result.append(i)
print(result)

asyncio.run(print_yielded_values())
```
---
```
1-main.py
import asyncio
async_comprehension = import('1-async_comprehension').async_comprehension

async def main():
print(await async_comprehension())

asyncio.run(main())
```
---
```
2-main.py
import asyncio
measure_runtime = import('2-measure_runtime').measure_runtime

async def main():
return await(measure_runtime())

print(asyncio.run(main()))
```

## Notes

- Ensure all code and docstrings are properly type-annotated and formatted.
- Documentation for ALL modules and functions is required.
- Use `asyncio` and `random` for coroutine implementations.
- Testing scripts (`0-main.py`, `1-main.py`, `2-main.py`) are provided for local validation.

---

*Project inspired by Holberton School's advanced Python back-end curriculum.*

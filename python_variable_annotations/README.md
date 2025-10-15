# Python Variable Annotations

This project focuses on the practical use of **type annotations in Python 3**. You’ll learn how to specify precise function signatures and variable types, embrace *duck typing*, and validate your code with [mypy](http://mypy-lang.org/).

---

## 💡 Concepts and Resources

- Advanced Python
- [Python 3 Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to **explain** (without the help of Google):

- What *type annotations* are in Python 3
- How to use type annotations for function signatures and variable types
- What *duck typing* is and how it applies in Python
- How to validate your code with **mypy**

---

## ⚙️ Requirements

- **Allowed editors:** vi, vim, emacs
- **Python Version:** 3.9 (Ubuntu 20.04 LTS)
- All files must end with a new line
- *Shebang* required on the first line:  
  `#!/usr/bin/env python3`
- Include a README.md file at project root
- Code style: [pycodestyle](http://pycodestyle.pycqa.org/) (v2.5)
- All files must be executable
- File lengths tested with `wc`
- **Documentation required:**  
  - All modules, classes, and functions must have *real* docstrings explaining their purpose (actual sentences, not just single words)
- Use `python3 -c 'print(__import__(\"my_module\").__doc__)'` to display module doc
- Use `python3 -c 'print(__import__(\"my_module\").MyClass.__doc__)'` for classes
- Use `python3 -c 'print(__import__(\"my_module\").my_function.__doc__)'` for functions

---

## 📋 Tasks & Files

| Task | File                      | Description                                                                    | Annotation Example                                   |
|------|---------------------------|--------------------------------------------------------------------------------|------------------------------------------------------|
| 0    | `0-add.py`                | `add(a: float, b: float) -> float`                                             | `{'a': float, 'b': float, 'return': float}`          |
| 1    | `1-concat.py`             | `concat(str1: str, str2: str) -> str`                                          | `{'str1': str, 'str2': str, 'return': str}`          |
| 2    | `2-floor.py`              | `floor(n: float) -> int`                                                       | `{'n': float, 'return': int}`                        |
| 3    | `3-to_str.py`             | `to_str(n: float) -> str`                                                      | `{'n': float, 'return': str}`                        |
| 4    | `4-define_variables.py`   | Annotated variables: a, pi, i_understand_annotations, school                   | `a: int`, `pi: float`, `i...: bool`, `school: str`   |
| 5    | `5-sum_list.py`           | `sum_list(input_list: List[float]) -> float`                                   | `{'input_list': List[float], 'return': float}`       |
| 6    | `6-sum_mixed_list.py`     | `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`                    | `{'mxd_lst': List[Union[int, float]], 'return': float}` |
| 7    | `7-to_kv.py`              | `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`                     | `{'k': str, 'v': Union[int, float], 'return': Tuple[str, float]}` |
| 8    | `8-make_multiplier.py`    | `make_multiplier(multiplier: float) -> Callable[[float], float]`               | `{'multiplier': float, 'return': Callable[[float], float]}` |
| 9    | `9-element_length.py`     | `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]`        | `{'lst': Iterable[Sequence], 'return': List[Tuple[Sequence, int]]}` |

---

## 🦆 Duck Typing

Duck typing allows Python to be flexible:  
> “If it looks like a duck and quacks like a duck, it must be a duck.”

You’ll annotate iterables and sequences so functions accept any type that fits the required interface, not strictly a list.

---

## ✅ Validation With MyPy

Validate type annotation usage with:
```
mypy <filename.py>
```

---

## 📚 Example Usage

Each file in the project contains a type-annotated function or variable. Example from `0-add.py`:

```
def add(a: float, b: float) -> float:
"""
Adds two float numbers and returns the result as a float.
"""
return a + b
```
Function annotations appear with `__annotations__`:

```
print(add.annotations) # {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

---

## 🗂 Directory Structure
```
python_variable_annotations/
├── 0-add.py
├── 1-concat.py
├── 2-floor.py
├── 3-to_str.py
├── 4-define_variables.py
├── 5-sum_list.py
├── 6-sum_mixed_list.py
├── 7-to_kv.py
├── 8-make_multiplier.py
├── 9-element_length.py
└── README.md
```

---

## 📎 Corrections

- Make sure all functions, classes, and modules have real docstrings.
- Use correct type hints from the Python’s `typing` module as needed.
- Comply with style and documentation requirements for full score.

---

## ✍️ Author

- **Repository:** [holbertonschool-web_back_end](https://github.com/abo-ah-md/holbertonschool-web_back_end)
- **Directory:** `python_variable_annotations`

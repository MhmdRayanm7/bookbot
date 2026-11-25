
# BookBot

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-121011?logo=gnubash&logoColor=white)

BookBot is my first [Boot.dev](https://www.boot.dev) project!

A simple Python command-line application that analyzes text files and generates word counts and character frequency reports.

## Features

- Read and analyze text files
- Count the total number of words
- Calculate case-insensitive letter frequencies
- Sort characters by frequency
- Generate formatted analysis reports
- Accept file paths through command-line arguments

## Concepts Practiced

- Python fundamentals
- File handling
- Functions and modules
- Lists and dictionaries
- Sorting and string manipulation
- Command-line arguments

## Usage

Requires Python 3.

```bash
python3 main.py path/to/book.txt
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

## Project Structure

| File | Purpose |
| --- | --- |
| main.py | CLI entry point and report generation |
| stats.py | Word counting and character analysis |

---

Built as part of the [Boot.dev Build BookBot](https://www.boot.dev/courses/build-bookbot-python) guided project.

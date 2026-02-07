# Console Todo Application

**Version**: 1.0.0
**Phase**: I - In-Memory Console Application

## Overview

A modular, console-based todo application built with Python 3.13+ that stores tasks in memory during runtime. This project demonstrates spec-driven development using Claude Code and Spec-Kit Plus, following clean architecture principles.

## Features

- ✅ Add new todo tasks with descriptions
- ✅ View all tasks in a formatted list
- ✅ Mark tasks as complete
- ✅ Update task descriptions
- ✅ Delete tasks
- ✅ Interactive CLI menu with command aliases
- ✅ Input validation and error handling
- ✅ In-memory storage (no persistence)

## Prerequisites

- Python 3.13 or later
- UV package manager

## Quick Start

### 1. Install UV (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Set Up the Project

```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py
```

## Usage

When you launch the application, you'll see an interactive menu with 6 commands. You can use either numbers (1-6) or command names (add, list, complete, update, delete, exit).

## Development

```bash
# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=src tests/

# Format code
uv run ruff format src/ tests/

# Check linting
uv run ruff check src/ tests/
```

## Project Structure

```
src/models/          # Data structures
src/services/        # Business logic
src/cli/             # User interface
src/utils/           # Helpers
tests/               # Test files
main.py              # Entry point
```

## Documentation

- Specification: `specs/001-console-todo/spec.md`
- Implementation Plan: `specs/001-console-todo/plan.md`
- Tasks: `specs/001-console-todo/tasks.md`

Built with Claude Code and Spec-Kit Plus

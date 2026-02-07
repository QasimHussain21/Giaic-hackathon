# CLI Commands Contract

**Date**: 2026-02-06
**Phase**: 1 (Design)
**Feature**: 001-console-todo

## Overview

This document defines the command-line interface contract for the console todo application. It specifies the interactive menu system, command syntax, input/output formats, and error handling behavior.

## Interface Type

**Interactive Menu (REPL-style)**: The application runs in a continuous loop, displaying a menu and accepting user commands until the user chooses to exit.

**No Command-Line Arguments**: The application does not accept command-line arguments for operations (e.g., `python main.py add "task"`). All interaction is through the interactive menu after launch.

---

## Application Launch

### Command
```bash
python main.py
```

or (with UV)

```bash
uv run main.py
```

### Behavior
1. Display welcome banner
2. Display main menu
3. Wait for user input

### Example Output
```
╔══════════════════════════════════════════════════════════════╗
║         Welcome to Console Todo Application v1.0             ║
║      Your tasks live here (until you close the app)         ║
╚══════════════════════════════════════════════════════════════╝

Main Menu:
  1. Add new task
  2. View all tasks
  3. Mark task as complete
  4. Update task description
  5. Delete task
  6. Exit

Enter command (1-6 or name): _
```

---

## Command 1: Add New Task

### Menu Option
- Number: `1`
- Aliases: `add`, `new`, `create`

### Input Flow
```
You selected: Add new task
Enter task description: Buy groceries
```

### Input Validation
- **Required**: Task description (non-empty, non-whitespace)
- **Max Length**: 500 characters
- **Allowed Characters**: Any UTF-8 text

### Success Response
```
✓ Task added successfully!
  ID: 1
  Description: Buy groceries
  Status: Todo

Press Enter to continue...
```

### Error Responses

**Empty Description**:
```
✗ Error: Task description cannot be empty.
Please try again.

Press Enter to continue...
```

**Too Long**:
```
✗ Error: Task description must be 500 characters or less.
Current length: 523 characters

Press Enter to continue...
```

### Side Effects
- Creates new Task with auto-generated ID
- Adds task to TaskManager storage
- Increments next available ID

---

## Command 2: View All Tasks

### Menu Option
- Number: `2`
- Aliases: `list`, `view`, `show`, `all`

### Input Flow
```
You selected: View all tasks
```

### Success Response (With Tasks)
```
Your Tasks:
┌──────┬──────────────────────────────────────────────────────┬───────────┐
│  ID  │ Description                                          │  Status   │
├──────┼──────────────────────────────────────────────────────┼───────────┤
│  1   │ Buy groceries                                        │ ○ Todo    │
│  2   │ Write documentation                                  │ ✓ Done    │
│  3   │ Review pull requests                                 │ ○ Todo    │
└──────┴──────────────────────────────────────────────────────┴───────────┘

Total: 3 tasks (1 completed, 2 pending)

Press Enter to continue...
```

### Success Response (Empty List)
```
Your Tasks:

  No tasks yet! Use "Add new task" to create your first task.

Press Enter to continue...
```

### Side Effects
None (read-only operation)

---

## Command 3: Mark Task as Complete

### Menu Option
- Number: `3`
- Aliases: `complete`, `done`, `finish`

### Input Flow
```
You selected: Mark task as complete
Enter task ID: 1
```

### Input Validation
- **Required**: Task ID (positive integer)
- **Must Exist**: Task with given ID must exist in system

### Success Response
```
✓ Task marked as complete!
  ID: 1
  Description: Buy groceries
  Status: ✓ Done

Press Enter to continue...
```

### Error Responses

**Invalid ID Format**:
```
✗ Error: Invalid task ID. Please enter a number.

Press Enter to continue...
```

**Task Not Found**:
```
✗ Error: Task with ID 999 not found.
Use "View all tasks" to see available task IDs.

Press Enter to continue...
```

**Already Complete** (Warning, not error):
```
ℹ Task is already marked as complete.
  ID: 1
  Description: Buy groceries
  Status: ✓ Done

Press Enter to continue...
```

### Side Effects
- Updates task's `completed` field to `True`

---

## Command 4: Update Task Description

### Menu Option
- Number: `4`
- Aliases: `update`, `edit`, `modify`

### Input Flow
```
You selected: Update task description
Enter task ID: 1
Current description: Buy groceries
Enter new description: Buy groceries and milk
```

### Input Validation
- **Required**: Task ID (positive integer, must exist)
- **Required**: New description (non-empty, non-whitespace, ≤500 chars)

### Success Response
```
✓ Task updated successfully!
  ID: 1
  Old: Buy groceries
  New: Buy groceries and milk

Press Enter to continue...
```

### Error Responses

**Invalid ID Format**:
```
✗ Error: Invalid task ID. Please enter a number.

Press Enter to continue...
```

**Task Not Found**:
```
✗ Error: Task with ID 999 not found.
Use "View all tasks" to see available task IDs.

Press Enter to continue...
```

**Empty New Description**:
```
✗ Error: Task description cannot be empty.
Please try again.

Press Enter to continue...
```

**Too Long**:
```
✗ Error: Task description must be 500 characters or less.
Current length: 523 characters

Press Enter to continue...
```

### Side Effects
- Updates task's `description` field

---

## Command 5: Delete Task

### Menu Option
- Number: `5`
- Aliases: `delete`, `remove`, `rm`

### Input Flow
```
You selected: Delete task
Enter task ID: 1
Current task: Buy groceries (Todo)
Are you sure you want to delete this task? (y/n): y
```

### Input Validation
- **Required**: Task ID (positive integer, must exist)
- **Required**: Confirmation (y/yes or n/no, case-insensitive)

### Success Response
```
✓ Task deleted successfully!
  ID: 1
  Description: Buy groceries

Press Enter to continue...
```

### Error Responses

**Invalid ID Format**:
```
✗ Error: Invalid task ID. Please enter a number.

Press Enter to continue...
```

**Task Not Found**:
```
✗ Error: Task with ID 999 not found.
Use "View all tasks" to see available task IDs.

Press Enter to continue...
```

**Delete Cancelled**:
```
ℹ Delete cancelled. Task not removed.

Press Enter to continue...
```

### Side Effects
- Removes task from TaskManager storage
- Task ID is not reused

---

## Command 6: Exit

### Menu Option
- Number: `6`
- Aliases: `exit`, `quit`, `q`

### Input Flow
```
You selected: Exit

Goodbye! Your tasks will be lost when the application closes.

Thank you for using Console Todo Application.
```

### Behavior
- Display farewell message
- Remind user that tasks are not saved
- Exit the application cleanly (exit code 0)

### Side Effects
- Application terminates
- All in-memory data is lost

---

## Special Inputs

### Help
**Triggers**: `help`, `h`, `?`

**Response**:
```
Help - Available Commands:
  1 / add      - Add a new task
  2 / list     - View all tasks
  3 / complete - Mark a task as done
  4 / update   - Update task description
  5 / delete   - Remove a task
  6 / exit     - Quit the application

Tips:
  - Task IDs are shown in the "View all tasks" list
  - Use ID numbers to reference specific tasks
  - All tasks are stored in memory only

Press Enter to continue...
```

### Invalid Command
**Triggers**: Any input that doesn't match a valid command or number

**Response**:
```
✗ Invalid command: "xyz"

Please enter a number (1-6) or command name.
Type "help" to see available commands.

Press Enter to continue...
```

### Keyboard Interrupt (Ctrl+C)
**Triggers**: User presses Ctrl+C

**Behavior**:
```
^C
Interrupt detected. Exiting gracefully...

Goodbye! Your tasks will be lost when the application closes.
```

Exit cleanly without error.

---

## Input/Output Formats

### Input Format
- **Interactive text input**: All inputs via `input()` prompts
- **Encoding**: UTF-8
- **Case Sensitivity**: Command names are case-insensitive; task descriptions preserve case

### Output Format
- **Plain text** with Unicode box-drawing characters for tables
- **Color**: None (Phase I is plain text only)
- **Encoding**: UTF-8

### Status Symbols
- `○` - Incomplete task
- `✓` - Completed task
- `✗` - Error indicator
- `ℹ` - Information/warning indicator

---

## Error Handling Contract

### Error Categories

1. **Validation Errors**: Invalid input format or values
   - Display clear error message
   - Return to menu (don't crash)
   - Allow user to retry

2. **Not Found Errors**: Resource (task ID) doesn't exist
   - Display "not found" message
   - Suggest using "View all tasks"
   - Return to menu

3. **System Errors**: Unexpected exceptions
   - Display generic error message
   - Log exception details (if logging implemented)
   - Return to menu gracefully

### Error Message Format
```
✗ Error: [Clear description of what went wrong]
[Optional: Suggestion for how to fix]

Press Enter to continue...
```

---

## Performance Contract

### Response Time Targets
- **Menu display**: Instant (<100ms)
- **Add task**: <100ms
- **View all tasks**: <500ms (up to 1000 tasks)
- **Update/Complete/Delete task**: <100ms

### Scalability
- Application must remain responsive with up to 1000 tasks
- View command may paginate in future if list becomes unwieldy

---

## Testing Contract

### Manual Testing Scenarios

1. **Happy Path**: Add → View → Complete → Update → Delete → Exit
2. **Empty State**: View tasks when none exist
3. **Invalid Inputs**: Test each command with invalid inputs
4. **Edge Cases**: Empty descriptions, very long descriptions, invalid IDs
5. **Interrupt**: Press Ctrl+C during various prompts

### Automated Testing

- **Integration Tests**: Simulate user input sequences
- **Mock stdin/stdout**: Capture and verify console output
- **Error Path Coverage**: Test all error conditions

---

## Future Enhancements (Phase II+)

These features are NOT in Phase I but are documented for future reference:

- **Search/Filter**: Search tasks by keyword
- **Sorting**: Sort tasks by ID, creation date, status
- **Bulk Operations**: Complete/delete multiple tasks
- **Task Details**: View detailed task information including timestamps
- **Undo**: Undo last operation
- **Color Output**: Use Rich library for colored, styled output
- **Command History**: Arrow key navigation for previous commands
- **Auto-completion**: Tab completion for command names

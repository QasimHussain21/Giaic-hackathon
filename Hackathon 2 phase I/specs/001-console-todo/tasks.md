# Tasks: In-Memory Console Todo Application

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/, research.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths below use single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize UV project with Python 3.13+ in project root (creates pyproject.toml)
- [ ] T002 Configure pyproject.toml with project metadata and dev dependencies (pytest, pytest-cov, ruff)
- [ ] T003 Create .gitignore file with Python patterns (.venv/, __pycache__/, *.pyc, .pytest_cache/, htmlcov/)
- [ ] T004 [P] Create src/models/ directory with __init__.py
- [ ] T005 [P] Create src/services/ directory with __init__.py
- [ ] T006 [P] Create src/cli/ directory with __init__.py
- [ ] T007 [P] Create src/utils/ directory with __init__.py
- [ ] T008 [P] Create tests/unit/ directory
- [ ] T009 [P] Create tests/integration/ directory
- [ ] T010 Create tests/conftest.py with pytest fixtures for common test data
- [ ] T011 Create README.md with project overview, setup instructions, and usage guide
- [ ] T012 Run uv sync to initialize virtual environment and install dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T013 Implement Task dataclass in src/models/task.py with id, description, completed, created_at fields
- [ ] T014 Add Task.__post_init__() validation method (ID > 0, description non-empty, length ≤500 chars)
- [ ] T015 Add Task.mark_complete() method to set completed=True
- [ ] T016 Add Task.update_description() method with validation
- [ ] T017 Add Task.__str__() method for human-readable output with status symbols
- [ ] T018 Implement TaskManager class in src/services/task_manager.py with _tasks dict and _next_id counter
- [ ] T019 Add TaskManager.__init__() to initialize empty storage and ID counter at 1
- [ ] T020 [P] Implement input validators in src/utils/validators.py (validate_description, validate_task_id)
- [ ] T021 [P] Implement output formatters in src/utils/formatters.py (format_task_list, format_success, format_error)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Developer can add new todo tasks and view all tasks in a formatted list

**Independent Test**: Launch application, add tasks, view task list, verify IDs and descriptions display correctly

### Implementation for User Story 1

- [ ] T022 [P] [US1] Implement TaskManager.add_task(description) in src/services/task_manager.py
- [ ] T023 [P] [US1] Implement TaskManager.get_all_tasks() in src/services/task_manager.py
- [ ] T024 [P] [US1] Implement TaskManager.task_count() helper method in src/services/task_manager.py
- [ ] T025 [US1] Create add_task command handler in src/cli/commands.py (prompts for description, calls service)
- [ ] T026 [US1] Create view_tasks command handler in src/cli/commands.py (gets tasks, formats output)
- [ ] T027 [US1] Handle empty task list case in view_tasks command (display friendly message)
- [ ] T028 [US1] Add validation and error handling for add_task command (empty description, too long)
- [ ] T029 [US1] Test add_task and view_tasks integration manually via CLI

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mark Tasks as Complete (Priority: P2)

**Goal**: Developer can mark specific tasks as complete using task IDs

**Independent Test**: Add tasks, mark specific task as complete, verify status changes when viewing task list

### Implementation for User Story 2

- [ ] T030 [US2] Implement TaskManager.get_task(task_id) in src/services/task_manager.py
- [ ] T031 [US2] Implement TaskManager.mark_task_complete(task_id) in src/services/task_manager.py
- [ ] T032 [US2] Create complete_task command handler in src/cli/commands.py (prompts for ID, calls service)
- [ ] T033 [US2] Add task ID validation in complete_task command (numeric check, existence check)
- [ ] T034 [US2] Add error handling for non-existent task IDs (clear error message)
- [ ] T035 [US2] Update view_tasks formatter to visually distinguish completed tasks (✓ vs ○ symbols)
- [ ] T036 [US2] Test mark complete workflow manually via CLI

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Descriptions (Priority: P3)

**Goal**: Developer can modify the description of existing tasks

**Independent Test**: Add tasks, update task description, verify updated description displays when viewing tasks

### Implementation for User Story 3

- [ ] T037 [US3] Implement TaskManager.update_task(task_id, new_description) in src/services/task_manager.py
- [ ] T038 [US3] Create update_task command handler in src/cli/commands.py (prompts for ID and new description)
- [ ] T039 [US3] Display current description before prompting for new description in update_task command
- [ ] T040 [US3] Add validation for new description (non-empty, ≤500 chars) in update_task command
- [ ] T041 [US3] Add error handling for non-existent task IDs in update command
- [ ] T042 [US3] Test update workflow manually via CLI

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Developer can permanently remove tasks from the list

**Independent Test**: Add tasks, delete specific task, verify deleted task no longer appears in list

### Implementation for User Story 4

- [ ] T043 [US4] Implement TaskManager.delete_task(task_id) in src/services/task_manager.py
- [ ] T044 [US4] Create delete_task command handler in src/cli/commands.py (prompts for ID)
- [ ] T045 [US4] Display task details before deletion and prompt for confirmation (y/n)
- [ ] T046 [US4] Add error handling for non-existent task IDs in delete command
- [ ] T047 [US4] Handle deletion cancellation (user enters 'n')
- [ ] T048 [US4] Test delete workflow manually via CLI including cancellation

**Checkpoint**: All CRUD operations should now be fully functional

---

## Phase 7: User Story 5 - Interactive CLI Menu (Priority: P5)

**Goal**: Developer sees a polished menu interface with all available commands

**Independent Test**: Launch application, verify menu displays clearly, test all commands via menu numbers and aliases

### Implementation for User Story 5

- [ ] T049 [US5] Create display_welcome_banner() function in src/cli/menu.py with ASCII art header
- [ ] T050 [US5] Create display_main_menu() function in src/cli/menu.py with all 6 commands listed
- [ ] T051 [US5] Create get_user_command() function in src/cli/menu.py (handles numbers and aliases)
- [ ] T052 [US5] Implement command routing logic in src/cli/menu.py (maps input to command handlers)
- [ ] T053 [US5] Add command aliases support (add/new/create, list/view, complete, update/edit, delete/rm, exit/quit)
- [ ] T054 [US5] Add help command handler that displays all available commands with descriptions
- [ ] T055 [US5] Add invalid command error handling with helpful message
- [ ] T056 [US5] Implement main application loop in main.py (welcome → menu → command → repeat)
- [ ] T057 [US5] Add "Press Enter to continue" pause after each command completes
- [ ] T058 [US5] Add exit command that displays goodbye message and terminates cleanly
- [ ] T059 [US5] Add Ctrl+C interrupt handler for graceful exit
- [ ] T060 [US5] Test full menu interaction flow with all commands

**Checkpoint**: Interactive menu system complete, all features accessible through user-friendly interface

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T061 [P] Run ruff format on all source files (src/ and tests/) to ensure PEP-8 compliance
- [ ] T062 [P] Run ruff check on all source files and fix any linting issues
- [ ] T063 [P] Add docstrings to all public functions and classes following Google style
- [ ] T064 [P] Add type hints to all function signatures
- [ ] T065 Write unit tests for Task model in tests/unit/test_task.py (creation, validation, methods)
- [ ] T066 Write unit tests for TaskManager in tests/unit/test_task_manager.py (all CRUD operations)
- [ ] T067 Write unit tests for validators in tests/unit/test_validators.py
- [ ] T068 Write unit tests for formatters in tests/unit/test_formatters.py
- [ ] T069 Write integration test for full CLI flow in tests/integration/test_cli_flow.py
- [ ] T070 Run pytest with coverage (pytest --cov=src tests/) and verify >80% coverage
- [ ] T071 Update README.md with final usage examples and screenshots (text-based)
- [ ] T072 Verify quickstart.md instructions work end-to-end
- [ ] T073 Create sample session transcript showing all commands in README.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1 - MVP)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 (needs view_tasks for verification)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Builds on US1 (needs add_task and view_tasks)
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Builds on US1 (needs add_task and view_tasks)
- **User Story 5 (P5)**: Can start after US1-US4 complete - Wraps all commands in menu interface

### Within Each User Story

- Models before services (Task before TaskManager)
- Services before CLI commands (TaskManager before command handlers)
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T004-T009)
- Foundational utilities (validators, formatters) marked [P] can run in parallel (T020-T021)
- All TaskManager methods marked [P] within a story can run in parallel
- Different user stories can be worked on in parallel by different team members after Foundational phase
- Polish tasks marked [P] can run in parallel (T061-T064, T065-T068)

---

## Parallel Example: User Story 1

```bash
# Launch TaskManager methods together (once Task model complete):
Task: "Implement TaskManager.add_task(description) in src/services/task_manager.py"
Task: "Implement TaskManager.get_all_tasks() in src/services/task_manager.py"
Task: "Implement TaskManager.task_count() helper method in src/services/task_manager.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T012)
2. Complete Phase 2: Foundational (T013-T021) - **CRITICAL blocking phase**
3. Complete Phase 3: User Story 1 (T022-T029)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Create simple menu.py with basic loop to test add and view commands
6. Demo MVP functionality

**MVP Deliverable**: Developers can add and view tasks through a basic console interface

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready (T001-T021)
2. Add User Story 1 (T022-T029) → Test independently → MVP Demo
3. Add User Story 2 (T030-T036) → Test independently → Mark complete feature added
4. Add User Story 3 (T037-T042) → Test independently → Update feature added
5. Add User Story 4 (T043-T048) → Test independently → Delete feature added
6. Add User Story 5 (T049-T060) → Test independently → Polished menu interface complete
7. Polish (T061-T073) → Production-ready quality

Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T021)
2. Once Foundational is done:
   - Developer A: User Story 1 (T022-T029)
   - Developer B: User Story 2 (T030-T036) - wait for US1 view_tasks
   - Developer C: User Story 3 (T037-T042) - wait for US1 add_task
3. Stories complete and integrate independently
4. All team members collaborate on US5 menu integration
5. Parallel testing and polish (T061-T073)

---

## Testing Strategy

### Manual Testing After Each Story

- **US1**: Add 3 tasks, view list, verify IDs and descriptions
- **US2**: Add tasks, mark one complete, view list, verify visual distinction
- **US3**: Add task, update description, view list, verify change
- **US4**: Add tasks, delete one, view list, verify removal
- **US5**: Launch app, test all menu options and aliases, verify help command

### Automated Testing (Phase 8)

- **Unit Tests**: Test each class/function in isolation with various inputs
- **Integration Tests**: Test full command flows (add → view → complete → delete)
- **Coverage Target**: >80% (per constitution Phase I success criteria)
- **Focus Areas**: Task model validation, TaskManager operations, validators

### Edge Case Testing

Test scenarios from spec.md edge cases:
- Empty task description
- Task description >500 chars
- Invalid task IDs (non-numeric, negative, non-existent)
- Already completed task re-completion
- Duplicate task descriptions
- Ctrl+C interrupt handling

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Count Summary

- **Phase 1 (Setup)**: 12 tasks
- **Phase 2 (Foundational)**: 9 tasks (CRITICAL - blocks all stories)
- **Phase 3 (US1 - MVP)**: 8 tasks
- **Phase 4 (US2)**: 7 tasks
- **Phase 5 (US3)**: 6 tasks
- **Phase 6 (US4)**: 6 tasks
- **Phase 7 (US5)**: 12 tasks
- **Phase 8 (Polish)**: 13 tasks

**Total**: 73 tasks

**Parallel Opportunities**: 15+ tasks can run in parallel
**Independent Stories**: US1-US4 can be developed in parallel after Foundational phase
**MVP Scope**: Phases 1-3 only (29 tasks) delivers basic working application

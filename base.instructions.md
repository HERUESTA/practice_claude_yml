# Code Quality Instructions

Based on review feedback, the following coding standards and practices should be followed:

## Function Design Principles

### Single Responsibility Principle
Functions should have a single, well-defined responsibility. When a function performs multiple distinct tasks, it should be broken down into smaller, focused functions.

**Example violation:** A single function that handles file reading, data filtering, scoring calculations, aggregation, and file writing should be split into separate functions like:
- `load_users()` - Handle file reading and JSON parsing
- `filter_users()` - Apply filtering logic
- `calculate_scores()` - Handle scoring and ranking logic  
- `summarize()` - Aggregate results and statistics
- `save_result()` - Handle output file writing

This improves code maintainability, testability, and readability.

## Error Handling
Always implement proper error handling for:
- File operations (reading/writing)
- JSON parsing
- Division operations (check for zero division)
- Empty result sets that could cause division by zero

## Code Quality Standards
- Use meaningful variable names instead of single-letter variables (avoid `x`, `d`, `res`, `f`, `out`, `u`, `r`)
- Add type annotations for function parameters and return values
- Include docstrings for functions
- Use context managers (`with` statements) for file operations to prevent resource leaks
- Avoid magic numbers - use named constants instead (e.g., define `MIN_AGE = 20`, `SCORE_THRESHOLDS = [40, 60, 80]`)
- Add appropriate comments for complex logic
- Validate input parameters and handle edge cases (empty files, malformed JSON, etc.)

## Resource Management
Always use proper resource management patterns:
- Use `with` statements for file operations
- Close resources explicitly when `with` statements cannot be used
- Handle exceptions that may prevent proper resource cleanup
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

## Code Quality Standards
- Use meaningful variable names instead of single-letter variables
- Add type annotations for function parameters and return values
- Include docstrings for functions
- Use context managers (`with` statements) for file operations
- Avoid magic numbers - use named constants instead
- Add appropriate comments for complex logic
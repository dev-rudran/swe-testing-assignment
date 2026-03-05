# Testing Strategy

This document outlines the testing approach for Quick-Calc, demonstrating understanding of software testing concepts from Lecture 3.

## What Was Tested

### Unit Testing
The unit tests verify that individual functions work correctly in isolation:

- **Addition**: Positive, negative, and mixed number operations
- **Subtraction**: Positive results and negative results
- **Multiplication**: Positive numbers and zero
- **Division**: Standard division, decimal results, and division by zero (edge case)
- **Clear functionality**: Reset calculator state

### Integration Testing
Integration tests verify that different parts of the application work together correctly:

- Complete user workflows (e.g., entering "5", pressing "+", entering "3", pressing "=")
- Clear after calculation
- Chained operations
- Decimal calculations

## What Was NOT Tested and Why

The following were intentionally not tested:

- **GUI appearance**: Visual testing is subjective and requires manual verification
- **User experience**: Interaction patterns are best tested via user feedback
- **Performance**: The calculator operations are simple and fast; performance testing is unnecessary
- **Platform-specific behavior**: Tkinter handles cross-platform differences

## Testing Pyramid

The Testing Pyramid illustrates the proportion of different test types:

```
        /\
       /  \
      / UI \          <- Few E2E tests
     /------\
    /Integration\     <- Some integration tests
   /------------\
  /   Unit      \    <- Many unit tests
 /    Tests      \
/________________\
```

My test suite reflects this pyramid:
- **13 unit tests**: Most tests at the unit level for fast feedback
- **7 integration tests**: Fewer tests that verify component interaction

This structure provides:
- Fast execution (unit tests run quickly)
- Good coverage of core logic
- Reasonable confidence in the system's behavior

## Black-box vs White-box Testing

### Unit Tests: White-box Testing
Unit tests are designed with knowledge of the internal implementation:
- Tests directly call `calc.add()`, `calc.subtract()`, etc.
- Verify internal state changes (e.g., `previous_input`, `operator`)
- Test edge cases based on code understanding

### Integration Tests: Black-box Testing
Integration tests treat the system as a "black box":
- Focus on user workflows and expected outputs
- No knowledge of internal state
- Verify end-to-end functionality

## Functional vs Non-functional Testing

### Functional Testing (Covered)
- Correct arithmetic operations
- Division by zero handling
- Clear functionality
- Input validation

### Non-functional Testing (Not Covered)
- **Performance**: Not applicable for simple calculator
- **Security**: No sensitive data or external inputs
- **Usability**: Requires user feedback
- **Compatibility**: Tkinter provides cross-platform support

This approach follows industry best practices: focus functional testing on core requirements.

## Regression Testing

The test suite serves as a regression safety net for future updates:

1. **Before making changes**: Run `pytest` to ensure all tests pass
2. **After changes**: Re-run tests to catch any regressions
3. **Continuous Integration**: Tests can be automated in CI/CD pipelines

Example workflow:
```bash
# Before making changes
pytest tests/ -v
# All 20 tests pass

# Make changes to calculator logic
# ...

# After changes
pytest tests/ -v
# If any test fails, you introduced a regression
```

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_add_positive_numbers | Unit | Pass |
| test_add_negative_numbers | Unit | Pass |
| test_add_mixed_numbers | Unit | Pass |
| test_subtract_positive_numbers | Unit | Pass |
| test_subtract_result_negative | Unit | Pass |
| test_multiply_positive_numbers | Unit | Pass |
| test_multiply_by_zero | Unit | Pass |
| test_divide_positive_numbers | Unit | Pass |
| test_divide_result_with_decimal | Unit | Pass |
| test_divide_by_zero_raises_error | Unit | Pass |
| test_clear_resets_calculator | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_full_addition_workflow | Integration | Pass |
| test_full_subtraction_workflow | Integration | Pass |
| test_full_multiplication_workflow | Integration | Pass |
| test_full_division_workflow | Integration | Pass |
| test_clear_after_calculation | Integration | Pass |
| test_chained_operations | Integration | Pass |
| test_decimal_calculation | Integration | Pass |

**Total: 20 tests, 20 passed**

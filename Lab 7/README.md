# Lab 7: Fuzz Testing

## Objective
To identify and fix input validation bugs using the Hypothesis fuzz testing library.

## Tools Used
- Python
- Pytest
- Hypothesis

## Functions Tested
1. nights_stayed()
2. room_floor()
3. booking_label()

## Bugs Identified
- Invalid date formats and non-numeric values.
- Missing or invalid room codes.
- Empty guest names and None inputs.

## Bug Fixes
Added input validation and defensive programming to prevent unexpected inputs from crashing the application.

## Test Results
- Before fixing: 3 tests failed.
- After fixing: 3 tests passed.

## Conclusion
Hypothesis successfully generated unexpected inputs and identified bugs in all three functions. After implementing input validation, all fuzz tests passed.

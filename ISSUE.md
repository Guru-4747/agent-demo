Title: Average function crashes for an empty list

The average(numbers) function in calculator.py raises ZeroDivisionError when
numbers is an empty list.

Expected behavior:
- average([]) returns 0.
- average([2, 4, 6]) returns 4.
- Negative numbers, a single number, and decimal numbers keep working.

Add a regression test for this issue and preserve the existing tests.

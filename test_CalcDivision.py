# ********RoostGPT********
"""
Test generated by RoostGPT for test aman28thMay using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=division_531bd48a9c
ROOST_METHOD_SIG_HASH=division_eae366bb2d

Scenario 1: Division of two positive numbers
Details:
  TestName: test_division_of_positive_numbers
  Description: This test is intended to verify the correctness of the division operation when both the inputs are positive numbers.
Execution:
  Arrange: Initialize two positive numbers, num1 and num2.
  Act: Invoke the function division with num1 and num2 as parameters.
  Assert: Check that the returned value is equal to the division of num1 by num2.
Validation:
  Rationalize: This test ensures that the function correctly divides two positive numbers. This is a fundamental requirement for any division function.

Scenario 2: Division of two negative numbers
Details:
  TestName: test_division_of_negative_numbers
  Description: This test is intended to verify the correctness of the division operation when both the inputs are negative numbers.
Execution:
  Arrange: Initialize two negative numbers, num1 and num2.
  Act: Invoke the function division with num1 and num2 as parameters.
  Assert: Check that the returned value is equal to the division of num1 by num2.
Validation:
  Rationalize: This test ensures that the function correctly divides two negative numbers. This is essential as division of two negative numbers results in a positive number.

Scenario 3: Division of a positive number by zero
Details:
  TestName: test_division_by_zero
  Description: This test is intended to verify that the function correctly handles division by zero.
Execution:
  Arrange: Initialize a positive number num1 and set num2 to zero.
  Act: Invoke the function division with num1 and num2 as parameters.
  Assert: Check that the returned value is "Cannot divide by zero".
Validation:
  Rationalize: This test ensures that the function correctly handles division by zero, which is not a valid mathematical operation. This is a critical requirement for any division function to avoid undefined behavior.

Scenario 4: Division of zero by a positive number
Details:
  TestName: test_division_of_zero
  Description: This test is intended to verify that the function correctly handles division of zero by a positive number.
Execution:
  Arrange: Initialize num1 to zero and num2 to a positive number.
  Act: Invoke the function division with num1 and num2 as parameters.
  Assert: Check that the returned value is zero.
Validation:
  Rationalize: This test ensures that the function correctly handles division of zero by a positive number, which should always result in zero. This is a basic mathematical rule and must be correctly handled by the function.
"""

# ********RoostGPT********
import pytest
from calc import division

class Test_CalcDivision:
    @pytest.mark.positive
    def test_division_of_positive_numbers(self):
        num1, num2 = 10, 2
        result = division(num1, num2)
        assert result == 5, 'Failed to divide two positive numbers'

    @pytest.mark.positive
    def test_division_of_negative_numbers(self):
        num1, num2 = -10, -2
        result = division(num1, num2)
        assert result == 5, 'Failed to divide two negative numbers'

    @pytest.mark.negative
    def test_division_by_zero(self):
        num1, num2 = 10, 0
        result = division(num1, num2)
        assert result == "Cannot divide by zero", 'Failed to handle division by zero'

    @pytest.mark.positive
    def test_division_of_zero(self):
        num1, num2 = 0, 10
        result = division(num1, num2)
        assert result == 0, 'Failed to handle division of zero by a positive number'

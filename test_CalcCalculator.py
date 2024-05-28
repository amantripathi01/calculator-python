# ********RoostGPT********
"""
Test generated by RoostGPT for test aman28thMay using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=calculator_9ebd2df6b3
ROOST_METHOD_SIG_HASH=calculator_ad84dc0779

Scenario 1: Test Addition Operation
Details:
  TestName: test_calculator_addition
  Description: The test is intended to verify the addition operation in the calculator function.
Execution:
  Arrange: Initialize two numbers and the operation as '+'.
  Act: Invoke the calculator function with the two numbers and the operation.
  Assert: Confirm that the result is the sum of the two numbers.
Validation:
  This test is important to ensure that the calculator function correctly performs the addition operation and returns the expected result.

Scenario 2: Test Subtraction Operation
Details:
  TestName: test_calculator_subtraction
  Description: The test is intended to verify the subtraction operation in the calculator function.
Execution:
  Arrange: Initialize two numbers and the operation as '-'.
  Act: Invoke the calculator function with the two numbers and the operation.
  Assert: Confirm that the result is the difference of the two numbers.
Validation:
  This test is important to ensure that the calculator function correctly performs the subtraction operation and returns the expected result.

Scenario 3: Test Multiplication Operation
Details:
  TestName: test_calculator_multiplication
  Description: The test is intended to verify the multiplication operation in the calculator function.
Execution:
  Arrange: Initialize two numbers and the operation as '*'.
  Act: Invoke the calculator function with the two numbers and the operation.
  Assert: Confirm that the result is the product of the two numbers.
Validation:
  This test is important to ensure that the calculator function correctly performs the multiplication operation and returns the expected result.

Scenario 4: Test Division Operation
Details:
  TestName: test_calculator_division
  Description: The test is intended to verify the division operation in the calculator function.
Execution:
  Arrange: Initialize two numbers and the operation as '/'.
  Act: Invoke the calculator function with the two numbers and the operation.
  Assert: Confirm that the result is the quotient of the two numbers.
Validation:
  This test is important to ensure that the calculator function correctly performs the division operation and returns the expected result.

Scenario 5: Test Division by Zero
Details:
  TestName: test_calculator_division_by_zero
  Description: The test is intended to verify that the calculator function handles division by zero.
Execution:
  Arrange: Initialize a number and the operation as '/', with the second number as 0.
  Act: Invoke the calculator function with the number, 0, and the operation.
  Assert: Confirm that the result is "Cannot divide by zero".
Validation:
  This test is important to ensure that the calculator function handles division by zero and returns the expected result.

Scenario 6: Test Invalid Operation
Details:
  TestName: test_calculator_invalid_operation
  Description: The test is intended to verify that the calculator function handles an invalid operation.
Execution:
  Arrange: Initialize two numbers and an invalid operation.
  Act: Invoke the calculator function with the two numbers and the invalid operation.
  Assert: Confirm that the result is "Invalid operation".
Validation:
  This test is important to ensure that the calculator function handles an invalid operation and returns the expected result.
"""

# ********RoostGPT********
import pytest
from calc import calculator

class Test_CalcCalculator:

    def test_calculator_addition(self):
        num1, num2 = 10, 5
        operation = '+'
        result = calculator(num1, num2, operation)
        assert result == 15, 'Failed on Test Addition Operation'

    def test_calculator_subtraction(self):
        num1, num2 = 10, 5
        operation = '-'
        result = calculator(num1, num2, operation)
        assert result == 5, 'Failed on Test Subtraction Operation'

    def test_calculator_multiplication(self):
        num1, num2 = 10, 5
        operation = '*'
        result = calculator(num1, num2, operation)
        assert result == 50, 'Failed on Test Multiplication Operation'

    def test_calculator_division(self):
        num1, num2 = 10, 5
        operation = '/'
        result = calculator(num1, num2, operation)
        assert result == 2, 'Failed on Test Division Operation'

    def test_calculator_division_by_zero(self):
        num1, num2 = 10, 0
        operation = '/'
        result = calculator(num1, num2, operation)
        assert result == "Cannot divide by zero", 'Failed on Test Division by Zero'

    def test_calculator_invalid_operation(self):
        num1, num2 = 10, 5
        operation = '^'
        result = calculator(num1, num2, operation)
        assert result == "Invalid operation", 'Failed on Test Invalid Operation'

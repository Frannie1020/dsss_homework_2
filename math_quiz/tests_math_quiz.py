import unittest
from math_quiz import generate_random_num, get_random_operator, generate_problem

class TestMathGame(unittest.TestCase):
    # Unit tests for the math quiz functions.

    def test_generate_random_num(self):
        # Test if random numbers generated are within the specified range.
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if the operator is one of the expected values.
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = get_random_operator()
            self.assertIn(operator, operators)

    def test_generate_problem(self):
        # Test if the generated problem and answer are correct.
        test_cases = [
            (9, 3, '+', '9 + 3', 12),
            (9, 3, '-', '9 - 3', 6),
            (9, 3, '*', '9 * 3', 27),
            (10, 6, '+', '10 + 6', 16),
            (10, 6, '-', '10 - 6', 4),
            (10, 6, '*', '10 * 6', 60)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
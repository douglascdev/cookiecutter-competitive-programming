from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch
import cp_problem


class CPProblemTests(TestCase):
    """
    Each method starting with "test_" will run when you run this script.
    You can copy the "test_problem" method and simply replace the variables with the input and expected output.
    """

    def io_test(self, problem_input, problem_output, method=cp_problem.problem) -> None:
        """
        Mocks the input method and the standard output and tests if the expected output is printed.
        :param problem_input: input that will be mocked into input() calls within the function
        :param problem_output: the output that the method is expected to print()
        :param method: method that will be called with mocked input and output, cp_problem.problem by default
        """
        with patch("builtins.input", side_effect=problem_input.split("\n")), patch(
            "sys.stdout", new=StringIO()
        ) as fake_out:
            method()
            self.assertEqual(fake_out.getvalue(), problem_output)

    @staticmethod
    def method() -> None:
        _ = input()
        print("1", end="")

    def test_io_test(self) -> None:
        """
        Tests if the mock function is working as intended
        """
        problem_input = """1"""
        problem_output = """1"""
        self.io_test(problem_input, problem_output, self.method)

    def test_problem(self) -> None:
        """
        Enter the input and expected output below. Running this file will run this test automatically.
        Copy and paste this method to create multiple tests.
        """
        problem_input = """"""
        problem_output = """"""
        self.io_test(problem_input, problem_output)


if __name__ == "__main__":
    main()

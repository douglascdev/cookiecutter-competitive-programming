from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch
from typing import Callable
import cp_problem


def run_with_mocked_io(problem_input: str, method: Callable) -> str:
    """
    Mocks the input method and the standard output and tests if the expected output is printed.
    :param problem_input: input that will be mocked into input() calls within the function
    :param method: method that will be called with mocked input and output
    :return: the output printed while running the method
    """
    with patch("builtins.input", side_effect=problem_input.split("\n")), patch(
        "sys.stdout", new=StringIO()
    ) as fake_out:
        method()
        return fake_out.getvalue()


class CPProblemTests(TestCase):
    """
    Each method starting with "test_" will run when you run this script.
    You can copy the "test_problem" method and simply replace the variables with the input and expected output.
    """

    def test_problem(self) -> None:
        """ Enter the input and expected output below and run this file """
        problem_input = """"""
        expected_output = """"""
        actual_output = run_with_mocked_io(problem_input=problem_input, method=cp_problem.problem)
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    main()

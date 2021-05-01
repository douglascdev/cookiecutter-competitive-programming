from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch
import cp_problem


class CPProblemTests(TestCase):
    def io_test(self, problem_input, problem_output, method=cp_problem.problem):
        with patch('builtins.input', return_value=problem_input), patch('sys.stdout', new=StringIO()) as fake_out:
            method()
            self.assertEqual(fake_out.getvalue(), problem_output)

    @staticmethod
    def method():
        _ = input()
        print("1", end="")

    def test_io_test(self):
        problem_input = """1"""
        problem_output = """1"""
        self.io_test(problem_input, problem_output, self.method)

    def test_problem(self):
        problem_input = """"""
        problem_output = """"""
        self.io_test(problem_input, problem_output)


if __name__ == '__main__':
    main()

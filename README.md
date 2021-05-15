# Cookiecutter for Python Competitive Programming
A cookiecutter template for competitive programming with mocked input and output to facilitate testing/TDD. 

The advantage of this approach is that you can easily create methods to test inputs and outputs replacing values that are entered with stdin and stdout by entering the values in a string, and then just paste your solution on the contest directly.

The running time is also printed for each test by default.

## Usage
Install cookiecutter:
```
pip install cookiecutter
```
Create a project using the template:
```
cookiecutter https://github.com/douglascdev/cookiecutter-competitive-programming
```
You'll be asked for the project name, which will be created at the current folder.


After that, you can implement the tests to make sure your code will work on the file ```cp_problem_tests.py```, and your solution at ```cp_problem.py```.

Further explanations are on the files.

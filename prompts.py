from dataclasses import dataclass


@dataclass
class Solution:
    text: str  # the text solution to a problem
    value_name: str  # the name of the value used to measure the solution, e.g. "length" or "score"
    value: int  # the value of the solution, e.g. 5 or 10


class MathPrompt:
    def __init__(
        self,
        problem: str,  # text description of the problem to be solved
        instruction: str,  # instructions on what type of solution to provide and in what format
        solution_description: str,  # a description of the solutions and how they are ordered (e.g., "arranged in descending order based on their lengths, where lower values are better")
        solutions: list[
            Solution
        ] = [],  # a list of solutions to the problem sorted in order of ascending value
    ):
        self.problem = problem
        self.solution_description = solution_description
        self.solutions = solutions
        self.instruction = instruction
        self.prompt_string = ""

    def update_prompt_string(self):
        """
        Creates a string representation of the prompt that can be used to display the prompt to the user or provide it to a language model.
        """
        solutions_string = "\n\n".join(
            f"Text: {solution.text}\n{solution.value_name}: {solution.value}"
            for solution in self.solutions
        )

        self.prompt_string = f"{self.problem}\n\n{self.solution_description}\n\n{solutions_string}\n\n{self.instruction}"

    def add_solution(self, solution: Solution):
        """
        Adds a solution to the list of solutions, sorts the list by value in ascending order, and updates the prompt string.
        """
        self.solutions.append(solution)

        # sort the solutions by value in ascending order
        self.solutions.sort(key=lambda solution: solution.value)

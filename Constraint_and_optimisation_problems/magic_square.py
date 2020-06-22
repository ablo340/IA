from constraint import *

problem = Problem()


# magic square with n order
def magic_square(n):
    if n == 1:
        return 1

    if n == 2:
        return -1

    magic_number = n*(n*n + 1)/2

    # define variables in their domain
    problem.addVariables(range(0, n*n), range(1, n*n + 1))

    # Constraints
    problem.addConstraint(AllDifferentConstraint(), range(0, n*n))

    problem.addConstraint(ExactSumConstraint(magic_number), [i*(n + 1) for i in range(n)])  # diagonal constraint
    problem.addConstraint(ExactSumConstraint(magic_number), [(i * (n-1)) + 2 for i in range(n)])  # diagonal constraint

    for row in range(n):  # rows constraint
        problem.addConstraint(ExactSumConstraint(magic_number),
                              [row * n + i for i in range(n)])

    for col in range(n):  # cols constraint
        problem.addConstraint(ExactSumConstraint(magic_number),
                              [col + n * i for i in range(n)])

    return problem.getSolutions()


if __name__ == "__main__":
    
    # magic square 3x3
    print(magic_square(3))

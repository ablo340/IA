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

    """# define variables in their domain
    problem.addVariables(range(0, 9), range(1, 9+1))
    
    # Constraints
    problem.addConstraint(AllDifferentConstraint(), range(0, 9))
    
    problem.addConstraint(ExactSumConstraint(15), [0, 4, 8])  # diagonal constraint
    problem.addConstraint(ExactSumConstraint(15), [2, 4, 6])  # diagonal constraint
    
    for row in range(3):  # rows constraint
        problem.addConstraint(ExactSumConstraint(15),
                              [row*3+i for i in range(3)])
    
    for col in range(3):  # cols constraint
        problem.addConstraint(ExactSumConstraint(15),
                              [col+3*i for i in range(3)])
    
    # Solutions
    solutions = problem.getSolutions()"""

    solutions = magic_square(3)  # magic square 3x3
    print(solutions)

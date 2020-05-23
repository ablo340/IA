from abc import ABC, abstractmethod


class Variable:
    '''Class representing a named variable with its associated domain.'''

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.value = None

    def is_assigned(self):
        return self.value is not None

    def __eq__(self, other):
        if not isinstance(other, Variable):
            return NotImplemented
        return self.name == other.name

    def __repr__(self):
        return '{} {}'.format(self.name, self.domain)


class Constraint(ABC):
    '''Class representing a constraint on a set of variables.'''

    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def is_satisfied(self):
        pass


class Problem():
    '''Class representing a CSP with a set of variables and a set of constraints.'''

    def __init__(self, name, variables, constraints):
        self.name = name
        self.variables = variables
        self.constraints = constraints

    def is_solved(self):
        return all(v.is_assigned() for v in self.variables) and all(c.is_satisfied() for c in self.constraints)

    def solve(self):
        while not self.is_solved():
            i = 0
            while i < len(self.variables):  # for each variables
                c = 0
                while not self.variables[i].is_assigned():  # while no assigned
                    if c < len(self.variables[i].domain):
                        self.variables[i].value = self.variables[i].domain[c]  # get the values in his domain

                        if not all(c.is_satisfied() for c in self.constraints):  # if constraints violated
                            self.variables[i].value = None  # reset current value
                            c += 1
                    else:
                        i -= 1  # backtracking
                        c = self.variables[i].value + 1  # last value of previous variable + 1
                        self.variables[i].value = None  # change previous value

                i += 1

        return ['{} : {}'.format(v.name, v.value) for v in self.variables]

    def __repr__(self):
        v = '\n'.join(['  * {}'.format(v) for v in self.variables])
        c = '\n'.join(['  * {}'.format(c) for c in self.constraints])
        return '==={}===\n\nVariables:\n\n{}\n\nConstraints:\n\n{}\n'.format(self.name, v, c)
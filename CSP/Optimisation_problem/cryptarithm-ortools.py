from ortools.sat.python import cp_model

model = cp_model.CpModel()

# Variables
w = model.NewIntVar(0, 9, 'W')
o = model.NewIntVar(0, 9, 'O')
u = model.NewIntVar(0, 9, 'U')
r = model.NewIntVar(0, 9, 'R')
t = model.NewIntVar(1, 9, 'T')
f = model.NewIntVar(1, 9, 'F')

# Constraints
letters = [w, o, u, r, t, f]
model.AddAllDifferent(letters)
model.Add(2 * (100 * t + 10 * w + o) == 1000 * f + 100 * o + 10 * u + r)


# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

print()
print('Statistics')
print('  - status          :', solver.StatusName(status))
print('  - conflicts       :', solver.NumConflicts())
print('  - branches        :', solver.NumBranches())
print('  - wall time (s)   :', solver.WallTime())
print('  - solutions found :', ['{} = {}'.format(v, solver.Value(v)) for v in letters])
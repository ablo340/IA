from ortools.sat.python import cp_model

budget = 10000
numb_worker = 1200
area = 110

model = cp_model.CpModel()

# Define variables
corn = model.NewIntVar(0, area + 1, 'X')
barley = model.NewIntVar(0, area+1, 'Y')

# Define constraints
model.Add(100*corn + 200*barley <= budget)
model.Add(10*corn + 30*barley <= numb_worker)
model.Add(corn + barley <= numb_worker)

# objective function
model.Maximize(50*corn + 120*barley)

# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print('Maximum of objective function: %i' % solver.ObjectiveValue())
    print()
    print('length value : ', solver.Value(corn))
    print('width value: ', solver.Value(barley))

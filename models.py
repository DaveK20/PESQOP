from pulp import *

model = None
x = LpVariable("x")
y = LpVariable("y") 

def solve(title:str, sense, objective, restrictions:list):
    global model 
    
    model = LpProblem(title, sense)

    model += objective
    for restriction in restrictions:
        model += restriction

    status=  model.solve() 
    print(value(x))
    print(value(y))
    print(value(model.objective))

def verify_model(model):
    expected_keys = ['title', 'objective', 'sense', 'restrictions']
    keys = model.keys()
    return keys == expected_keys

if __name__ == "__main__":
    solve('geladeiras', LpMaximize, 100*x+50*y, [
        x<=1500,
        y<=6000,
        10*x+8*y<=25000,
        x+y<=4500
    ])
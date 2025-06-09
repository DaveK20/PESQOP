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
    #return model

def verify_model(model):
    keys = model.keys()
    print(keys)


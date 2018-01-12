unprinted_designs= ['iphone case','robot pendant','dodecagedron']
completed_models= []

while unprinted_designs:
    current_design= unprinted_designs.pop()
    print("Prontening model: " + current_design)
    completed_models.append(current_design)
print("The following model have been printed")
for completed_model in completed_models:
    print(completed_models)




def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed(completed_models):
    print("The following models have been printed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs= ['iphone case','robot pendant','dodecagedron']
completed_models= []
print_models(unprinted_designs,completed_models)
show_completed(completed_models)
    
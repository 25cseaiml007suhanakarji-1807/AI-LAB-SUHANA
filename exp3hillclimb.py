#hill climbing is the local search algorithm that repeatedly moves to the neighbouring state with the highest value until no better neighbour exists
#it is a local search algorithm

# Objective function

def objective_function(x):
    return -(x**2)+10

#Hill climbing function
def hill_climbing(start,step_size,max_iterations):
    current= start
    current_value=objective_function(current)

    for i in range(max_iterations):
        left=current-step_size
        right=current+step_size

        left_value=objective_function(left)
        right_value=objective_function(right)

        # Move to the better neighbour
        if(left_value > current_value):
            current=left
            current_value=left_value
        elif right_value > current_value:
            current=right
        else:
            break
    return current,current_value

# Main program
start= float(input("Enter the starting value:"))
step_size=float(input("Enter the step size:"))
max_iterations=int(input("Enter maximum iterations:"))

best_position,best_value=hill_climbing(start,step_size,max_iterations)

print("\nBest Position=",best_position)
print("Maximum Value=", best_value)
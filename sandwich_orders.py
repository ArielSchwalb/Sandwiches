sandwich_orders = ["ruben", "falafel", "blt"]

finished_sandwiches = []

while sandwich_orders:
# Make each sandwich until there are no more unmade sandwiches. 
# Move each sandwich into the list of finished sandwiches. 
    current_sandwich = sandwich_orders.pop()

    print(f"Making sandwich: {current_sandwich.title()}")

    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.

print("\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
# Part 1
# Calculate simple interest by gathering three things (principle, number of years, rate of interest).
# Get user input for p (p = principle).
p = input("What is your principle? ")
# Get user input for n (n = number of years).
n = input("What is your number of years? ")
# Get user input for r (r = rate of interest).
r = input("What is your rate of interest? ")
# Convert user inputs p, n, r to int(). Links to an external site.
p = int(p)
n = int(n)
r = int(r)
# Calculate the simple interest of p, n, r (multiple p, n, r, and then divide by 100).
interest = (p * n * r) / 100
# Print out the simple interest value.
print(interest)


# Part 2
# Create a list of your favorite food items, the list should have a minimum of 5 elements.
fav_food = ["sushi", "steak", "fruit", "cheese", "desserts"]
# List out the 3rd element in the list.
print(fav_food[2])
# Add additional items to the current list and display the list.
fav_food.append("chocolate")
print(fav_food)
# Insert an element named tacos at the 3rd index position of the list and print out the list elements.
fav_food.insert(2, "tacos")
print(fav_food)
# Part 3
# Using a for-loop and a range function, print "I am a programmer" 5 times.
for x in range(5):
    print("I am a programmer")
# Create a function that displays out the square values of numbers from 1 to 9.
for x in range(1, 10):
    print(x**2)
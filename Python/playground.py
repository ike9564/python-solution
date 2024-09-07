"""class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self, bark):
        print("woof!")"""




# Gowon said, "No victor, no vanquished"
# print("Gowon said, 'No victor, no vanquished'")

# Gowon said that No victor, no vanquished.
# print("Gowon said that, no victor, no vanquished.")

# sequence[start:stop:step]

def greet(name):
    return f"Good morning, {name}."

print(greet("David"))


string = "This is David's pen"

football_teams = ['Chelsea', 'Manchester United', 'Arsenal', 'Liverpool']

football_teams.append('New Caslte')
football_teams.insert(1, 'Wolves')

# How to create a list
"""
countries = list('Brazil', 'Canada', 'Denmark', 'Egypt', 'Nigeria')
print(type(countries))
"""


# Second method
cities = ['Ontario', 'Abuja', 'Lagos', 'Cairo']
print(type(cities))


drinks = ['Fanta', 'Sprite', 'Coke', 'Chapman', 'Pepsi', 'Mirinda', 'Water']
print(len(drinks))
print(type(drinks))
print(drinks)

# Accessing Items in the list

print(drinks[0])
print(drinks[-1])

first_drink, second_drink, third_drink, *others = drinks
print(first_drink)
print(second_drink)
print(third_drink)
print(others)

print(drinks[1:7])
print(drinks[1: ])

drinks[0] = 'wine'
print(drinks)

# Finding items in a list

exist = "wine" in drinks
print(exist)

does_not_exist = 'malt' in drinks
print(does_not_exist)

# Add items to list

drinks.append("goldspot")
print(drinks)

drinks.append("chivita")
print(drinks)
print(len(drinks))

# Insert items in a list

drinks.insert(5, 'beer')
print(drinks)

print(drinks.index('Mirinda'))

single_item = "apple",
single_item_1 = ("pear")
multiple_fruits = ('pear', 'apple')
print(len(multiple_fruits))


countries = ["Angola", "Brazil", "Canada", "Denmark", "Ethopia",
              "France", "Guyana", "Hungary", "Israel", "Japan"]

for country in countries:
    print(country)

for country in range(len(countries), ):
    print(country)



print()


def add_two_numbers(num_1, num_2):
    total = num_1 + num_2
    return total

def anything(*names):
    pass

while True:
    pass



# Class work
# 1. Write a function that prints from 100 down to 0
def hundred_to_zero():
    while count < 100:
        print(count)
        count = count - 1
        if count == 1:
            break
print(count)

# 2. Write a function that takes a list as an argument and returns a greeting personalized with each name on the list
def greet_names(names):
    greetings = []
    for name in names:
        greeting = f"Hello, {name}!"
        greetings.append(greeting)
    return greetings


# 3. Write a function that takes 2 parameters: a first name and a last name and returns the full name in title case
def full_name_in_title_case(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

first_name = "Ike"
last_name = "Ikeotuonye"
print(full_name_in_title_case(first_name, last_name))


# 4.write a function thats calculates degrees to farenheit
def degrees_to_fahrenheit(degrees):
    C = int(input("Enter temperature"))
    in_fahrenheit = C * 9/5 + 32
    return in_fahrenheit

print(degrees_to_fahrenheit(45))


"""
The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:

git config --global user.name "John Doe"
git config --global user.email johndoe@example.com


Again, you need to do this only once if you pass the --global option, because then Git will always use that information for anything you do on that system. If you want to override this with a different name or email address for specific projects, you can run the command without the --global option when you’re in that project.

Many of the GUI tools will help you do this when you first run them.

"""

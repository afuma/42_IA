

def recipe_names(dico):
    for key, value in dico.items():
        print(key)

def recipe_details(dico, key):
    print("Recipe for " + key)
    print("\tIngredients list: " + str(dico[key]["ingredients"]))
    print("\tTo be eaten for: " + str(dico[key]["meal"]) + ".")
    print("\tTakes: " + str(dico[key]["prep_time"]) + " minutes of cooking.")

def recipe_delete(dico, key):
    dico.pop(key)

def recipe_add(dico): #mettre des try, except
    print("Enter a name:")
    new_key = int_error(input())
    print("Enter ingredients:")
    new_ingredients = int_error(input())
    print("Enter a meal type:")
    # while (int_error(input()) == 0)
    new_meal = int_error(input())
    print("Enter a preparation time:")
    new_prep_time = int_error(input())
    dico[new_key] = {"ingredients": new_ingredients,
                    "meal": new_meal,
                    "prep_time": new_prep_time
                }

def int_error(var):
    try:
        var = int(input(">> "))
    except ValueError:
        print("Sorry, this option does not exist.")
        return (0)
    return (var)

def main(dico):
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    print()

    option = 0
    while (option != 5):
        print("Select an option:")
        try:
            option = int(input(">> "))
        except ValueError:
            print("AssignementError: entrez un nombre")

        if (option == 1):
            recipe_add(dico)
            print()
        elif(option == 2):
            key = input(">> ")
            recipe_delete(dico, key)
            print()
        elif(option == 3):
            key = input(">> ")
            recipe_details(dico, key)
            print()
        elif(option == 4):
            recipe_names(dico)
        elif(option == 5):
            print("Cookbook closed. Goodbye !")
            break

Sandwich = {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal":"lunch",
            "prep_time":10
        }

Cake = {"ingredients": ["flour", "sugar", "eggs"],
            "meal":"dessert",
            "prep_time":60
        }

Salad = {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
            "meal":"lunch",
            "prep_time":15
        }

cookbook = {"Sandwich": Sandwich, "Cake": Cake, "Salad": Salad}

main(cookbook)
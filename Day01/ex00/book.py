
from datetime import datetime
from recipe import Recipe

class Book:

    def __init__(self, name, recipes_list):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = recipes_list

    def set_last_update(self):
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name):
        for chapter, recipe_chapter_list in self.recipes_list.items():
            if (recipe_chapter_list is not None):
                for recipe in recipe_chapter_list:
                    if (recipe.name == name):
                        return (recipe)

    def get_recipe_by_types(self, recipe_type):
        list_recipes_name = []
        for chapter, recipe_chapter_list in self.recipes_list.items():
            if ((recipe_chapter_list is not None) and (chapter == recipe_type)):
                    for recipe in recipe_chapter_list:
                        list_recipes_name.append(recipe.name)
                    return (list_recipes_name)

    def add_recipe(self, recipe):
        self.set_last_update()
        if (not isinstance(recipe, Recipe)):
            print("Error: object must be a recipe !")
            return
        for chapter, recipe_chapter_list in self.recipes_list.items():
            if (recipe.recipe_type == chapter):
                    recipe_chapter_list.append(recipe)

recipe_1 = Recipe("Salad", 1, 5, ["salad, tomates, oignons"], "lunch", "a good salad")
recipe_2 = Recipe("glace", 3, 10, ["vanille, creme"], "dessert", "delicious glace")
recipes_list = {"starter": [], "lunch": [recipe_1], "dessert": []}

book = Book("Recette gourmande", recipes_list)

'''
    VERIFICATION: get_recipe_by_name
print(book.get_recipe_by_name("Salad"))

# VERIFICATION: add_recipe
print(book.get_recipe_by_types("dessert"))
book.add_recipe("bonjour")
print(book.get_recipe_by_types("dessert"))

    VERIFICATION DE LA DATE:
print("creation_date: " + str(book.CREATION_DATE))
print("last_update: " + str(book.last_update))
n_recipe = book.get_recipe_by_name("Salad")
print("creation_date: " + str(book.CREATION_DATE))
print("last_update: " + str(book.last_update))
'''
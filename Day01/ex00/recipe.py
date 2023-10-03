'''
import sys

def main():
    if (len(sys.argv) > 2):
        print("Assertion error: more than one argument are provided")
    if (len(sys.argv) > 1):
        nbr = 0
        arg = sys.argv[1]
'''

def int_error(var):
    return (isinstance(var, int))

def str_error(var):
    return (isinstance(var, str))

def list_error(var):
    return (isinstance(var, list))

class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
        '''self.name = self.set_name(name)
        self.cooking_lvl = self.set_cooking_lvl(cooking_lvl)
        self.cooking_time = self.set_cooking_time(cooking_time)
        self.ingredients = self.set_ingredients(ingredients)
        self.description = self.set_description(description)
        self.recipe_type = self.set_recipe_type(recipe_type)'''

        self.set_name(name)
        self.set_cooking_lvl(cooking_lvl)
        self.set_cooking_time(cooking_time)
        self.set_ingredients(ingredients)
        self.set_recipe_type(recipe_type)
        self.set_description(description)

    # SETTERS
    def set_name(self, name):
        if (not str_error(name)):
            return ("Error: name must be str !")
        self.name = name

    def set_cooking_lvl(self, cooking_lvl):
        if (not int_error(cooking_lvl)):
            return ("Error: cooking_lvl must be int !")
        
        if (cooking_lvl < 1 or cooking_lvl > 5):
            return ("Error: cooking_lvl must be in the range of 1 to 5 !")
        self.cooking_lvl= cooking_lvl

    def set_cooking_time(self, cooking_time):
        if (not int_error(cooking_time)):
            return ("Error: cooking_time must be int")
        if (cooking_time < 0):
            return ("Error: cooking_time must be a positive number !")
        self.cooking_time = cooking_time

    def set_ingredients(self, ingredients):
        if (not list_error(ingredients)):
            return ("Error: ingredients must be list !")
        for elem in ingredients:
            if (not str_error(elem)):
                return ("Error: elements of ingredients must be str !")
        self.ingredients = ingredients

    def set_description(self, description):
        if (not str_error(description)):
            return ("Error: description must be str !")
        self.description = description

    def set_recipe_type(self, recipe_type):
        if (not str_error(recipe_type)):
            return ("Error: recipe_type must be str !")
        if (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
            return ("Error: recipe_type is not (starter or lunch or dessert) !")
        self.recipe_type = recipe_type

    # GETTERS
    def get_name(self):
        return (self.name)

    def get_cooking_lvl(self):
        return (self.cooking_lvl)

    def get_cooking_time(self):
        return (self.cooking_time)

    def get_ingredients(self):
        return (self.ingredients)

    def get_description(self):
        return (self.description)

    def get_recipe_type(self):
        return (self.recipe_type)

    def __str__(self):
        txt = ""
        txt = "Description a mettre ici"
        return (txt)
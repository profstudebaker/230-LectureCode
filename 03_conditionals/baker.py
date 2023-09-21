# generate recipe function
def generate_recipe(flour, water, salt, yeast, name_of_dough):
    '''
    Takes in weight of ingredients and returns
    a pretty formatted string of the recipe.

    Params
    ------

    Returns
    -------
    '''
    return "" #TODO: return a string with all of the recipe ingredients
    # NOTE: we are not printing
    # we are also not getting user input 

# bake function 
def bake(selection, flour):
    # TODO: based on the value of selection, 
    # return the name and the appropriate amount of each ingredient
    # TODO: return -1 if they passed in invalid selection
    return "Test Name", 12.5, 1.666, 1 

# main program part where you print and get input
if __name__ == "__main__":
    # save getting user input for the end
    # test our functions and make sure they work first
    # when you are testing, you can pass in "dummy values"
    # test with integer inputs
    # test with float inputs to make sure it rounds to int
    print(generate_recipe(10, 4, 5, 6, "Sourdough Loaf"))

    # test bake with dummy values too
    # make sure valid selections work
    # make sure invalid selection gives you -1
    print(bake(1, 100))
    print(bake(7, 100)) # invalid so should return -1

    # assign multiple values from a function
    name, water, salt, yeast = bake(1, 100)
    print(name)

    # after you have tested all your functions and they work
    # get input for flour and selection
    # pass those values into bake function
    # use the output of bake() as inputs to generate_recipe()
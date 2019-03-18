def cakes(recipe, available):
    '''
    Take each ingredient from the recipe, see if it is in the available ones
    and calculate how many full cakes you can make with it.
    Example:
    > recipe = {flour: 500, sugar: 200, eggs: 1}
    > avaliable = {flour: 1200, sugar: 1200, eggs: 5, milk: 200}
    > print(cakes(recipe, available))
    > 2
    '''
    answer = []
    for i in recipe.keys():
        if i in available.keys():
            answer.append(available[i]//recipe[i])
        else:
            answer.append(0)
    return min(answer)
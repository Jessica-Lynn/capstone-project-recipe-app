#pseudocode:

"""To convert recipe to gluten-free"""

"""Taking in recipe ingredients the user enters (via radio buttons);
    app returns a GF equivalent for that ingredient type.

    Includes measurement and prep details for that ingredient.

    This would have to be done for each ingredient that needs to be substituted.
    """

#Logic:
# 1) have a button for user to select-- 'Make this recipe Gluten-Free';
#   now app knows what to check for and convert recipe to

# 2) on the backend:

#GF
#CONDITIONS: add 1/4 tsp. xantham gum per 1 cup GF flour used; decrease liquid by 1/2; double protein (eggs)

GLUTEN_TO_GF = { 
    '1/2 cup regular all purpose flour': ('1:1 gluten-free flour', '1/8 tsp. xantham gum'),
    '1/2 cup regular whole grain flour': ('1:1 gluten-free flour', '1/8 tsp. xantham gum'),
    '1 cup regular all purpose flour': ('1:1 gluten-free flour', '1/4 tsp. xantham gum'),
    '1 cup regular whole grain flour': ('1:1 gluten-free flour', '1/4 tsp. xantham gum'),
}


# 3) User adds ingredients (one at a time- each with ingredient type, measurement, and prep details)

# 4) User hits submit button -- python takes over 

# 5) Pseudocode:
#       define function (should take in ingredients user entered as a list of strings-- measurement is a float)
#
#       have 'UPDATED recipe ingredient list'-- a list of strings to add updated ingredients to
#                                                  -- each ingredient is one string and includes measurement info
#
#       for each ingredient user selected, check if it matches a key in GLUTEN_TO_GF dictionary:
#           if no:
#               OK to add ingredient to UPDATED list
#           if yes:
#               find key's value (ingredient's GF equivalent)
#               make substitution/ add to UPDATED list
#
#                       NOTE: Measurements args passed in as a float
#           for each UPDATED ingredient in 'UPDATED recipe ingredient list':
#               if ingredient is a GF substitute:
#                   check UPDATED ingredient list for liquid measurements
#                        compare it to Global Liquid ingred list
#                        get ingredient type (str) AND measurement (float)
#                        take float-- divide that number by 1/2
#                   add ingredient with updated measurement to 'UPDATED recipe ingredient list'
#               
#           for each UPDATED ingredient in 'UPDATED recipe ingredient list':
#               if ingredient is a GF substitute:
#                   check UPDATED ingredient list for number of eggs/ egg whites/ egg yolks        
#                   take that number - multiply by 2
#                   add ingredient with updated measurement to 'UPDATED recipe ingredient list'
#                    
#
#       return UPDATED ingredient list

#   define a new function to add UPDATED ingredient list to recipe


# 6) Recipe would be updated with ingredient info -- all else (instructions, servings etc.) would be the same     

# 7) Display this new info and all other info to User

# 8) User can save the recipe their Recipe Box associated with their account
#           - when user clicks submit button; it will be added to their user profile page (like in Ratings Lab)


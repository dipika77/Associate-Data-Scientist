# Setting Category variables

#instructions
'''Print the frequency of the responses in the "keep_in" variable and make sure the count of NaN values are shown.Convert the "keep_in" variable to a categorical Series.
Add the list of new categories provided by the adoption agency, new_categories, to the "keep_in" column.
Print the frequency counts of the keep_in column and do not drop NaN values.'''

# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs["keep_in"].cat.add_categories(new_categories)

# Check frequency counts one more time
print(dogs['keep_in'].value_counts(dropna = False))




#instructions
'''Print out the categories of the categorical Series dogs["likes_children"].
Print out the frequency table for "likes_children" to see if any "maybe" responses remain.
Remove the "maybe" category from the Series.
Print out the categories of "likes_children" one more time.
'''

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the `"maybe" category
dogs["likes_children"] = dogs["likes_children"].cat.remove_categories(["maybe"])
print(dogs["likes_children"].value_counts())

# Print the categories one more time
print(dogs['likes_children'].cat.categories)



#Updating categories
#instructions
'''Create a dictionary called my_changes that will update the Maybe? category to Maybe.
Rename the categories in likes_children using the my_changes dictionary.
Update the categories one more time so that all categories are uppercase using the .upper() method.
Print out the categories of the updated likes_children Series.'''

# Create the my_changes dictionary
my_changes = {"Maybe?": "Maybe"}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs["likes_children"].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs['likes_children'].cat.categories)
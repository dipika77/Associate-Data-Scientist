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




#instructions
'''Create a dictionary named update_coats to map both wirehaired and medium-long to medium.
Collapse the categories listed in this new dictionary and save this as a new column, coat_collapsed.
Convert this new column into a categorical Series.
Print the frequency table of this new Series.'''

# Create the update_coats dictionary
update_coats = {
  "wirehaired": "medium",
  "medium-long": "medium"
}


# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs["coat"].replace(update_coats)

# Convert the column to categorical
dogs["coat_collapsed"] = dogs["coat_collapsed"].astype("category")

# Print the frequency table
print(dogs["coat_collapsed"].value_counts())



#Reordering categories
#instructions

'''Print out the current categories of the "size" pandas Series.
Reorder categories in the "size" column using the categories "small", "medium", "large", do not set the ordered parameter.

Update the reorder_categories() method so that pandas knows the variable has a natural order.

Add a argument to the method so that the "size" column is updated without needing to save it to itself.'''

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# Reorder the categories, specifying the Series is ordinal, and overwriting the original series
dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace = True
)


#instructions
'''Print out the frequency table of "sex" for each category of the "size" column.
Print out the frequency table of "keep_in" for each category of the "size" column.'''

# Previous code
dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace=True
)

# How many Male/Female dogs are available of each size?
print(dogs.groupby("size")["sex"].value_counts())

# Do larger dogs need more room to roam?
print(dogs.groupby('size')['keep_in'].value_counts())



#cleansing and accessing data
#instructions
'''Update the misspelled response "Malez" to be "male" by creating the replacement map, replace_map.
Replace all occurrences of "Malez" with "male" by using replace_map.
Remove the leading spaces of the " MALE" and " FEMALE" responses.
Convert all responses to be strictly lowercase.
Convert the "sex" column to a categorical pandas Series.'''

# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs["sex"].str.strip()

# Make all responses lowercase
dogs["sex"] = dogs["sex"].str.lower()

# Convert to a categorical Series
dogs["sex"] = dogs["sex"].astype("category")

print(dogs["sex"].value_counts())




#instructions
'''Print the "coat" value for the dog with an ID of 23807
For dogs with a long "coat", print the number of each "sex".

Print the average age of dogs with a "breed" of "English Cocker Spaniel".

Filter to the dogs with "English" in their "breed" name using the .contains() method.'''


# Print the category of the coat for ID 23807
print(dogs.loc[23807, "coat"])

# Find the count of male and female dogs who have a "long" coat
print(dogs.loc[dogs["coat"] == "long", "sex"].value_counts())

# Print the mean age of dogs with a breed of "English Cocker Spaniel"
print(dogs.loc[dogs['breed'] == 'English Cocker Spaniel','age' ].mean())

# Count the number of dogs that have "English" in their breed name
print(dogs["breed"].str.contains("English", regex=False).shape[0])


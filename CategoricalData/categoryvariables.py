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
# working with categorical data in python

# Introduction to categorical data


#instruction
'''Explore the Above/Below 50k variable by printing out a description of the variable's contents.
Explore the Above/Below 50k variable by printing out a frequency table of the values found in this column.
Rerun .value_counts(), but this time print out the relative frequency values instead of the counts.
'''

# Explore the Above/Below 50k variable
print(adult["Above/Below 50k"].describe())

# Print a frequency table of "Above/Below 50k"
print(adult["Above/Below 50k"].value_counts())

# Print relative frequency values
print(adult["Above/Below 50k"].value_counts(normalize=True))



#categorical data in pandas


#instructions
'''Create a pandas Series, series1, using the list_of_occupations (do not set the dtype).
Print both the data type and number of bytes used of this new Series.
Create a second pandas Series, series2, using the list_of_occupations and set the dtype to "category".

Print both the data type and number of bytes used of this new Series.'''

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(list_of_occupations, dtype="category")

# Print out the data type and number of bytes for series2
print("series2 data type:", series2.dtype)
print("series2 number of bytes:", series2.nbytes)
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
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




#instruction
'''Create a categorical pandas Series without using pd.Series().
Specify the three known medal categories such that "Bronze" < "Silver" < "Gold".
Specify that the order of the categories is important when creating this Series.'''

# Create a categorical Series and specify the categories (let pandas know the order matters!)
medals = pd.Categorical(medals_won, categories=["Bronze", "Silver", "Gold"], ordered=True)
print(medals)



#instruction
'''Call the correct attribute on the adult DataFrame to review the data types.
Create a dictionary with keys: "Workclass", "Education", "Relationship", and "Above/Below 50k".
Set the value for each key to be "category".
Use the newly created dictionary, adult_dtypes, when reading in adult.csv
'''

# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
   "Workclass": "category",
   "Education": "category",
   "Relationship": "category",
   "Above/Below 50k": "category" 
}

# Read in the CSV using the dtypes parameter
adult2 = pd.read_csv(
  "adult.csv",
  dtype = adult_dtypes
  
)
print(adult2.dtypes)


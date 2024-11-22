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




#instructions
'''Split the adult dataset across the "Sex" and "Above/Below 50k" columns, saving this object as gb.
Print out the number of observations found in each group.
Using gb, find the average of each numerical column.'''

# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by=["Sex", "Above/Below 50k"])

# Print out how many rows are in each created group
print(gb.size())

# Print out the mean of each group for all columns
print(gb.mean())




#instructions
'''Create a list of the names for two user-selected variables: "Education" and "Above/Below 50k".
Create a GroupBy object, gb, using the user_list as the grouping variables.
Calculate the mean of "Hours/Week" across each group using the most efficient approach covered in the video.'''


# Create a list of user-selected variables
user_list = ["Education", "Above/Below 50k"] 

# Create a GroupBy object using this list
gb = adult.groupby(by=user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb['Hours/Week'].mean())

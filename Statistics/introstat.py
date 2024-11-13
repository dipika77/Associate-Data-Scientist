# introduction to statistics

# measure of center
#instructions
'''Import numpy with the alias np.
Subset food_consumption to get the rows where the country is 'USA'.
Calculate the mean of food consumption in the usa_consumption DataFrame, which is already created for you.
Calculate the median of food consumption in the usa_consumption DataFrame.'''

# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_consumption['consumption']))


#instructions
'''Import matplotlib.pyplot with the alias plt.
Subset food_consumption to get the rows where food_category is 'rice'.
Create a histogram of co2_emission in rice_consumption DataFrame and show the plot.
Use .agg() to calculate the mean and median of co2_emission for rice.'''

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))


# measures of spread
#instructions
'''Calculate the variance and standard deviation of co2_emission for each food_category with the .groupby() and .agg() methods; compare the values of variance and standard deviation.
Create a histogram of co2_emission for the beef in food_category and show the plot.
Create a histogram of co2_emission for the eggs in food_category and show the plot.'''

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.std, np.var]))

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category']=='beef']['co2_emission'].hist()
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
plt.show()


#instructions
'''Calculate the quartiles of the co2_emission column of food_consumption.
Calculate the six quantiles that split up the data into 5 pieces (quintiles) of the co2_emission column of food_consumption.
Calculate the eleven quantiles of co2_emission that split up the data into ten pieces (deciles).'''

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0,0.25, 0.5, 0.75, 1]))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0,0.2,0.4,0.6,0.8,1]))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]))


#instructions
'''Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission. Store the resulting DataFrame as emissions_by_country.
Compute the first and third quartiles of emissions_by_country and store these as q1 and q3.
Calculate the interquartile range of emissions_by_country and store it as iqr.
Calculate the lower and upper cutoffs for outliers of emissions_by_country, and store these as lower and upper.
Subset emissions_by_country to get countries with a total emission greater than the upper cutoff or a total emission less than the lower cutoff.'''

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)


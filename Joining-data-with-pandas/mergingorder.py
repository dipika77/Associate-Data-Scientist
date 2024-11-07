# using merge_ordered()

#instructions
'''Use merge_ordered() to merge gdp and sp500 using a left join where the year column from gdp is matched with the date column from sp500.
Print gdp_sp500.

Use the merge_ordered() function again, similar to before, to merge gdp and sp500, using the function's ability to fill in missing data for returns by forward-filling the missing values. Assign the resulting table to the variable gdp_sp500.
Subset the gdp_sp500 table, select the gdp and returns columns, and save as gdp_returns.
Print the correlation matrix of the gdp_returns table using the .corr() method.
'''

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on= 'year', right_on= 'date', 
                             how= 'left')

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())



#instructions
'''Use merge_ordered() to merge the inflation and unemployment tables on date with an inner join, and save the results as inflation_unemploy.
Print the inflation_unemploy dataframe.
Using inflation_unemploy, create a scatter plot with unemployment_rate on the horizontal axis and cpi (inflation) on the vertical axis.'''

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation,unemployment, on = 'date', how = 'inner')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x = 'unemployment_rate',y =  'cpi', kind = 'scatter')
plt.show()


#instructions
'''Use merge_ordered() on gdp and pop, merging on columns date and country with the fill feature, save to ctry_date.
Perform the same merge of gdp and pop, but join on country and date (reverse of step 1) with the fill feature, saving this as date_ctry.'''

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop,on = ['date', 'country'], 
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on = ['country', 'date'], fill_method = 'ffill')

# Print date_ctry
print(date_ctry)



#using merge_asof()

#instructions
'''Use merge_asof() to merge jpm (left table) and wells together on the date_time column, where the rows with the nearest times are matched, and with suffixes=('', '_wells'). Save to jpm_wells.
Use merge_asof() to merge jpm_wells (left table) and bac together on the date_time column, where the rows with the closest times are matched, and with suffixes=('_jpm', '_bac'). Save to jpm_wells_bac.
Plot the close prices of close_jpm, close_wells, and close_bac from price_diffs.'''

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on = 'date_time', suffixes = ('', '_wells'), direction = 'nearest')


# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on = 'date_time', suffixes = ('_jpm', '_bac'), direction = 'nearest')


# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()


#instructions
'''Using merge_asof(), merge gdp and recession on date, with gdp as the left table. Save to the variable gdp_recession.
Create a list using a list comprehension and a conditional expression, named is_recession, where for each row if the gdp_recession['econ_status'] value is equal to 'recession' then enter 'r' else 'g'.
Using gdp_recession, plot a bar chart of gdp versus date, setting the color argument equal to is_recession.'''

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on = 'date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind= 'bar', y= 'gdp', x='date', color= is_recession, rot=90)
plt.show()


#instructions
'''Use merge_ordered() on gdp and pop on columns country and date with the fill feature, save to gdp_pop and print.Add a column named gdp_per_capita to gdp_pop that divides gdp by pop.
Pivot gdp_pop so values='gdp_per_capita', index='date', and columns='country', save as gdp_pivot.
Use .query() to select rows from gdp_pivot where date is greater than equal to "1991-01-01". Save as recent_gdp_pop.'''

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()


# reshaping data with .melt()
#instructions
'''Use .melt() to unpivot all of the columns of ur_wide except year and ensure that the columns with the months and values are named month and unempl_rate, respectively. Save the result as ur_tall.
Add a column to ur_tall named date which combines the year and month columns as year-month format into a larger string, and converts it to a date data type.
Sort ur_tall by date and save as ur_sorted.
Using ur_sorted, plot unempl_rate on the y-axis and date on the x-axis.'''

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')


# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x = 'date', y = 'unempl_rate')
plt.show()



#instructions
'''Use .melt() on ten_yr to unpivot everything except the metric column, setting var_name='date' and value_name='close'. Save the result to bond_perc.
Using the .query() method, select only those rows where metric equals 'close', and save to bond_perc_close.
Use merge_ordered() to merge dji (left table) and bond_perc_close on date with an inner join, and set suffixes equal to ('_dow', '_bond'). Save the result to dow_bond.
Using dow_bond, plot only the Dow and bond values.'''

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', suffixes=('_dow', '_bond'), how='inner')

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()
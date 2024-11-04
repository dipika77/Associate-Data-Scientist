# Advance merging

#Filtering joins

#instructions
'''Merge employees and top_cust with a left join, setting indicator argument to True. Save the result to empl_cust.
Select the srid column of empl_cust and the rows where _merge is 'left_only'. Save the result to srid_list.
Subset the employees table and select those rows where the srid is in the variable srid_list and print the results.'''

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])



#instructions
'''Merge non_mus_tcks and top_invoices on tid using an inner join. Save the result as tracks_invoices.
Use .isin() to subset the rows of non_mus_tcks where tid is in the tid column of tracks_invoices. Save the result as top_tracks.
Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.
Merge cnt_by_gid with the genres table on gid and print the result.'''

# Merge the non_mus_tcks and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on = 'tid', how = 'inner')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid': 'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on ='gid'))



# concatenate data frames vertically
#instructions
'''Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.
Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.
Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.'''

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                            ignore_index = True,
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join = 'inner',
                               sort=True)
print(tracks_from_albums)



#instructions
'''Concatenate the three tables together vertically in order with the oldest month first, adding '7Jul', '8Aug', and '9Sep' as keys for their respective months, and save to inv_jul_thr_sep.
Use the .agg() method to find the average of the total column from the grouped invoices.
Create a bar chart of avg_inv_by_month.'''

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind = 'bar')
plt.show()


# verifying integrating
#instructions
'''Concatenate the classic_18 and classic_19 tables vertically where the index goes from 0 to n-1, and save to classic_18_19.
Concatenate the pop_18 and pop_19 tables vertically where the index goes from 0 to n-1, and save to pop_18_19.

With classic_18_19 on the left, merge it with pop_18_19 on tid using an inner join.
Use .isin() to filter classic_18_19 where tid is in classic_pop.'''

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on ='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)


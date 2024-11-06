#left joins

#instructions
'''Merge the movies table, as the left table, with the financials table using a left join, and save the result to movies_financials.
Count the number of rows in movies_financials with a null value in the budget column.'''

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)


#instructions
'''Merge toy_story and taglines on the id column with a left join, and save the result as toystory_tag.
With toy_story as the left table, merge to it taglines on the id column with an inner join, and save as toystory_tag.'''

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines , on = 'id', how = 'left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)


# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on = 'id')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)


# other joins
#instructions
'''Merge action_movies and scifi_movies tables with a right join on movie_id. Save the result as action_scifi.
Update the merge to add suffixes, where '_act' and '_sci' are suffixes for the left and right tables, respectively.
From action_scifi, subset only the rows where the genre_act column is null.
Merge movies and scifi_only using the id column in the left table and the movie_id column in the right table with an inner join.'''

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how = 'inner', left_on = 'id', right_on ='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)


#instructions
'''Merge movie_to_genres and pop_movies using a right join. Save the results as genres_movies.
Group genres_movies by genre and count the number of id values.'''

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, left_on = 'movie_id', right_on = 'id', how='right')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()


#instructions
'''Save to iron_1_and_2 the merge of iron_1_actors (left) with iron_2_actors tables with an outer join on the id column, and set suffixes to ('_1','_2').
Create an index that returns True if name_1 or name_2 are null, and False otherwise.'''

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     how = 'outer',
                                     on = 'id',
                                     suffixes= ('_1','_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())



#Merging table to itself

#instructions
'''To a variable called crews_self_merged, merge the crews table to itself on the id column using an inner join, setting the suffixes to '_dir' and '_crew' for the left and right tables respectively.
Create a Boolean index, named boolean_filter, that selects rows from the left table with the job of 'Director' and avoids rows with the job of 'Director' in the right table.
Use the .head() method to print the first few rows of direct_crews.'''

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())


#Merging on indexes

#instructions
'''Merge the movies and ratings tables on the id column, keeping all rows from the movies table, and save the result as movies_ratings.'''

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on= 'id')

# Print the first few rows of movies_ratings
print(movies_ratings.head())


#instructions
'''With the sequels table on the left, merge to it the financials table on index named id, ensuring that all the rows from the sequels are returned and some rows from the other table may not be returned, Save the results to sequels_fin.
Merge the sequels_fin table to itself with an inner join, where the left and right tables merge on sequel and id respectively with suffixes equal to ('_org','_seq'), saving to orig_seq.
Select the title_org, title_seq, and diff columns of orig_seq and save this as titles_diff.
Sort by titles_diff by diff in descending order and print the first few rows.'''

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending = False).head())
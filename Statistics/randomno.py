# random numbers and probability

#instructions
'''Count the number of deals Amir worked on for each product type using .value_counts() and store in counts.
Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on. Save this as probs.'''

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs =  counts / amir_deals.shape[0]
print(probs)


#instructions
'''Set the random seed to 24.
Take a sample of 5 deals without replacement and store them as sample_without_replacement.
Take a sample of 5 deals with replacement and save as sample_with_replacement
'''

# Set random seed
seed = np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace = True)
print(sample_with_replacement)



#instructions
'''Create a histogram of the group_size column of restaurant_groups, setting bins to [2, 3, 4, 5, 6]. Remember to show the plot.

Count the number of each group_size in restaurant_groups, then divide by the number of rows in restaurant_groups to calculate the probability of randomly selecting a group of each size. Save as size_dist.
Reset the index of size_dist.
Rename the columns of size_dist to group_size and prob.

Calculate the expected value of the size_dist, which represents the expected group size, by multiplying the group_size by the prob and taking the sum.

Calculate the probability of randomly picking a group of 4 or more people by subsetting for groups of size 4 or more and summing the probabilities of selecting those groups.'''

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins = [2,3,4,5,6])
plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)


#instructions
'''To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.
Import uniform from scipy.stats and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called prob_less_than_5.
Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.
Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.'''

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 min
prob_greater_than_5 = 1- uniform.cdf(5, min_time, max_time)
print(prob_greater_than_5)

# Calculate probability of waiting less than 10 mins
prob_between_10_and_20 = uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)



#instructions
'''Set the random seed to 334.
Import uniform from scipy.stats.
Generate 1000 wait times from the continuous uniform distribution that models Amir's wait time. Save this as wait_times.
Create a histogram of the simulated wait times and show the plot.'''

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()



#The binomial distribution

#instructions
'''Import binom from scipy.stats and set the random seed to 10.
Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on.
Simulate a typical week of Amir's deals, or one week of 3 deals.
Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals.
Print the mean number of deals he won per week.'''

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1,0.3, size=1))

# Simulate 1 week of 3 deals
print(binom.rvs(3,0.3, size=1))

# Simulate 52 weeks of 3 deals

deals = binom.rvs(3,0.3, size=52)

# Print mean deals won per week
print(deals.mean())


#instructions
'''What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.
What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.
What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.'''

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3,3, 0.3)

print(prob_3)

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1,3,0.3)

print(prob_less_than_or_equal_1)

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1,3,0.3)

print(prob_greater_than_1)


#instructions
'''Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.
Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.
Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%.'''

# Expected number won with 30% win rate
won_30pct = 3 * 0.30
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)
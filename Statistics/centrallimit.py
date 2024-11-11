# The central limit theorem

#the normal distributions

#instructions
'''Create a histogram with 10 bins to visualize the distribution of the amount. Show the plot.'''

# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins = 10)
plt.show()


#instructions
'''What's the probability of Amir closing a deal worth less than $7500?

What's the probability of Amir closing a deal worth more than $1000?

What's the probability of Amir closing a deal worth between $3000 and $7000?

What amount will 25% of Amir's sales be less than?'''

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000,2000)

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)


#instructions
'''Currently, Amir's average sale amount is $5000. Calculate what his new average amount will be if it increases by 20% and store this in new_mean.
Amir's current standard deviation is $2000. Calculate what his new standard deviation will be if it increases by 30% and store this in new_sd.
Create a variable called new_sales, which contains 36 simulated amounts from a normal distribution with a mean of new_mean and a standard deviation of new_sd.
Plot the distribution of the new_sales amounts using a histogram and show the plot.'''

# Calculate new average amount
new_mean = 5000 * 1.2

# Calculate new standard deviation
new_sd = 2000 * 1.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()


#instructions
'''Create a histogram of the num_users column of amir_deals and show the plot.
Set the seed to 104.
Take a sample of size 20 with replacement from the num_users column of amir_deals, and take the mean.
Repeat this 100 times using a for loop and store as sample_means. This will take 100 different samples and calculate the mean of each.
Convert sample_means into a pd.Series, create a histogram of the sample_means, and show the plot.
'''

# Create a histogram of num_users and show
amir_deals['num_users'].hist()
plt.show()

# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals
samp_20 = amir_deals['num_users'].sample(20, replace = True)

# Take mean of samp_20
print(samp_20.mean())

# Set seed to 104
np.random.seed(104)

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()


#instructions
'''Set the random seed to 321.
Take 30 samples (with replacement) of size 20 from all_deals['num_users'] and take the mean of each sample. Store the sample means in sample_means.
Print the mean of sample_means.
Print the mean of the num_users column of amir_deals.'''

# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20, replace = True)
  # Take mean of cur_sample
  cur_mean = cur_sample.mean()
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(amir_deals['num_users'].mean())


#the poisson distribution

#instructions
'''Import poisson from scipy.stats and calculate the probability that Amir responds to 5 leads in a day, given that he responds to an average of 4.

Amir's coworker responds to an average of 5.5 leads per day. What is the probability that she answers 5 leads in a day?

What's the probability that Amir responds to 2 or fewer leads in a day?

What's the probability that Amir responds to more than 10 leads in a day?'''

# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_5 = poisson.pmf(5,4)

print(prob_5)

# Probability of 5 responses
prob_coworker = poisson.pmf(5, 5.5)

print(prob_coworker)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2,4)

print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10,4)

print(prob_over_10)


#More probability distribution

#instructions
'''Import expon from scipy.stats. What's the probability it takes Amir less than an hour to respond to a lead?

What's the probability it takes Amir more than 4 hours to respond to a lead?

What's the probability it takes Amir 3-4 hours to respond to a lead?'''



# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
probability =  1 - (expon.cdf(4, scale = 2.5))
print(probability)

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))
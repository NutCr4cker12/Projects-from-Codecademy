import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# Calculate the number of people who answered 'Ceballos' and save the answer to the  variable total_ceballos.
# Print the variable to the terminal to see its value.

total = sum([1 for n in survey_responses if n == 'Ceballos'])
print total
# >> 33

# Calculate the percentage of people in the survey who voted for Ceballos and save it to the variable percentage_ceballos.
# Print the variable to the terminal to see its value.

lenght = float(len(survey_responses))
perc = total / (lenght)
print perc
# >> 0.4714

# In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. Your supervisors are concerned because this is a very different outcome than what the poll predicted. They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.
#
# Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town's population as its parameters. Then divide the distribution by the number of survey responses. Save your calculation to the variable possible_surveys.

possible_surveys = np.random.binomial(lenght, 0.54, 10000) / lenght

# Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.

plt.hist(possible_surveys, range = (0,1),bins = 20)
plt.show()

# As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos in the actual election.
#
# Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote and save it to the variable ceballos_loss_surveys.
#
# Print the variable to the terminal.

possible = float(len(possible_surveys))
incorrect  =len(possible_surveys[possible_surveys < 0.5])
ceballos = incorrect /possible
print ceballos
# >> 0.2097

# Your co-worker points out that your poll would be more accurate if it had more responders.
#
# Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people. Divide the distribution by the size of the survey and save your findings to large_survey.

large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, 0.54, size=10000) / large_survey_length 

# Now, recalculate the percentage of surveys that would have an outcome of Ceballos losing and save it to the variable ceballos_loss_new, and print the value to the terminal.

incorrect_pred = len(large_survey[large_survey < 0.5])
ceballos_loss_new = incorrect_pred / large_survey_length 
print ceballos_loss_new 
# >> 0.0

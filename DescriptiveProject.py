'''
This script is to be used to complete the tasks using the saved sample data.
'''

# Import needed libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st


# Simulating the deck of cards
value = list(range(1, 10) + [10] * 4) * 4
suits = list(['Spade', 'Diamond', 'Heart', 'Club']) * 13
labels = list(['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']) * 4

deck = pd.DataFrame([value, suits, labels]).transpose()
deck.columns = ['Card Value', 'Suit', 'Label']

# Print some of the cards
print '\n--------------Card Deck--------------'
print deck.head()



# Task 1.
# First, create a histogram depicting the relative frequencies of the card values.

ax = deck['Card Value'].hist(bins = 10, normed = True, edgecolor = 'black', alpha = 0.5)
ax.set(ylabel="Relative Frequency", xlabel="Card Value", title="Histogram of card values in the deck")

plt.show()


# Task 2.
# Load the samples

samples = pd.read_csv('Samples.csv')

print '\n---------------------------------Samples------------------------------------'
print samples.head()


# Task 3.
# Report descriptive statistics of the samples

print '\n\n-----------------------------\nMeasures of central tendency\n-----------------------------'
print 'Mean\t |\t{0}\nMedian\t |\t{1}\nMode\t |\t{2}'.format(round(samples.CardSum.mean(), 2),
                                                            samples.CardSum.median(),
                                                            samples.CardSum.mode()[0])

print '\n---------------------------------------\nMeasures of variability\n---------------------------------------'
print 'Variance\t\t |\t{0}\nStandard Deviation\t |\t{1}\nIQR\t\t\t |\t{2}'.format(round(samples.CardSum.var(), 2),
                                                            round(samples.CardSum.std(), 2),
                                                            samples.CardSum.quantile(0.75) - samples.CardSum.quantile(0.25))



# Task 4.
# Histogram of card sums

ax1 = samples.CardSum.hist(normed = True, edgecolor = 'black', alpha = 0.5, bins = 8)

ax1.set(ylabel="Relative Frequency",
        xlabel="Card sums",
        title="Histogram of sampled card sums")

plt.show()


# Task 5.
# Estimates from the samples


zscore = st.norm.ppf(.05)
print '\nz-score for probability 0.05 = {0}'.format(zscore)

margin_of_error = zscore * samples.CardSum.std()

print '90% of the sum of drawn cards will fall approzimately between {0} and {1}'.format(
    samples.CardSum.mean() + margin_of_error,
    samples.CardSum.mean() - margin_of_error)

zscore = (20 - samples.CardSum.mean()) / samples.CardSum.std()

print 'z-score for the value 20 = {0}'.format(zscore)

prob = 1 - st.norm.cdf(zscore)

print 'Probability of drawing a sample with the card value sum at least 20 is {0}'.format(prob)

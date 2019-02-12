import familiar
from scipy.stats import ttest_1samp as tt
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

# Perfect, now the first thing we want to show is that our most basic package, the Vein Pack, actually has a significant impact on the subscribers. It would be a marketing goldmine if we can show that subscribers to the Vein Pack live longer than other people.

# Lifespans of Vein Pack users are returned by the function lifespans(package='vein'), which is part of the familiar module. Call that function and save the data into a variable called vein_pack_lifespans.

vein_pack_lifespans = familiar.lifespans(package='vein')

# Now use the 1-Sample T-Test to compare vein_pack_lifespans to the average life expectancy 71. Save the result into a variable called vein_pack_test.

tstat,pval = tt(vein_pack_lifespans, 71)

# Let's check if the results are significant! Check the pvalue of vein_pack_test. If it's less than 0.05, we've got significance!

print format(pval, '0.10f')
# >> 0.0000000003

# We want to present this information to the CEO, Vlad, of this incredible finding. Let's print some information out! If the test's p-value is less than 0.05, print "The Vein Pack Is Proven To Make You Live Longer!". Otherwise print "The Vein Pack Is Probably Good For You Somehow!"

if pval < 0.05:
  print "The Vein Pack Is Proven To Make You Live Longer!"
else:
  print "The Vein Pack Is Probably Good For You Somehow!"
# >> The Vein Pack Is Proven To Make You Live Longer!
  
# In order to differentiate Familiar's different product lines, we'd like to compare this lifespan data between our different packages. Our next step up from the Vein Pack is the Artery Pack. Let's get the lifespans of Artery Pack subscribers using the same method, called with package='artery' instead. Save the value into a variable called artery_pack_lifespans.

artery_pack_lifespans = familiar.lifespans(package='vein')

# Now we want to show that the subscribers to the Artery Pack experience a significant improvement even beyond what a Vein Pack subscriber's benefits. Import the 2-Sample T-Test and we'll use that to see if there is a significant difference between the two subscriptions.

# Okay let's run the 2-Sample test! Save the results into a variable named package_comparison_results.

package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

# Let's see the results! If the p-value from our experiment is less than 0.05, the results are significant and we should print out "the Artery Package guarantees even stronger results!". Otherwise we should print out "the Artery Package is also a great product!"

if package_comparison_results.pvalue < 0.05:
  print "the Artery Package guarantees even stronger results!"
else:
  print "the Artery Package is also a great product!"
# >> the Artery Package is also a great product!

# Well, shame that it's not significantly better, but maybe there's a way to demonstrate the benefits of the Artery Package yet.

# If your lifespan isn't significantly increased by signing up for the Artery Package, maybe we can make some other claim about the benefits of the package. To that end, we've sent out a survey collecting the iron counts for our subscribers, and filtered that data into "low", "normal", and "high".

# We received 200 responses from our Vein Package subscribers. 70% of them had low iron counts, 20% had normal, and 10% of them have high iron counts.

# We were only able to get 145 responses from our Artery Package subscribers, but only 20% of them had low iron counts. 60% had normal, and 20% have high iron counts.

iron_contingency_table = familiar.iron_counts_for_package()
print iron_contingency_table
# >> [[140, 29], [40, 87], [20, 29]]

# We want to be able to tell if what seems like a higher number of our Artery Package subscribers is a significant difference from what was reported by Vein Package subscribers. Import the Chi-Squared test so that we can find out.

# Run the Chi-Squared test on the iron_contingency_table and save the p-value in a variable called iron_pvalue. Remember that this test returns four things: the test statistic, the p-value, the number of degrees of freedom, and the expected frequencies.

_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

# Here's the big moment: if the iron_pvalue is less than 0.05, print out "The Artery Package Is Proven To Make You Healthier!" otherwise we'll have to use our other marketing copy: "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"

if iron_pvalue < 0.05:
  print "The Artery Package Is Proven To Make You Healthier!"
else:
  print "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"
# >> The Artery Package Is Proven To Make You Healthier!

import numpy as np
import fetchmaker as ft
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

rottweilerTail = ft.get_tail_length("rottweiler")


whippetResc = ft.get_is_rescue("whippet")
whippetSaveCount = np.count_nonzero(whippetResc)
whippetTotCount = np.size(whippetResc)


binom_pval = binom_test(whippetSaveCount, n=whippetTotCount, p=0.08)
print binom_pval

whippet = ft.get_weight("whippet")
terrier = ft.get_weight("terrier")
pitbull = ft.get_weight("pitbull")

fstat, pval = f_oneway(whippet,terrier,pitbull)

v = np.concatenate([whippet,terrier,pitbull])
labels = ['whippet']*len(whippet) + ['terrier']*len(terrier) + ['pitbull']*len(pitbull)

print pairwise_tukeyhsd(v,labels, 0.05)

poodleCol = ft.get_color("poodle")
shiCol = ft.get_color("shihtzu")

aa = [[np.count_nonzero(poodleCol == "black"),
    np.count_nonzero(shiCol == "black")],[np.count_nonzero(poodleCol == "brown"),
    np.count_nonzero(shiCol == "brown")],[np.count_nonzero(poodleCol == "gold"),
    np.count_nonzero(shiCol == "gold")],[np.count_nonzero(poodleCol == "grey"),
    np.count_nonzero(shiCol == "grey")],[np.count_nonzero(poodleCol == "white"),
    np.count_nonzero(shiCol == "white")]]

print aa

chi2, pval, dof, expected = chi2_contingency(aa)
print pval

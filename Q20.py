import numpy as np
from scipy import stats

design_A = np.array([0.12, 0.14, 0.11, 0.13, 0.15, 0.12])
design_B = np.array([0.18, 0.19, 0.17, 0.20, 0.16, 0.19])

t_stat, p_value = stats.ttest_ind(design_A, design_B)

print("T-statistic:", t_stat)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis — significant difference exists.")
else:
    print("Fail to reject the null hypothesis — no significant difference.")

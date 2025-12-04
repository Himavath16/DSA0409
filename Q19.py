import numpy as np 
import scipy.stats as stats 
drug = np.array([12,15,14,13,16,18,10,11,17,14]) 
placebo = np.array([5,7,6,4,5,6,7,8,5,6]) 
drug_mean = np.mean(drug) 
placebo_mean = np.mean(placebo) 
drug_ci = stats.t.interval(0.95, len(drug)-1, loc=drug_mean, scale=stats.sem(drug)) 
placebo_ci = stats.t.interval(0.95, len(placebo)-1, loc=placebo_mean, 
scale=stats.sem(placebo)) 
print("95% CI for Drug Group:", drug_ci) 
print("95% CI for Placebo Group:", placebo_ci)
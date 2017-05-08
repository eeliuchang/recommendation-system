import math
import numpy as np
from scipy.stats.stats import pearsonr

# Calculate the euclidean distance between two people 
def distance(pref, person1, person2, distance_metric):
	""" This function is to calculate all the distance metrics 
	based on the same items users have rated
	"""
	distance = 0
	rating1 = []
	rating2 = []
	for item in pref[person1]:
		if (item in pref[person2]):
			rating1.append(pref[person1][item])
			rating2.append(pref[person2][item])
	
	return distance_metric(rating1, rating2)

def euclidean_distance(v1, v2):
	return math.sqrt(sum([(v1[i]-v2[i])**2 for i in range(len(v1))]))

def manhattan_distance(v1, v2):
	return sum([abs(v1[i] - v2[i]) for i in range(len(v1))])

def pearson_correlation(v1, v2):
	v1_mean = np.mean(v1)
	v2_mean = np.mean(v2)
	v1_std = math.sqrt(sum([(v1[i] - v1_mean) ** 2 for i in range(len(v1))])/len(v1))
	v2_std = math.sqrt(sum([(v2[i] - v2_mean) ** 2 for i in range(len(v2))])/len(v2))
	cov = sum([(v1[i] - v1_mean) * (v2[i] - v2_mean) for i in range(len(v1))])/len(v1)
	if (v1_std != 0 and v2_std != 0):
		return cov/(v1_std * v2_std)
	else:
		return 0
	#return pearsonr(v1,v2)[0]


def cosine_correlation(v1, v2):
	v1_std = math.sqrt(sum([(v1[i]) ** 2 for i in range(len(v1))])*1.0/len(v1))
	v2_std = math.sqrt(sum([(v2[i]) ** 2 for i in range(len(v2))])*1.0/len(v2))
	cov = sum([(v1[i]) * (v2[i]) for i in range(len(v1))])*1.0/len(v1)
	return cov*1.0/v1_std/v2_std 



pref = {1:{'python':1, 'java':2, 'c':3}, 2: {'python':3, 'scala':2, 'java':1}, 3: {'python':2, 'c++': 1, 'java': 2}}
sol1 = distance(pref, 1,3, pearson_correlation)
print(sol1)
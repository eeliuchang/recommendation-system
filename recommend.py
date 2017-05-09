#!/usr/bin/evn python
from distance import distance, pearson_correlation, cosine_correlation

def recommend(pref, person, distance_metric):
	""" 
	This function takes the preferences of users and recommend items for person.
	"""
	weighted_totals = {}
	weights = {}
	threshold = 0.1
	for p in pref:
		if (p != person):
			sim = distance(pref, person, p, distance_metric)
			for item in pref[p]:
				if (item not in pref[person] and sim > threshold):
					if (item not in weighted_totals):
						weighted_totals.setdefault(item, 0)
						weights.setdefault(item, 0)

					weighted_totals[item] +=  sim * pref[p][item]  
					weights[item] += sim

	result_list = [(weighted_totals[i]/weights[i], i) for i in weights]
	sorted_list = sorted(result_list)
	reverse_list = list(reversed(sorted_list))

	return reverse_list

#pref = {1:{'python':1, 'java':2, 'c':3}, 2: {'python':3, 'scala':2, 'java':1}, 3: {'python':2, 'c++': 1, 'java': 3}}
#sol =  recommend(pref, 1, cosine_correlation)
#print(sol)

				

#!/usr/bin/evn python
from distance import distance, pearson_correlation, cosine_correlation

def nearestNeighbours(pref, person, distance_metric):
	"""
	This function finds the users who have the most similar tastes as the given person.
	The returned list is from the most similar to least.
	"""
	distance_list = []
	for other in pref.keys():
		if (person == other): 
			continue
		else:
			distance_list.append((distance(pref, person, other, distance_metric), other))
	sorted_list = sorted(distance_list)
	reverse_sorted_list = list(reversed(sorted_list))
	return reverse_sorted_list


pref = {1:{'python':1, 'java':2, 'c':3}, 2: {'python':3, 'scala':2, 'java':1}, 3: {'python':2, 'c++': 1, 'java': 3}}
sol =  nearestNeighbours(pref, 1, cosine_correlation)
print(sol)
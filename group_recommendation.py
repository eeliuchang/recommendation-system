from input_file import input_data, item_name_map, match_item
from recommend import recommend
from distance import cosine_correlation, pearson_correlation
from recommender_system import recommender_system

def group_recommendation(people, weights, path_to_data, path_to_item, distance_metric):
	group_recommendation = {}
	for person in people:
		person_recommendations = recommender_system(path_to_data, path_to_item, person, distance_metric)
		for score, item in person_recommendations:
			if (item not in group_recommendation):
				group_recommendation.setdefault(item, 0)
				
			group_recommendation[item] = weights[person] * score

	result = [(group_recommendation[item], item) for item in group_recommendation]
	sorted_result = sorted(result)
	return list(reversed(sorted_result))

path_to_data = "./ml-100k/u.data"
path_to_item = "./ml-100k/u.item"
result = group_recommendation(['934', '196'], {'934': 0.8, '196': 0.2}, path_to_data, path_to_item, cosine_correlation)
for elem in result[:100]:
	print(elem)
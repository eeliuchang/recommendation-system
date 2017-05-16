from input_file import input_data, item_name_map, match_item
from recommend import recommend
from distance import cosine_correlation, pearson_correlation

def recommender_system(path_to_data, path_to_item, person, distance_metric):
	""" 
	This is the main file to combine all the other functions in order to recommend 
	products to a user.
	"""
	data = input_data(path_to_data)
	item_name = item_name_map(path_to_item)
	recommend_items = recommend(data, person, distance_metric)
	result = match_item(recommend_items, item_name)
	return result



path_to_data = "./ml-100k/u.data"
path_to_item = "./ml-100k/u.item"
result = recommender_system(path_to_data, path_to_item, '196', cosine_correlation)
#for elem in result[:10]:
#	print(elem)




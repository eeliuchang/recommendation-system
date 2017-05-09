#!usr/bin/evn python

def input_data(path):
	pref = {}
	with open(path, 'rb') as file:
		for line in file.readlines():
			line_stripped = line.strip().split('\t')
			user_id = line_stripped[0]
			item_id = line_stripped[1]
			rating = line_stripped[2]
			if (user_id not in pref):
				pref[user_id] = {}
			
			pref[user_id][item_id] = int(rating)
	return pref

def item_name_map(path):
	result_map = {}
	with open(path, 'rb') as file:
		for line in file.readlines():
			line_stripped = line.strip().split('|')
			item_id = line_stripped[0]
			name = line_stripped[1]
			result_map[item_id] = name

	return result_map

def match_item(item_ranks, item_name):
		item_name_ranks = []
		for (score,item) in item_ranks:
			item_name_ranks.append((score, item_name[item]))

		return item_name_ranks



#path_to_data = "./ml-100k/u.data"
#result = input_data(path_to_data)
#path_to_item = "./ml-100k/u.item"
#result_map = item_name_map(path_to_item)
#print result_map['934']



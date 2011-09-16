food = [
	{'name':'carrot', 'food_group':'vegetable', 'tasty':True, 'color':'orange'},
	{'name':'eggplant', 'food_group':'vegetable', 'tasty':False, 'color':'purple'},
	{'name':'kale', 'food_group':'vegetable', 'tasty':True, 'color':'green'},
	{'name':'wheatgrass', 'food_group':'vegetable', 'tasty':False, 'color':'green'},
	{'name':'kohlrabi', 'food_group':'vegetable', 'tasty':True, 'color':'green'},
	{'name':'orange', 'food_group':'fruit', 'tasty':True, 'color':'orange'},
	{'name':'grapes', 'food_group':'fruit', 'tasty':False, 'color':'purple'},
	{'name':'kiwi', 'food_group':'fruit', 'tasty':True, 'color':'green'},
	{'name':'pistachio ice cream', 'food_group':'dairy', 'tasty':True, 'color':'green'}
]

def filter_1(list_of_dicts, **kwargs):
	filtered_list = []
	for item in list_of_dicts:
		add_to_list = True
		for k, v in kwargs.items():
			if item[k] != v:
				add_to_list = False
				break
		if add_to_list:
			filtered_list.append(item)
	return filtered_list

def filter_2(list_of_dicts, **kwargs):
	"""iteratively filter list of dicts for each kwarg"""
	for k, v in kwargs.items():
		list_of_dicts = [f for f in list_of_dicts if f[k] == v]
	return list_of_dicts

def filter_3(list_of_dicts, **kwargs):
	"""[k for k,v in kwargs.iteritems() if list_of_dicts[0][k] == v] 
    to build a list where all keys match, while outer comprehension is
	to iterate across all dicts
	"""
	return [d for d in list_of_dicts if len([k for k,v in kwargs.iteritems() if d[k] == v]) == len(kwargs)]

#bonus... try a lambda?
	
		
		

	

print filter_1(food, color='green', food_group='vegetable')
print filter_2(food, color='green', food_group='vegetable')
print filter_3(food, color='green', food_group='vegetable')

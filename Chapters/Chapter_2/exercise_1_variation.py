import requests
import ast

url = "https://raw.githubusercontent.com/pythondatabook/sources/main/ch2/list_of_dicts.txt"
response = requests.get(url).text.strip()
data = ast.literal_eval(response)

def intersection(list1:list, list2:list) -> list:
    return [value for value in list1 if value in list2]

photo_groups = {}

for i in range(0, len(data)-1):
    for j in range(i+1, len(data)):
        intersect = intersection(data[i]['tags'], data[j]['tags'])
        for key in intersect:
            photo_groups.setdefault(key, []).extend([data[i]['name'], data[j]['name']])
            photo_groups[key] = list(sorted(set(photo_groups[key]), key=photo_groups[key].index)) # SORTING BY THE ORIGINAL ORDER BEFORE TRANSFORMING TO SET

print(photo_groups)
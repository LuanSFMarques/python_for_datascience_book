import requests
import ast

url = "https://raw.githubusercontent.com/pythondatabook/sources/main/ch2/list_of_dicts.txt"
response = requests.get(url).text.strip()
data = ast.literal_eval(response)

def intersection(list1:list, list2:list) -> str:
    return "_".join([value for value in list1 if value in list2])

photo_groups = {}

for i in range(0, len(data)-1):
    for j in range(i+1, len(data)):
        intersect = intersection(data[i]['tags'], data[j]['tags'])
        if intersect:
            photo_groups.setdefault(intersect, [data[i]['name'], data[j]['name']])

print(photo_groups)
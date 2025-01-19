dict1 = {"name": "cj", "age": 18, "city": "karachi"}
dict2 = {"name": "abdullah", "city": "karachi"}


mk = ["name", "age", "city", "country"]

missing_dict0 = [key for key in dict1 if key not in dict2]
missing_dict1 = [key for key in mk if key not in dict1]
missing_dict2 = [key for key in mk if key not in dict2]


print("Missing keys in dict0:",missing_dict0)
print("Missing keys in dict1:", missing_dict1)
print("Missing keys in dict2:",missing_dict2)

dict4=(dict1.items() | dict2.items())
print(dict4)



    
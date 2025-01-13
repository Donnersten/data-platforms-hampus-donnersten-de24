# Fråga 0
# source_path = input("ange source path: ")
# destination = input("ang destination: ")

# print(f"source: {source_path}")
# print(f"destination: {destination}")
# -------------------------------------------------------
# Fråga 1
#  a) 
# print(f"{'key':<20}Value")
# data = {
#     "id" : 101,
#     "name" : "Erika",
#     "is_active" : True,
#     "age" : 45
# }

# for x, y in data.items():
#     print(f"{x:<20}{y:<20}")

# # b)

# if type(data["id"]) == int and type(data["name"]) == str and type(data["is_active"]) == bool and type(data["age"]) == int:
#     print(True)
# else:
#     print(False)

# # c) 
# data_2 = [{"id" : 102,
#     "name" : "Marcus",
#     "is_active" : True,
#     "age" : 34},
#     {"id" : 103,
#     "name" : "David",
#     "is_active" : False,
#     "age" : 29},
#     {"id" : 104,
#     "name" : "Anna",
#     "is_active" : True,
#     "age" : 41.5},
#     {"id" : 106,
#     "name" : "Ingrid",
#     "is_active" : "NOPE",
#     "age" : 8}]


# print(data_2)

# # d / e)
# def test_if_dict_ok(list):
#     for i in list:
#         if type(i["id"]) == int and type(i["name"]) == str and type(i["is_active"]) == bool and type(i["age"]) == int:
#             print(True)
#         else:
#             print(False)

# test_if_dict_ok(data_2)

#-------------------------------------------------------
# Fråga 2 
list_1 = ["hej", "då", "jag", "None", "kan", "vet", "oj", "sen", "el", "wow"]
list_2 = ["hej", "då", "jag", "cool", "kan", "vet", "oj", "sen", "el", "wow"]
def check_ten_elements(list):
    if len(list) != 10 or None in list:
        raise ValueError("To few or to many elements supposed to be 10 or includes None")
    else:
        print("OK")

check_ten_elements(list_2)

#--------------------------------------------------------
# Fråga 3
# 
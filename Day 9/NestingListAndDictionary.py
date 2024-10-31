# capitals = {
#     "France": "Paris",
#     "Geramny": "Berlin",
# }

# #Nested List in Dictionary


# travel_log = {
#     "France": ["Paris", "Lille","Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

#Print Lille

# print(travel_log["France"][1])

# nestted_list = ["A", "B",["C","D"]]

# print(nestted_list[2] [1])

travel_log = {
    "France": {
        "Citties_Visited": ["Paris", "Lille","Dijon"],
        "Total_Visits": 12
        },
    "Germany":{
        "Citties_Visited": ["Stuttgart", "Berlin"],
        "Total_Visits": 5
    }
}

print(travel_log["France"]["Citties_Visited"][2])
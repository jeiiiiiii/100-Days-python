programming_Dictionary = {
    "Bug": "Lorem Ipsum",
    "Functions": "Lorem Ipsum1",
    "Loop":"Lorem ipsum2",
}


print(programming_Dictionary["Bug"])

programming_Dictionary["Code"] = "Lorem Ipsum3"

print(programming_Dictionary)

empty_dictionary = {}

#Delete existing dictionary

# programming_Dictionary = {}

# print(programming_Dictionary)

#Edit Dictionary

# programming_Dictionary["Bug"] = "Moth"
# print(programming_Dictionary)


#Loop dictionary

for key in programming_Dictionary:
    print(key)
    print(programming_Dictionary[key])




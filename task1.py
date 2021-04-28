shopping_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for key in shopping_dict:
    values = [value.capitalize() for value in shopping_dict[key]]
    print("Idę do ", key.capitalize(),", kupuję tu następujące  rzeczy :", values)
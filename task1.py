shopping_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for key in shopping_dict:
    values = [value.capitalize() for value in shopping_dict[key]]
    print("Idę do ", key.capitalize(),", kupuję tu następujące  rzeczy :", values)

count = 0
# using isinstance
for x in shopping_dict:
   if isinstance(shopping_dict[x], list):
      count += len(shopping_dict[x])
print("W sumie kupuję ",count," produktów w ", len(shopping_dict), "sklepach.")
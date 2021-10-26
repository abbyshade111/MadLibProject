"""This program is a Mad Lib. It will prompt you to input strings to complete the story"""
print("Mad Libs has started!")
name = input("Please provide your name: ")
adjective_1 = input("Please provide an adjective: ")
adjective_2 = input("Please provide another adjective: ")
adjective_3 = input("Please provide a third adjectie: ")
verb_1 = input("Please provide a verb: ")
verb_2 = input("Please provide another verb: ")
verb_3 = input("Please provide one more verb: ")
noun_1 = input("Please provide a noun: ")
noun_2 = input("Please provide a second noun: ")
noun_3 = input("Please provide a third noun: ")
noun_4 = input("Please provide one last noun: ")
animal = input("Please provide an animal: ")
food = input("Please provide a food item: ")
fruit = input("Please provide a fruit: ")
number = input("Please provide a number: ")
superhero = input("Please provide a superhero name: ")
country = input("Please provide the name of a country: ")
dessert = input("Please provide a dessert: ")
year = input("Please provide a year: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %s ruled the world."

print (STORY % (adjective_1, name, verb_1, adjective_2, noun_1, noun_2, animal, food, verb_2, noun_3, fruit, adjective_3, name, verb_3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun_4))

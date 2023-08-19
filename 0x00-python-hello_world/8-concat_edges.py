#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find(",", str.find(",")+1)+2:str.find(",", str.find(",")+1)+38]
print(str)

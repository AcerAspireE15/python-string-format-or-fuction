numbers = [4, 5, 6]
string = "numbers:{0},{1},{2}".format(numbers[0], numbers[1], numbers[2])
print(string)

number = [6, 5, 2018]
string = "Date:{0}/{1}/{2}".format(number[0], number[1], number[2])
print(string)

a = "{x}/{y}".format(x=100, y=200)
print(a)

print(":".join(["apple", "banana", "mango"]))

print("hello there".replace("there","world"))

newstring = "hello there"
print(newstring.replace("there", "world"))

newstring = "this ia a string"
print(newstring.startswith("this"))

newstring = "this ia a string"
print(newstring.startswith("there"))

newstring = "this ia a string"
print(newstring.endswith("string"))

newstring = "this ia a string"
print(newstring.endswith("this"))

newstring = "this ia a string"
print(newstring.upper())

newstring = "This ia a String"
print(newstring.lower())
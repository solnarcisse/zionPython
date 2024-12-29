#Slicing Method
my_string = "Zatanna is the strongest lady magician!"
reversed_string = my_string[::-1]

print(my_string)
print(reversed_string) 


#Looping Method
my_string2 = "The John Birch Society (JBS) is an American right-wing political advocacy group.Founded in 1958."
reversed_string2 = ""

print("Starting point: " + reversed_string2)

for char in my_string2:
    print("adding ..." + char)
    reversed_string2 = char + reversed_string2 
    print(reversed_string2)

print("The final result is: " + reversed_string2)
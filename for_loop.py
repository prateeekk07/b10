#multiplication table

input_number = int(input("enter a number"))

for i in range(1,11):
    multi = i * input_number
    print(f"{input_number} * {i} = {multi}")

#Capital letter   
name_list = ["prateek","ROhIT","palak"]

for i in name_list: 
    print(i.capitalize(), end=" ")

name_list = ["a","b","c","d","e","f","t"]

for i in range(0,len(name_list)): 
    print(name_list[i])


   

# for testing purpose
print("hello world")
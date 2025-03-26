#create a Dictonary of student Marks
my_dict = {
    "John": 85,
    "Alice": 90,
    "Bob": 75,
    "Charlie": 80,
    "David": 95,
    "Eve": 88,
    "Alexander": 92,
    "Frank": 82,


    

 }
student_name=input("Enter the students name:")
if student_name in my_dict:
     print( student_name,"'s Marks :", my_dict[student_name])
else:
     print("student not found.")


#Demostrate list slicing



#create a list of number from 1 to 10
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", list)
#Extract the first five elements from the list
print("Extracted first five elements:", list[:5])
print(list[:5])

#Reverse these extracted elements

print("Reversed first five elements:", list[:5][::-1])
print(list[:5][::-1])

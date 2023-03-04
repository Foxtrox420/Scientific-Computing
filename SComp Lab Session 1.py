print("Hello Word")

a = 5 #In python, we don't need to specify the data type like int or char
      #loosely type variable, meaning that it will auto assign 
b = "Hello" #This will auto assign b to the string Hello 
print(f"Variable a = {a} and Variable b = {b}") #The ones in {} will assign the values we set before
print("Variable a =", a, "and Variable b =", b) #This works the same as before 
print("Variable a = %d and Variable b = %s"%(a,b))#Method similar to C 

#inputing methods
value = input("Please input something: ") #This is basically the scanf
#value int(input("Please input something: ")) #using the specifier int will tell the program to keep the data type to int, if we dont specify it will end up becoming string. 
print(value) #This is basically the printf 

# Operators
# + - * / $ < > 
# ^ (This is not how you use power because this symbol is XOR)
# ** (This is the correct way of using power in python)
# // (Flooring division) The difference with normal / is that it removes the decimal point. e.x 5//2 = 2

print(8+4)
print(7-3)
print(3*3)
print(5/2)
print(10%3)
print(3<5) #True
print(6>10)#False
print(5**3)
print(5//2)

#Selection
name = input("Insert your name here: ")
if name == "Kennard":
    print("Access granted")
    age = int(input("Insert your age here"))
    if age > 10:
      print(age)
elif name == "John Cena":
    print("Access denied")
else: 
    print("Access denied")


#Repetition 
for i in range(10): #loop from 0 - 9
  print(i) #this is the same like in C where it prints all of the values from 0-9 

for i in range(1,10,2):
  print(i) #this prints all values from 1-10 with a gap 2 so 1,3,5,7,9

#Print reverse
for i in range(10, 1, -1):  #This prints all from 10 - 0 
  print(i)

number = 10
while number > 0: 
  print("Number is :", number)
  number -= 1 #this prints numbers from 10 to 1 

#Function 
#def -> define 
def sum(a,b): 
  return a+b 

print(sum(3,9)) #Prints the variables after undergoing the function 
 #To call it back, what you do is sum(variable1, variable2) the variables can be taken from inputs or pre determined

def printName(Name):
  print("My name is:", name)

printName("Kennard")

#If we don't put in parameters, it will execute the function like normally
def testFunction():
  print("This is the test function")

testFunction()

#Data Structure 
#THis consists of list, set, dictionary and tuple

list_1 = [1,3,5,7] # list ([])
                   # size can change or in other words dynamic. 
print(list_1) 
list_1.append(8) #This line adds 8 to the already existing list 
print(list_1)
list_1.insert(0,10) #insert in index 0 with number 10
print(list_1)
list_1.pop() #Like pop tail, removes the last variable
print(list_1)
list_1.remove(5)#Removes 5 from the list
print(list_1)
list_1.sort()#Sorting ascending 
print(list_1)

#Ordered = Have an index
#Unordered = Doesn't have an index

#Mutable = values can be changed
#Non Mutable = values can't be changed and have a fixed value 

#Set = uses {}, can't put in duplicate values
#Dictionary = uses {}, the form is associative array 
# Associative array = array that doesn't use na index, instead a key to value relationship

#Example : JSON
#Stores 3 values -> Jevon, Susan, Andrew
dict_1 = {"key_1" : "Jevon",
          "key_2" : "Susan",
          "key_3" : "Andrew"}
print(dict_1["key_1"]) #Output is Jevon


#Set can't have a duplicate value
set_1 = {"Budi", "Andi", 3, 5, "Juan", "Andi"}
print(set_1)

#Tuple = not mutable(cant change the value in a tuple)
tuple_1 = (1, 7, 10, "Roger", "Angga", 20)
print(tuple_1)

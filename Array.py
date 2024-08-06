#Define Array
numbers =[15,25,45,19,29,73,28,41]

#Accessing Elements
print("4th Element:",numbers[4])
print("Last Element:",numbers[7])

#Modifying Elements
print("Before Modified Element",numbers[1])
numbers[1]=49
print("Modified Element",numbers[1])

#Get Length of Array
print(len(numbers))

#Adding an Element
numbers.append(62)
numbers.append(250)

#Removing an Element
numbers.remove(45)
numbers.remove(28)

#Itarating through an Array
for shanth in numbers:
    print(shanth)

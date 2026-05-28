numbers = input("Enter numbers separated by space: ").split()
newNumber = [ ]
for i in numbers:
	  newNumber.append(int(i))
	  
avg = sum(newNumber)/len(newNumber)

print (avg)	  
	  
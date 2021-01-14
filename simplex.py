#Get user to define variables

print("How many decision variables do you have?")
numVar = int(input())

targetType = "null"
while (targetType != "min" and targetType != "max"):
    print("Is this is a min(imization) or max(imization) problem?")
    targetType = input()

decVar = ["A"] * numVar

#Set up Target Function
print("Target Function Setup:")

for i in range(numVar):
    while (isinstance(decVar[i], int) == False):
        print("Enter coefficient for variable", (i+1))
        decVar[i] = int(input())

print (decVar)



#Get User to Define Variables

print("How many decision variables do you have?")
numVar = input()

targetType = "null"
while (targetType != ("min" or "max")):
    print("Is this is a min(imization) or max(imization) problem?")
    targetType = input()

decVar = []
print("There are " + numVar + " variables")

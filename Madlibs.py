

print("Add three nouns")
nouns = [input(),input(),input()]
print("Add two adjectives")
adjective = [input(),input()]
print("Add a verb")
verbs =[input()]




def show():
    print("Agent" + adjective[0] + nouns[0]+"you are currently on a top secret mission")
    print("where you will be using the identity of a "+ adjective[1]+ " zoologist.")
    print("You work specifically with the " + nouns[1])
    print(" in the " + nouns[2]+ " where you will teach them how to "+verbs[0])

show()

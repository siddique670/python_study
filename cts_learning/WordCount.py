import operator
# Count it Dude!

# Read in file

file = open("speech.txt", "r")
text = file.read()
print(text)

# Count the words
words = {}
for word in text.split():
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1
sortedwords = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
print(sortedwords)
#print(words)
# Write the counted words into a new file

# file = open("speech.txt", "w")
# file.write("Hello Amir")
# file.close()

file = open("speech.txt", "w")
file.write("Total Words - {}\nUnique Words - {}\n\n".format(len(text.split()), len(sortedwords)))
for wordinfo in sortedwords:
    file.write("{} - {}\n".format(wordinfo[0], wordinfo[1]))
file.close()

######  For file creating, Reading and Writing  #########

# file = open("funny.txt", "w")  # for only create a file.

# file.write("Hello my name is nick.\nThis is my new file!")  # for write someting in file.
# file.write("Hello")
# file = open("funny.txt", "r")  # for read the content from txt file
# print(file.read())
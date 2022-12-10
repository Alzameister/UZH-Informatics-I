from collections import defaultdict


# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    
    index_dictionary = {}
    words = []

    #Go through lists of strings and add keys and values to dictionary
    for index, string in enumerate(dataset):
        string = string.lower()
        words = string.split()
        print(words)

        for word in words:
            if word not in index_dictionary:
                index_dictionary[word] = []
            index_dictionary[word].append(index)

    return index_dictionary
# You can see the output of your function here
print(reverse_index(dataset))

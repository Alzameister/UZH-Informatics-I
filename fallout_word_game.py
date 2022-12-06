import random

LENGTH = 5
NUM_WORDS = 8
ATTEMPTS = 4

#Get words.txt list online
with open("words.txt") as f:
    word_list = f.read().splitlines()

#List Comprehension with transformation (word.upper()) and filter (if...)
fixed_length_words = [word.upper() 
                        for word in word_list 
                        if len(word) == LENGTH]

random.shuffle(fixed_length_words)
words = fixed_length_words[0:NUM_WORDS]
password = random.choice(words)

print(words)
print(password)

attempts = ATTEMPTS
while attempts > 0:
    guess = input()
    if guess == password:
        print("ACCESS GRANTED!")
        break
    else:
        print("ACCESS DENIED!")
        attempts -= 1
import random

LENGTH = 5
NUM_WORDS = 8
ATTEMPTS = 4

class GameLogic:
    def __init__(self, num_words, length, attempts):
        self.num_words = num_words
        self.length = length
        self.attempts = attempts

        with open("words.txt") as f:
            word_list = f.read().splitlines()

        #List Comprehension with transformation (word.upper()) and filter (if...)
        fixed_length_words = [word.upper() 
                                for word in word_list 
                                if len(word) == LENGTH]

        random.shuffle(fixed_length_words)
        self.words = fixed_length_words[0:NUM_WORDS]
        self.password = random.choice(self.words)

        
    def check(self, guess):
        attempts = ATTEMPTS
        while attempts > 0:
            guess = input("> ")
            if len(guess) != self.length:
                return ["WRONG LENGTH"]
                #Go to the start of while loop
                continue
            if guess == self.password:
                return ["ACCESS GRANTED!"]
            feedback = []
            feedback.append("ACCESS DENIED!")
            matching = sum([1 for p,q in zip(self.password,guess) 
                            if p == q])
            feedback.append(f"{matching}/{LENGTH} matching")
            self.attempts -= 1
            return False, feedback



class GameRunner:
    def __init__(self, logic) -> None:
        self.logic = logic

    def run(self):
        print(self.logic.password)
        print("".join(self.logic.words))
        while self.logic.attempts > 0:
            guess = input("> ")
            access, feedback = self.logic.check(guess)
            print(feedback)
            if access: break

logic = GameLogic(8, 5, 4)
runner = GameRunner(logic)
runner.run()
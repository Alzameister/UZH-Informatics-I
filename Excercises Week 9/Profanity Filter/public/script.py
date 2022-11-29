#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = sorted(keywords, key=len)
        self.__template = template

    #Censor word
    def __clean(self, msg):
        print(msg.lower())
        msg = msg.lower()
        for keyword in self.__keywords:
            if keyword in msg:
                censor_template = list(self.__template)

                if len(censor_template) < len(keyword):
                    #Extend profanity_template to the length of the to censor word
                    while len(censor_template) < len(keyword):
                        censor_template.extend(list(self.__template))
                        if len(censor_template) - len(keyword) == 2:
                            censor_template = censor_template[:-2]
                        elif len(censor_template) - len(keyword) == 1:
                            censor_template = censor_template[:-1]
                elif len(censor_template) > len(keyword):
                    while len(censor_template) > len(keyword):
                        censor_template.pop()
                

                
                censor_template = "".join(censor_template)

                msg = msg.replace(keyword, censor_template)

                print(msg)

        return msg

    def filter(self, msg):
        words = msg.split(" ")
        msg = ""
        for idx, word in enumerate(words):
            words[idx] = self.__clean(word)
            if idx < len(words)-1:
                msg = msg + words[idx] + " "
            else:
                msg = msg + words[idx]
        
        return msg

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["du", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc du fishotter MaStArD jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno

# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    def match(self,words):
            sorted_word=sorted(self.word)
            matches=[]

            for candidate in words:
                if candidate.lower() ==self.word:
                    continue
                if sorted(candidate.lower())==sorted_word:
                    matches.append(candidate)
            return matches


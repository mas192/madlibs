# simple madlibs

def madlibs():
    adj = input("Please input an adjective: ")
    verb1 = input("Please input a past tense verb: ")
    verb2 = input("Please input a verb: ")
    famousPerson = input("Please input a famous person name: ")
    yourName = input("Please input your name: ")
    crazyVerb = input("Please input a crazy verb: ")
    crazyNoun = input("Please input a crazy noun: ")
    funnyAdj1, funnyAdj2, funnyAdj3 = input("Please input three funny adjectives: ").split(sep=",")

    madlib = f"There are {adj} differences between {famousPerson} and the rest of the species on earth, but one that has been expressed is that {famousPerson} alone is able to imagine the future. For a long time, {yourName} and perhaps {famousPerson} have {verb1} that future. But it’s now becoming apparent that it’s not all doom and gloom. There’s a chance for {famousPerson} to make {crazyVerb}, to complete our journey of development, manage our impact, and once again become a {crazyNoun} in balance with nature. All we need is the will to do so. We now have the opportunity to create the perfect home for {famousPerson}, and restore the {funnyAdj1}, {funnyAdj2}, and {funnyAdj3} world that {yourName} inherited. Just imagine that."
    print(madlib)
if __name__ == '__main__':
    madlibs()
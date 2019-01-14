import sys, os, re
from enum import Enum

class Type(Enum):
    KEYWORD = 1
    AND = 2
    OR = 3
    NOT = 4

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenPtr = 0

    def error(self):
        print("Error at token: "+self.tokens[self.tokenPtr]["token"])
        os._exit()

    def eat(self, keyType):
        if keyType == self.tokens[self.tokenPtr]["type"]:
            self.tokenPtr += 1
        else:
            self.error()
    
    def parseBasicExpression(self):
        if self.tokens[self.tokenPtr]["type"] == Type.NOT:
            self.eat(Type.NOT)
        self.eat(Type.KEYWORD)


def lexer(query):
    query = query.lower()
    query = re.sub("[^A-Za-z0-9_]", " ", query)
    query = re.sub(" +", " ", query)
    tokens = query.split(" ")
    tokensList = []
    for i in range(len(tokens)):
        if tokens[i] == "and":
            tokensList.append({"token": tokens[i], "type": Type.AND})
        elif tokens[i] == "not":
            tokensList.append({"token": tokens[i], "type": Type.NOT})
        elif tokens[i] == "or":
            tokensList.append({"token": tokens[i], "type": Type.OR})
        else:
            tokensList.append({"token": tokens[i], "type": Type.KEYWORD})
    
    return tokensList

query = input()
print(lexer(query))



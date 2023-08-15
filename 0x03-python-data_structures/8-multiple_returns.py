#!/usr/bin/python3

def multiple_returns(sentence):

    """
    Gives the string length.
    """

    if sentence == "":

        return (0, None)

    return (len(sentence), sentence[0])

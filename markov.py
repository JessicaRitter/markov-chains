"""Generate Markov text from text files."""

from random import choice
# import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(input_path)
    text_string = opened_file.read()

    return text_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """


    chains = {}

    word_list = text_string.split()
    #print word_list

    for i in range(len(word_list) - 2):
        bigram = (word_list[i], word_list[i +1])
        if bigram in chains:
            chains[bigram].append(word_list[i + 2])
        else:
            chains[bigram] = [word_list[i + 2]]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    starter_bigram = choice(chains.keys())
    word1, word2 = starter_bigram[:]
    words.append(word1)
    words.append(word2)


    while starter_bigram in chains.keys():
        random_word = choice(chains[starter_bigram])
        starter_bigram = (starter_bigram[1], random_word)
        words.append(random_word)
    return " ".join(words)



# input_path = "green-eggs.txt"
input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

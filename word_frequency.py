#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    text = ""
    while not is_sentence(text):
        text = input("Enter a sentence: ").strip()
    return text

def word_frequency(text): 
    words = text.lower().split()
    
    unique_words = []
    word_frequency = []
    
    for word in words:
        word = word.strip('.,!?')

        if word in unique_words:
            word_frequency[unique_words.index(word)] += 1
        else: 
            unique_words.append(word)
            word_frequency.append(1)
    return unique_words, word_frequency

def printing(words, frequencies):
    for word in words:
        print(f"{word}   amount appeared: {frequencies[words.index(word)]}")

if __name__ == "__main__":
    text = get_sentence()
    words, frequencies = word_frequency(text)
    printing(words, frequencies)
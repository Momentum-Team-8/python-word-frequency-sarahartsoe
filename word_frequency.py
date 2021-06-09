# from os import read

import string
from typing import Text


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# start by opening the file, read the file

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as one_today:
        text = one_today.readlines()
    d = dict()
    for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            elif word in STOP_WORDS:
                pass
            else:
                d[word] = 1
    for word in list(d.keys()):
        print(word, "|", d[word])
    
    
# ignore stop words
# count frequency of each word


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


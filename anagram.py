import os
import itertools
import md5


def load_words(lengths,
               dictionary=os.path.join(os.path.dirname(__file__), 'wordlist')):
    """
    Load the words dictionary

    Keyword arguments:
    lengths -- the lengths of the input words
    dictionary -- the path to the dictionary
    """
    with open(dictionary, 'r') as f:
        return set(
            [word.rstrip() for word in f if len(word.rstrip()) in lengths])


def check_words(words, md5_hash):
    """
    Load the words dictionary

    Keyword arguments:
    words -- the anagram words as an array
    md5_hash -- the md5 hash of the solved anagram
    """
    word_source = load_words([len(word) for word in words])
    found = []
    letters = []
    for word in words:
        for letter in word:
            if letter not in letters:
                letters.append(letter)
    for word in word_source:
        for index, letter in enumerate(word):
            if letter in letters:
                if index + 1 == len(word):
                    found.append(word)
            else:
                break
    permutations = list(itertools.permutations(found, len(words)))
    for permutation in permutations:
        generated_hash = md5.new()
        generated_hash.update(' '.join(permutation))
        if generated_hash.hexdigest() == md5_hash:
            return ' '.join(permutation)


if __name__ == '__main__':
    print(check_words(["poultry", "outwits", "ants"], "4624d200580677270a54ccff86b9610e"))

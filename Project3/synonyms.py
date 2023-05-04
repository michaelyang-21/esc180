'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0.00
    for word in vec1:
        if word in vec2:
            numerator += vec1[word]*vec2[word]

    denominator = norm(vec1) * norm(vec2)

    fraction = numerator / denominator

    return fraction



def build_semantic_descriptors(sentences):
    semantic = {}

    for sentence in sentences:
        subsentence = list(set(sentence))
        for word in subsentence:
            word = word.lower()
            if word in semantic.keys():
                for another in subsentence:
                    another = another.lower()
                    if another != word:
                        if another in semantic[word]:
                            semantic[word][another] += 1
                        else:
                            semantic[word][another] = 1
            else:
                dictionary = {}
                for another in subsentence:
                    another = another.lower()
                    if another != word:
                        if another in dictionary:
                            dictionary[another] += 1
                        else:
                            dictionary[another] = 1
                semantic[word] = dictionary

    return semantic



def build_semantic_descriptors_from_files(filenames):
    textfile = ""

    for file in filenames:
        textfile += open(file, "r", encoding="latin1").read()
        textfile.casefold()
        textfile += " "

    textfile = textfile.replace("!", ".")
    textfile = textfile.replace("?", ".")
    textfile = textfile.replace("\n", " ")
    textfile = textfile.replace("--", " ")
    textfile = textfile.replace(":", " ")
    textfile = textfile.replace(";", " ")
    textfile = textfile.replace(",", " ")
    textfile = textfile.replace("-", " ")

    textfile = textfile.split(".")

    text = []

    for i in range(len(textfile)):
        text.append(textfile[i].split(" "))

    for i in range(len(text)):
        for j in range(len(text[i])):
            if "" in text[i]:
                text[i].remove("")

    return build_semantic_descriptors(text)



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    max = -99999999

    if word.lower() not in semantic_descriptors:
        return choices[0]

    for choice in choices:
        choice = choice.lower()

    word = word.lower()

    out = choices[0]
    for choice in choices:
        if choice not in semantic_descriptors:
            similarity = -1
            if similarity > max:
                max = similarity
                out = choice
        else:
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
            if similarity > max:
                max = similarity
                out = choice

    return out


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    num = 0.00

    f = open(filename, "r", encoding="latin1").read()
    f = f.casefold()
    f = f.split("\n")

    qanda = []
    for question in f:
        qanda.append(question.split(" "))

    for question in qanda:
        if most_similar_word(question[0], question[2:], semantic_descriptors, similarity_fn) == question[1]:
            num += 1

    percent = num/len(qanda) * 100
    return percent


# out = build_semantic_descriptors([["I", "like", "cheese"], ["I", "like", "food"]])
#
# print(out)
#
#semantic = build_semantic_descriptors_from_files(["sentence1.txt", "sentence2.txt"])
# most_similar_word("cat", ["feline", "rocket"], semantic, cosine_similarity)

# print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
# ["i", "am", "a", "spiteful", "man"],
# ["i", "am", "an", "unattractive", "man"],
# ["i", "believe", "my", "liver", "is", "diseased"],
# ["however", "i", "know", "nothing", "at", "all", "about", "my",
# "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))
#print(run_similarity_test("answers.txt", semantic, cosine_similarity))

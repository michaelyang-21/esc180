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
    numerator = 0.0
    for word in vec1:
        if word in vec2:
            numerator += vec1[word]*vec2[word]

    denominator = norm(vec1) * norm(vec2)

    return numerator / denominator



def build_semantic_descriptors(sentences):
    semantic = {}

    for sentence in sentences:
        L = list(set(sentence))
        for word in L:
            word = word.lower()
            if word in semantic:
                for another in L:
                    if another != word:
                        if another in semantic[word]:
                            semantic[word][another] += 1
                        else:
                            semantic[word][another] = 1
            else:
                dictionary = {}
                for another in L:
                    if another != word:
                        if another in dictionary:
                            dictionary[another] += 1
                        else:
                            dictionary[another] = 1
                        semantic[word] = dictionary

    return semantic



def build_semantic_descriptors_from_files(filenames):
    textfile = ""

    for i in range(len(filenames)):
        textfile += open(filenames[i], "r", encoding="latin1").read()
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

    for i in range(len(textfile)-1):
        text.append(textfile[i].split(" "))

    for i in text:
        for j in i:
            while '' in i:
                i.remove('')

    dict = build_semantic_descriptors(text)
    return dict



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    out = choices[0]
    max = -10000000
    word = word.lower()
    for i in range(len(choices)):
        choices[i] = choices[i].lower()


    if word not in semantic_descriptors:
        print("hi")
        return choices[0]

    for i in range(len(choices)):
        if choices[i] not in semantic_descriptors:
            similarity = -1
        else:
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[i]])

        if i == 0:
            max = similarity

        if similarity > max:
            max = similarity
            out = choices[i]

    return out


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0.00

    f = open(filename, "r", encoding="latin1").read()
    f = f.casefold()
    f = f.split("\n")

    qanda = []
    for question in f:
        qanda.append(question.split(" "))
    for question in qanda:
        if most_similar_word(question[0], question[2:], semantic_descriptors, similarity_fn) == question[1]:
            correct += 1


    return (correct/len(qanda) ) * 100

# import time
# start = time.time()
# sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
# finish = time.time()
# res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
# finish = time.time()
#
# print(finish - start)
#
# print(res)

# out = build_semantic_descriptors([["I", "like", "cheese"], ["I", "like", "food"]])
#
# print(out)
#
# semantic = build_semantic_descriptors_from_files(["wp.txt"])
# most_similar_word("cat", ["feline", "rocket"], semantic, cosine_similarity)


print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))
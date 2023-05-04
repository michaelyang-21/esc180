f = open("versedog.txt", encoding = "latin1")
#all_text = f.read()

for line in f.readlines():
    print(line, end = "")

"abc. asdf? asdfasdf!".replace("!", ".").replace("?", ".")

"abc adf alkdsjf".split()

def approx_count_sentences(text):
    punctuation = ["?", "!"]
    for punc in punctuation:
        text = text.replace(punc, ".")
    return len(text.split("."))

def approx_count_words(text):
    return len(text.split())

english = open("losttime.txt", encoding = "latin1").read()

print(approx_count_sentences(english))
print(approx_count_words(english))
print(approx_count_words(english) / approx_count_sentences(english))
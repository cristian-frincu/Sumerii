# A program that will summarize text as concise as possible
# -*- coding: utf-8 -*-

import operator

source_text = """"""

# with open('data.txt', 'r') as myfile:
#     source_text=myfile.read().replace('\n', ' ')
# print "Loaded Data"
sentences = source_text.split(".")
# print "Split sentences"
words = [(i) for j in range(len(sentences)) for i in sentences[j].split(" ")]
# print "Split words"
word_popularity = {x: words.count(x) for x in set(words)}
# print "Word Popularity"
sentence_popularity = ()
sentence_order = 0
for sentence in sentences:
    sentence_value = 0
    for word in sentence.split(" "):
        sentence_value += word_popularity[word]
    sentence_popularity += ((sentence_value, sentence_order, sentence),)
    sentence_order += 1
    # print str(sentence_order) + "/" + str(len(sentences)) + sentence


def getKey(item):
    return item[1]

sentence_popularity = sorted(sentence_popularity, reverse=True)
sentence_ordered_popularity = sorted(sentence_popularity[0:4], key=getKey)

print "Top sentences:"
for sentence in sentence_ordered_popularity:
    print sentence[0]," : "+sentence[2]


print "Top Words:"
sorted_words = sorted(word_popularity.items(),key=operator.itemgetter(1),reverse=True)
for word in sorted_words[0:10]:
	print word[1]," : ",word[0]


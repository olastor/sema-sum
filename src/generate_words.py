import json
import re
import nltk
import editdistance

# Defines the minimum edit distance between each word (pairwise)
MIN_EDIT_DIST = 2

def filter_words(tagged_words, max_len=2048):
  # filter adjectives and length
  adjectives = [w for w, t in tagged_words if t == 'ADJ' and re.match(r'^[a-z]{3,10}$', w)]

  # filter out similar words
  res = []
  for word in set(adjectives):
    valid = True

    for existing in res:
      if editdistance.eval(word, existing) <= MIN_EDIT_DIST:
        valid = False
        break

    if valid:
      res.append(word)

  if len(res) > max_len:
    res = sorted(res, key=lambda x: len(x))[:max_len]

  return sorted(res)

# ENGLISH
words_en = filter_words(nltk.corpus.brown.tagged_words(tagset='universal'))

print(len(words_en))
with open('output/words_en.json', 'w') as f:
  f.write(json.dumps(words_en))

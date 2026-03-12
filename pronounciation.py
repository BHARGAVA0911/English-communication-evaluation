from nltk.corpus import cmudict
nltk.download("cmudict")
d = cmudict.dict()

def analyze_pronunciation(text):
    words = word_tokenize(text.lower())
    pronunciation_count = sum(1 for word in words if word in d)
    pronunciation_score = (pronunciation_count / len(words))*9 if len(words) > 0 else 0
    if pronunciation_score >= 8:
      return 5
    elif pronunciation_score >= 6:
      return 4
    elif pronunciation_score >= 4:
      return 3
    elif pronunciation_score >= 2:
      return 2
    else:
      return 1

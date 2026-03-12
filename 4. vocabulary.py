def analyze_vocabulary(transcript):
    doc = nlp(transcript)

    # Extract words that are not stop words and are alphabetic
    words = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]

    # Calculate vocabulary richness (unique words / total words)
    vocab_richness = len(set(words)) / len(words) if len(words) > 0 else 0

    # Determine the vocabulary band
    if vocab_richness > 0.4:
        vocab_band = 5
    elif vocab_richness > 0.3:
        vocab_band = 4
    elif vocab_richness > 0.2:
        vocab_band = 3
    elif vocab_richness > 0.1:
        vocab_band = 2
    else:
        vocab_band = 1

    return vocab_band

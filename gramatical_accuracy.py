import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def analyze_grammatical_accuracy(transcript):
    doc = nlp(transcript)

    tense_errors = check_tense(doc)
    subject_verb_errors = check_subject_verb_agreement(doc)
    structure_errors = check_sentence_structure(doc)
    punctuation_errors = check_punctuation(doc)

    total_errors = tense_errors + subject_verb_errors + structure_errors + punctuation_errors
    grammatical_accuracy = max(5 - total_errors, 1)

    return grammatical_accuracy

def check_tense(doc):
    errors = 0
    tense_patterns = {'past': 'VBD', 'present': 'VB', 'future': 'MD'}  # Simplified tense patterns
    current_tense = None

    for sent in doc.sents:
        sentence_tense = None

        for token in sent:
            if token.pos_ == 'VERB':
                if token.tag_ in tense_patterns.values():
                    sentence_tense = identify_tense(token.tag_)
                    break

        if sentence_tense:
            if current_tense and current_tense != sentence_tense:
                errors += 1
            current_tense = sentence_tense

    return errors

def identify_tense(tag):
    if tag in ['VBD', 'VBN']:
        return 'past'
    elif tag in ['VBP', 'VBZ', 'VB']:
        return 'present'
    elif tag == 'MD':
        return 'future'
    return None

def check_subject_verb_agreement(doc):
    errors = 0
    for sent in doc.sents:
        for token in sent:
            # Look for noun subject linked to a verb
            if token.dep_ == 'nsubj' and token.head.pos_ == 'VERB':
                # Singular subject (NN) should match singular verb form (VBZ)
                if token.tag_ == 'NN' and token.head.tag_ != 'VBZ':
                    errors += 1
                # Plural subject (NNS) should match plural verb form (VBP)
                elif token.tag_ == 'NNS' and token.head.tag_ != 'VBP':
                    errors += 1
    return errors


def check_sentence_structure(doc):
    errors = 0
    for sent in doc.sents:
        if not any(token.dep_ == 'ROOT' for token in sent):
            errors += 1  # Incomplete sentence or missing main verb
    return errors

def check_punctuation(doc):
    errors = 0
    sentence_endings = {'.', '!', '?'}
    allowed_punctuation = {',', '.', ':', ';'}

    for sent in doc.sents:
        # Check if the sentence ends with appropriate punctuation
        if not any(token.text in sentence_endings for token in sent):
            errors += 1  # Missing end punctuation

        # Check for misplaced or consecutive punctuation marks
        for token in sent:
            if token.text in allowed_punctuation:
                # Check if the next token is also a punctuation mark
                if token.i < len(doc) - 1 and doc[token.i + 1].text in allowed_punctuation:
                    errors += 1  # Consecutive punctuation
                # Check for incorrect usage of colon and semicolon
                if token.text == ':' or token.text == ';':
                    if token.i + 1 < len(doc) and doc[token.i + 1].text in allowed_punctuation - {'.', '!'}:
                        errors += 1

    return errors

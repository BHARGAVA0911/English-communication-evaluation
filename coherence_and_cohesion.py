def analyze_coherence_and_cohesion(transcript):
    doc = nlp(transcript)
    sentences = list(doc.sents)

    if len(sentences) < 2:
        return 1  # Not enough sentences to evaluate coherence

    similarity_scores = []

    # Calculate similarity between consecutive sentences
    for i in range(1, len(sentences)):
      if sentences[i-1].vector.any() and sentences[i].vector.any():
        similarity = sentences[i-1].similarity(sentences[i])
        similarity_scores.append(similarity)
      else:
        similarity_scores.append(0)

    # Calculate the average similarity score
    avg_similarity = sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0

    # Score based on the average similarity
    if avg_similarity > 0.7:
        coherence_score = 5
    elif avg_similarity > 0.5:
        coherence_score = 4
    elif avg_similarity > 0.3:
        coherence_score = 3
    else:
        coherence_score = 2

    # Count the use of cohesive markers
    cohesive_markers = {'however', 'therefore', 'moreover', 'in addition', 'furthermore', 'consequently','whereas', 'but',
                        'yet','on the other hand', 'nevertheless', 'on the contrary', 'by comparison', 'where', 'compared to',
                        'up against', 'balanced against', 'although', 'conversely', 'meanwhile', 'after all',
                        'in contrast','for example', 'for instance', 'in this case', 'in another case', 'on this occasion',
                        'in this situation', 'take the case of', 'to demonstrate', 'to illustrate', 'as an illustration','because',
                        'for', 'since', 'obviously', 'evidently', 'furthermore', 'moreover','beside', 'indeed', 'in fact', 'in addition',
                        'in any case', 'that is' }
    transitions_used = [token.text.lower() for token in doc if token.text.lower() in cohesive_markers]

    cohesion_score = 5 if len(transitions_used) > 2 else 3 if len(transitions_used) > 0 else 1

    # Combine coherence and cohesion scores
    overall_score = (coherence_score + cohesion_score) // 2
    return overall_score

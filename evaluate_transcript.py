def evaluate_transcript(transcript,audio_file):
    # Define the evaluation criteria
    criteria = {
        "Grammatical Accuracy": 0,
        "Fluency": 0,
        "Pronunciation": 0,
        "Vocabulary": 0,
        "Coherence and Cohesion": 0,
    }

    grammatical_errors = analyze_grammatical_accuracy(transcript)

    criteria["Grammatical Accuracy"] = max(5 - grammatical_errors, 1)
    criteria["Fluency"] = analyze_fluency(audio_file,transcript)
    criteria["Pronunciation"] = analyze_pronunciation(transcript)
    criteria["Vocabulary"] = analyze_vocabulary(transcript)
    criteria["Coherence and Cohesion"] = analyze_coherence_and_cohesion(transcript)

    total_score = sum(criteria.values())

    return criteria, total_score

def interpret_score(total_score):
    if total_score >= 22:
        return "Excellent"
    elif total_score >= 18:
        return "Very Good"
    elif total_score >= 13:
        return "Good"
    elif total_score >= 9:
        return "Fair"
    elif total_score >= 5:
        return "Poor"
    else:
        return "Very Poor"

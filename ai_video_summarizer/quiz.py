"""
quiz.py
Generates a simple fill-in-the-blank quiz from the transcribed text,
so students can quickly self-test on what the video covered.
"""

import random


def generate_quiz(text: str, num_questions: int = 3) -> str:
    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 30]

    if len(sentences) < 2:
        return "⚠️ Not enough content to generate a quiz."

    quiz = ""
    num_questions = min(num_questions, len(sentences))

    for i in range(num_questions):
        sentence = sentences[i]
        words = sentence.split()

        if len(words) < 4:
            continue

        keyword = random.choice(words[2:-1])
        question = sentence.replace(keyword, "_____")

        # build distractor options from other words in the sentence
        options = list(set(w.strip(",;:") for w in words if w.lower() != keyword.lower()))
        random.shuffle(options)
        options = options[:3] + [keyword]
        random.shuffle(options)

        quiz += f"\n**Q{i + 1}:** {question}\n\n"
        for j, opt in enumerate(options):
            quiz += f"{chr(65 + j)}) {opt}  \n"
        quiz += f"**Answer:** {keyword}\n\n---\n"

    return quiz if quiz else "⚠️ Not enough content to generate a quiz."

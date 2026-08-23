"""
summarizer.py
Summarizes transcribed text using a Hugging Face summarization pipeline.
"""

from transformers import pipeline

# distilbart is small and fast enough for a live classroom/viva demo.
_summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

_CHUNK_SIZE = 800   # characters per chunk sent to the model
_MAX_CHUNKS = 5     # cap total chunks so long videos still summarize quickly


def _clean_text(text: str) -> str:
    return text.replace("\n", " ").strip()


def summarize_text(text: str) -> str:
    text = _clean_text(text)

    if len(text) < 100:
        return "⚠️ Not enough meaningful speech was found to summarize."

    chunks = [text[i:i + _CHUNK_SIZE] for i in range(0, len(text), _CHUNK_SIZE)]
    chunks = chunks[:_MAX_CHUNKS]

    partial_summaries = []
    for chunk in chunks:
        result = _summarizer(
            chunk,
            max_length=120,
            min_length=40,
            do_sample=False,
        )
        partial_summaries.append(result[0]["summary_text"])

    return "📌 " + " ".join(partial_summaries)

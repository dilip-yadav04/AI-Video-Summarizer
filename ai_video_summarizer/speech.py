"""
speech.py
Converts speech in an audio file to text with timestamps, using faster-whisper.
"""

from faster_whisper import WhisperModel

# "tiny" + int8 keeps this fast enough to run live during a viva/demo on a laptop.
# Swap to "base" or "small" for better accuracy if you have more time/compute.
_model = WhisperModel("tiny", compute_type="int8")


def speech_to_text_with_timestamps(audio_path: str):
    """
    Transcribes the given audio file.
    Returns (full_text, timestamps_string).
    """
    segments, _ = _model.transcribe(audio_path, beam_size=5)

    full_text = ""
    timestamps = ""

    for seg in segments:
        clean = seg.text.strip()
        if len(clean) > 3:  # skip near-empty/noise segments
            full_text += clean + " "
            timestamps += f"{round(seg.start, 1)}s - {round(seg.end, 1)}s: {clean}\n"

    return full_text.strip(), timestamps.strip()

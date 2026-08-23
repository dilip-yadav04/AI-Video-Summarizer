"""
audio_utils.py
Extracts a mono, 16kHz WAV audio track from a video file using ffmpeg.
This is the format faster-whisper expects for transcription.
"""

import os
import subprocess


def extract_audio(video_path: str, session_id: str, max_seconds: int = 180) -> str:
    """
    Extracts audio from the given video file and saves it as a .wav file.
    max_seconds caps the clip length so a demo/viva run stays quick.
    """
    os.makedirs("temp", exist_ok=True)
    audio_path = f"temp/audio_{session_id}.wav"

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", video_path,
            "-t", str(max_seconds),
            "-ar", "16000",
            "-ac", "1",
            audio_path,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return audio_path

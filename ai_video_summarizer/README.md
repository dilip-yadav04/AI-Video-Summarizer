# 🎬 AI Video Summarizer

An AI-powered tool that helps students quickly understand a video when they're short on time.
Upload a video file, or paste a YouTube link, and get:

- 📄 **A short summary** of the spoken content
- 🧠 **An auto-generated quiz** (fill-in-the-blank) to self-test understanding
- ⏱️ **A timestamped transcript**, so you can jump to any part of the video
- 📥 **A downloadable PDF report** with the summary and quiz, for offline revision

## How it works (pipeline)

1. **`downloader.py`** – downloads the video if a YouTube URL is given (via `yt-dlp`)
2. **`audio_utils.py`** – extracts a clean 16kHz mono audio track (via `ffmpeg`)
3. **`speech.py`** – transcribes speech to text with timestamps (via `faster-whisper`)
4. **`summarizer.py`** – summarizes the transcript (via a Hugging Face summarization pipeline)
5. **`quiz.py`** – generates a quick fill-in-the-blank quiz from the transcript
6. **`pdf_utils.py`** – builds a downloadable PDF report of the summary + quiz
7. **`app.py`** – ties everything together in a Gradio web UI

## Setup

```bash
pip install -r requirements.txt
```

You'll also need **ffmpeg** installed and available on your system PATH.

## Run

```bash
python app.py
```

This opens a local web app where you can upload a video or paste a YouTube link.

## Notes

- The Whisper model is set to `tiny` and audio is capped to a few minutes for
  fast turnaround during a live demo — swap to a larger model / remove the cap
  for higher accuracy on full-length videos.
- Downloaded videos, extracted audio, and generated PDFs are saved under
  `temp/` and `output/`.

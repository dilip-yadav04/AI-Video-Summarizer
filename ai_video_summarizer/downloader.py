"""
downloader.py
Handles downloading a video from a YouTube URL using yt-dlp.
"""

import os
import yt_dlp


def download_youtube(url: str, session_id: str) -> str:
    """
    Downloads a YouTube video to the temp/ folder and returns the local file path.
    Uses the smallest available mp4 format to keep downloads fast for a demo/viva.
    """
    os.makedirs("temp", exist_ok=True)

    output_template = f"temp/video_{session_id}.%(ext)s"

    ydl_opts = {
        "format": "worst[ext=mp4]/best[ext=mp4]/best",  # fastest option that still plays
        "outtmpl": output_template,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

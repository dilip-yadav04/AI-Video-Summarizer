"""
app.py
Main Gradio app: upload a video OR paste a YouTube link, and get back
a summary, an auto-generated quiz, a timestamped transcript, and a PDF report.
"""

import time
import gradio as gr

from downloader import download_youtube
from audio_utils import extract_audio
from speech import speech_to_text_with_timestamps
from summarizer import summarize_text
from quiz import generate_quiz
from pdf_utils import create_pdf


def process(video, youtube_url, quiz_toggle, progress=gr.Progress()):
    try:
        progress(0, desc="🚀 Starting...")
        session_id = str(int(time.time()))  # unique id so runs never overwrite each other

        # Step 1: get the video, either from YouTube or the uploaded file
        if youtube_url:
            video_path = download_youtube(youtube_url, session_id)
        elif video:
            video_path = video
        else:
            return "❌ Please upload a video or paste a YouTube link.", "", "", None

        # Step 2: extract audio
        progress(0.2, desc="🎧 Extracting audio...")
        audio_path = extract_audio(video_path, session_id)

        # Step 3: transcribe
        progress(0.4, desc="🧠 Transcribing speech...")
        text, timestamps = speech_to_text_with_timestamps(audio_path)

        if not text.strip():
            return "❌ No speech detected in this video.", "", "", None

        # Step 4: summarize
        progress(0.6, desc="📄 Summarizing...")
        summary = summarize_text(text)

        # Step 5: quiz (optional)
        quiz = ""
        if quiz_toggle:
            progress(0.8, desc="📝 Generating quiz...")
            quiz = generate_quiz(text)

        # Step 6: PDF report
        progress(0.9, desc="📄 Building PDF report...")
        pdf_path = create_pdf(summary, quiz, session_id)

        progress(1.0, desc="✅ Done")
        return summary, quiz, timestamps, pdf_path

    except Exception as e:
        return f"❌ Error: {str(e)}", "", "", None


with gr.Blocks(theme=gr.themes.Soft(), title="AI Video Summarizer") as app:

    gr.Markdown("# 🎬 AI Video Summarizer")
    gr.Markdown(
        "Upload a video or paste a YouTube link to get a quick summary, "
        "a self-test quiz, and a timestamped transcript — built for quick revision."
    )

    with gr.Row():
        video_in = gr.Video(label="Upload Video")
        youtube_in = gr.Textbox(label="YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

    quiz_toggle = gr.Checkbox(label="Generate Quiz", value=True)
    run_btn = gr.Button("⚡ Process Video", variant="primary")

    with gr.Tabs():
        with gr.Tab("📄 Summary"):
            summary_out = gr.Textbox(lines=12, show_copy_button=True)

        with gr.Tab("🧠 Quiz"):
            quiz_out = gr.Markdown()

        with gr.Tab("⏱️ Timestamped Transcript"):
            timestamps_out = gr.Textbox(lines=12, show_copy_button=True)

    pdf_out = gr.File(label="Download PDF Report")

    run_btn.click(
        process,
        inputs=[video_in, youtube_in, quiz_toggle],
        outputs=[summary_out, quiz_out, timestamps_out, pdf_out],
    )

if __name__ == "__main__":
   app.launch(share=True, inbrowser=True)

# 🎬 AI Video Summarizer & Quiz Maker

> **Turn long educational videos into short, understandable revision material.**

**AI Video Summarizer & Quiz Maker** is an AI-powered learning tool designed for students who want to quickly understand educational videos when they are short on time.

The application allows users to **upload a video file or provide a YouTube URL** and automatically generates:

* 📄 **AI-generated summary** of the spoken content
* 🧠 **Auto-generated fill-in-the-blank quiz** for self-assessment
* ⏱️ **Timestamped transcript** for easy navigation
* 📥 **Downloadable PDF report** containing the summary and quiz
* 🌐 **Simple Gradio web interface** for easy interaction

---

## ✨ Features

### 🎥 Video Input

Upload a local video file or paste a **YouTube URL**.

### 🎙️ Speech-to-Text

The project uses **Faster-Whisper** to convert spoken audio into text while preserving timestamps.

### 🤖 AI Summarization

The extracted transcript is processed using a **Hugging Face summarization pipeline** to generate a concise summary.

### 🧠 Automatic Quiz Generation

The system creates **fill-in-the-blank questions** from the transcript so students can test their understanding.

### ⏱️ Timestamped Transcript

Every section of the transcript contains timestamps, making it easy to identify where specific information appears in the original video.

### 📄 PDF Report

Students can download a structured PDF containing the generated summary and quiz for **offline revision**.

### ⚡ Fast Demo Mode

The project currently uses the **Whisper `tiny` model** and limits audio duration to keep processing fast during demonstrations.

---

## 🔄 How It Works

```text
              🎥 Video / YouTube URL
                       │
                       ▼
              ┌─────────────────┐
              │  downloader.py  │
              │   yt-dlp        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ audio_utils.py  │
              │     ffmpeg      │
              └────────┬────────┘
                       │
                16kHz Mono Audio
                       │
                       ▼
              ┌─────────────────┐
              │    speech.py    │
              │  Faster-Whisper │
              └────────┬────────┘
                       │
                Timestamped Text
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
    ┌─────────────────┐   ┌─────────────────┐
    │  summarizer.py  │   │     quiz.py     │
    │ Hugging Face AI │   │ Quiz Generator  │
    └────────┬────────┘   └────────┬────────┘
             │                     │
             └──────────┬──────────┘
                        ▼
               ┌─────────────────┐
               │  pdf_utils.py   │
               │   PDF Report    │
               └────────┬────────┘
                        │
                        ▼
               📥 Downloadable PDF
```

---

## 🛠️ Project Structure

```text
AI-Video-Summarizer/
│
├── app.py                  # Gradio web application
├── downloader.py           # YouTube video downloader
├── audio_utils.py          # Audio extraction and processing
├── speech.py               # Speech-to-text transcription
├── summarizer.py           # AI-based text summarization
├── quiz.py                 # Automatic quiz generation
├── pdf_utils.py            # PDF report generation
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── temp/                   # Temporary video/audio files
└── output/                 # Generated PDF reports
```

---

## 🧩 Technology Stack

| Technology             | Purpose                              |
| ---------------------- | ------------------------------------ |
| 🐍 **Python**          | Core programming language            |
| 🎙️ **Faster-Whisper** | Speech recognition and transcription |
| 🤗 **Hugging Face**    | AI text summarization                |
| 🎞️ **FFmpeg**         | Audio extraction and processing      |
| 📺 **yt-dlp**          | YouTube video downloading            |
| 🌐 **Gradio**          | Web-based user interface             |
| 📄 **PDF Library**     | PDF report generation                |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Video-Summarizer.git
```

### 2. Navigate to the Project

```bash
cd AI-Video-Summarizer
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Make sure **FFmpeg** is installed and available in your system's `PATH`.

Verify the installation:

```bash
ffmpeg -version
```

---

## ▶️ Run the Application

Start the Gradio application using:

```bash
python app.py
```

After starting the application, open the local Gradio URL shown in the terminal.

You can then:

1. 🎥 Upload a video
2. 🔗 Or paste a YouTube URL
3. 🎙️ Extract and transcribe the audio
4. 🤖 Generate an AI summary
5. 🧠 Generate a quiz
6. ⏱️ View the timestamped transcript
7. 📥 Download the PDF report

---

## 📄 Example Output

The generated report contains:

```text
=====================================
       AI VIDEO LEARNING REPORT
=====================================

📄 SUMMARY

[AI-generated summary of the video]

-------------------------------------

🧠 QUIZ

1. The ________ algorithm is used to...
   
2. ________ is responsible for...

3. The main purpose of ________ is...

-------------------------------------

⏱️ TIMESTAMPED TRANSCRIPT

[00:00] Introduction...
[00:35] Main concept...
[01:42] Important example...
[02:58] Conclusion...
```

---

## 🚀 Future Improvements

The project can be extended with several advanced features:

* 🎯 **Better quiz generation** using LLMs
* 📚 **Multiple quiz types** such as MCQs, true/false and short answers
* 🌍 **Multi-language transcription and summarization**
* 🗣️ **Speaker identification**
* 🔍 **Keyword and topic extraction**
* 📊 **Student performance tracking**
* ☁️ **Cloud deployment**
* 📱 **Mobile-friendly interface**
* ⚡ Support for **long-duration videos**
* 🤖 Integration with larger and more accurate AI models

---

## ⚠️ Current Limitations

* The project currently uses the **Whisper `tiny` model** for faster processing.
* Audio duration is limited for faster live demonstrations.
* Larger videos may require more processing time and system resources.
* Summarization quality depends on the transcript quality and selected AI model.
* FFmpeg must be installed separately on the system.

> 💡 **Tip:** For better transcription accuracy, replace the `tiny` Whisper model with `base`, `small`, `medium`, or another suitable model depending on your hardware.

---

## 🎯 Use Cases

This project can be useful for:

* 👨‍🎓 Students preparing for exams
* 📚 Quick revision of lectures
* 🎥 Educational YouTube videos
* 🧑‍🏫 Lecture summarization
* 💻 Online courses
* 📝 Creating revision notes
* 🧠 Self-assessment through quizzes

---

## 💡 Why This Project?

Students often spend hours watching long lectures just to revise a few important concepts.

This project combines **Speech Recognition + Natural Language Processing + AI Summarization + Automatic Quiz Generation** into a single application.

Instead of watching an entire video again, students can quickly obtain the **key concepts, transcript, and quiz** they need for revision.

---

## 🔐 Privacy

Videos and generated files are processed locally when running the application locally. Temporary files are stored in the `temp/` directory and generated reports are stored in the `output/` directory.

---

## 👨‍💻 Author

**Dilip Yadav**

B.Tech — Computer Science & Engineering (AI & ML)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

**Made with Python, AI & ❤️ for smarter learning.**

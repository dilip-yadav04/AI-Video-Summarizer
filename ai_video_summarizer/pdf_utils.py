"""
pdf_utils.py
Builds a downloadable PDF report containing the summary and quiz,
so the output can be saved/shared/printed after the demo.
"""

import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def create_pdf(summary: str, quiz: str, session_id: str) -> str:
    os.makedirs("output", exist_ok=True)
    file_path = f"output/summary_report_{session_id}.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>AI Video Summarizer — Report</b>", styles["Title"]))
    content.append(Spacer(1, 16))

    content.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
    content.append(Paragraph(summary.replace("\n", "<br/>"), styles["Normal"]))
    content.append(Spacer(1, 16))

    content.append(Paragraph("<b>Quiz</b>", styles["Heading2"]))
    content.append(Paragraph(quiz.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(content)
    return file_path

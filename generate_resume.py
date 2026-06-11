"""Generate resume.pdf from portfolio content. Run: python generate_resume.py"""
from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "sanskritig1705@gmail.com | +91-8080248884 | linkedin.com/in/sanskritigupta17", align="C")

def add_section(pdf, title):
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(79, 142, 247)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)

def add_bullet(pdf, text, bold_prefix=None):
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    x = pdf.get_x()
    pdf.cell(4, 5, "-")
    if bold_prefix:
        pdf.set_font("Helvetica", "B", 9)
        pdf.write(5, bold_prefix)
        pdf.set_font("Helvetica", "", 9)
        pdf.write(5, text)
    else:
        pdf.multi_cell(0, 5, text)
    pdf.ln(1)

def build():
    pdf = ResumePDF()
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 10, "Sanskriti Gupta", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(79, 142, 247)
    pdf.cell(0, 6, "AI & Data Science Engineer | Full Stack (MERN)", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, "B.Tech AI&DS @ PICT (2024-28) | CGPA: 9.65 | Pune, India", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    add_section(pdf, "EDUCATION")
    add_bullet(pdf, "Pune Institute of Computer Technology - B.Tech, AI & Data Science (2024-2028)", "PICT: ")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, "  CGPA: 9.65/10.0 | Top of branch", new_x="LMARGIN", new_y="NEXT")
    add_bullet(pdf, "Poddar Brio International School - Class XII (2024) | 87.6%", "")
    add_bullet(pdf, "Infant Jesus School - Class X (2022) | 98.6%", "")
    pdf.ln(2)

    add_section(pdf, "TECHNICAL SKILLS")
    skills = [
        "Languages: C++, Python, JavaScript",
        "Frontend: React.js, HTML5, CSS3",
        "Backend: Node.js, Express.js, REST APIs, JWT Authentication",
        "Databases: MongoDB, PostgreSQL, Prisma ORM",
        "AI/NLP: OpenAI GPT, Groq API, LangChain, NLP, GenAI",
        "Tools: Git, GitHub, Vercel, Jupyter",
    ]
    for s in skills:
        add_bullet(pdf, s)
    pdf.ln(2)

    add_section(pdf, "PROJECTS")
    projects = [
        ("AI SQL Generator", "NL-to-SQL converter with GPT-3.5-turbo, query history, syntax highlighting. Deployed on Vercel + Render. (HTML, JS, Node.js, Express, OpenAI API)"),
        ("LingoQuest", "Gamified language-learning platform (German, Spanish, Hindi) with XP tracking and streak rewards. (HTML, CSS, JavaScript)"),
        ("PaySure - Financial Safety Platform", "Loan affordability system with NLP legal agreement analyzer and fraud detection. (React, Node.js, MongoDB, Groq API, JWT)"),
    ]
    for name, desc in projects:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(0, 5, name, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(0, 4, desc)
        pdf.ln(2)

    add_section(pdf, "ACHIEVEMENTS & CERTIFICATIONS")
    achievements = [
        "Top Student in Branch - 9.65 CGPA, Highest in AI&DS at PICT (2024-25)",
        "200+ LeetCode problems solved (Arrays, Trees, Graphs, DP, Sliding Window)",
        "NPTEL Certified - Python for Data Science (87%)",
        "Coursera - Natural Language Processing Specialization (Verified)",
        "Coursera - Generative AI with Large Language Models (DeepLearning.AI, Verified)",
    ]
    for a in achievements:
        add_bullet(pdf, a)
    pdf.ln(2)

    add_section(pdf, "LINKS")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 5, "GitHub: github.com/sanaryan175", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, "LinkedIn: linkedin.com/in/sanskritigupta17", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, "Email: sanskritig1705@gmail.com", new_x="LMARGIN", new_y="NEXT")

    pdf.output("resume.pdf")
    print("Created resume.pdf")

if __name__ == "__main__":
    build()

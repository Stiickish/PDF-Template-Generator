from fpdf import FPDF
import pandas as pd

# Define PDF
# P = Portrait mode, mm = millimeters, A4 = paper size
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)

# Read the file
# Create x pages with a headline of Topic
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()  # Add page

    # Set details about the page
    # times = font family, B = Bold, size = text size
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 100, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

    # Multiple Lines
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Define the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1)

    # Nested for loop to generate the pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Define the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1)

        # Multiple Lines
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("notebook.pdf")

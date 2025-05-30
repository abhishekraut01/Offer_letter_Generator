import pandas as pd
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
import shutil

# Step 1: Load CSV
df = pd.read_csv("data/candidates.csv")
df.columns = df.columns.str.strip()  # Clean column names

# Step 2: Define folders
template_path = "templates/offer_letter_template.docx"
docx_output_dir = "output/docx"
pdf_output_dir = "output/pdf"

# Step 3: Create folders if not exist
os.makedirs(docx_output_dir, exist_ok=True)
os.makedirs(pdf_output_dir, exist_ok=True)

# Step 4: Generate DOCX offer letters
for _, row in df.iterrows():
    doc = DocxTemplate(template_path)
    context = {
        "first_name": row["First Name"],
        "last_name": row["Last Name"],
        "email": row["Email"],
        "phone_number": row["Phone Number"],
        "city_state": row["City"],
        "college_name": row["College Name"],
        "college_year": row["College Year"],
        "linkedin": row["LinkedIn Profile"],
        "github": row["Github Profile"],
        "interested_domain": row["Interested Domain"]
    }
    filename = f"Offer_Letter_{row['First Name']}_{row['Last Name']}.docx".replace(" ", "_")
    filepath = os.path.join(docx_output_dir, filename)
    doc.render(context)
    doc.save(filepath)
    print(f"Generated DOCX: {filename}")

# Step 5: Convert DOCX to PDF
print("Converting DOCX to PDF...")
convert(docx_output_dir, pdf_output_dir)
print("All PDFs generated successfully in 'output/pdf/' folder.")

"""
Recompile all 30 HTML files in andalucia_comun to PDF using Microsoft Edge headless.
After compiling, copy each PDF to PDFs_Para_Imprimir/Andalucia_Comun/.
Verify with pypdf that 0 asterisks are found in extracted text.
"""

import os
import glob
import subprocess
import shutil
import pypdf

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SRC_DIR = "andalucia_comun"
DEST_DIR = os.path.join("PDFs_Para_Imprimir", "Andalucia_Comun")

os.makedirs(DEST_DIR, exist_ok=True)

html_files = sorted(glob.glob(f"{SRC_DIR}/*.html"))
print(f"Starting recompilation of {len(html_files)} themes...")

success_count = 0
for idx, html_file in enumerate(html_files):
    pdf_filename = os.path.splitext(os.path.basename(html_file))[0] + ".pdf"
    pdf_path = os.path.join(SRC_DIR, pdf_filename)
    dest_path = os.path.join(DEST_DIR, pdf_filename)
    
    abs_html = os.path.abspath(html_file)
    abs_pdf = os.path.abspath(pdf_path)
    
    cmd = [EDGE_PATH, "--headless", "--disable-gpu", f"--print-to-pdf={abs_pdf}", abs_html]
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(abs_pdf):
        # copy to dest
        shutil.copy2(abs_pdf, dest_path)
        
        # Verify text with pypdf
        reader = pypdf.PdfReader(abs_pdf)
        num_pages = len(reader.pages)
        total_text = ' '.join(page.extract_text() or '' for page in reader.pages)
        count_doubles = total_text.count('**')
        count_singles = total_text.count('*')
        
        print(f"[{idx+1}/{len(html_files)}] OK: {pdf_filename} ({num_pages} pags) - **={count_doubles}, *={count_singles}")
        success_count += 1
    else:
        print(f"[{idx+1}/{len(html_files)}] FAILED: {pdf_filename} -> {res.stderr}")

print(f"\nFinished: {success_count}/{len(html_files)} PDFs recompiled and copied.")

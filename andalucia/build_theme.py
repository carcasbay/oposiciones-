import os
import sys
import subprocess
import pypdf

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def compile_pdf(html_path, pdf_path):
    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)
    cmd = [EDGE_PATH, "--headless", "--disable-gpu", f"--print-to-pdf={abs_pdf}", abs_html]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(abs_pdf):
        reader = pypdf.PdfReader(abs_pdf)
        num_pages = len(reader.pages)
        size_kb = os.path.getsize(abs_pdf) // 1024
        print(f"[OK] PDF generated: {os.path.basename(abs_pdf)} ({num_pages} pags, {size_kb} KB)")
        return True, num_pages
    else:
        print(f"[ERROR] PDF generation failed for {html_path}: {res.stderr}")
        return False, 0

if __name__ == "__main__":
    if len(sys.argv) == 3:
        compile_pdf(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python build_theme.py <input.html> <output.pdf>")

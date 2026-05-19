"""Extract text from the three iPAS study guide PDFs into per-page text files.
Run once; output kept under d:/Code/IPAS/_pdf_text/ for later reference.
"""
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"d:/Code/IPAS")
SRC = ROOT / "學習指引"
OUT = ROOT / "_pdf_text"
OUT.mkdir(exist_ok=True)

FILES = {
    "s1": SRC / "AI應用規劃師(中級)-學習指引-科目1人工智慧技術應用規劃_20251222101833.pdf",
    "s2": SRC / "AI應用規劃師(中級)-學習指引-科目2大數據處理分析與應用_20251222101850.pdf",
    "s3": SRC / "AI應用規劃師(中級)-學習指引-科目3機器學習技術與應用_20251222101907.pdf",
}

for key, pdf in FILES.items():
    reader = PdfReader(str(pdf))
    out_file = OUT / f"{key}_full.txt"
    parts = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as e:
            text = f"[extract error: {e}]"
        parts.append(f"\n\n===== {key} PAGE {i:03d} =====\n{text}")
    out_file.write_text("".join(parts), encoding="utf-8")
    print(f"{key}: wrote {out_file} ({len(reader.pages)} pages)")

import re, base64, pathlib

SRC = pathlib.Path(r"C:\Users\Dell\Downloads\Nanak Chaudhuri — Strategic Collections & Recovery Leader.html")
OUT = pathlib.Path(__file__).parent.parent / "assets"
html = SRC.read_text(encoding="utf-8")

img_match = re.search(r'src="data:image/jpeg;base64,([^"]+)"', html)
photo_bytes = base64.b64decode(img_match.group(1))
(OUT / "photo.jpg").write_bytes(photo_bytes)
assert photo_bytes[:3] == b"\xff\xd8\xff", "not a valid JPEG header"
print(f"photo.jpg: {len(photo_bytes):,} bytes")

pdf_match = re.search(r'const PDF_B64\s*=\s*"([^"]+)";', html)
pdf_bytes = base64.b64decode(pdf_match.group(1))
(OUT / "resume.pdf").write_bytes(pdf_bytes)
assert pdf_bytes[:4] == b"%PDF", "not a valid PDF header"
print(f"resume.pdf: {len(pdf_bytes):,} bytes")

from pypdf import PdfWriter
merger=PdfWriter()

pdfs=["12thR_compressed.pdf","BVoc _compressed.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
print("✅ PDF merged successfully! Saved as merged.pdf")
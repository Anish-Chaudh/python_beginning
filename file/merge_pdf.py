import os
files = os.listdir("file/pdf_folder")
print(files)

from pypdf import PdfWriter
def merge_pdfs(pdf_list,output_path):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"successfully merged into {output_path}")

files = [f"file/pdf_folder/{file}" for file in files if file.endswith(".pdf")]
# output_path = "file/merged.pdf"
# merge_pdfs(files, output_path)
merge_pdfs(files, "file/merged.pdf")

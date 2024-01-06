from flask import Flask
from PyPDF2 import PyPDF2
app = Flask(__name__)

# Members API Route
@app.route("/members")
def members():
    return {"members": ["m1", "m2", "m3"]}


if __name__ == "__main__":
     app.run(debug=True)


   


def compressor(input, output):
    # we open the file
    with open(input, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter(file)

        for pageNumber in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(pageNumber)
            page.compressContentStreams()
            pdf_writer.addPage(page)
            with open(output, 'wb') as compressed_file:
                pdf_writer.write(compressed_file)


if __name__ == "__main__":
    input_path = "input.pdf"
    output_path = "output_compressed.pdf"
    compressor(input_path, output_path)



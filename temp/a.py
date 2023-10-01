from PyPDF2 import PdfReader

# Create a PdfFileReader object
pdf_file = PdfReader("done/Brochure.pdf")

# Get the page object for the first page
page = pdf_file.pages[0]

# Extract text from the page
text = page.extract_text()
print("No of pages in pdf is :",len(pdf_file.pages))
# Print the text
# print(text)
count = 0

for page in pdf_file.pages:
    text = page.extract_text()
    count += 1
    filename= f"./Brochure Dataset/page{count}.txt"
    with open(filename, "w") as f:
        # Write some text to the file
        f.write(text)
    # Close the file
    f.close()

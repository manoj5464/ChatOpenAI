from PyPDF2 import PdfReader
from flask import Flask,redirect
import os
class PdfParserAndTrainer:
    def __init__(self,request):
        self.request = request

    def parseTextFromPdf(self,file):
        print(os.path.abspath(os.getcwd()))
        try:
            # request_body = self.request.json
            # if 'filename' not in request_body:
            #     return {'error': 'Missing file name'}, 400
            
            count=0
            # Create a PdfFileReader object
            pdffileapth = os.path.join("api/training-data-set/pdf/",file)
            pdf_file = PdfReader(pdffileapth)
            print("No of pages in pdf is :",len(pdf_file.pages))
            for page in pdf_file.pages:
                text = page.extract_text()
                count += 1
                
                filename= f"api/training-data-set/text/pdfpage{count}.txt"
                print(filename)
                with open(filename, "w") as f:
                    # Write some text to the file
                    f.write(text)
                # Close the file
                f.close()
            self.movePdfFileAfterExtraction(pdffileapth,os.path.join("api/trained/pdf/",file))
            return {'success':True,'message':"Text Extract page wise successfully."},200
        except FileNotFoundError:
            # Handle the FileNotFoundError exception
            print("File not found!")
            return {'error': 'File Not Found'}, 400
        except Exception as e:
            print(e)
            return {'error': "Unknown"}, 400
        
    def movePdfFileAfterExtraction(self,source_path,destination_path):
        if os.path.exists(source_path):
            try:
                # Open the source file in read mode
                with open(source_path, 'rb') as source_file:
                    # Read the contents of the source file
                    file_contents = source_file.read()
                    
                    # Open the destination file in write mode
                    with open(destination_path, 'wb') as destination_file:
                        # Write the contents to the destination file
                        destination_file.write(file_contents)

                # Remove the source file after copying
                os.remove(source_path)
                print('File moved successfully.')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print('Source file does not exist.')


   
    def upload_file(self):
        mode = ''
        if 'file' not in self.request.files:
            return redirect(request.url)

        file = self.request.files['file']
        print("sdd"+file.filename)
        if file.filename == '':
            return redirect(self.request.url)
        ext = self.findExtension(file.filename)

        if ext == 'txt':
            mode="text"
        elif ext == '.pdf':
            mode="pdf"
        else :
            return redirect(self.request.url)

        print(file.filename,mode)
        if file:
            # You can save the uploaded file or perform any desired operations here.
            # For example, to save the file in the current directory:
            file.save(os.path.join(f'api/training-data-set/{mode}',file.filename))
            self.parseTextFromPdf(file.filename)
            return "Trained successfully."

        return "Some error occured please retry."

    def findExtension(self,filename):
        last_dot_index = filename.rfind(".")

        if last_dot_index != -1:
            # Extract the extension from the filename
            extension = filename[last_dot_index:]
        else:
            extension = ""
        
        return extension
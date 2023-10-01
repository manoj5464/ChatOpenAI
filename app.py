from flask import Flask,request
from api.pdf import PdfParserAndTrainer
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/trainedPdfData', methods=['POST'])
def uploadPdfFile():
    return PdfParserAndTrainer(request).upload_file()
if __name__ == '__main__':
    app.run(debug=True)
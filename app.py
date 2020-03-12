from flask import Flask, render_template, request
from werkzeug import secure_filename
from main import prediction
import os

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(os.path.join('static', 'storage', filename))
		file = os.path.join('static', 'storage', filename)
		result = prediction(os.path.join('static', 'storage', filename))
		filename = f.filename
		return render_template('result.html', file = file, result = result, filename=filename)

if __name__ == '__main__':
   app.run()
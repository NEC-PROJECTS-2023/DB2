from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app=Flask(__name__, static_folder='static', template_folder='templates')
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image',methods=['POST'])
def upload_image():
    print(request)
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html',filename=filename)

@app.route('/image/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__=='__main__':
    app.run(debug=True)
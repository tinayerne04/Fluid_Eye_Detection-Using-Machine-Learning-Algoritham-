from flask import Flask, flash, render_template, request, redirect, url_for
import urllib.request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wtforms.validators import InputRequired
from keras.models import load_model
from keras.preprocessing import image


# name = predictions

app = Flask(__name__)


dic = {0: 'Normal Eye', 1: 'Fluid Eye'}

model = load_model('flue-test.h5')

def pred_label(img_path, threshold=0.9):
    img = Image.open(img_path)
    img = img.resize((150, 150))
    img_array = np.array(img) 
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension
    prediction = model.predict(img_array)
    print("Raw Predictions:", prediction)
    predicted_class_index = np.argmax(prediction)

    if prediction[0][predicted_class_index] > threshold:
        return "Fluid Eye"

    # Otherwise, classify as "Normal Eye"
    else:
        return "Normal Eye"





app.config['SECRET_KEY'] = 'supersecreatkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif']


def allowed_file(filename):
        photos= UploadSet('photos', ('png', 'jpg'))

class uploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

   



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    form = uploadFileForm()
    result = None
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # return "File Has Been Uploaded."
        result = pred_label(filepath)


    return render_template('index.html',  form=form, result=result, image_filename = image_filename)


    
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='files/' + filename), code=301)
 

def get_output():
     if request.method == 'POST':
         img = request.files['my_image']
         image_path = "static/files" + img.filename
         img.save(image_path)
         p = pred_label(image_path)
     return render_template('index.html', predicted_class = p, image_path = image_path ) 


if __name__=='__main__':
    app.run(debug=True)
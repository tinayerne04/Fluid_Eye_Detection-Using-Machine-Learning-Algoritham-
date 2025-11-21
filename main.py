from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)

#dic = {0 : 'Normal Eye', 1 : 'Fluid Eye'}

#model = load_model('flue-test.h5')
#model.make_predict_function()

#def predict_label(img_path):
#	i = image.load_img(img_path, target_size=(100,100))
#	i = i.reshape(1, 100,100,3)
#	p = model.predict_class(i)
#	return dic[p[0]]



dic = {0: 'Normal Eye', 1: 'Fluid Eye'}

model = load_model('eye-100.h5')



def pred_label(img_path, threshold=0.9):
    img = Image.open(img_path)
    img = img.resize((144, 144))
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




# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")



@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/files/" + img.filename	
		img.save(img_path)

		p = pred_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
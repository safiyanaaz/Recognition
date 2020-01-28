from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
import base64
from PIL import Image
from io import BytesIO
import re
import pytesseract
from gtts import gTTS
from flask import jsonify
import speech_recognition as sr
import os
import time
import pyttsx3


from flask_assets import Bundle, Environment

app=Flask(__name__)
js = Bundle('app.js', output='gen/main.js')
assets=Environment(app)
assets.register('main_js',js)

@app.route('/',methods=['GET', 'POST'])
def home():
	
	return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])

def predict():
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')   # getting details of current speaking rate
	engine.setProperty('rate', 125)     # setting up new voice rate


	"""VOLUME"""
	volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1                      
	 #printing current volume level
	engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

	"""VOICE"""
	voices = engine.getProperty('voices')    
	
	
	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
	if request.method=='POST':
		
		#Taking inputs from camera to convert in image
		input1= request.form.get("input1") if request.form.get("input1") else None

		base64_data = re.sub('^data:image/.+;base64,', '',input1);
		im = Image.open(BytesIO(base64.b64decode(base64_data)))
		im.save('image.png', 'PNG')
	
	image_path= "image.png"
	imagename = "demo"
	img = Image.open(image_path)
	text = pytesseract.image_to_string(img)
	print(text)
	
	f = open("{0}.txt".format(imagename), 'w')
	f.write(text)
	f.close()
	f = open('{0}.txt'.format(imagename))
	x = f.read()

	language = 'en'
	audio = gTTS(text = x , lang = language , slow = False)
	r1=sr.Recognizer()
	#os.system(r"audiosproject\audio_name.wav")
	engine.say("Please Speak the name in which you want to save your audio file")
	engine.runAndWait()
	
	with sr.Microphone() as source:
		print('Speak now')
		
		audio_name=r1.listen(source)
		text_audio_name=r1.recognize_google(audio_name)
		text_audio_name=text_audio_name.replace(" ","")
		print(text_audio_name)
		engine.say("Your audio is saved as {0}.We are processing your audio Please Wait".format(text_audio_name))
		engine.runAndWait()

		#mytext = 'Your audio is saved as {0}.We are processing your audio Please Wait'.format()
		#language = 'en'
		#myobj = gTTS(text=mytext, lang=language, slow=False) 
		#myobj.save("saved.wav") 
		#os.system("saved.wav")
		#time.sleep(7)
	audio.save("{0}.wav".format(text_audio_name))
	os.system("{0}.wav".format(text_audio_name))
	print('saved audio')
		
	#return jsonify(text,image_path,imagename)

	return render_template('result.html',text=text)

if __name__ == '__main__':
	app.run(debug=True)
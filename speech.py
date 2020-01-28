'''{% assets "main_js" %}
<script type="text/javascript" src="{{ ASSET_URL }}"></script>
{% endassets %}
'''
	'''
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')   # getting details of current speaking rate
	engine.setProperty('rate', 125)     # setting up new voice rate


	"""VOLUME"""
	volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1                      
	 #printing current volume level
	engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

	"""VOICE"""
	voices = engine.getProperty('voices')    
	engine.say("Welcome to the app for Visually Impaired People Please Speak Retrieve or Click Picture")
	engine.runAndWait()
	engine.stop()


	#os.system(r"audiosproject\welcome.wav")
	#time.sleep(7)
	r2=sr.Recognizer()
	r3=sr.Recognizer()
	with sr.Microphone() as source:
		print('Speak retrieve or click picture')
		speak=r2.listen(source)
		start=r2.recognize_google(speak)
		print(start)
	if "retrieve" in start:
		engine.say("Speak the name of audio file you want to retrieve")
		engine.runAndWait()
		
		#os.system(r"audiosproject\retrieve.wav")
		with sr.Microphone() as source:
			print("Speak audio name")
			audio_name_retrieve=r3.listen(source)
			name=r3.recognize_google(audio_name_retrieve)
			audioo="{0}.wav".format(name)
			list_files =os.listdir(r"C:\Users\Lenovo\Desktop\text_recogniz_flask")
			if audioo in list_files:
				os.system(audioo)
			else:
				engine.say("Sorry No such audio Found")
				engine.runAndWait()
	elif "click picture" in start:
		print('Click Picture')'''
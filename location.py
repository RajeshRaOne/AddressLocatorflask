from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	URL = "http://maps.googleapis.com/maps/api/geocode/json"
	if request.method == 'POST':
		location = request.form["location"]
		location = location.strip()
		if(location != ''):
			location_detail = {'address':location}
			r = requests.get(url = URL, params = location_detail)
			data = r.json()
			latitude = data['results'][0]['geometry']['location']['lat']
			longitude = data['results'][0]['geometry']['location']['lng']
			formatted_address = data['results'][0]['formatted_address']
		else:
			latitude = "No input given"
			longitude = "No input given"
			formatted_address = "No input given"
		return render_template("result.html",result = formatted_address,Latitude=latitude,longitude=longitude)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
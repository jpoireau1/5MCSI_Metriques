from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("index.html")

@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def mongraphique2887393():
    return render_template("graphique2.html")

@app.route("/commits/")
def mongraphique2():
    return render_template("nbCommits.html")

@app.route('/commitAPI/')
def commits():
    response = urlopen('https://api.github.com/repos/jpoireau1/5MCSI_Metriques/commits')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for commit in json_content:
        author = commit.get('commit', {}).get('author', {}) # sha = commit.get('sha')
        date_commit = author.get('date')
        # results.append({'sha': sha, 'date': date_commit})
        results.append({'date': date_commit})
    return jsonify(results=results)

@app.route('/paris2/')
def meteo2():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
        # results.append({'temp': temp_day_value})
    return jsonify(results=results)

# chemin vers exercice 3 envoyé par mail pour remplacer l'API météo qui fontionne plus
@app.route("/newRapport/")
def mongraphique222():
    return render_template("graphiqueNewAPI.html")
  
if __name__ == "__main__":
  app.run(debug=True)

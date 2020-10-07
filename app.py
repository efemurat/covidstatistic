from flask import Flask, render_template, request
import json
from urllib.request import urlopen
import requests

app = Flask(__name__)
headers = {'content-type': 'application/json'}
url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json'
#filename = requests.post(url, data=json.dumps(dict(mynum=123)), headers=headers)
filename = "indir.json"


@app.route('/', methods=['GET'])
def index():
    return(render_template('home.html'))

@app.route("/" , methods=['POST'])


def result():
    country1 = request.form['country']
    casesCountry1 = getCases(country1)
    deathsCountry1 = getDeaths(country1)
    dateLabels = getDates()
    return(render_template('home.html', country1=country1, casesCountry1=casesCountry1, deathsCountry1=deathsCountry1, dateLabels=dateLabels  ))

def getCases(country):
    with open(filename, 'r') as json_file:
        jsonData = json.load(json_file)
        caseList = []
        for record in jsonData['records']:
            if record['countriesAndTerritories'] == country:
                caseList.append(int(record['cases']))
    return(list(reversed(caseList)))

def getDates():
    with open(filename, 'r') as json_file:
        jsonData = json.load(json_file)
        dateList = []
        for record in jsonData['records']:
            if record['countryterritoryCode'] == 'ZMB':
                dateList.append(record['dateRep'])
    return(list(reversed(dateList)))

def getDeaths(country):
    with open(filename, 'r') as json_file:
        jsonData = json.load(json_file)
        deathList = []
        for record in jsonData['records']:
            if record['countriesAndTerritories'] == country:
                deathList.append(int(record['deaths']))
    return(list(reversed(deathList)))



if __name__ == '__main__':
    app.run(debug=True)
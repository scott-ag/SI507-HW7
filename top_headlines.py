import requests
import secrets
from flask import Flask, render_template

nyt = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
params = {'api-key':secrets.API_KEY}
nytResponse = requests.get(nyt, params)
nytJson = nytResponse.json()

titles = []

for i in range(5):
    titles.append(nytJson['results'][i]['title'])

app = Flask(__name__)
@app.route('/')
def welcome():
    return '<h1>Welcome. :)</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    return render_template('headlines.html', name=nm, headlines=titles)

if __name__ == '__main__':
    app.run(debug=True)


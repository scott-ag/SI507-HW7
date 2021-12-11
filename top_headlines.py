import requests
import secret
from flask import Flask, render_template


def get_articles():
    nyt = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key':secret.API_KEY}
    nytResponse = requests.get(nyt, params).json()['results']
    articles = nytResponse[:5]
#    for i in range(5):
#        titles.append(nytResponse['results'][i]['title'])
#    return titles
    return articles


app = Flask(__name__)
@app.route('/')
def welcome():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    articles = get_articles()
    articles = [a['title'] for a in articles]
    return render_template('headlines.html', name=nm, headlines=articles)

@app.route('/links/<nm>')
def link(nm):
    articles = get_articles()
    headlines = [a['title'] for a in articles]
    links = [a['url'] for a in articles]
    return render_template('links.html', name=nm, headlines=headlines, links=links)

@app.route('/tables/<nm>')
def table(nm):
    articles = get_articles()
    headlines = [a['title'] for a in articles]
    links = [a['url'] for a in articles]
    images = [a['multimedia'][0]['url'] for a in articles]
    return render_template('tables.html', name=nm, headlines=headlines, links=links, images=images)


if __name__ == '__main__':
    app.run(debug=True)


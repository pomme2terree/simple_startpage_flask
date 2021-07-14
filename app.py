import os, time
import database
from flask import *

app = Flask(__name__)
app.secret_key = database.generate_string(16)

# Value Config
username = 'Takeus'
background = 'alphacoders_background_by_mimosa.jpg' # static/background/ (if you want no backgroud, leave empty)

@app.route('/')
def index():
    return render_template('index.html', title=username, links=database.return_links(), background=url_for('static',filename='background/'+str(background)))

@app.route('/<string:link>',methods=['post', 'get'])
def redirect_link(link):
    return redirect("https://google.com/search?q="+link)

@app.route('/url/<string:url>')
def redirect_url(url):
    return redirect("http://"+url)

@app.route('/redirect',methods=['post', 'get'])
def redirect_search():
    if request.method == 'POST':
        return redirect("https://google.com/search?q="+str(request.form['input-search']))
    return redirect(url_for('index'))

    

# Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=19500, debug=True)
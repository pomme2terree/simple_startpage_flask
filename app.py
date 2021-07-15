import os
from flask import *

app = Flask(__name__)
app.secret_key = os.urandom(16)


# Info Config
title = 'StartPage'
logo = True
logo_text = 'My StartPage' # Str (IF logo=False)
logo_img = 'logo_flaticon_freepik.png' # in static/background/ (IF logo=True)

# Backgrounds Config
background = False
background_color = '#95a5a6' # Hex (IF Background=False)
background_img = 'alphacoders_background_by_mimosa.jpg' # in static/background/ (IF background=True)


@app.route('/')
def index():
    return render_template('index.html',title=title, logo=logo,logo_text=logo_text,logo_img=url_for('static',filename='/'+str(logo_img)),background=background,background_color=background_color,background_img=url_for('static',filename='background/'+str(background_img)))

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
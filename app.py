import os
from flask import *

app = Flask(__name__)
app.secret_key = os.urandom(16)


# Info Config
title = 'StartPage'
search_engine = 5 #1:google #2:DuckDuckGo #3:Yandex
logo_text = 'My StartPage' # (IF logo=False)
logo_img = 'logo_flaticon_freepik.png' # in static/background/ (IF logo=True)

# Module Config
logo = True
time = True
links = True

# Backgrounds Config
background = True
background_color = '#95a5a6' # Hex (IF Background=False)
background_img = 'alphacoders_background_by_mimosa.jpg' # in static/background/ (IF background=True)

# Links
link_01 = ['Steam','https://store.steampowered.com','steam.png'] #1:URL #2:IMG (static/link_img)
link_02 = ['Youtube','https://youtube.com/','youtube.png'] #1:NAME #2:URL #3:IMG (static/link_img)
link_03 = ['Discord','https://discord.com','discord.png'] #1:NAME #2:URL #3:IMG (static/link_img)
link_04 = ['Deepl','https://deepl.com','deepl.png'] #1:NAME #2:URL #3:IMG (static/link_img)


@app.route('/')
def index():
    return render_template('index.html',title=title, logo=logo,logo_text=logo_text,logo_img=url_for('static',filename='/'+str(logo_img)),
    background=background,background_color=background_color,background_img=url_for('static',filename='background/'+str(background_img)),
    link_01_img=url_for('static',filename='/link_img/'+str(link_01[2])),link_02_img=url_for('static',filename='/link_img/'+str(link_02[2])),link_03_img=url_for('static',filename='/link_img/'+str(link_03[2])),link_04_img=url_for('static',filename='/link_img/'+str(link_04[2])),links=links,time=time,
    link_01=link_01[1],link_02=link_02[1],link_03=link_03[1],link_04=link_04[1],link_01_name=link_01[0],link_02_name=link_02[0],link_03_name=link_03[0],link_04_name=link_04[0],search_engine=search_engine,
    )

@app.route('/<string:link>',methods=['post', 'get'])
def redirect_link(link):
    if search_engine == 1:
        return redirect("https://google.com/search?q="+link)
    elif search_engine == 2:
        return redirect("https://duckduckgo.com/?q="+link)
    else:
        return redirect("https://yandex.com/search/?text="+link)


@app.route('/url/<string:url>')
def redirect_url(url):
    return redirect("http://"+url)

@app.route('/redirect',methods=['post', 'get'])
def redirect_search():
    if request.method == 'POST':
        if search_engine == 1:
            return redirect("https://google.com/search?q="+str(request.form['input-search']))
        elif search_engine == 2:
            return redirect("https://duckduckgo.com/?q="+str(request.form['input-search']))
        else:
            return redirect("https://yandex.com/search/?text="+str(request.form['input-search']))
    return redirect(url_for('index'))

    

# Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=19500, debug=True)
# simple_startpage_flask
A simple StartPage write in Python &amp; Flask


## Installation

```bash
pip install flask
py app.py
```

## Configuration
Edit app.py

```python
# Info Config
title = 'StartPage'
search_engine = 1 #1:google #2:DuckDuckGo #3:Yandex
logo_text = 'My StartPage' # (IF logo=False)
logo_img = 'logo_flaticon_freepik.png' # in static/background/ (IF logo=True)

# Module Config
logo = True
time = True
links = True

# Backgrounds Config
background = False
background_color = '#95a5a6' # Hex (IF Background=False)
background_img = 'alphacoders_background_by_mimosa.jpg' # in static/background/ (IF background=True)

# Links
link_01 = ['Steam','https://store.steampowered.com','steam.png'] #1:URL #2:IMG (static/link_img)
link_02 = ['Youtube','https://youtube.com/','youtube.png'] #1:NAME #2:URL #3:IMG (static/link_img)
link_03 = ['Discord','https://discord.com','discord.png'] #1:NAME #2:URL #3:IMG (static/link_img)
link_04 = ['Deepl','https://deepl.com','deepl.png'] #1:NAME #2:URL #3:IMG (static/link_img)

```


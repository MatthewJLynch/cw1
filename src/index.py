import os
from flask import Flask, url_for, render_template, json, redirect
app = Flask(__name__)

#The Homepage Route
@app.route("/")
def index():
  return render_template('index.html', title='Home')

#Featured Page
@app.route('/featured')
def featured():
  return render_template('featured.html', title='Featured Drinks', featured=featured)
  
#Drinks Page
@app.route('/drinks')
def drinks():
  return render_template('drinks.html', title='Drinks', drinks=drinks)

#About Page
@app.route('/about')
def about():
  return render_template('about.html', title='About', about=about)


#Catalogue Pages
#Tea Catalogue Page
@app.route('/drinks/tea')
def tea_catalogue():
  return render_template('tea-catalogue.html', title='Tea', tea_catalogue=tea_catalogue)

#Under 200 Cal Catalogue Page
@app.route('/drinks/under200cal')
def under200cal_catalogue():
  return render_template('under200cal-catalogue.html', title='Under 200 Cal', under200cal_catalogue=under200cal_catalogue)
 
#Seasonal Catalogue Page
@app.route('/drinks/seasonal')
def seasonal_catalogue():
  return render_template('seasonal-catalogue.html', title='Seasonal', seasonal_catalogue=seasonal_catalogue)


#Coffee Pages
#Americano Page
@app.route('/drinks/americano')
@app.route('/drinks/under200cal/americano')
def americano():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  americano = json.load(open(json_url))
  return render_template('americano.html', title='Americano', americano=americano)
  
#Caffe Latte Page
@app.route('/drinks/caffe-latte')
@app.route('/drinks/under200cal/caffe-latte')
def caffe_latte():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  caffe_latte = json.load(open(json_url))
  return render_template('caffe-latte.html', title='Caffe Latte', caffe_latte=caffe_latte)
  
#Cappuccino Page
@app.route('/drinks/cappuccino')
@app.route('/drinks/under200cal/cappuccino')
def cappuccino():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  cappuccino = json.load(open(json_url))
  return render_template('cappuccino.html', title='Cappuccino', cappuccino=cappuccino)

#Caramel Macchiato Page
@app.route('/drinks/caramel-macchiato')
def caramel_macchiato():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  caramel_macchiato = json.load(open(json_url))
  return render_template('caramel-macchiato.html', title='Caramel Macchiato', caramel_macchiato=caramel_macchiato)

#Cortado Page
@app.route('/drinks/cortado')
@app.route('/drinks/under200cal/cortado')
def cortado():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  cortado = json.load(open(json_url))
  return render_template('cortado.html', title='Cortado', cortado=cortado)
  
#Espresso Page
@app.route('/drinks/espresso')
@app.route('/drinks/under200cal/espresso')
def espresso():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  espresso = json.load(open(json_url))
  return render_template('espresso.html', title='Espresso', espresso=espresso)
  
#Espresso Macchiato Page
@app.route('/drinks/espresso-macchiato')
@app.route('/drinks/under200cal/espresso-macchiato')
def espresso_macchiato():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  espresso_macchiato = json.load(open(json_url))
  return render_template('espresso-macchiato.html', title='Espresso Macchiato', espresso_macchiato=espresso_macchiato)
  
#Flat White Page
@app.route('/drinks/flat-white')
def flat_white():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  flat_white = json.load(open(json_url))
  return render_template('flat-white.html', title='Flat White', flat_white=flat_white)
  
#Gingerbread Latte Page
@app.route('/drinks/gingerbread-latte')
@app.route('/drinks/seasonal/gingerbread-latte')
def gingerbread_latte():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  gingerbread_latte = json.load(open(json_url))
  return render_template('gingerbread-latte.html', title='Gingerbread Latte', gingerbread_latte=gingerbread_latte)
  
#Pumpkin Latte Page
@app.route('/drinks/pumpkin-latte')
@app.route('/drinks/seasonal/pumpkin-latte')
def pumpkin_latte():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  pumpkin_latte = json.load(open(json_url))
  return render_template('pumpkin-latte.html', title='Pumpkin Latte', pumpkin_latte=pumpkin_latte)
  
#Earl Grey Page
@app.route('/drinks/earl-grey')
@app.route('/drinks/tea/earl-grey')
@app.route('/drinks/under200cal/earl-grey')
def earl_grey():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  earl_grey = json.load(open(json_url))
  return render_template('earl-grey.html', title='Earl Grey', earl_grey=earl_grey)
  
#English Breakfast Tea Page
@app.route('/drinks/breakfast-tea')
@app.route('/drinks/tea/breakfast-tea')
@app.route('/drinks/under200cal/breakfast-tea')
def breakfast_tea():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "coffee-information.json")
  breakfast_tea = json.load(open(json_url))
  return render_template('breakfast-tea.html', title='Breakfast Tea', breakfast_tea=breakfast_tea)
  

#404 Page
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', title='Error'), 404
  return

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, url_for, render_template
app = Flask(__name__)

#The Homepage Route
@app.route("/")
def index():
  return render_template('index.html', title='Home')

#Coffee Page
@app.route('/coffee')
def coffee():
  return render_template('coffee.html', title='Coffee', coffee=coffee)

#404 Page
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', title='Page Not Found',
  page_not_found=page_not_found)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

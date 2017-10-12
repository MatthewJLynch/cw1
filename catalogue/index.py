from flask import Flask, url_for, render_template
app = Flask(__name__)

#The Homepage Route
@app.route("/")
def index():
  return render_template('base.html', title='Home')

#Berlin Page
@app.route('/berlin')
def berlin():
  return render_template('berlin.html', title='Berlin', berlin=berlin)

#404 Page
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', title='Page Not Found',
  page_not_found=page_not_found)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

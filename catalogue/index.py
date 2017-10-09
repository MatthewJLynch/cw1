from flask import Flask, url_for, render_template
app = Flask(__name__)

#The Homepage Route
@app.route("/")
def index():
  return render_template('index.html', title='Home')

#Berlin Page
@app.route('/berlin')
def berlin():
  return render_template('berlin.html', title='Berlin', berlin=berlin)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
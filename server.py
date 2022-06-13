from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=["GET", "POST"])
def index():
   return render_template("index.html")

@app.route('/result', methods=["GET", "POST"])
def results(): 
   if request.method == "POST":  
      session['name'] = request.form.get('name')
      session['location'] = request.form.get('city')
      session['language'] = request.form.get('lang')
      session['comment'] = request.form.get('comment')
      return render_template("result.html")


if __name__ == "__main__":
   app.run(debug=True)
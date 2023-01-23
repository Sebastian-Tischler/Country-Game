from flask import Flask, render_template, request, redirect, url_for
import random
from laender import countries

app = Flask(__name__)


# Initialize highscore
highscore = 0

@app.route("/")
def index():
    global highscore
    # Choose two random countries
    country1, country2 = random.sample(countries.items(), 2)
    return render_template("index.html", country1=country1[0], country2=country2[0])

@app.route("/check", methods=["POST"])
def check():
    global highscore
    # Get user's guess
    if "guess" in request.form:
        guess = request.form["guess"]
    else:
        return redirect(url_for("index", error="Please select an answer"))
    country1, country2 = random.sample(countries.items(), 2)
    # Check if guess is correct
    if (guess == "y" and country1[1] > country2[1]):
        highscore += 1
        new_country = random.choice(list(countries.items()))
        return redirect(url_for("index", country1=country1[0], country2=new_country[0]))
    elif (guess == "n" and country1[1] < country2[1]):
        highscore += 1
        return redirect(url_for("index", country1=country1[0], country2=country2[0]))
    else:
        return render_template("incorrect.html", highscore=highscore, answer="yes" if country1[1] > country2[1] else "no")

if __name__ == "__main__":
    app.run()




from flask import Flask, render_template, request, redirect, url_for
from search import custom_search
import format_results

app = Flask(__name__, template_folder='./templates')
NAME = "MooVieGo"


@app.route("/", methods=['GET'])
def home():
    # return render_template('test.html')
    return render_template('home.html')


@app.route('/search')
def search():
    term = request.args.get("term").replace(" ", "+")
    if term:
        return redirect("/search/{}".format(term))
    else:
        return redirect("/search/invalid")


@app.route("/search/<term>")
def search_term(term):
    res = custom_search(term)
    # print(len(res['items']))
    formatted = "<h2>Search results for '{}'</h2>".format(term.replace("+", " "))

    format_results.copy_template()
    format_results.copy_results(res['items'])

    return render_template("results.html")


@app.route("/search/invalid")
def invalid():
    return render_template("invalid.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)

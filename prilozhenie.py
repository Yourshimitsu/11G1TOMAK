from flask import *
from init import app

@app.route('/')
def first_page():
    return render_template("main.html")

@app.route('/catalog')
def catalog_page():
    return render_template("catalog.html")

@app.route('/card1')
def island_spa_page1():
    return render_template("card1.html")

@app.route('/card2')
def island_spa_page2():
    return render_template("card2.html")

@app.route('/card3')
def island_spa_page3():
    return render_template("card3.html")

@app.route('/about')
def island_spa_page4():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
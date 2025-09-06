from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {'title': 'Forrest Gump'},
    {'title': 'Lord of the Rings'},
    {'title': 'Forrest GumpMatrix'},
    {'title': 'Blade Runner'}
    ]

@app.route('/')
def homepage():
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
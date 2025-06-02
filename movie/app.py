from flask import Flask, render_template

app = Flask(__name__)

# Кино маалыматтары
movies = [
    {"title": "Inception", "year": 2010, "director": "Christopher Nolan"},
    {"title": "The Matrix", "year": 1999, "director": "The Wachowskis"},
    {"title": "Interstellar", "year": 2014, "director": "Christopher Nolan"}
]

# Актёр маалыматтары
actors = [
    {"name": "Leonardo DiCaprio", "movie": "Inception"},
    {"name": "Keanu Reeves", "movie": "The Matrix"},
    {"name": "Matthew McConaughey", "movie": "Interstellar"}
]

@app.route('/')
def index():
    return render_template("index.html", movies=movies, actors=actors)

if __name__ == '__main__':
    app.run(debug=True)

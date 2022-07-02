from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Benny',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 1, 2022'
    },
    {
        'author': 'ChickenBenny',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 1, 2022'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def aoubt():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)
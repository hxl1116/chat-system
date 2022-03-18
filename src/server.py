from flask import render_template

from src import create_app, db
from . import *

nav_links = [
    {'href': '/communities', 'name': 'communities'},
    {'href': '/channels', 'name': 'channels'},
    {'href': '/members', 'name': 'members'}
]

app = create_app()


@app.route('/')
def home():
    return render_template('home.html', nav=nav_links)


def main():
    db.init_app(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()

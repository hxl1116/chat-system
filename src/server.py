from flask import Flask, render_template
from flask_restful import Api

from api.channel import Channel
from api.community import Community
from api.member import Member
from db.utils import init_db

app = Flask(__name__)
api = Api(app)

cfg = {
    'debug': True,
    'port': 5000
}

nav_links = [
    {'href': '/communities', 'name': 'communities'},
    {'href': '/channels', 'name': 'channels'},
    {'href': '/members', 'name': 'members'}
]


@app.route('/')
def home():
    return render_template('home.html', nav=nav_links)


def init():
    init_db()

    api.add_resource(Community, '/communities')
    api.add_resource(Channel, '/channels', '/channels/<string:id>')
    api.add_resource(Member, '/members')


def main():
    init()

    app.run(**cfg)


if __name__ == '__main__':
    main()

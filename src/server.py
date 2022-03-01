from flask import Flask, render_template
from flask_restful import Api

from src.api.channel import Channel
from src.api.community import Community
from src.api.member import Member

app = Flask(__name__)
api = Api(app)

cfg = {
    'debug': True,
    'port': 62899
}

nav_links = [
    {'href': '/community', 'name': 'community'},
    {'href': '/channel', 'name': 'channel'},
    {'href': '/member', 'name': 'member'}
]


@app.route('/')
def home():
    return render_template('home.html', nav=nav_links)


def init():
    api.add_resource(Community, '/community')
    api.add_resource(Channel, '/channel', '/channel/<string:id>')
    api.add_resource(Member, '/member')


def main():
    init()

    app.run(**cfg)


if __name__ == '__main__':
    main()

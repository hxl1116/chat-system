from flask import Flask, render_template
from flask_restful import Api

from api.auth import SignUp, Login, Logout
from api.channel import Channel, ChannelList
from api.community import Community
from api.member import Member, MemberList

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
    api.add_resource(Community, '/communities')

    api.add_resource(ChannelList, '/channels')
    api.add_resource(Channel, '/channels/<string:channel_id>')

    api.add_resource(MemberList, '/members')
    api.add_resource(Member, '/members/<string:member_id>')

    api.add_resource(SignUp, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')


def main():
    init()

    app.run(**cfg)


if __name__ == '__main__':
    main()

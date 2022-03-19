from flask import render_template, Flask
from flask_restful import Api

from api.auth import SignUp, Login, Logout
from api.channel import ChannelList, Channel
from api.community import Community
from api.member import MemberList, Member
from db.utils import init_db

nav_links = [
    {'href': '/communities', 'name': 'communities'},
    {'href': '/channels', 'name': 'channels'},
    {'href': '/members', 'name': 'members'},
    {'href': '/signup', 'name': 'signup'},
    {'href': '/login', 'name': 'login'},
    {'href': '/logout', 'name': 'logout'}
]

DB_CFG = '../config/db.yml'
APP_CFG = '../config/app.yml'

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('home.html', nav=nav_links)


def init_app():
    api.add_resource(ChannelList, '/channels')
    api.add_resource(Channel, '/channels/<string:channel_id>')

    api.add_resource(Community, '/communities')

    api.add_resource(MemberList, '/members')
    api.add_resource(Member, '/members/<string:member_id>')

    api.add_resource(SignUp, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')


def main():
    init_db()
    init_app()

    app.run(debug=True)


if __name__ == '__main__':
    main()

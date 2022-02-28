from flask import Flask
from flask_restful import Api

from src.api.member import Member

app = Flask(__name__)
api = Api(app)

cfg = {
    'debug': True,
    'port': 62899
}


def init():
    api.add_resource(Member, '/')


def main():
    init()

    app.run(**cfg)


if __name__ == '__main__':
    main()

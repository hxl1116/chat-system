import os

from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from api.member import MemberList, Member
from src.api.channel import ChannelList, Channel
from src.api.community import Community

DB_CFG = '../config/db.yml'
APP_CFG = '../config/app.yml'

db = SQLAlchemy()


def get_config(path):
    from yaml import FullLoader, load

    yml_path = os.path.join(os.path.dirname(__file__), path)

    with open(yml_path, 'r') as file:
        cfg = load(file, Loader=FullLoader)

    return cfg


def get_db_uri(db_cfg, app_cfg):
    db_uri = app_cfg['db_uri'] \
        .replace('<user>', db_cfg['user']) \
        .replace('<pass>', db_cfg['pass']) \
        .replace('<host>', db_cfg['host']) \
        .replace('<port>', str(db_cfg['port'])) \
        .replace('<dbname>', db_cfg['database'])

    return db_uri


def create_app():
    app, db_cfg, app_cfg = Flask(__name__), get_config(DB_CFG), get_config(APP_CFG)

    app.config['SECRET_KEY'] = app_cfg['secret_key']
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri(db_cfg, app_cfg)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    auth_bp = Blueprint('auth', __name__)
    auth_api = Api(auth_bp)

    # TODO: Add auth resources to auth_api

    main_bp = Blueprint('main', __name__)
    main_api = Api(main_bp)

    # TODO: Add main resources to main_bp
    main_api.add_resource(ChannelList, '/channels')
    main_api.add_resource(Channel, '/channels/<string:chan_id>')

    main_api.add_resource(Community, '/communities')

    main_api.add_resource(MemberList, '/members')
    main_api.add_resource(Member, '/members/<string:member_id>')

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

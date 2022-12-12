import os

from flask import Flask
from flask import jsonify
from pylogix import PLC
from PLC_Data.auth import login_required

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from PLC_Data import db
    db.init_app(app)

    from PLC_Data import auth
    app.register_blueprint(auth.bp)

    from PLC_Data import plcdata
    app.register_blueprint(plcdata.bp)

    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/plcdata', endpoint='plcdata')
    @app.route('/')
    def index():
        return "<p>Log In to connect to your PLC</p> " \
               "<li><a href=auth/login>Log In</a>"
    @app.route('/plcdata')
    @login_required
    def plcdata():
        return "Enter the following in the address bar to get plc data" \
               "<li>/pylogix/v1.0/plc/'your plc address'/'your processor slot'/tags" \
                "<li> For example http://127.0.0.1:5000/pylogix/v1.0/plc/192.168.1.20/0/tags"

    @app.route('/pylogix/v1.0/plc/<ipAddress>/<int:slot>/tags', methods=['GET'])
    @login_required
    def get_all_tags(ipAddress, slot):
        tags = []

        comm = PLC(ipAddress, slot)
        ret = comm.GetTagList()
        comm.Close()

        if ret.Value is None:
            return jsonify(ret.Status)

        for tag in ret.Value:
            tags.append(
                {"tagName": tag.TagName,
                 "dataType": tag.DataType
                 })

        return jsonify({'tags': tags})


    return app




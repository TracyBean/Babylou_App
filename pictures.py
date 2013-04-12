import flask, flask.views
import os
import utils

class Pictures(flask.views.MethodView):
    @utils.login_required
    def get(self):
        songs = os.listdir('static/pictures')
        return flask.render_template("pictures.html")
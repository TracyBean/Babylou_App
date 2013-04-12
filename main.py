import flask, flask.views
import os

class Main(flask.views.MethodView):
    def get(self, page="index"):
    	page += ".html"
    	if os.path.isfile('templates/' + page):
    		return flask.render_template(page)
    	flask.abort(404)


 port = int(os.environ.get('PORT', 5000))
 app.run(host='0.0.0.0', port=port)

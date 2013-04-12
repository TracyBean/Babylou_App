import flask 
import settings

# Views
from main import Main
from login import Login
from remote import Remote
from music import Music
from pictures import Pictures




app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=['GET', 'POST'])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])
app.add_url_rule('/pictures/',
                 view_func=Pictures.as_view('pictures'),
                 methods=['GET'])





@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

app.debug = True
app.run()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
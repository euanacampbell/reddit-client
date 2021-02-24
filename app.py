from flask import Flask, render_template, redirect
from mod.reddit import reddit

app = Flask(__name__)
redt = reddit()

@app.route('/home')
def home():

    posts=redt.get_workspaces()

    posts=posts + posts
    return render_template('index.html', posts=posts)
    # return render_template('index.html')

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

    return(division_by_zero)

@app.errorhandler(404)
def page_not_found(e):

    return redirect("http://127.0.0.1:5000/home", code=302)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
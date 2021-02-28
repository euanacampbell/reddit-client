from flask import Flask, render_template, redirect, url_for, request
from mod.reddit import reddit


app = Flask(__name__)

reddit = reddit()

@app.route('/')
def home():
    return redirect(url_for('popular'))

@app.route('/popular')
def popular():
    default='popular'
    posts=reddit.get_subreddit(default)
    return render_template('index.html', posts=posts, subreddit=default)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.data:
        return redirect(url_for('popular'))
    else:
        return render_template('login.html')

    return render_template('login.html')

@app.route('/r/<subreddit>')
def subreddit(subreddit):

    posts=reddit.get_subreddit(subreddit)

    return render_template('index.html', posts=posts)

@app.route('/r/<subreddit>/<post_id>')
def post(subreddit, post_id):


    post = reddit.get_post_data(post_id)
    comments = reddit.get_comments(post_id)
    return render_template('post.html', post=post, comments=comments)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

    return(division_by_zero)

@app.errorhandler(404)
def page_not_found(e):

    return redirect(url_for('popular'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
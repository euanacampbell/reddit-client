from flask import Flask, render_template, redirect, url_for
from mod.reddit import reddit

app = Flask(__name__)
reddit = reddit()

@app.route('/home')
def home():

    posts=[]
    return render_template('index.html', posts=posts)

@app.route('/<subreddit>')
def subreddit(subreddit):

    posts=reddit.get_subreddit(subreddit)

    posts=posts + posts
    return render_template('index.html', posts=posts)

@app.route('/<subreddit>/<postid>')
def post(subreddit, postid):


    post = reddit.get_post_data(postid)
    return render_template('post.html', post=post)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

    return(division_by_zero)

@app.errorhandler(404)
def page_not_found(e):

    return redirect(url_for('home'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
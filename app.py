from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/home')
def home():

    posts = [
        {
            'id': '1234',
            'title': 'New WFH space',
            'text': 'It is not much but it is mine, after several months of saving',
            'comments': '15',
            'upvotes': '117',
            'subreddit': 'workspaces'
        },
        {
            'id': '1234',
            'title': 'My new battlestation',
            'text': 'I Love PC gaming soo much',
            'comments': '35',
            'upvotes': '1.2K',
            'subreddit': 'pcmasterrace'
        },
        {
            'id': '1234',
            'title': 'Carving of a penguin',
            'text': 'Only took a few hours',
            'comments': '2',
            'upvotes': '78',
            'subreddit': 'woodworking'
        }
    ]

    posts=posts + posts
    return render_template('index.html', posts=posts)
    # return render_template('index.html')

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

    return(division_by_zero)
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
"""will call the api"""
import requests
import os


class reddit_api():

    def __init__(self):

        self.base="https://oauth.reddit.com/"
        # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'

        auth = requests.auth.HTTPBasicAuth(os.environ.get('auth1'), os.environ.get('auth2'))

        # here we pass our login method (password), username, and password
        data = {'grant_type': 'password',
                'username': os.environ.get('username'),
                'password': os.environ.get('password')}

        # setup our header info, which gives reddit a brief description of our app
        headers = {'User-Agent': 'MyBot/0.0.1'}

        # send our request for an OAuth token
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)

        # convert response to JSON and pull access_token value
        TOKEN = res.json()['access_token']

        # add authorization to our headers dictionary
        self.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    
    def get_details_about_me(self):
        # while the token is valid (~2 hours) we just add headers=headers to our requests
        resp = requests.get(f'{self.base}api/v1/me', headers=self.headers)

        resp = resp.json()
        print(resp)
        
    
    def get_hot_posts_for_subreddit(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        if subreddit==None:
            return("")
        else:
            resp = requests.get(f'{self.base}/r/{subreddit}/hot',
                            headers=self.headers)
            resp = resp.json()
            return(resp)

    def get_trending_subreddits(self):
        """Returns a list of 5 trending subreddits"""
        res = requests.get('https://reddit.com/api/trending_subreddits.json',
                        headers=self.headers)
        res = res.json()
        print(res['subreddit_names'])

    def get_subreddit_about(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        if subreddit==None:
            return("")
        else:
            resp = requests.get(f'{self.base}/r/{subreddit}/about',
                            headers=self.headers)
            resp = resp.json()
            return(resp)
    
    def get_my_home(self):
        
        resp = requests.get('http://www.reddit.com/.json', headers = {'User-agent': 'your bot 0.1'})
        resp = resp.json()
        return(resp)

    def get_comments(self, subreddit, name):
        resp = requests.get(f'{self.base}/r/{subreddit}/comments/{name}',
                            headers=self.headers)
        resp = resp.json()
        return(resp)

if __name__=="__main__":
    api = reddit_api()
    print('')
    response = api.get_comments('pcmasterrace', 'lr5t9v')

    print(response)








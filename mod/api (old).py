"""will call the api"""
import requests
import os


class reddit_api():

    def __init__(self):

        self.base="https://oauth.reddit.com/"
        # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'

    def make_api_call(self, url):

        self.create_request_header()
        
        resp = requests.get(url, headers=self.headers)

        resp = resp.json()
        return(resp)
    
    def create_request_header(self):
        
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
        
        TOKEN = res.json()['access_token'] # convert response to JSON and pull access_token value
        self.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}} # add authorization to our headers dictionary

    
    def get_details_about_me(self):
        # while the token is valid (~2 hours) we just add headers=headers to our requests
        resp = self.make_api_call(f'{self.base}api/v1/me')

        print(resp)
        
    
    def get_hot_posts_for_subreddit(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        
        submissions = reddit.subreddit(subreddit).hot(limit=15)

        return(submissions)

    def get_trending_subreddits(self):
        """Returns a list of 5 trending subreddits"""
        res = self.make_api_call('https://reddit.com/api/trending_subreddits.json')

        print(res['subreddit_names'])

    def get_subreddit_about(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        if subreddit==None:
            return("")
        else:
            resp = self.make_api_call(f'{self.base}/r/{subreddit}/about')

            return(resp)
    
    def get_my_home(self):
        
        resp = requests.get('http://www.reddit.com/.json', headers = {'User-agent': 'your bot 0.1'})
        resp = resp.json()
        return(resp)

    def get_comments(self, subreddit, name):
        resp = self.make_api_call(f'{self.base}/r/{subreddit}/comments/{name}')

        return(resp)
    
    def get_post_details(self, name):
         
        url=f'https://www.reddit.com/comments/{name}.json'
        resp = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
        print(resp.status_code)
        print(url)
        resp = resp.json()
        print(resp)
        return(resp)

    

if __name__=="__main__":
    api = reddit_api()
    print('')
    response = api.get_comments('pcmasterrace', 'lr5t9v')

    print(response)








import os
import praw

class reddit_api():

    def __init__(self):
        # self.reddit = praw.Reddit(
        #     client_id=os.environ.get('auth1'),
        #     client_secret=os.environ.get('auth2'),
        #     user_agent="testscript for reddit",
        #     redirect_uri="http://localhost:8080",
        #     username=os.environ.get('username'),
        #     password=os.environ.get('password')
        # )

        print('creating instance')

        self.reddit = praw.Reddit(
            client_id='6CyqJ40yvWB6RA',
            client_secret='0T_s9kiT1KKEWwb_zCQUhpKTpvTdUA',
            user_agent="testscript for reddit",
            redirect_uri="http://localhost:8080",
            username='doctorrono',
            password='jadxa3-hYtcub-juxjaz'
        )
        
    
    def get_hot_posts_for_subreddit(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        response = self.reddit.subreddit(subreddit)
        
        return(response.hot(limit=30))


    def get_subreddit_about(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        
        response = self.reddit.subreddit(subreddit)

        return(response.description)

    def get_comments(self, name):

        submission = self.reddit.submission(id=name)

        return(submission.comments)
    
    def get_post_details(self, name):
         
        submission = self.reddit.submission(id=name)
        return(submission)  # to make it non-lazy
    
    def get_front_page(self):
        # page = self.reddit.redditor("doctorrono").submissions.hot()


        print(self.reddit.models.Front())

        # print(type(page))

        # return(page)

    

if __name__=="__main__":
    api = reddit_api()
    print('')
    response = api.get_post_details('ls7qih')

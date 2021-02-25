import os
import praw
from praw.models import MoreComments

class reddit_api():

    def __init__(self):

        self.reddit = praw.Reddit(
            client_id=os.environ.get('auth1'),
            client_secret=os.environ.get('auth2'),
            password=os.environ.get('password'),
            user_agent="testscript for reddit",
            redirect_uri="http://localhost:8080",
            username=os.environ.get('username'),
        )
        
    
    def get_hot_posts_for_subreddit(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        response = self.reddit.subreddit(subreddit)
        
        return(response.hot(limit=10))


    def get_subreddit_about(self, subreddit=None):
        """Returns dictionary hot posts for a particular subreddit"""
        
        response = self.reddit.subreddit(subreddit)

        return(response.description)

    def get_comments(self, name):
        comments=[]
        submission = self.reddit.submission(id=name)

        submission.comment_sort = 'best'
        submission.comment_limit = 15
        print(len(submission.comments))

        for top_level_comment in submission.comments:
            comment={}
            if isinstance(top_level_comment, MoreComments) or top_level_comment.stickied==True:
                continue
            comment['text']=top_level_comment.body
            comment['replies']=top_level_comment.replies
            try:
                comment['author']=top_level_comment.author.name
            except AttributeError:
                comment['author']=''

            comments.append(comment)

        return(comments)
    
    def get_post_details(self, name):
         
        submission = self.reddit.submission(id=name)
        return(submission)  # to make it non-lazy

    

if __name__=="__main__":
    api = reddit_api()
    print('')
    response = api.get_post_details('ls7qih')

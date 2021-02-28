"""Will call the api module and handle data coming back. Will be called by app.py"""
from mod.api import reddit_api
from linkpreview import link_preview
from praw.models import MoreComments

class reddit():

    def __init__(self):
        self.api = reddit_api()

    def get_frontpage(self):
        page = self.api.get_front_page()

        print(page)

    def get_comments(self, post_id):
        comments=[]
        submission_comments = self.api.get_comments(post_id)

        submission_comments.comment_sort = 'best'
        submission_comments.comment_limit = 15

        for top_level_comment in submission_comments:
            comment={}
            if isinstance(top_level_comment, MoreComments) or top_level_comment.stickied==True:
                continue
            comment['text']=top_level_comment.body
            comment['id']=top_level_comment.id
            if float(top_level_comment.score) > 999:
                number=float(top_level_comment.score)/1000
                comment['score']=str("{:.1f}".format(number)) + 'K'
            else:
                comment['score']=str(top_level_comment.score)

            comment['replies']=top_level_comment.replies
            try:
                comment['author']=top_level_comment.author.name
            except AttributeError:
                comment['author']=''

            comments.append(comment)

        return(comments)

    def get_dict_from_sub(self, submission):
        post={}
        post['title']=submission.title
        if len(submission.selftext) >= 300:
            post['text']=submission.selftext[0:300] + " ..."
        else:
            post['text']=submission.selftext
        post['text_full']=submission.selftext
        post['num_comments']="{:,}".format(submission.num_comments)
        if float(submission.score) > 999:
            number=float(submission.score)/1000
            post['upvotes']=str("{:.1f}".format(number)) + 'K'
        else:
            post['upvotes']=str(submission.score)
        post['upvote_ratio']=submission.upvote_ratio
        post['subreddit']=submission.subreddit
        post['name']=submission.id
        post['post_url']=f"/r/{submission.subreddit}/{submission.id}"
        post['author']=submission.author.name

        post['media_url']=submission.url

        if submission.url.endswith(('.jpg', '.png')):
            post['media']={
                'type': 'image',
                'media_url': submission.url
            }
        elif submission.url.startswith('https://www.reddit.com/r/'):
            post['media']={
                'type': 'none',
                'link_url': submission.url
            }
        else:
            post['media']={
                'type': 'link',
                'link_url': submission.url,
                'link_domain': submission.url.split('/')[2]
            }

        return(post)

    def get_subreddit(self, subreddit):
        posts = self.api.get_hot_posts_for_subreddit(subreddit)

        posts_formatted = []

        for post in posts:
            if post.stickied != True:
                posts_formatted.append(self.get_dict_from_sub(post))
         
        return(posts_formatted)
    
    def get_post_data(self, post_id):

        submission = self.api.get_post_details(post_id)

        post = self.get_dict_from_sub(submission)
        print(submission.url)
        return(post)


if __name__=="__main__":

    app = reddit()
    print('')
    response = app.get_post_data('lt7tnd')

    for i in response:
        print(f"{i}: {response[i]}")

"""Will call the api module and handle data coming back. Will be called by app.py"""
from mod.api import reddit_api


class reddit():

    def __init__(self):
        self.api = reddit_api()

    def get_homepage_content(self):
        pass

    def get_comments(self, post_id):
        return(self.api.get_comments(post_id))

    def get_dict_from_sub(self, submission):
        post={}
        post['title']=submission.title
        if len(submission.selftext) >= 300:
            post['text']=submission.selftext[0:300] + " ..."
        else:
            post['text']=submission.selftext
        post['text_full']=submission.selftext
        post['num_comments']="{:,}".format(submission.num_comments)
        post['upvotes']="{:,}".format(submission.score)
        post['subreddit']=submission.subreddit
        post['name']=submission.id
        post['post_url']=f"/r/{submission.subreddit}/{submission.id}"

        post['img_url']=submission.url

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
    response = app.get_comments('lrks0g')

    for i in response:
        print(i)

"""Will call the api module and handle data coming back. Will be called by app.py"""
from mod.api import reddit_api

class reddit():

    def __init__(self):
        self.api = reddit_api()

    def get_homepage_content(self):
        pass

    def get_comments(self):
        pass

    def get_subreddit(self, subreddit):
        to_return=[]
        posts = self.api.get_hot_posts_for_subreddit(subreddit)
        print(posts)

        try:
            print(posts['error'])
            return(to_return)
        except KeyError:
            pass

        for post in posts['data']['children']:
            if post['data']['pinned']==False:
                data = post['data']
                new_post={}
                new_post['title']=data['title']
                if len(data['selftext']) >= 300:
                    new_post['text']=data['selftext'][0:300] + " ..."
                else:
                    new_post['text']=data['selftext']
                new_post['text_full']=data['selftext']
                new_post['num_comments']="{:,}".format(data['num_comments'])
                new_post['upvotes']="{:,}".format(data['ups'])
                new_post['subreddit']=data['subreddit']
                new_post['name']=data['name']

                new_post['img_url']=data['url']             

                to_return.append(new_post)
        return(to_return)


if __name__=="__main__":
    app = reddit()
    print('')
    response = app.get_workspaces()

    # print(response)

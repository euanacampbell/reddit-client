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

        if len(posts)==0:
            return(to_return)

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
                new_post['name']=data['id']
                new_post['post_url']=f"/{data['subreddit']}/{data['id']}"

                new_post['img_url']=data['url']             

                to_return.append(new_post)
        return(to_return)
    
    def get_post_data(self, post_id):
        print("get post data")

        post={}
        data = self.api.get_post_details(post_id)[0]
        data = data['data']['children'][0]['data']
        print("DATA")
        print(data)

        post['title']=data['title']
        if len(data['selftext']) >= 300:
            post['text']=data['selftext'][0:300] + " ..."
        else:
            post['text']=data['selftext']
        post['text_full']=data['selftext']
        post['num_comments']="{:,}".format(data['num_comments'])
        post['upvotes']="{:,}".format(data['ups'])
        post['subreddit']=data['subreddit']
        post['name']=data['id']
        post['post_url']=f"/{data['subreddit']}/{data['name']}"

        post['img_url']=data['url']

        return(post)


if __name__=="__main__":
    app = reddit()
    print('')
    response = app.get_post_data('lrzhvb')

    print(response)

    # print(response)

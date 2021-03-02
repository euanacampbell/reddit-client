# Reddit Client

Reddit Client is a web-based Reddit viewer allowing you to search and view subreddits, including their posts and comments.

It utilises the Reddit API

## Installation

Install the appropriate Python packages.

```bash
pip3 install -r requirements.txt 
```
Environment variables are also needed for connecting to the Reddit API.

```bash
export auth1=<client id>
export auth2=<client secret>
export username=<reddit username>
export auth1=<reddit password>
```

## Usage
Project can be accessed at [reddit.euan.app](https://reddit.euan.app)

## Local Usage

```bash
export FLASK_APP=app

flask run
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

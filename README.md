# Comics publisher

A simple script that allows you to publish comics from [xkcd](https://xkcd.com/).

## Environment


### Requirements

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Environment variables

- VK_APP_TOKEN

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
VK_APP_TOKEN=vk1.a.VGIbB6RUQ...
```

#### How to get

Create a VK group with permissions to general info,
photo, wall, groups and access at any time. 

Create standalone app [here](https://vk.com/dev),
then find your `client_id` in the app info, and get your `access_token` [here](https://vk.com/dev/implicit_flow_user)
as `VK_APP_TOKEN`.

### How to install

Set your `version`, `group_id` and `access_token` in `post_comic_vk_group.py`

### Run

Launch on Linux(Python 3) or Windows:
```
python post_comic_vk_group.py
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
# Comics publisher

A simple script that allows you to publish comics from [xkcd](https://xkcd.com/).

### How to install

First of all you need to create a VK group with permissions to general info,
photo, wall, groups and access at any time. 

Create standalone app [here](https://vk.com/dev),
then find your `client_id` in the app info, then get your `access_token` [here](https://vk.com/dev/implicit_flow_user)
and store it in `.env` file as `VK_APP_TOKEN`.

Set your `version`, `group_id` and `access_token` in `post_comic_vk_group.py`

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

To post a comic run:
```
python post_comic_vk_group.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
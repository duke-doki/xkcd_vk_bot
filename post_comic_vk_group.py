import os
import random
import shutil
from pathlib import Path

import requests
from environs import Env

from download_image import download_image, fetch_file_extension


def get_server_url(access_token, version, group_id):
    vk_url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {'access_token': access_token, 'v': version, 'group_id': group_id}
    vk_response = requests.get(vk_url, params=params)
    vk_response.raise_for_status()
    upload_url = vk_response.json()['response']['upload_url']

    return upload_url


def save_comic_to_album(url, access_token, version,
                        group_id, comic_dir, extension):
    with open(f"{comic_dir}{extension}", 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
    response.raise_for_status()
    response_details = response.json()
    save_params = {
        'access_token': access_token,
        'hash': response_details['hash'],
        'photo': response_details['photo'],
        'server': response_details['server'],
        'v': version,
        'group_id': group_id
    }
    save_url = 'https://api.vk.com/method/photos.saveWallPhoto'
    save_response = requests.post(save_url, params=save_params)
    save_response.raise_for_status()
    save_details = save_response.json()['response'][0]

    return save_details


def publish_image(access_token, version, group_id,
                  save_details, author_comment):
    publish_params = {
        'access_token': access_token,
        'v': version,
        'owner_id': (-1) * group_id,
        'from_group': 1,
        'attachments': f"photo{save_details['owner_id']}_{save_details['id']}",
        'message': author_comment
    }
    publish_url = 'https://api.vk.com/method/wall.post'
    publish_response = requests.post(publish_url, params=publish_params)
    publish_response.raise_for_status()


def get_last_comic_num():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    end_num = response.json()['num']

    return end_num


def get_random_comic(end_num):
    comic_num = random.randint(1, end_num)
    url = f'https://xkcd.com/{comic_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    comic_details = {
        'image_url': response_json['img'],
        'author_comment': response_json['alt'],
        'comic_num': comic_num
    }

    return comic_details


if __name__ == '__main__':
    env = Env()
    env.read_env()
    access_token = env.str('VK_APP_TOKEN')
    version = 5.154
    group_id = env.int('GROUP_ID')
    Path('files').mkdir(exist_ok=True)
    try:
        end_num = get_last_comic_num()
        comic_details = get_random_comic(end_num)
        comic_dir = Path('files').joinpath(f"image{comic_details['comic_num']}")

        download_image(
            comic_details['image_url'],
            comic_dir
        )
        file_extension = fetch_file_extension(comic_details['image_url'])

        upload_url = get_server_url(
            access_token,
            version,
            group_id
        )

        save_details = save_comic_to_album(
            upload_url,
            access_token,
            version,
            group_id,
            comic_dir,
            file_extension
        )

        publish_image(
            access_token,
            version,
            group_id,
            save_details,
            comic_details['author_comment']
        )
    finally:
        shutil.rmtree('files')

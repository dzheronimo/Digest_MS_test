import requests as re
from rest_framework import status


class Post:
    def __init__(self, id, title, post, rating):
        self.post_id = id
        self.title = title
        self.post = post
        self.rating = rating


class Digest:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.digest_list: list = self.create_digest()

    def parse_users_subscriptions(self) -> dict:
        """Собирает подписки пользователя"""
        self.user_id = 1  ####
        subscriptions = re.get(f'http://127.0.0.1:8000/users/{self.user_id}/subscriptions/')
        if subscriptions.status_code is status.HTTP_200_OK:
            return subscriptions.json()
        else:
            return {}

    def parse_posts_from_subscriptions(self) -> list:
        """Собирает посты из подписок"""
        posts_to_filter = []
        subscriptions = self.parse_users_subscriptions()
        for source in subscriptions['subscriptions']:   # source - ID источника (имя используемое в эндпоинте)
            posts = re.get(f'http://127.0.0.1:8000/{source}/posts/')
            if posts.status_code is status.HTTP_200_OK:
                posts = posts.json().get('posts')
                for post in posts:
                    posts_to_filter.append(post)
        return posts_to_filter

    def filter_relevant_posts(self) -> list:
        """Фильтрует релевантные посты для текущего пользователя"""
        posts = self.parse_posts_from_subscriptions()
        to_digest = []
        for post in posts:
            if int(post.get('rating')) >= 4:
                to_digest.append(post)
        return to_digest

    def create_digest(self):
        """Создание дайджеста из отфильтрованных постов"""
        digest = []
        posts = self.filter_relevant_posts()
        for post in posts:
            post_id = int(post.get('id'))
            title = (post.get('title'))
            post_text = post.get('post')
            rating = int(post.get('rating'))
            post_instance = Post(post_id, title, post_text, rating)
            digest.append(post_instance)
        return digest

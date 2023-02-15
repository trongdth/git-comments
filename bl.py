# -*- coding: utf-8 -*-

import requests
import json
import pytz

from datetime import datetime
from models.pull_request import PullRequest
from models.comment import Comment

"""
curl \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/pulls
"""


def all_pull_requests(user_token, user_id, repos, created_at):
    prs = []

    headers = {'Authorization': 'Bearer {}'.format(user_token),
               'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get(
        "https://api.github.com/repos/{}/pulls".format(repos), headers=headers)
    if response.status_code != 200:
        raise Exception(
            "Sorry, cannot get pull request for repos {}".format(repos))

    list = json.loads(response.text)

    for dict in list:
        if dict['user']['login'] == user_id and datetime.strptime(dict['created_at'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc) >= created_at:
            pr = PullRequest(dict['url'], dict['id'],
                             dict['user']['login'], dict['created_at'])
            prs.append(pr)
    return prs


"""
curl \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews
"""


def all_comments(user_token, pull_request):
    comments = []
    headers = {'Authorization': 'Bearer {}'.format(user_token),
               'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get(
        "{}/reviews".format(pull_request.url), headers=headers)
    if response.status_code != 200:
        raise Exception(
            "Sorry, cannot get comments for pull request {}".format(pull_request.url))

    list = json.loads(response.text)
    for dict in list:
        if dict['user']['login'] != pull_request.login:
            comment = Comment(dict['id'], url=dict['html_url'],
                              reviewer=dict['user']['login'])
            comments.append(comment)
    return comments

# -*- coding: utf-8 -*-

class PullRequest(object):

    def __init__(self, url, html_url, id, login, created_at):
        self.url = url
        self.html_url = html_url
        self.id = id
        self.login = login
        self.created_at = created_at

    def __repr__(self):
        return 'PullRequest {}: {}({} - {})'.format(self.html_url, self.id, self.login, self.created_at)

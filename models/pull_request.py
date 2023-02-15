# -*- coding: utf-8 -*-

class PullRequest(object):

    def __init__(self, url, id, login, created_at):
        self.url = url
        self.id = id
        self.login = login
        self.created_at = created_at

    def __repr__(self):
        return 'PullRequest {}: {}({} - {})'.format(self.url, self.id, self.login, self.created_at)

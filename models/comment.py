# -*- coding: utf-8 -*-
class Comment(object):

    def __init__(self, id, url, reviewer):
        self.id = id
        self.url = url
        self.reviewer = reviewer

    def __repr__(self):
        return 'Comment {}: {}({})'.format(self.url, self.id, self.reviewer)

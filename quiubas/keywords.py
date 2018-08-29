from .base import base


class keywords(base):

    def __init__(self, quiubas):
        base.__init__(self, quiubas)
        self.base_name = 'keywords'
        self.action_name = 'keyword/{id}'

    def create(self, params):
        return self.action(params)

    def getResponses(self, id, params=None):
        return self.quiubas.network.get([self.action_name + '/responses', {'id': id}], params)

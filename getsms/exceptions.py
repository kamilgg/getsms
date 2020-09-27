class APIError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class ServiceAccountError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

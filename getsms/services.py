from getsms.types import SMSService

SMSHUB_API_URL = "https://smshub.org/stubs/handler_api.php"
FIVESIM_API_URL = "http://api1.5sim.net/stubs/handler_api.php"
SMSACTIVATE_API_URL = "https://sms-activate.ru/stubs/handler_api.php"


class SMSHub(SMSService):
    def __init__(self, token):
        self.api_url = SMSHUB_API_URL
        self.token = token


class FiveSim(SMSService):
    def __init__(self, token):
        self.api_url = FIVESIM_API_URL
        self.token = token


class SMSActivate(SMSService):
    def __init__(self, token):
        self.api_url = SMSACTIVATE_API_URL
        self.token = token

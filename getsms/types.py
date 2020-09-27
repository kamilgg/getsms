import json

from getsms import apihelper


class SMSService:
    """
    Класс сервиса по приему СМС

    :param api_url: str
        ссылка API вашего сервиса
    :param token: str
        токен для доступа к API, берется в личном кабинете сервиса
    """

    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token

    def get_balance(self):
        """
        Возвращает баланс аккаунта

        :return: float
        """

        r = apihelper.get_balance(self.api_url, self.token)
        balance = float(r.split(':')[1])
        return balance

    def get_free_numbers(self, country=None):
        """
        Возвращает список свободных номеров в формате json

        :param country: str
            необязательный параметр, список и обозначение стран смотреть в вашем сервисе
        :return:
        """

        r = apihelper.get_numbers_status(self.api_url, self.token, country)
        json_r = json.loads(r)
        return json_r

    def get_number(self, service, forward=0):
        """
        Покупает новый номер

        :param service: str
            обозначение сервиса, для которого берете номер. Полный список смотреть в вашем сервисе
        :param forward: int
            1 - номер с переадресацией, 0 - без. Не у всех сервисов есть возможность купить номер с передаресацией
        :return: Order
        """

        r = apihelper.get_number(self.api_url, self.token, service, forward)
        response, order_id, number = r.split(':')
        order = Order(self, number, order_id)
        return order


class Order:
    """
    Класс заказа, который содержит номер и id заказа в вашем сервисе

    :param service: SMSService
        сервис, в котором был куплен номер
    :param number:
        номер телефона, который был куплен
    :param order_id:
        номер заказа
    """

    def __init__(self, service: SMSService, number, order_id):
        self.service = service
        self.number = number
        self.order_id = order_id

    def get_status(self):
        """
        Возвращает статус заказа. Возможные ответы:
        STATUS_WAIT_CODE - ожидание смс
        STATUS_WAIT_RETRY:$lastcode - ожидание уточнения кода (где $lastcode - прошлый, неподошедший код)
        STATUS_WAIT_RESEND - ожидание повторной отправки смс
        STATUS_CANCEL - активация отменена

        :return: str
        """

        result = apihelper.get_status(self.service.api_url, self.service.token, self.order_id)
        status = result.split(':')[0]
        return status

    def get_code(self):
        """
        Возвращает полученный код. Если код не получени, возвращает 'STATUS_WAIT_CODE'

        :return: str
        """

        result = apihelper.get_status(self.service.api_url, self.service.token, self.order_id)
        code = result.split(':')[-1]
        return code

    def set_ready(self):
        """
        Устанавливает статус готовности номера (когда сервис уже выслал код подтверждения)

        :return: bool
        """

        status = 1
        result = apihelper.set_status(self.service.api_url, self.service.token, self.order_id, status)
        if result == 'ACCESS_READY':
            return True
        else:
            return False

    def cancel_number(self):
        """
        Отменяет купленный номер

        :return: bool
        """

        status = 8
        result = apihelper.set_status(self.service.api_url, self.service.token, self.order_id, status)
        if result == 'ACCESS_CANCEL':
            return True
        else:
            return False

    def set_retry(self):
        """
        Устанавливает статус повторного приема смс для номера

        :return: bool
        """

        status = 3
        result = apihelper.set_status(self.service.api_url, self.service.token, self.order_id, status)
        if result == 'ACCESS_RETRY_GET':
            return True
        else:
            return False

    def set_finish(self):
        """
        Завершает заказ после получения кода

        :return: bool
        """

        status = 6
        result = apihelper.set_status(self.service.api_url, self.service.token, self.order_id, status)
        if result == 'ACCESS_ACTIVATION':
            return True
        else:
            return False

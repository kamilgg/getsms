import requests
from .exceptions import APIError, ServiceAccountError

API_ERRORS = ['NO_ACTIVATION', 'BAD_ACTION', 'BAD_SERVICE', 'BAD_KEY', 'ERROR_SQL', 'NO_KEY']
ACCOUNT_ERRORS = ['NO_NUMBERS', 'NO_BALANCE']

session = requests.Session()


def _make_request(api_url, token, action, params={}, method='GET'):
    default_params = {
        'api_key': token,
        'action': action
    }
    params.update(default_params)
    r = session.request(method, api_url, params=params)
    if r.status_code == 200 or r.status_code == 201:
        if r.text in API_ERRORS:
            raise APIError(r.text)
        elif r.text in ACCOUNT_ERRORS:
            raise ServiceAccountError(r.text)
        return r.text
    else:
        raise r.raise_for_status()


def get_numbers_status(api_url, token, country):
    """
    Запрос количества доступных номеров.
    Возможность выбора страны смотреть у себя в сервисе

    :param api_url:
    :param token:
    :param country:
    :return:
    """

    action = 'getNumbersStatus'
    params = {}
    if country:
        params = {
            'country': country
        }
    result = _make_request(api_url, token, action, params=params)
    return result


def get_balance(api_url, token):
    """
    Получение баланса аккаунта

    :param api_url:
    :param token:
    :return:
    """

    action = 'getBalance'
    result = _make_request(api_url, token, action)
    return result


def get_number(api_url, token, service, forward=0, operator='any', country=None):
    """
    Получение нового номера

    :param api_url:
    :param token:
    :param service:
    :param forward:
    :param operator:
    :param country:
    :return:
    """

    action = 'getNumber'
    params = {
        'service': service,
        'forward': forward,
        'operator': operator
    }
    if country:
        params.update({'country': country})
    result = _make_request(api_url, token, action, params)
    return result


def set_status(api_url, token, order_id, status, forward=0):
    """
    Установка статуса заказа

    :param api_url:
    :param token:
    :param order_id:
    :param status:
    :param forward:
    :return:
    """

    action = "setStatus"
    params = {
        'id': order_id,
        'status': status,
        'forward': forward
    }
    result = _make_request(api_url, token, action, params)
    return result


def get_status(api_url, token, order_id):
    """
    Получение статуса заказа

    :param api_url:
    :param token:
    :param order_id:
    :return:
    """

    action = "getStatus"
    params = {
        'id': order_id,
    }
    result = _make_request(api_url, token, action, params)
    return result

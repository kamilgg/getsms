## Модуль для работы с сервисами по приему смс на виртуальные номера для Python3

* [Настройка](#settings)
* [Установка](#installation)
* [Использование](#using)
* [Возможные ошибки](#errors)
* [Обозначение сервисов](#services)

<a name="settings"><h2>Настройка</h2></a>
Перед установкой нужно получить ключ API в настройках профиля на сайте сервиса, который вам нужен: 
[SMSHUB](), 
[5SIM](), 
[SMS-ACTIVATE]().

<a name="installation"><h2>Установка</h2></a>
Для работы модуля `smska` требуется Python3.

Используйте `pip` для установки библиотеки через GitHub:

```bash
$ pip install git+https://github.com/kamilgg/smska.git
```

или через PyPI:

```bash
$ pip install getsms
```

<a name="using"><h2>Использование</h2></a>

```python
from getsms import SMSHub

sms_hub = SMSHub("токен_сервиса_smska.net")

# Получение баланса аккаунта
balance = sms_hub.get_balance()

# Получение числа свободных номеров сервиса (forward по умолчанию равен 0)
free_numbers = sms_hub.get_free_numbers(service="vk", forward=0)

# Получение номера для принятия СМС (forward по умолчанию равен 0)
order = sms_hub.get_new_number(service="vk", forward=0)
number = order.number

#Получение статуса заказа
status = order.get_status()

# Получение кода из СМС
# (Не рекомендуется делать более 3 запросов в секунду)
code = order.get_code()

#Изменение статуса заказа (возвращают True, если статус изменен)
#Отмена номера. Номер Вам не нужен:
order.cancel_number()

#Принять СМС повторно:
order.set_retry()
```

<a name="errors"><h2>Возможные ошибки</h2></a>
- **BAD_KEY** - неверный API-ключ
- **ERROR_SQL** - ошибка SQL-сервера
- **BAD_ACTION** - некорректное действие
- **BAD_SERVICE** - некорректное наименование сервиса
- **NO_ACTIVATION** - id активации не существует
- **BAD_STATUS** - некорректный статус

<a name="services"><h2>Обозначение сервисов</h2></a>
**Актуальный список сервисов смотреть на сайте вашего сервиса**. Например:<br/><br/> 
- [SMS-HUB](https://smshub.org/main#getServices) <br/>
- [5SIM](https://5sim.net/docs/api1_ru.txt)<br/>
- [SMS-ACTIVATE](https://sms-activate.ru/ru/api2//#number).<br/>
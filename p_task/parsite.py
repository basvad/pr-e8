import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from p_task.models import Results
from celery import shared_task

@shared_task
def parsite(instance):
    address=instance.address
    if not (address.startswith('http') and  address.startswith('https')):
        address = 'http://' + address
    try:
        res = requests.get(address,timeout=30)
        #меняем статус задачи
        instance.task_status = 2
        #меняем статус http
        instance.http_status = res.status_code
        instance.save()
        _words_count=0
        if res.ok:
            words = res.text.split()
            _words_count = words.count("Python")
            #записываем результат
            result = Results(address=instance.address,words_count=_words_count,http_status_code=instance.http_status)
            result.save()
            #меняем статус задачи
            instance.task_status = 3
            instance.save()
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
        #меняем статус задачи
        instance.task_status = 3
        #меняем статус http
        instance.http_status = 404
        instance.save()

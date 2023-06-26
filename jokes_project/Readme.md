# Celery를 이용하여 scheduled job을 처리하는 샘플

### 데모 실행하는 방법

$ python manage.py runserver
$ celery -A jokes_project worker -l info -P gevent
$ celery -A jokes_project beat -l info

### 기타 참조할 내용
Everything about using Celery with django

Link for videl tutorial - https://www.youtube.com/watch?v=JYQG7zlLJrE&list=PLLz6Bi1mIXhHKA1Szy2aj9Jbs6nw9fhNY


### python version 생성
$ pip freeze > requirements.txt

### requirements.txt로 부터 설치
$ pip install -r requirements.txt
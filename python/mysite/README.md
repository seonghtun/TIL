## custom Djagno 사용법

#### 서버 실행 방법
허용 host, 프로세스 포트 지정 
runserver + ' ' + 'host' + 'port'
```
python manage.py runserver 0.0.0.0:8000
```

#### DATABASE setting
1. setting.py 의 파일에서 사용하고자 하는 데이터베이스로 DATABASES 변수의 default.ENGINE 값을 
변경해준다
2. 여기서는 OPTIONS key 를 사용하여 외부 .cnf 파일을 만들어 설정 관리를 하였으니,
입맛에 맞춰 사용하면된다. 파일을 올리진 않고 예시를 만들어놓았다.

```
# mysql.cnf

[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

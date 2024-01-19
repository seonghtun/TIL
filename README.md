## docker mysql 사용방법

docker run options
- -d : daemon background 실행
- -e : enviroment variable 환경변수 추가
- -p  host port:docker port = port 포워딩
- --name : container name 지정
''' 
$ docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql:latest
'''

from flask import Flask, request
import logging

app = Flask(__name__)

# 액세스 로그를 위한 커스텀 핸들러 생성
access_log_handler = logging.FileHandler('app.log')
access_log_format = '[%(asctime)s] %(message)s'
access_log_handler.setFormatter(logging.Formatter(access_log_format))

# Flask 앱의 로깅을 위해 별도의 로거 생성
access_log = logging.getLogger('access')
access_log.setLevel(logging.INFO)
access_log.addHandler(access_log_handler)

# Flask에 로깅 함수 연결
@app.after_request
def after_request(response):
    access_log.info('%s - - %s %s HTTP/1.1 %s',
        request.remote_addr,
        request.method,
        request.path,
        response.status_code)
    return response

@app.route('/v1/color/red')
def red():
    return 'red'

@app.route('/v1/color/orange')
def orange():
    return 'orange'

@app.route('/v1/color/melon')
def melon():
    return 'melon'

app.run(host='0.0.0.0', port=8080)
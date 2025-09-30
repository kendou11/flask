from flask import Blueprint, redirect, url_for

# 블루 프린트 : 라우팅 함수를 관리하는 역할
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return 'Hello Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))


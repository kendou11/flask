from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=['POST']) # meethods=('POST') 이렇게 써도 상관 X
def create(question_id):
    question = Question.query.get(question_id)
    content = request.form['content'] # 폼태그에서 내용 받아온 것

    # 1번 방식
    # answer = Answer(content=content, create_date=datetime.now()) # create 함수
    # question.answer_set.append(answer) # 역으로 append해서 답변 등록

    # 2번 방식
    answer = Answer(question=question, content=content, create_date=datetime.now())
    db.session.add(answer)

    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))
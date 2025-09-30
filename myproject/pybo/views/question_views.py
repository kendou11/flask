from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')  # question이 별칭

@bp.route('/list/') # question으로 간 다음 하위인 list로 감
def _list():  # list는 예약어여서 앞에 _붙여줌
    question_list=Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/') # <url parameter> -> question 아이디만 받아서 원하는 부분만 보여줌
def detail(question_id):
    question = Question.query.get_or_404(question_id)  # get 말고 get_or_404 쓰면 값이 없을 때 404 page를 보여줌 / ctrl누르고 클릭하면 함수 정의 보여줌
    return render_template('question/question_detail.html', question=question)

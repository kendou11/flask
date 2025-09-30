from pybo import db

# 질문 모델 생성
class Question(db.Model):    # class() -> 괄호 안에 내용 : 다른 클래스를 상속받을 때 괄호 안에 씀
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False) # not null = nullable
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 답변 모델 생성
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # cascade => 질문 삭제하면 답변도 같이 삭제하게 해주는 것 / backref 역참조
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
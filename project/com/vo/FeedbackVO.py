from project import db, app
from project.com.vo.LoginVO import LoginVO


class FeedbackVO(db.Model):
    __tablename__ = 'feedbackmaster'
    feedbackId = db.Column('feedbackId', db.Integer, primary_key=True, autoincrement=True)
    feedbackSubject = db.Column('feedbackSubject', db.String(100))
    feedbackDescription = db.Column('feedbackDescription', db.String(500))
    feedbackRating = db.Column('feedbackRating', db.Integer)
    feedbackDate = db.Column('feedbackDate', db.String(15))
    feedbackTime = db.Column('feedbackTime', db.String(15))
    feedbackTo_LoginId = db.Column('feedbackTo_LoginId', db.Integer)
    feedbackFrom_LoginId = db.Column('feedbackFrom_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'feedbackId': self.feedbackId,
            'feedbackSubject': self.feedbackSubject,
            'feedbackDescription': self.feedbackDescription,
            'feedbackRating': self.feedbackRating,
            'feedbackDate': self.feedbackDate,
            'feedbackTime': self.feedbackTime,
            'feedbackTo_LoginId': self.feedbackTo_LoginId,
            'feedbackFrom_LoginId': self.feedbackFrom_LoginId

        }


# db.create_all()
with app.app_context():
    db.create_all()
from project import db, app
from project.com.vo.LoginVO import LoginVO


class UserVO(db.Model):
    __tablename__ = 'usermaster'
    userId = db.Column('userId', db.Integer, primary_key=True, autoincrement=True)
    userFirstName = db.Column('userFirstName', db.String(100), nullable=False)
    userLastName = db.Column('userLastName', db.String(100), nullable=False)
    userGender = db.Column('userGender', db.String(100), nullable=False)
    userBirthDate = db.Column('userBirthDate', db.String(100), nullable=False)
    userAddress = db.Column('userAddress', db.String(100), nullable=False)
    userContact = db.Column('userContact', db.String(100), nullable=False)
    user_LoginId = db.Column('user_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'userId': self.userId,
            'userFirstName': self.userFirstName,
            'userLastName': self.userLastName,
            'userGender': self.userGender,
            'userBirthDate': self.userBirthDate,
            'userAddress': self.userAddress,
            'userContact': self.userContact,
            'user_LoginId': self.user_LoginId
        }


# db.create_all()
with app.app_context():
    db.create_all()
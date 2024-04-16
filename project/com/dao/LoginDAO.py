from project import db
from project.com.vo.LoginVO import LoginVO


class LoginDAO():
    def insertLogin(self, loginVO):
        db.session.add(loginVO)
        db.session.commit()

    def validateLogin(self, loginVO):
        loginList = LoginVO.query.filter_by(loginUsername=loginVO.loginUsername, loginPassword=loginVO.loginPassword)

        return loginList

    def adminBlockDriver(self, loginVO):
        db.session.merge(loginVO)
        db.session.commit()

    def adminBlockUser(self, loginVO):
        db.session.merge(loginVO)
        db.session.commit()

    def driverUsernameByLoginId(self, loginVO):
        loginVoList = LoginVO.query.filter_by(loginId=loginVO.loginId).all()

        return loginVoList

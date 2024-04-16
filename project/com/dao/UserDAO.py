from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.UserVO import UserVO


class UserDAO():
    def insertUser(self, userVO):
        db.session.add(userVO)

        db.session.commit()

    def viewUser(self):
        registerList = db.session.query(UserVO, LoginVO) \
            .join(LoginVO, UserVO.user_LoginId == LoginVO.loginId).all()

        return registerList

    def adminViewUser(self):
        userVOList = db.session.query(UserVO, LoginVO) \
            .join(LoginVO, UserVO.user_LoginId == LoginVO.loginId).all()
        return userVOList

    def userDetailsByLoginId(self, userVO):
        userVoList = UserVO.query.filter_by(user_LoginId=userVO.user_LoginId).all()
        return userVoList

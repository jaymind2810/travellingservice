from project import db
from project.com.vo.DriverVO import DriverVO
from project.com.vo.LoginVO import LoginVO


class DriverDAO():
    def insertDriver(self, driverVO):
        db.session.add(driverVO)

        db.session.commit()

    def viewDriver(self):
        registerList = db.session.query(DriverVO, LoginVO) \
            .join(LoginVO, DriverVO.driver_LoginId == LoginVO.loginId).all()

        return registerList

    def adminViewDriver(self):
        driverVOList = db.session.query(DriverVO, LoginVO) \
            .join(LoginVO, DriverVO.driver_LoginId == LoginVO.loginId).all()
        return driverVOList

    def driverDetailByLoginId(self, driverVO):
        driverVOList = DriverVO.query.filter_by(driver_LoginId=driverVO.driver_LoginId).all()

        return driverVOList


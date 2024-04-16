from project import db, app
from project.com.vo.LoginVO import LoginVO


class DriverVO(db.Model):
    __tablename__ = 'drivermaster'
    driverId = db.Column('driverId', db.Integer, primary_key=True, autoincrement=True)
    driverFirstName = db.Column('driverFirstName', db.String(100), nullable=False)
    driverLastName = db.Column('driverLastName', db.String(100), nullable=False)
    driverGender = db.Column('driverGender', db.String(100), nullable=False)
    driverBirthDate = db.Column('driverBirthDate', db.String(100), nullable=False)
    driverAddress = db.Column('driverAddress', db.String(100), nullable=False)
    driverContact = db.Column('driverContact', db.String(100), nullable=False)
    driver_LoginId = db.Column('driver_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'driverId': self.driverId,
            'driverFirstName': self.driverFirstName,
            'driverLastName': self.driverLastName,
            'driverGender': self.driverGender,
            'driverBirthDate': self.driverBirthDate,
            'driverAddress': self.driverAddress,
            'driverContact': self.driverContact,
            'driver_LoginId': self.driver_LoginId
        }


# db.create_all()
with app.app_context():
    db.create_all()

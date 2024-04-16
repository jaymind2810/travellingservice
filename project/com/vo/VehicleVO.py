from project import db
from project.com.vo.LoginVO import LoginVO
from project import app

class VehicleVO(db.Model):
    __tablename__ = 'vehiclemaster'
    vehicleId = db.Column('vehicleId', db.Integer, primary_key=True, autoincrement=True)
    vehicleName = db.Column('vehicleName', db.String(100))
    vehicleNumber = db.Column('vehicleNumber', db.String(100))
    seaterCapacity = db.Column('seaterCapacity', db.String(100))
    vehicleDescription = db.Column('vehicleDescription', db.String(100))
    vehicle_LoginId = db.Column('vehicle_LoginId',db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'vehicleId': self.vehicleId,
            'vehicleName': self.vehicleName,
            'vehicleNumber': self.vehicleNumber,
            'seaterCapacity': self.seaterCapacity,
            'vehicleDescription': self.vehicleDescription,
            'vehicle_LoginId': self.vehicle_LoginId
        }


# db.create_all()
with app.app_context():
    db.create_all()
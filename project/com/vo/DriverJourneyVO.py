from project import db, app
from project.com.vo.LoginVO import LoginVO
from project.com.vo.CityVO import CityVO

from project.com.vo.SharingTypeVO import SharingTypeVO
from project.com.vo.StateVO import StateVO


class DriverJourneyVO(db.Model):
    __tablename__ = 'driverjourneymaster'
    driverJourneyId = db.Column('driverJourneyId', db.Integer, primary_key=True, autoincrement=True)
    driverJourney_SharingTypeId = db.Column('driverJourney_SharingTypeId', db.Integer,
                                            db.ForeignKey(SharingTypeVO.sharingTypeId))
    driverJourney_SourceStateId = db.Column('driverJourney_SourceStateId', db.Integer, db.ForeignKey(StateVO.stateId))
    driverJourney_SourceCityId = db.Column('driverJourney_SourceCityId', db.Integer, db.ForeignKey(CityVO.cityId))
    driverJourney_DestinationStateId = db.Column('driverJourney_DestinationStateId', db.Integer,
                                                 db.ForeignKey(StateVO.stateId))
    driverJourney_DestinationCityId = db.Column('driverJourney_DestinationCityId', db.Integer,
                                                db.ForeignKey(CityVO.cityId))
    driverJourneyDate = db.Column('driverJourneyDate', db.String(100), nullable=False)
    driverJourneyTime = db.Column('driverJourneyTime', db.String(100), nullable=False)
    driverJourney_LoginId = db.Column('driverJourney_LoginId', db.Integer,
                                      db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'driverJourneyId': self.driverJourneyId,
            'driverJourney_SharingTypeId': self.driverJourney_SharingTypeId,
            'driverJourney_SourceStateId': self.driverJourney_SourceStateId,
            'driverJourney_SourceCityId': self.driverJourney_SourceCityId,
            'driverJourney_DestinationStateId': self.driverJourney_DestinationStateId,
            'driverJourney_DestinationCityId': self.driverJourney_DestinationCityId,
            'driverJourneyDate': self.driverJourneyDate,
            'driverJourneyTime': self.driverJourneyTime,
            'driverJourney_LoginId': self.driverJourney_LoginId
        }


# db.create_all()
with app.app_context():
    db.create_all()

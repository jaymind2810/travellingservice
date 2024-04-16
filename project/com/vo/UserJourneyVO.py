from project import db, app
from project.com.vo.CityVO import CityVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SharingTypeVO import SharingTypeVO
from project.com.vo.StateVO import StateVO


class UserJourneyVO(db.Model):
    __tablename__ = 'userjourneymaster'
    userJourneyId = db.Column('userJourneyId', db.Integer, primary_key=True, autoincrement=True)
    userJourney_SharingTypeId = db.Column('userJourney_SharingTypeId', db.Integer,
                                          db.ForeignKey(SharingTypeVO.sharingTypeId))
    userJourney_SourceStateId = db.Column('userJourney_SourceStateId', db.Integer, db.ForeignKey(StateVO.stateId))
    userJourney_SourceCityId = db.Column('userJourney_SourceCityId', db.Integer, db.ForeignKey(CityVO.cityId))
    userJourney_DestinationStateId = db.Column('userJourney_DestinationStateId', db.Integer,
                                               db.ForeignKey(StateVO.stateId))
    userJourney_DestinationCityId = db.Column('userJourney_DestinationCityId', db.Integer, db.ForeignKey(CityVO.cityId))
    userJourneyDate = db.Column('userJourneyDate', db.String(100), nullable=False)
    userJourneyTime = db.Column('userJourneyTime', db.String(100), nullable=False)
    userJourney_LoginId = db.Column('userJourney_LoginId', db.Integer,
                                    db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'userJourneyId': self.userJourneyId,
            'userJourney_SharingTypeId': self.userJourney_SharingTypeId,
            'userJourney_SourceStateId': self.userJourney_SourceStateId,
            'userJourney_SourceCityId': self.userJourney_SourceCityId,
            'userJourney_DestinationStateId': self.userJourney_DestinationStateId,
            'userJourney_DestinationCityId': self.userJourney_DestinationCityId,
            'userJourneyDate': self.userJourneyDate,
            'userJourneyTime': self.userJourneyTime,
            'userJourney_LoginId': self.userJourney_LoginId
        }


# db.create_all()
with app.app_context():
    db.create_all()

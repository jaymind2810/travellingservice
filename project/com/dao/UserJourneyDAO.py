from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.CityVO import CityVO
from project.com.vo.SharingTypeVO import SharingTypeVO
from project.com.vo.StateVO import StateVO
from project.com.vo.UserJourneyVO import UserJourneyVO


class UserJourneyDAO():
    def insertUserJourney(self, userJourneyVO):
        db.session.add(userJourneyVO)

        db.session.commit()

    def viewUserSourceJourney(self, userJourneyVO):
        userSourceJourneyList = db.session.query(UserJourneyVO, SharingTypeVO, StateVO, CityVO) \
            .join(SharingTypeVO, UserJourneyVO.userJourney_SharingTypeId == SharingTypeVO.sharingTypeId) \
            .join(StateVO, UserJourneyVO.userJourney_SourceStateId == StateVO.stateId) \
            .join(CityVO, UserJourneyVO.userJourney_SourceCityId == CityVO.cityId) \
            .filter(UserJourneyVO.userJourney_LoginId == userJourneyVO.userJourney_LoginId).all()

        return userSourceJourneyList

    def viewUserDestinationJourney(self, userJourneyVO):
        userDestinationJourneyList = db.session.query(UserJourneyVO, SharingTypeVO, StateVO, CityVO) \
            .join(SharingTypeVO, UserJourneyVO.userJourney_SharingTypeId == SharingTypeVO.sharingTypeId) \
            .join(StateVO, UserJourneyVO.userJourney_DestinationStateId == StateVO.stateId) \
            .join(CityVO, UserJourneyVO.userJourney_DestinationCityId == CityVO.cityId) \
            .filter(UserJourneyVO.userJourney_LoginId == userJourneyVO.userJourney_LoginId).all()
        return userDestinationJourneyList

    def deleteUserJourney(self, userJourneyId):
        userJourneyList = UserJourneyVO.query.get(userJourneyId)

        db.session.delete(userJourneyList)

        db.session.commit()

    def editUserJourney(self, userJourneyVO):
        userJourneyList = db.session.query_property()

        return userJourneyList

    def updateUserJourney(self, userJourneyVO):
        db.session.merge(userJourneyVO)

        db.session.commit()

    def ajaxUserJourney(self, cityVO):
        ajaxUserJourneyList = UserJourneyVO.query.filter_by(UserJourney_StateId=UserJourneyVO.userJourney_StateId).all()

        return ajaxUserJourneyList

    def findUser_LoginId(self, driverJourneyVO):
        userJourneyList = UserJourneyVO.query.filter_by(
            userJourney_SourceStateId=driverJourneyVO.driverJourney_SourceStateId,
            userJourney_SourceCityId=driverJourneyVO.driverJourney_SourceCityId,
            userJourney_DestinationStateId=driverJourneyVO.driverJourney_DestinationStateId,
            userJourney_DestinationCityId=driverJourneyVO.driverJourney_DestinationCityId,
            userJourneyDate=driverJourneyVO.driverJourneyDate,
            userJourneyTime=driverJourneyVO.driverJourneyTime).all()

        return userJourneyList

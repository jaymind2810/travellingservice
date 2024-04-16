from project import db
from project.com.vo.CityVO import CityVO
from project.com.vo.DriverJourneyVO import DriverJourneyVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SharingTypeVO import SharingTypeVO
from project.com.vo.StateVO import StateVO


class DriverJourneyDAO():
    def insertDriverJourney(self, driverJourneyVO):
        db.session.add(driverJourneyVO)

        db.session.commit()

    def viewDriverSourceJourney(self, driverJourneyVO):
        driverSourceJourneyList = db.session.query(DriverJourneyVO, SharingTypeVO, StateVO, CityVO) \
            .join(SharingTypeVO, DriverJourneyVO.driverJourney_SharingTypeId == SharingTypeVO.sharingTypeId) \
            .join(StateVO, DriverJourneyVO.driverJourney_SourceStateId == StateVO.stateId) \
            .join(CityVO, DriverJourneyVO.driverJourney_SourceCityId == CityVO.cityId) \
            .filter(DriverJourneyVO.driverJourney_LoginId == driverJourneyVO.driverJourney_LoginId).all()

        return driverSourceJourneyList

    def viewDriverDestinationJourney(self, driverJourneyVO):
        driverDestinationJourneyList = db.session.query(DriverJourneyVO, SharingTypeVO, StateVO, CityVO, ) \
            .join(SharingTypeVO, DriverJourneyVO.driverJourney_SharingTypeId == SharingTypeVO.sharingTypeId) \
            .join(StateVO, DriverJourneyVO.driverJourney_DestinationStateId == StateVO.stateId) \
            .join(CityVO, DriverJourneyVO.driverJourney_DestinationCityId == CityVO.cityId) \
            .filter(DriverJourneyVO.driverJourney_LoginId == driverJourneyVO.driverJourney_LoginId).all()
        return driverDestinationJourneyList

    def driverViewJourney(self, driverJourneyVO):
        driverJourneyList = db.session.query(DriverJourneyVO, SharingTypeVO, StateVO, CityVO) \
            .join(SharingTypeVO, DriverJourneyVO.driverJourney_SharingTypeId == SharingTypeVO.sharingTypeId) \
            .join(StateVO, DriverJourneyVO.driverJourney_DestinationStateId == StateVO.stateId) \
            .join(CityVO, DriverJourneyVO.driverJourney_DestinationCityId == CityVO.cityId) \
            .filter(DriverJourneyVO.driverJourney_LoginId == driverJourneyVO.driverJourney_LoginId).all()

        return driverJourneyList

    def deleteDriverJourney(self, driverJourneyId):
        driverJourneyList = DriverJourneyVO.query.get(driverJourneyId)

        db.session.delete(driverJourneyList)

        db.session.commit()

    def editDriverJourney(self, driverJourneyVO):
        driverJourneyList = DriverJourneyVO.query.filter_by(driverJourneyId=driverJourneyVO.driverJourneyId)

        return driverJourneyList

    def updateDriverJourney(self, driverJourneyVO):
        db.session.merge(driverJourneyVO)

        db.session.commit()

    def ajaxDriverJourney(self, cityVO):
        ajaxDriverJourneyList = DriverJourneyVO.query.filter_by(
            DriverJourney_StateId=DriverJourneyVO.driverJourney_StateId).all()

        return ajaxDriverJourneyList

    def findDriver_LoginId(self, userJourneyVO):
        driverJourneyList = DriverJourneyVO.query.filter_by(
            driverJourney_SourceStateId=userJourneyVO.userJourney_SourceStateId,
            driverJourney_SourceCityId=userJourneyVO.userJourney_SourceCityId,
            driverJourney_DestinationStateId=userJourneyVO.userJourney_DestinationStateId,
            driverJourney_DestinationCityId=userJourneyVO.userJourney_DestinationCityId,
            driverJourneyDate=userJourneyVO.userJourneyDate,
            driverJourneyTime=userJourneyVO.userJourneyTime).all()

        return driverJourneyList

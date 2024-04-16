from project import db
from project.com.vo.CityVO import CityVO
from project.com.vo.StateVO import StateVO


class CityDAO():
    def insertCity(self, cityVO):
        db.session.add(cityVO)

        db.session.commit()

    def viewCity(self):
        cityList = db.session.query(CityVO, StateVO).join(StateVO, CityVO.city_StateId == StateVO.stateId).all()

        return cityList

    def deleteCity(self, cityId):
        cityList = CityVO.query.get(cityId)

        db.session.delete(cityList)

        db.session.commit()

    def editCity(self, cityVO):
        cityList = CityVO.query.filter_by(cityId=cityVO.cityId)

        return cityList

    def updateCity(self, cityVO):
        db.session.merge(cityVO)

        db.session.commit()

    def ajaxCityProduct(self, cityVO):
        ajaxProductCityList = CityVO.query.filter_by(city_StateId=cityVO.city_StateId).all()

        return ajaxProductCityList

    def ajaxSourceCityDriverJourney(self, cityVO):
        ajaxDriverJourneySourceCityList = CityVO.query.filter_by(city_StateId=cityVO.city_StateId).all()

        return ajaxDriverJourneySourceCityList

    def ajaxDestinationCityDriverJourney(self, cityVO):
        ajaxDriverJourneyDestinationCityList = CityVO.query.filter_by(city_StateId=cityVO.city_StateId).all()

        return ajaxDriverJourneyDestinationCityList

    def ajaxSourceCityUserJourney(self, cityVO):
        ajaxUserJourneySourceCityList = CityVO.query.filter_by(city_StateId=cityVO.city_StateId).all()

        return ajaxUserJourneySourceCityList

    def ajaxDestinationCityUserJourney(self, cityVO):
        ajaxUserJourneyDestinationCityList = CityVO.query.filter_by(city_StateId=cityVO.city_StateId).all()

        return ajaxUserJourneyDestinationCityList

    def viewCityByCityId(self, cityVO):
        cityVOList = CityVO.query.filter_by(cityId=cityVO.cityId).all()
        return cityVOList

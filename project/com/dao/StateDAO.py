from project import db
from project.com.vo.StateVO import StateVO


class StateDAO():
    def insertState(self, stateVO):
        db.session.add(stateVO)
        db.session.commit()

    def viewState(self):
        stateList = StateVO.query.all()

        return stateList

    def deleteState(self, stateVO):
        stateList = StateVO.query.get(stateVO.stateId)

        db.session.delete(stateList)

        db.session.commit()

    def editState(self, stateVO):
        # stateList = StateVO.query.get(stateVO.stateId)

        # stateList = StateVO.query.filter_by(stateId=stateVO.stateId)

        stateList = StateVO.query.filter_by(stateId=stateVO.stateId).all()

        return stateList

    def updateState(self, stateVO):
        db.session.merge(stateVO)

        db.session.commit()

    def viewStateByStateId(self, stateVO):
        stateVOList = StateVO.query.filter_by(stateId=stateVO.stateId).all()
        return stateVOList

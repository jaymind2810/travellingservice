from project import db
from project.com.vo.SharingTypeVO import SharingTypeVO


class SharingTypeDAO():
    def insertSharingType(self, sharingTypeVO):
        db.session.add(sharingTypeVO)
        db.session.commit()

    def viewSharingType(self):
        sharingTypeList = SharingTypeVO.query.all()

        return sharingTypeList

    def deleteSharingType(self, sharingTypeVO):
        sharingTypeList = SharingTypeVO.query.get(sharingTypeVO.sharingTypeId)

        db.session.delete(sharingTypeList)

        db.session.commit()

    def editSharingType(self, sharingTypeVO):
        # sharingTypeList = SharingTypeVO.query.get(sharingTypeVO.sharingTypeId)

        # sharingTypeList = SharingTypeVO.query.filter_by(sharingTypeId=sharingTypeVO.sharingTypeId)

        sharingTypeList = SharingTypeVO.query.filter_by(sharingTypeId=sharingTypeVO.sharingTypeId).all()

        return sharingTypeList

    def updateSharingType(self, sharingTypeVO):
        db.session.merge(sharingTypeVO)

        db.session.commit()

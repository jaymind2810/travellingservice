from project import db
from project.com.vo.VehicleVO import VehicleVO
from project.com.vo.LoginVO import LoginVO


class VehicleDAO():
    def insertVehicle(self, vehicleVO):
        db.session.add(vehicleVO)

        db.session.commit()

    def viewVehicle(self,vehicleVO):
        vehicleList = VehicleVO.query.filter_by(vehicle_LoginId=vehicleVO.vehicle_LoginId).all()

        return vehicleList

    def deleteVehicle(self, vehicleVO):
        vehicleList = VehicleVO.query.get(vehicleVO.vehicleId)

        db.session.delete(vehicleList)

        db.session.commit()

    def editVehicle(self, vehicleVO):
        # vehicleList = VehicleVO.query.get(vehicleVO.vehicleId)

        # vehicleList = VehicleVO.query.filter_by(vehicleId=vehicleVO.vehicleId)

        vehicleList = VehicleVO.query.filter_by(vehicleId=vehicleVO.vehicleId).all()

        return vehicleList

    def updateVehicle(self, vehicleVO):
        db.session.merge(vehicleVO)

        db.session.commit()

    def getVehicleDetails(self, vehicleVO):
        vehicleVOList = VehicleVO.query.filter_by(vehicle_LoginId=vehicleVO.vehicle_LoginId).all()
        return vehicleVOList

from flask import request, render_template, redirect, url_for, session

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.VehicleDAO import VehicleDAO
from project.com.vo.VehicleVO import VehicleVO


@app.route('/driver/loadVehicle', methods=['GET'])
def driverLoadVehicle():
    try:
        if adminLoginSession() == 'driver':
            return render_template('driver/addVehicle.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/driver/insertVehicle', methods=['POST'])
def driverInsertVehicle():
    try:
        if adminLoginSession() == 'driver':
            vehicleName = request.form['vehicleName']
            vehicleNumber = request.form['vehicleNumber']
            seaterCapacity = request.form['seaterCapacity']
            vehicleDescription = request.form['vehicleDescription']

            vehicleVO = VehicleVO()
            vehicleDAO = VehicleDAO()

            vehicleVO.vehicleName = vehicleName
            vehicleVO.vehicleNumber = vehicleNumber
            vehicleVO.seaterCapacity = seaterCapacity
            vehicleVO.vehicleDescription = vehicleDescription
            vehicleVO.vehicle_LoginId = session ['session_loginId']

            vehicleDAO.insertVehicle(vehicleVO)

            return redirect(url_for('driverViewVehicle'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/driver/viewVehicle', methods=['GET'])
def driverViewVehicle():
    try:
        if adminLoginSession() == 'driver':
            vehicleVO = VehicleVO()
            vehicleDAO = VehicleDAO()

            vehicleVO.vehicle_LoginId = session['session_loginId']
            vehicleVOList = vehicleDAO.viewVehicle(vehicleVO)
            print("__________________", vehicleVOList)
            return render_template('driver/viewVehicle.html', vehicleVOList=vehicleVOList)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/deleteVehicle', methods=['GET'])
def driverDeleteVehicle():
    try:
        if adminLoginSession() == 'driver':
            vehicleVO = VehicleVO()
            vehicleDAO = VehicleDAO()

            vehicleId = request.args.get('vehicleId')

            vehicleVO.vehicleId = vehicleId

            vehicleDAO.deleteVehicle(vehicleVO)

            return redirect(url_for('driverViewVehicle'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/driver/editVehicle', methods=['GET'])
def driverEditVehicle():
    try:
        if adminLoginSession() == 'driver':
            vehicleVO = VehicleVO()
            vehicleDAO = VehicleDAO()

            vehicleId = request.args.get('vehicleId')

            vehicleVO.vehicleId = vehicleId

            vehicleVOList = vehicleDAO.editVehicle(vehicleVO)

            print("=======vehicleVOList=======", vehicleVOList)

            print("=======type of vehicleVOList=======", type(vehicleVOList))

            return render_template('driver/editVehicle.html', vehicleVOList=vehicleVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/driver/updateVehicle', methods=['POST'])
def driverUpdateVehicle():
    try:
        if adminLoginSession() == 'driver':
            vehicleId = request.form['vehicleId']
            vehicleName = request.form['vehicleName']
            vehicleNumber = request.form['vehicleNumber']
            seaterCapacity = request.form['seaterCapacity']
            vehicleDescription = request.form['vehicleDescription']

            vehicleVO = VehicleVO()
            vehicleDAO = VehicleDAO()

            vehicleVO.vehicleId = vehicleId
            vehicleVO.vehicleName = vehicleName
            vehicleVO.vehicleNumber = vehicleNumber
            vehicleVO.seaterCapacity = seaterCapacity
            vehicleVO.vehicleDescription = vehicleDescription

            vehicleDAO.updateVehicle(vehicleVO)

            return redirect(url_for('driverViewVehicle'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)

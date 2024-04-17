import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template, redirect, url_for, jsonify, session

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.CityDAO import CityDAO
from project.com.dao.DriverDAO import DriverDAO
from project.com.dao.DriverJourneyDAO import DriverJourneyDAO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.SharingTypeDAO import SharingTypeDAO
from project.com.dao.StateDAO import StateDAO
from project.com.dao.UserJourneyDAO import UserJourneyDAO
from project.com.dao.VehicleDAO import VehicleDAO
from project.com.vo.CityVO import CityVO
from project.com.vo.DriverJourneyVO import DriverJourneyVO
from project.com.vo.DriverVO import DriverVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.StateVO import StateVO
from project.com.vo.VehicleVO import VehicleVO


@app.route('/driver/loadDriverJourney', methods=['GET'])
def driverLoadDriverJourney():
    try:
        if adminLoginSession() == 'driver':
            sharingTypeDAO = SharingTypeDAO()
            sharingTypeVOList = sharingTypeDAO.viewSharingType()

            stateDAO = StateDAO()
            stateVOList = stateDAO.viewState()

            cityDAO = CityDAO()
            cityVOList = cityDAO.viewCity()

            return render_template('driver/addDriverJourney.html', sharingTypeVOList=sharingTypeVOList,
                                   stateVOList=stateVOList, cityVOList=cityVOList, )
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/ajaxSourceCityDriverJourney')
def driverAjaxSourceCityDriverJourney():
    try:
        if adminLoginSession() == 'driver':
            cityVO = CityVO()

            cityDAO = CityDAO()

            city_StateId = request.args.get('driverJourney_SourceStateId')

            cityVO.city_StateId = city_StateId

            ajaxDriverJourneySourceCityList = cityDAO.ajaxSourceCityDriverJourney(cityVO)

            ajaxDriverJourneySourceCityJson = [i.as_dict() for i in ajaxDriverJourneySourceCityList]

            return jsonify(ajaxDriverJourneySourceCityJson)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/ajaxDestinationCityDriverJourney')
def driverAjaxDestinationCityDriverJourney():
    try:
        if adminLoginSession() == 'driver':
            cityVO = CityVO()

            cityDAO = CityDAO()

            city_StateId = request.args.get('driverJourney_DestinationStateId')

            cityVO.city_StateId = city_StateId

            ajaxDriverJourneyDestinationCityList = cityDAO.ajaxDestinationCityDriverJourney(cityVO)

            ajaxDriverJourneyDestinationCityJson = [i.as_dict() for i in ajaxDriverJourneyDestinationCityList]

            return jsonify(ajaxDriverJourneyDestinationCityJson)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/insertDriverJourney', methods=['POST'])
def driverInsertDriverJourney():
    try:
        if adminLoginSession() == 'driver':

            driverJourney_SharingTypeId = request.form['driverJourney_SharingTypeId']
            driverJourney_SourceStateId = request.form['driverJourney_SourceStateId']
            driverJourney_SourceCityId = request.form['driverJourney_SourceCityId']
            driverJourney_DestinationStateId = request.form['driverJourney_DestinationStateId']
            driverJourney_DestinationCityId = request.form['driverJourney_DestinationCityId']
            driverJourneyDate = request.form['driverJourneyDate']
            driverJourneyTime = request.form['driverJourneyTime']

            driverJourneyVO = DriverJourneyVO()
            driverJourneyDAO = DriverJourneyDAO()

            driverJourneyVO.driverJourney_SharingTypeId = driverJourney_SharingTypeId
            driverJourneyVO.driverJourney_SourceStateId = driverJourney_SourceStateId
            driverJourneyVO.driverJourney_SourceCityId = driverJourney_SourceCityId
            driverJourneyVO.driverJourney_DestinationStateId = driverJourney_DestinationStateId
            driverJourneyVO.driverJourney_DestinationCityId = driverJourney_DestinationCityId
            driverJourneyVO.driverJourneyDate = driverJourneyDate
            driverJourneyVO.driverJourneyTime = driverJourneyTime
            driverJourneyVO.driverJourney_LoginId = session['session_loginId']

            driverJourneyDAO.insertDriverJourney(driverJourneyVO)

            stateVO = StateVO()
            stateDAO = StateDAO()

            stateVO.stateId = driverJourney_SourceStateId
            sourceStateList = stateDAO.viewStateByStateId(stateVO)
            sourceStateName = sourceStateList[0].stateName
            print('sourceStateName>>>>', sourceStateName)

            stateVO.stateId = driverJourney_DestinationStateId
            destinationStateList = stateDAO.viewStateByStateId(stateVO)
            destinationStateName = destinationStateList[0].stateName
            print('destinationStateName>>>>', destinationStateName)

            cityVO = CityVO()
            cityDAO = CityDAO()

            cityVO.cityId = driverJourney_SourceCityId
            sourceCityList = cityDAO.viewCityByCityId(cityVO)
            sourceCityName = sourceCityList[0].cityName
            print('sourceCityName>>>>', sourceCityName)

            cityVO.cityId = driverJourney_DestinationCityId
            destinationCityList = cityDAO.viewCityByCityId(cityVO)
            destinationCityName = destinationCityList[0].cityName
            print('destinationCityName>>>>', destinationCityName)

            userJourneyDAO = UserJourneyDAO()
            userJourneyVOList = userJourneyDAO.findUser_LoginId(driverJourneyVO)
            print('userJourneyVOList>>>>>', userJourneyVOList)

            if len(userJourneyVOList) != 0:
                for i in userJourneyVOList:
                    userJourney_LoginId = i.userJourney_LoginId
                    print('userJourney_LoginId>>>>>>>>>>>>>>>>', userJourney_LoginId)

                    loginVO = LoginVO()
                    loginDAO = LoginDAO()
                    loginVO.loginId = userJourney_LoginId

                    loginVOList = loginDAO.driverUsernameByLoginId(loginVO)
                    print('loginVOList>>>', loginVOList)

                    if len(loginVOList) != 0:
                        loginUsername = loginVOList[0].loginUsername
                        print('loginUsername>>>>', loginUsername)
                    else:
                        pass

                    vehicleVO = VehicleVO()
                    vehicleDAO = VehicleDAO()
                    vehicleVO.vehicle_LoginId = session['session_loginId']
                    vehicleVOList = vehicleDAO.getVehicleDetails(vehicleVO)

                    if len(vehicleVOList) != 0:
                        vehicleName = vehicleVOList[0].vehicleName
                        print('vehicleName>>>',vehicleName)
                        vehicleNumber = vehicleVOList[0].vehicleNumber
                        print('vehicleNumber>>>', vehicleNumber)
                        seaterCapacity = vehicleVOList[0].seaterCapacity
                        print('seaterCapacity>>>', seaterCapacity)

                    driverVO = DriverVO()
                    driverDAO = DriverDAO()

                    driverVO.driver_LoginId = session['session_loginId']
                    driverVOList = driverDAO.driverDetailByLoginId(driverVO)

                    if len(driverVOList) != 0:
                        driverContact = driverVOList[0].driverContact
                        print('driverContact>>>', driverVOList)

                    # sender = "travelingtransport1@gmail.com"
                    #
                    # receiver = loginUsername
                    #
                    # msg = MIMEMultipart()
                    #
                    textMsg = 'SourceState:{}\n\nSourceCity:{}\n\nDestinationState:{}\n\nDestinationCity:{}\n\n' \
                              'Date:{}\n\nTime:{}\n\nvehicleName:{}\n\nvehicleNumber:{}\n\nseaterCapacity:{}' \
                              '\n\nDriverContact:{}'.format(sourceStateName, sourceCityName, destinationStateName,
                                                         destinationCityName, driverJourneyDate, driverJourneyTime,
                                                         vehicleName, vehicleNumber, seaterCapacity, driverContact)
                    print(textMsg, "--------Driver Journy Details----------")
                    # # =========== Mail Send Functionality ===============
                    # msg['From'] = sender
                    #
                    # msg['To'] = receiver
                    #
                    # msg['Subject'] = "Driver Journey Details"
                    #
                    # msg.attach(MIMEText(textMsg, 'plain'))
                    #
                    # server = smtplib.SMTP('smtp.gmail.com', 587)
                    #
                    # server.starttls()
                    #
                    # server.login(sender, "jaymin@123")
                    #
                    # text = msg.as_string()
                    #
                    # server.sendmail(sender, receiver, text)
                    #
                    # server.quit()

            return redirect(url_for('driverViewDriverJourney'))
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/viewDriverJourney', methods=['GET'])
def driverViewDriverJourney():
    try:
        if adminLoginSession() == 'driver':
            driverJourneyVO = DriverJourneyVO()
            driverJourneyDAO = DriverJourneyDAO()

            driverJourneyVO.driverJourney_LoginId = session['session_loginId']
            driverSourceJourneyVOList = driverJourneyDAO.viewDriverSourceJourney(driverJourneyVO)
            # print(driverSourceJourneyVOList)
            driverDestinationJourneyVOList = driverJourneyDAO.viewDriverDestinationJourney(driverJourneyVO)
            # print(driverDestinationJourneyVOList)

            driverJourneyListLength = len(driverSourceJourneyVOList)

            return render_template('driver/viewDriverJourney.html', driverSourceJourneyVOList=driverSourceJourneyVOList,
                                   driverDestinationJourneyVOList=driverDestinationJourneyVOList,
                                   driverJourneyListLength=driverJourneyListLength)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/viewUserJourney', methods=['GET'])
def driverViewUserJourney():
    try:
        if adminLoginSession() == 'driver':
            driverJourneyDAO = DriverJourneyDAO()
            driverSourceJourneyVOList = driverJourneyDAO.viewDriverSourceJourney()
            driverDestinationJourneyVOList = driverJourneyDAO.viewDriverDestinationJourney()
            print(driverSourceJourneyVOList)
            print(driverDestinationJourneyVOList)
            return render_template('driver/viewUserJourney.html', driverSourceJourneyVOList=driverSourceJourneyVOList,
                                   driverDestinationJourneyVOList=driverDestinationJourneyVOList)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/deleteDriverJourney', methods=['GET'])
def driverDeleteDriverJourney():
    try:
        if adminLoginSession() == 'driver':
            driverJourneyDAO = DriverJourneyDAO()
            driverJourneyVO = DriverJourneyVO()
            driverJourneyId = request.args.get('driverJourneyId')
            driverJourneyVO.driverJourneyId = driverJourneyId
            driverJourneyDAO.deleteDriverJourney(driverJourneyId)

            return redirect(url_for('driverViewDriverJourney'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/driver/editDriverJourney', methods=['GET'])
def driverEditDriverJourney():
    try:
        if adminLoginSession() == 'driver':

            driverJourneyVO = DriverJourneyVO()

            driverJourneyDAO = DriverJourneyDAO()

            stateDAO = StateDAO()

            cityDAO = CityDAO()

            sharingTypeDAO = SharingTypeDAO()

            driverJourneyId = request.args.get('driverJourneyId')

            driverJourneyVO.driverJourneyId = driverJourneyId

            driverJourneyVOList = driverJourneyDAO.editDriverJourney(driverJourneyVO)

            stateVOList = stateDAO.viewState()

            cityVOList = cityDAO.viewCity()

            sharingTypeVOList = sharingTypeDAO.viewSharingType()

            return render_template('driver/editDriverJourney.html', sharingTypeVOList=sharingTypeVOList,
                                   stateVOList=stateVOList, cityVOList=cityVOList,
                                   driverJourneyVOList=driverJourneyVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/driver/updateDriverJourney', methods=['POST'])
def driverUpdateDriverJourney():
    try:
        if adminLoginSession() == 'driver':
            driverJourney_SharingTypeId = request.form['driverJourney_SharingTypeId']
            driverJourney_SourceStateId = request.form['driverJourney_SourceStateId']
            driverJourney_SourceCityId = request.form['driverJourney_SourceCityId']
            driverJourney_DestinationStateId = request.form['driverJourney_DestinationStateId']
            driverJourney_DestinationCityId = request.form['driverJourney_DestinationCityId']
            driverJourneyDate = request.form['driverJourneyDate']
            driverJourneyTime = request.form['driverJourneyTime']

            driverJourneyVO = DriverJourneyVO()
            driverJourneyDAO = DriverJourneyDAO()

            driverJourneyVO.driverJourney_SharingTypeId = driverJourney_SharingTypeId
            driverJourneyVO.driverJourney_SourceStateId = driverJourney_SourceStateId
            driverJourneyVO.driverJourney_SourceCityId = driverJourney_SourceCityId
            driverJourneyVO.driverJourney_DestinationStateId = driverJourney_DestinationStateId
            driverJourneyVO.driverJourney_DestinationCityId = driverJourney_DestinationCityId
            driverJourneyVO.driverJourneyDate = driverJourneyDate
            driverJourneyVO.driverJourneyTime = driverJourneyTime
            driverJourneyVO.driverJourney_LoginId = session['session_loginId']

            driverJourneyDAO.updateDriverJourney(driverJourneyVO)

            return redirect(url_for('driverViewDriverJourney'))
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)

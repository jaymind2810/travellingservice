import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template, redirect, url_for, jsonify, session

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.CityDAO import CityDAO
from project.com.dao.DriverJourneyDAO import DriverJourneyDAO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.SharingTypeDAO import SharingTypeDAO
from project.com.dao.StateDAO import StateDAO
from project.com.dao.UserDAO import UserDAO
from project.com.dao.UserJourneyDAO import UserJourneyDAO
from project.com.vo.CityVO import CityVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.StateVO import StateVO
from project.com.vo.UserJourneyVO import UserJourneyVO
from project.com.vo.UserVO import UserVO


@app.route('/user/loadUserJourney', methods=['GET'])
def userLoadUserJourney():
    try:
        if adminLoginSession() == 'user':
            sharingTypeDAO = SharingTypeDAO()
            sharingTypeVOList = sharingTypeDAO.viewSharingType()

            stateDAO = StateDAO()
            stateVOList = stateDAO.viewState()

            cityDAO = CityDAO()
            cityVOList = cityDAO.viewCity()

            return render_template('user/addUserJourney.html', sharingTypeVOList=sharingTypeVOList,
                                   stateVOList=stateVOList, cityVOList=cityVOList, )
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/user/ajaxSourceCityUserJourney')
def userAjaxSourceCityUserJourney():
    try:
        if adminLoginSession() == 'user':
            cityVO = CityVO()

            cityDAO = CityDAO()

            city_StateId = request.args.get('userJourney_SourceStateId')

            cityVO.city_StateId = city_StateId

            ajaxUserJourneySourceCityList = cityDAO.ajaxSourceCityUserJourney(cityVO)
            print(ajaxUserJourneySourceCityList)
            ajaxUserJourneySourceCityJson = [i.as_dict() for i in ajaxUserJourneySourceCityList]
            print(ajaxUserJourneySourceCityJson)
            return jsonify(ajaxUserJourneySourceCityJson)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/user/ajaxDestinationCityUserJourney')
def userAjaxDestinationCityUserJourney():
    try:
        if adminLoginSession() == 'user':
            cityVO = CityVO()

            cityDAO = CityDAO()

            city_StateId = request.args.get('userJourney_DestinationStateId')

            cityVO.city_StateId = city_StateId

            ajaxUserJourneyDestinationCityList = cityDAO.ajaxDestinationCityUserJourney(cityVO)
            print(ajaxUserJourneyDestinationCityList)
            ajaxUserJourneyDestinationCityJson = [i.as_dict() for i in ajaxUserJourneyDestinationCityList]

            return jsonify(ajaxUserJourneyDestinationCityJson)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/user/insertUserJourney', methods=['POST'])
def userInsertUserJourney():
    try:
        if adminLoginSession() == 'user':

            userJourney_SharingTypeId = request.form['userJourney_SharingTypeId']
            userJourney_SourceStateId = request.form['userJourney_SourceStateId']
            userJourney_SourceCityId = request.form['userJourney_SourceCityId']
            userJourney_DestinationStateId = request.form['userJourney_DestinationStateId']
            userJourney_DestinationCityId = request.form['userJourney_DestinationCityId']
            userJourneyDate = request.form['userJourneyDate']
            userJourneyTime = request.form['userJourneyTime']

            userJourneyVO = UserJourneyVO()
            userJourneyDAO = UserJourneyDAO()

            userJourneyVO.userJourney_SharingTypeId = userJourney_SharingTypeId
            userJourneyVO.userJourney_SourceStateId = userJourney_SourceStateId
            userJourneyVO.userJourney_SourceCityId = userJourney_SourceCityId
            userJourneyVO.userJourney_DestinationStateId = userJourney_DestinationStateId
            userJourneyVO.userJourney_DestinationCityId = userJourney_DestinationCityId
            userJourneyVO.userJourneyDate = userJourneyDate
            userJourneyVO.userJourneyTime = userJourneyTime
            userJourneyVO.userJourney_LoginId = session['session_loginId']

            userJourneyDAO.insertUserJourney(userJourneyVO)

            stateVO = StateVO()
            stateDAO = StateDAO()

            stateVO.stateId = userJourney_SourceStateId
            sourceStateList = stateDAO.viewStateByStateId(stateVO)
            sourceStateName = sourceStateList[0].stateName
            print('sourceStateName>>>>', sourceStateName)

            stateVO.stateId = userJourney_DestinationStateId
            destinatioStateList = stateDAO.viewStateByStateId(stateVO)
            destinationStateName = destinatioStateList[0].stateName
            print('destinationStateName>>>>', destinationStateName)

            cityVO = CityVO()
            cityDAO = CityDAO()

            cityVO.cityId = userJourney_SourceCityId
            sourceCityList = cityDAO.viewCityByCityId(cityVO)
            sourceCityName = sourceCityList[0].cityName
            print('sourceCityName>>>>', sourceCityName)

            cityVO.cityId = userJourney_DestinationCityId
            destinationCityList = cityDAO.viewCityByCityId(cityVO)
            destinationCityName = destinationCityList[0].cityName
            print('destinationCityName>>>>', destinationCityName)

            driverJourneyDAO = DriverJourneyDAO()
            driverJourneyVOList = driverJourneyDAO.findDriver_LoginId(userJourneyVO)
            print('driverJourneyVOList>>>>>', driverJourneyVOList)

            if len(driverJourneyVOList) != 0:
                for i in driverJourneyVOList:
                    driverJourney_LoginId = i.driverJourney_LoginId
                    print('driverJourney_LoginId>>>>>>>>>>>>>>>>', driverJourney_LoginId)

                    loginVO = LoginVO()
                    loginDAO = LoginDAO()
                    loginVO.loginId = driverJourney_LoginId

                    loginVOList = loginDAO.driverUsernameByLoginId(loginVO)
                    print('loginVOList>>>', loginVOList)

                    if len(loginVOList) != 0:
                        loginUsername = loginVOList[0].loginUsername
                        print('loginUsername>>>>', loginUsername)
                    else:
                        pass

                    userVO = UserVO()
                    userDAO = UserDAO()

                    userVO.user_LoginId = session['session_loginId']
                    userVOList = userDAO.userDetailsByLoginId(userVO)

                    if len(userVOList) != 0:
                        userContact = userVOList[0].userContact
                        print('userContact>>>', userVOList)

                    # sender = "travelingtransport1@gmail.com"
                    #
                    # receiver = loginUsername
                    #
                    # msg = MIMEMultipart()

                    textMsg = 'SourceState:{}\n\nSourceCity:{}\n\nDestinationState:{}\n\nDestinationCity:{}\n\nDate:{}\n\nTime:{}\n\nUserContact:{}'.format(
                        sourceStateName, sourceCityName, destinationStateName, destinationCityName, userJourneyDate,
                        userJourneyTime, userContact)

                    print(textMsg, "--------User Insert journey-----------")

                    # msg['From'] = sender
                    #
                    # msg['To'] = receiver
                    #
                    # msg['Subject'] = "User Journey Details"
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
                else:
                    pass

            return redirect(url_for('userViewUserJourney'))
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/user/viewUserJourney', methods=['GET'])
def userViewUserJourney():
    try:
        if adminLoginSession() == 'user':
            userJourneyVO = UserJourneyVO()
            userJourneyDAO = UserJourneyDAO()
            userJourneyVO.userJourney_LoginId = session['session_loginId']
            userSourceJourneyVOList = userJourneyDAO.viewUserSourceJourney(userJourneyVO)
            userDestinationJourneyVOList = userJourneyDAO.viewUserDestinationJourney(userJourneyVO)
            print(userSourceJourneyVOList)
            print(userDestinationJourneyVOList)

            userJourneyListLength = len(userSourceJourneyVOList)

            return render_template('user/viewUserJourney.html', userSourceJourneyVOList=userSourceJourneyVOList,
                                   userDestinationJourneyVOList=userDestinationJourneyVOList,
                                   userJourneyListLength=userJourneyListLength)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/user/deleteUserJourney', methods=['GET'])
def userDeleteUserJourney():
    try:
        if adminLoginSession() == 'user':
            userJourneyVO = UserJourneyVO()
            userJourneyDAO = UserJourneyDAO()

            userJourneyId = request.args.get('userJourneyId')

            userJourneyVO.userJourneyId = userJourneyId

            userJourneyDAO.deleteUserJourney(userJourneyId)

            return redirect(url_for('userViewUserJourney'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/user/editUserJourney', methods=['GET'])
def userEditUserJourney():
    try:
        if adminLoginSession() == 'user':

            userJourneyVO = UserJourneyVO()

            userJourneyDAO = UserJourneyDAO()

            sharingTypeDAO = SharingTypeDAO()

            stateDAO = StateDAO()

            cityDAO = CityDAO()

            userJourneyId = request.args.get('userJourneyId')

            userJourneyVO.userJourneyId = userJourneyId

            userSourceJourneyVOList = userJourneyDAO.editUserJourney(userJourneyVO)
            userDestinationJourneyVOList = userJourneyDAO.editUserJourney(userJourneyVO)

            sharingTypeVOList = sharingTypeDAO.viewSharingType()

            stateVOList = stateDAO.viewState()

            cityVOList = cityDAO.viewCity()

            return render_template('user/editUserJourney.html', userSourceJourneyVOList=userSourceJourneyVOList,
                                   userDestinationJourneyVOList=userDestinationJourneyVOList,
                                   sharingTypeVOList=sharingTypeVOList, stateVOList=stateVOList,
                                   cityVOList=cityVOList, )
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/user/updateUserJourney', methods=['POST'])
def userUpdateUserJourney():
    try:
        if adminLoginSession() == 'user':
            userJourney_SharingTypeId = request.form['userJourney_SharingTypeId']
            userJourney_SourceStateId = request.form['userJourney_SourceStateId']
            userJourney_SourceCityId = request.form['userJourney_SourceCityId']
            userJourney_DestinationStateId = request.form['userJourney_DestinationStateId']
            userJourney_DestinationCityId = request.form['userJourney_DestinationCityId']
            userJourneyDate = request.form['userJourneyDate']
            userJourneyTime = request.form['userJourneyTime']

            userJourneyVO = UserJourneyVO()
            userJourneyDAO = UserJourneyDAO()

            userJourneyVO.userJourney_SharingTypeId = userJourney_SharingTypeId
            userJourneyVO.userJourney_SourceStateId = userJourney_SourceStateId
            userJourneyVO.userJourney_SourceCityId = userJourney_SourceCityId
            userJourneyVO.userJourney_DestinationStateId = userJourney_DestinationStateId
            userJourneyVO.userJourney_DestinationCityId = userJourney_DestinationCityId
            userJourneyVO.userJourneyDate = userJourneyDate
            userJourneyVO.userJourneyTime = userJourneyTime
            userJourneyVO.userJourney_LoginId = session['session_loginId']

            userJourneyDAO.updateUserJourney(userJourneyVO)

            return redirect(url_for('userViewUserJourney'))
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)

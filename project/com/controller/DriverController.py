import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template, redirect

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.DriverDAO import DriverDAO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.DriverVO import DriverVO
from project.com.vo.LoginVO import LoginVO


@app.route('/driver/loadDriver', methods=['GET'])
def adminLoadDriver():
    try:
        return render_template('driver/register.html')
    except Exception as ex:
        print(ex)


@app.route('/driver/insertDriver', methods=['POST'])
def driverInsertDriver():
    try:
        loginUsername = request.form['loginUsername']

        loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
        print("password=", loginPassword)

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        # # =========== Mail Send Functionality ===============
        # sender = "travelingtransport1@gmail.com"
        #
        # receiver = loginUsername
        #
        # msg = MIMEMultipart()
        #
        # msg['From'] = sender
        #
        # msg['To'] = receiver
        #
        # msg['Subject'] = "PYTHON PASSWORD"
        #
        # msg.attach(MIMEText(loginPassword, 'plain'))
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

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginRole = "driver"
        loginVO.loginStatus = "active"
        loginDAO.insertLogin(loginVO)

        driverFirstName = request.form['driverFirstName']
        driverLastName = request.form['driverLastName']
        driverGender = request.form['driverGender']
        driverAddress = request.form['driverAddress']
        driverBirthDate = request.form['driverBirthDate']
        driverContact = request.form['driverContact']

        driverVO = DriverVO()
        driverDAO = DriverDAO()

        driverVO.driverFirstName = driverFirstName
        driverVO.driverLastName = driverLastName
        driverVO.driverGender = driverGender
        driverVO.driverAddress = driverAddress
        driverVO.driverBirthDate = driverBirthDate
        driverVO.driverContact = driverContact
        driverVO.driver_LoginId = loginVO.loginId

        driverDAO.insertDriver(driverVO)
        app.logger.info('--------New Driver Created.------------')

        # server.quit()

        return redirect('/')
    except Exception as ex:
        app.logger.error('A warning occurred to Create driver')
        print(ex)


@app.route('/admin/viewDriver')
def adminViewDriver():
    try:
        if adminLoginSession() == 'admin':
            driverDAO = DriverDAO()

            driverVOList = driverDAO.adminViewDriver()
            return render_template('admin/viewDriver.html', driverVOList=driverVOList)

        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

# @app.route('/admin/viewUser')
# def adminViewRegister():
#     try:
#         if adminLoginSession() == "admin":
#             registerDAO = RegisterDAO()
#             registerVOList = registerDAO.viewRegister()
#             print(registerVOList)
#             return render_template("admin/viewUser.html", registerVOList=registerVOList)
#         else:
#             return redirect(url_for("adminLogoutSession"))
#     except Exception as ex:
#         print(ex)

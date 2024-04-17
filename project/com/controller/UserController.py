import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template, redirect

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.UserDAO import UserDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.UserVO import UserVO


@app.route('/user/loadUser', methods=['GET'])
def adminLoadUser():
    try:
        return render_template('user/register.html')
    except Exception as ex:
        print(ex)


@app.route('/user/insertUser', methods=['POST'])
def userInsertUser():
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
        loginVO.loginRole = "user"
        loginVO.loginStatus = "active"
        loginDAO.insertLogin(loginVO)
        # print(loginVO, "000000000 login VO")

        # print("loginId", loginVO.loginId)

        userFirstName = request.form['userFirstName']
        userLastName = request.form['userLastName']
        userGender = request.form['userGender']
        userAddress = request.form['userAddress']
        userBirthDate = request.form['userBirthDate']
        userContact = request.form['userContact']

        userVO = UserVO()
        userDAO = UserDAO()

        userVO.userFirstName = userFirstName
        userVO.userLastName = userLastName
        userVO.userGender = userGender
        userVO.userAddress = userAddress
        userVO.userBirthDate = userBirthDate
        userVO.userContact = userContact
        userVO.user_LoginId = loginVO.loginId


        userDAO.insertUser(userVO)
        app.logger.info('--------New User Created.------------')

        # server.quit()

        return redirect('/')
    except Exception as ex:
        app.logger.error('A warning occurred to Create user.')
        print(ex)


@app.route('/admin/viewUser')
def adminViewUser():
    try:
        if adminLoginSession() == 'admin':
            userDAO = UserDAO()
            userVOList = userDAO.adminViewUser()
            return render_template('admin/viewUser.html', userVOList=userVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

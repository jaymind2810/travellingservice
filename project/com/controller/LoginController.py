from flask import request, render_template, redirect, url_for, session

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


@app.route('/', methods=['GET'])
def adminLoadLogin():
    try:
        session.clear()
        return render_template('admin/login.html')
    except Exception as ex:
        print(ex)


@app.route("/admin/validateLogin", methods=['POST'])
def adminValidateLogin():
    try:
        loginUsername = request.form['loginUsername']
        loginPassword = request.form['loginPassword']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginStatus = "active"

        loginVOList = loginDAO.validateLogin(loginVO)

        loginDictList = [i.as_dict() for i in loginVOList]

        print(loginDictList)

        lenLoginDictList = len(loginDictList)

        if lenLoginDictList == 0:

            msg = 'Username Or Password is Incorrect !'

            return render_template('admin/login.html', error=msg)

        elif loginVO.loginStatus == 'inactive':

            blockmsg = 'Your account access is temporary Blocked by Admin !'

            return render_template('admin/login.html', error=blockmsg)


        else:

            for row1 in loginDictList:

                loginId = row1['loginId']

                loginUsername = row1['loginUsername']

                loginRole = row1['loginRole']

                session['session_loginId'] = loginId

                session['session_loginUsername'] = loginUsername

                session['session_loginRole'] = loginRole

                session.permanent = True

                if loginRole == 'admin':
                    return redirect(url_for('adminLoadDashboard'))

                elif loginRole == 'driver':
                    return redirect(url_for('driverLoadDashboard'))

                elif loginRole == 'user':
                    return redirect(url_for('userLoadDashboard'))


    except Exception as ex:
        print(ex)


@app.route('/admin/loadDashboard', methods=['GET'])
def adminLoadDashboard():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/index.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/driver/loadDashboard', methods=['GET'])
def driverLoadDashboard():
    try:
        if adminLoginSession() == 'driver':
            return render_template('driver/index.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/user/loadDashboard', methods=['GET'])
def userLoadDashboard():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/index.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/loginSession')
def adminLoginSession():
    try:
        if 'session_loginId' and 'session_loginRole' in session:

            if session['session_loginRole'] == 'admin':

                return 'admin'

            elif session['session_loginRole'] == 'driver':

                return 'driver'

            elif session['session_loginRole'] == 'user':

                return 'user'

            print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")

        else:

            print("<<<<<<<<<<<<<<<<False>>>>>>>>>>>>>>>>>>>>")

            return False
    except Exception as ex:
        print(ex)


@app.route("/admin/logoutSession", methods=['GET'])
def adminLogoutSession():
    try:
        session.clear()
        return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/admin/blockDriver')
def adminBlockDriver():
    try:
        if adminLoginSession() == 'admin':
            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginId = request.args.get('loginId')
            loginStatus = 'inactive'

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            loginDAO.adminBlockDriver(loginVO)

            return redirect(url_for('adminViewDriver'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/unblockDriver')
def adminUnblockDriver():
    try:
        if adminLoginSession() == 'admin':
            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginId = request.args.get('loginId')
            loginStatus = 'active'

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            loginDAO.adminBlockDriver(loginVO)

            return redirect(url_for('adminViewDriver'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/blockUser')
def adminBlockUser():
    try:
        if adminLoginSession() == 'admin':
            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginId = request.args.get('loginId')
            loginStatus = 'inactive'

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            loginDAO.adminBlockDriver(loginVO)

            return redirect(url_for('adminViewUser'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/unblockUser')
def adminUnblockUser():
    try:
        if adminLoginSession() == 'admin':
            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginId = request.args.get('loginId')
            loginStatus = 'active'

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            loginDAO.adminBlockDriver(loginVO)

            return redirect(url_for('adminViewUser'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

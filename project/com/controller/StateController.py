from flask import request, render_template, redirect, url_for

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.StateDAO import StateDAO
from project.com.vo.StateVO import StateVO


@app.route('/admin/loadState', methods=['GET'])
def adminLoadState():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addState.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertState', methods=['POST'])
def adminInsertState():
    try:
        if adminLoginSession() == 'admin':
            stateName = request.form['stateName']
            stateDescription = request.form['stateDescription']

            stateVO = StateVO()
            stateDAO = StateDAO()

            stateVO.stateName = stateName
            stateVO.stateDescription = stateDescription

            stateDAO.insertState(stateVO)

            return redirect(url_for('adminViewState'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewState', methods=['GET'])
def adminViewState():
    try:
        if adminLoginSession() == 'admin':
            stateDAO = StateDAO()
            stateVOList = stateDAO.viewState()
            print("__________________", stateVOList)
            return render_template('admin/viewState.html', stateVOList=stateVOList)
        else:
            return redirect(url_for('adminLogoutSession'))


    except Exception as ex:
        print(ex)


@app.route('/admin/deleteState', methods=['GET'])
def adminDeleteState():
    try:
        if adminLoginSession() == 'admin':
            stateVO = StateVO()

            stateDAO = StateDAO()

            stateId = request.args.get('stateId')

            stateVO.stateId = stateId

            stateDAO.deleteState(stateVO)

            return redirect(url_for('adminViewState'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/editState', methods=['GET'])
def adminEditState():
    try:
        if adminLoginSession() == 'admin':
            stateVO = StateVO()

            stateDAO = StateDAO()

            stateId = request.args.get('stateId')

            stateVO.stateId = stateId

            stateVOList = stateDAO.editState(stateVO)

            print("=======stateVOList=======", stateVOList)

            print("=======type of stateVOList=======", type(stateVOList))

            return render_template('admin/editState.html', stateVOList=stateVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/updateState', methods=['POST'])
def adminUpdateState():
    try:
        if adminLoginSession() == 'admin':
            stateId = request.form['stateId']
            stateName = request.form['stateName']
            stateDescription = request.form['stateDescription']

            stateVO = StateVO()
            stateDAO = StateDAO()

            stateVO.stateId = stateId
            stateVO.stateName = stateName
            stateVO.stateDescription = stateDescription

            stateDAO.updateState(stateVO)

            return redirect(url_for('adminViewState'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)

from flask import request, render_template, redirect, url_for

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.SharingTypeDAO import SharingTypeDAO
from project.com.vo.SharingTypeVO import SharingTypeVO


@app.route('/admin/loadSharingType', methods=['GET'])
def adminLoadSharingType():
    try:
        if adminLoginSession() == 'admin':

            return render_template('admin/addSharingType.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertSharingType', methods=['POST'])
def adminInsertSharingType():
    try:
        if adminLoginSession() == 'admin':

            sharingTypeName = request.form['sharingTypeName']

            sharingTypeVO = SharingTypeVO()
            sharingTypeDAO = SharingTypeDAO()

            sharingTypeVO.sharingTypeName = sharingTypeName

            sharingTypeDAO.insertSharingType(sharingTypeVO)

            return redirect(url_for('adminViewSharingType'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewSharingType', methods=['GET'])
def adminViewSharingType():
    try:
        if adminLoginSession() == 'admin':

            sharingTypeDAO = SharingTypeDAO()
            sharingTypeVOList = sharingTypeDAO.viewSharingType()
            print("__________________", sharingTypeVOList)
            return render_template('admin/viewSharingType.html', sharingTypeVOList=sharingTypeVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteSharingType', methods=['GET'])
def adminDeleteSharingType():
    try:
        if adminLoginSession() == 'admin':

            sharingTypeVO = SharingTypeVO()

            sharingTypeDAO = SharingTypeDAO()

            sharingTypeId = request.args.get('sharingTypeId')

            sharingTypeVO.sharingTypeId = sharingTypeId

            sharingTypeDAO.deleteSharingType(sharingTypeVO)

            return redirect(url_for('adminViewSharingType'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/editSharingType', methods=['GET'])
def adminEditSharingType():
    try:
        if adminLoginSession() == 'admin':

            sharingTypeVO = SharingTypeVO()

            sharingTypeDAO = SharingTypeDAO()

            sharingTypeId = request.args.get('sharingTypeId')

            sharingTypeVO.sharingTypeId = sharingTypeId

            sharingTypeVOList = sharingTypeDAO.editSharingType(sharingTypeVO)

            print("=======sharingTypeVOList=======", sharingTypeVOList)

            print("=======type of sharingTypeVOList=======", type(sharingTypeVOList))

            return render_template('admin/editSharingType.html', sharingTypeVOList=sharingTypeVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/updateSharingType', methods=['POST'])
def adminUpdateSharingType():
    try:
        if adminLoginSession() == 'admin':

            sharingTypeId = request.form['sharingTypeId']
            sharingTypeName = request.form['sharingTypeName']

            sharingTypeVO = SharingTypeVO()
            sharingTypeDAO = SharingTypeDAO()

            sharingTypeVO.sharingTypeId = sharingTypeId
            sharingTypeVO.sharingTypeName = sharingTypeName

            sharingTypeDAO.updateSharingType(sharingTypeVO)

            return redirect(url_for('adminViewSharingType'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)

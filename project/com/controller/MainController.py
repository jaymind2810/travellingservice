from flask import render_template, session

from project import app

# @app.route('/', methods=['GET'])
# def adminLoadLogin():
#     try:
#         session.clear()
#         return render_template('admin/login.html')
#     except Exception as ex:
#         print(ex)


# @app.route('/admin/viewUser')
# def adminViewUser():
#     try:
#         if adminLoginSession() == 'admin':
#             return render_template('admin/viewUser.html')
#         else:
#             return redirect(url_for('adminLogoutSession'))
#
#     except Exception as ex:
#         print(ex)

# @app.route('/driver/viewUserJourney')
# def driverViewUserJourney():
#     try:
#         return render_template('driver/viewUserJourney.html')
#
#     except Exception as ex:
#         print(ex)
#
# @app.route('/user/viewDriverJourney')
# def userViewDriverJourney():
#     try:
#         return render_template('user/viewDriverJourney.html')
#
#     except Exception as ex:
#         print(ex)

# @app.route('/driver/viewDriverJourney')
# def driverViewJourney():
#     try:
#         return render_template('driver/viewDriverJourney.html')
#
#     except Exception as ex:
#         print(ex)
#
# @app.route('/user/loadUserJourney')
# def userLoadJourney():
#     try:
#         return render_template('user/addUserJourney.html')
#
#     except Exception as ex:
#         print(ex)
#
# @app.route('/user/viewUserJourney')
# def userViewJourney():
#     try:
#         return render_template('user/viewUserJourney.html')
#
#     except Exception as ex:
#         print(ex)

@app.route('/user/loadContact')
def userLoadContact():
    try:
        return render_template('user/contact.html')

    except Exception as ex:
        print(ex)

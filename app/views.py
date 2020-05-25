from flask import Blueprint, render_template, request, Response, redirect, url_for, session

view_blue = Blueprint('view_1', __name__)


@view_blue.route('/home')
def index():
    usern=session.get('users')
    # usern =request.cookies.get('users')#users为set_cookie的赋值
    return render_template('index.html',use=usern)#use为html变量


@view_blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user1=request.form.get('user')
        if user1 == "zgx":
            return True
        # user1 = request.form.get('user')
        # session['users'] =user1
        # resp=Response(response='yeah,%s' % user1)
        # # resp.set_cookie('users',user1)#操作cookie  赋值给users
        # return resp
        # return username



@view_blue.route('/quit')
def quit():
    session.clear()
    resp=redirect(url_for('view_1.index'))
    # resp.delete_cookie('users')
    return resp
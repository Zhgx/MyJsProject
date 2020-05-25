from flask import Blueprint, url_for

view1_blue = Blueprint('view1', __name__)


@view1_blue.route('/for')
def hello_world():
    return 'Hi'


@view1_blue.route('/url_for')
def url():
    result = url_for('view1.hello_world')
    return  result

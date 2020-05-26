#coding=UTF-8
from flask import Flask, render_template, request, jsonify,url_for
#创建应用实例，接受来自web服务器的请求
app = Flask(__name__)

#通过路由找到对应的视图函数，然后处理
@app.route('/')
def index():
    return render_template('ajaxIndex.html')

@app.route('/ajax', methods=['POST'])
def ajax_post():
    name=request.values['name']
    password=request.values['password']
    if name == 'anders'and password == '123':
        return "True"
    else:
        return "False"
@app.route('/user_info',methods=['GET'])
def user_info():
    return render_template('someinfo.html')



@app.route('/thumbnail',methods=['GET'])
def tumb_info():
    return render_template('thumbnail.html')
if __name__ == '__main__':
    app.run(debug=True)
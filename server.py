# coding: UTF-8

from setting import session
from flask import Flask, render_template, request, redirect, url_for,jsonify
from sqlalchemy.ext.declarative import DeclarativeMeta
import sqlalchemy.orm
from user import *
from memoList import *
import json
from setting import Base
from setting import ENGINE

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mypage',methods=['GET', 'POST'])
def mypage():
    if request.method == 'POST':
		session.name = request.form['name']
		name=session.name
		password = request.form['password']
		user = User()
		users = session.query(User).all()
		session.add(user)  
		session.commit()
		for user in users:
			if(user.name == name and user.password == password):
				memoList = MemoList()
				memos = session.query(MemoList).all()
				session.add(memoList)  
				session.commit()
				return render_template('mypage.html',name=name, password=password)
			else:
				return redirect(url_for('index'))

@app.route('/regist',methods=['GET', 'POST'])
def regist():
	if request.method == 'POST':
		category = request.form['category']
		main = request.form['main']
		link = request.form['link']
		memoList = MemoList()
		memoList.category = category
		memoList.main = main
		memoList.link = link
		memos = session.query(MemoList).all()
		session.add(memoList)
		session.commit()
		return render_template('mypage.html',name=session.name,memo=memos)

@app.route('/postText', methods=['POST'])
def getAllList():
	memoList = MemoList()
	result = session.query(MemoList).all()
	response = []
	for results in result:
		response.append(results.category)
	
	
	result = json.dumps(result, cls=AlchemyEncoder)#jsonify(MemoListSchema(many=True).dump(response))
	print('result')
	print(result)
   	return result


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def main():
	app.debug = True
	app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
	main()

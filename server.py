# coding: UTF-8

from setting import session
from flask import Flask, render_template, request, redirect, url_for
from user import *
from memoList import *

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
		return render_template('mypage.html',name=session.name)


def main():
	app.debug = True
	app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
	main()

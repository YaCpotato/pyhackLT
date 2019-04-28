# coding: UTF-8

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mypage',methods=['GET', 'POST'])
def mypage():
    if request.method == 'POST':
		name = request.form['name']
		password = request.form['password']
		if(name == "admin" and password == "admin"):
			return render_template('mypage.html',name=name, password=password)
	

def main():
	app.debug = True
	app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
	main()

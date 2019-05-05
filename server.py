# coding: UTF-8

from setting import session
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.ext.declarative import DeclarativeMeta
from user import *
from memoList import *
import json
from setting import Base
from setting import ENGINE

app = Flask(__name__)

#root
@app.route('/')
def index():
	return render_template('index.html')

#mypageへのリクエスト（ログインリクエスト）
@app.route('/mypage',methods=['POST'])
def mypage():

	#postリクエストが飛んできたら
    if request.method == 'POST':

		#request内のユーザー名、パスワードを変数に格納
		name = request.form['name']
		password = request.form['password']

		#userテーブルのセッションを作成
		user = User()

		#nameカラムがnameのレコードを持ってくる
		users = session.query(User).\
    	filter(User.name == name).\
    	all()

		#27行目でsessionのクエリを発行したので追加してコミットする
		session.add(user)  
		session.commit()

		#持ってきたレコードを順に見ていく
		for user in users:
			if(user.password == password):

				#passwordが合っているのが見つかったら、idとnameを
				session.name = name

				#mypageのHTMLをレンダリング
				return render_template('mypage.html',name=session.name)
			else:
				#合ってなかったら、ログイン失敗、リダイレクト
				return redirect(url_for('index'))

#メモ登録リクエストがきたら
@app.route('/regist',methods=['POST'])
def regist():
	if request.method == 'POST':

		#カテゴリとメイン項目を空欄では受け付けない
		if(len(request.form['category'])!=0 or len(request.form['main'])!=0):

			#requestで飛んできたカテゴリ、メイン、リンクを変数に格納
			category = request.form['category']
			main = request.form['main']
			link = request.form['link']

			#memoListテーブルのセッションを作成
			memoList = MemoList()

			#格納した変数をそれぞれテーブルのレコードにセットする
			memoList.category = category
			memoList.main = main
			memoList.link = link

			#sessionのクエリを発行したので追加してコミットする
			session.add(memoList)
			session.commit()

			#mypageにレンダリング
			return render_template('mypage.html',name=session.name)
		else:
			#登録に失敗したらリダイレクト
			return redirect(url_for('/mypage'))
	

		
#メモリストのgetter
@app.route('/getMemo', methods=['POST'])
def getAllList():

	#memoListセッションを作成
	memoList = MemoList()

	#memoListテーブルの全レコードを持ってくる
	result = session.query(MemoList).all()
	
	#list型のresultをjsonにダンプ
	result = json.dumps(result, cls=AlchemyEncoder)

	#resultをリターンする-->Javascriptのajaxのresponseに入る
   	return result


#list型をjsonにしてくれるスゴイやつ
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

#サーバーのデバッグモードの有無とipとポートの選択
def main():
	app.debug = True
	app.run(host='127.0.0.1', port=8080)

#おまじない
if __name__ == '__main__':
	main()

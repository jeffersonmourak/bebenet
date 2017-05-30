#users.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.userBB import UserModelBB

class bbUser(object):
		
	def on_post(self, req, resp):
		db = MySQLdb.connect (host = "localhost",user = "root",passwd = "ronaldo",db = "BDnet",charset="utf8", use_unicode = True)
		cursor = db.cursor()
		body = req.stream.read()
		print body
		newuserBBsql = self.mountUser(body)
		print body
		equery = "INSERT INTO usuario (cpf,nome,idade,nFilhos,login,senha) VALUES (%s, %s, %s, %s,%s,%s)"

		try:
			cursor.execute(equery, (newuserBBsql['cpf'], newuserBBsql['nome'], newuserBBsql['idade'], newuserBBsql['nFilhos'],newuserBBsql['login'],newuserBBsql['senha'],))
			cursor.execute("SELECT LAST_INSERT_ID() FROM usuario");
			result = {'id': int(cursor.fetchone()[0])}
			resp.body = json.dumps(result)
			resp.status = falcon.HTTP_201 
			db.commit()
		except:
			db.rollback()
			print "Insert ERROR: ", sys.exc_info()[0]
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao alterar o banco de dados! Usuario nao foi inserido."
		db.close()

	def mountUser(self, uData):
		return json.loads(uData)

class bbUserLogin(object):
	def on_get(self, req, resp, login, senha):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "root",passwd = "ronaldo",db = "BDnet",charset="utf8", use_unicode = True)
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  

		sql = "SELECT true FROM usuario WHERE login = '%s' and senha = '%s'" % (login, senha)
		cursor.execute(sql)

		rows = cursor.rowcount

		result = {'logado' : True}
		print "passou"
		if(rows <= 0):
			resp.status = falcon.HTTP_403
			result = {'logado' : False}

		resp.body = json.dumps(result)

		db.close()  

	def mountUser(self, uData):
		return json.loads(uData)

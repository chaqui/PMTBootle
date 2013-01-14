#encoding: utf-8
from bottle import get, run, request, post, error, debug
import sqlite3
bandera= False
cabecera='''<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title>'''
cabecera2='''</title>
</head>
<body>'''
pie='''</body>
</html>'''
@error(404)
def error():
	return "error pagina no encontrada"
@get('/login')
def login_form():
	return cabecera+"login"+cabecera2+'''<form method="POST" action="/login">
		Porfavor ingrese los siguientes datos para el login:
		<br>
		nombre:
		<input type="text"name="name">
		<br>
		contraseña:
		<input type="password" name="password">
		<br>
		<input type="submit" value="login"/>
		<br>
		<a href="/registro">Registrate</a>
		</form>'''+pie
@post('/login')
def login_submit():
	nombre=request.forms.get('name')
	passw=request.forms.get('password')
	resp=buscar(nombre,passw,True)
	if resp==False:
		print"False"
		return cabecera+"error de login "+cabecera2+'''error debes de <a href="/registrar">registrate</a>'''+pie
	else:
		print"true"
		bandera=False
		return cabecera+"Binevenido "+cabecera2+'''Bienvenido'''+pie

@get ('/registro')
def formRegistrarse():
	return cabecera+"registrarse"+cabecera2+'''
	<form method="POST" action="/login">
		Porfavor ingrese los siguientes datos para el login:
		<br>
		nombre:
		<input type="text"name="name">
		<br>
		contraseña:
		<input type="password" name="password">
		<br>
		repita su contraseña:
		<input type="password" name="password2">
		<br>
		<input type="submit" value="login"/>
		<br>
		<a href="/registro">Registrate</a>
		</form>
	'''+pie
@post ('/registro')
def registrarse():
	nombre=request.forms.get('name')
	passw=request.forms.get('password')
	passw1=request.forms.get('password2')
	if passw1== passw:
		if buscar(nombre,passw,False):
			pass
	else:
		return cabecera+"registrarse"+cabecera2+'''
		Error ingrese bien las contraseñas
		<form method="POST" action="/login">
		Porfavor ingrese los siguientes datos para el login:
		<br>
		nombre:
		<input type="text"name="name">
		<br>
		contraseña:
		<input type="password" name="password">
		<br>
		repita su contraseña:
		<input type="password" name="password2">
		<br>
		<input type="submit" value="login"/>
		<br>
		<a href="/registro">Registrate</a>
		</form>
	'''+pie
def buscar(nom,con,b):
	con=sqlite3.connect('bdapp.db')
	if b:
		con.row_factory = sqlite3.Row
		cursor=con.cursor()
		nom1=(nom,)
		cursor.execute("SELECT * FROM Usuarios")
		b = cursor.fetchone()
		cursor.execute("SELECT * FROM Usuarios WHERE Nombre = '%s'" % nom1)
		a =cursor.fetchone()
		if a==None:
			return False
		else:
			if a['Contraseña']==con:
				return True
			else:
				return False
	else:
		cursor.execute("SELECT * FROM Usuarios WHERE Nombre = '%s'" % nom1)
		a =cursor.fetchone()
		if a==None:
			return True
		else:
			return False
debug(True)
run(host="localhost",port=8080)
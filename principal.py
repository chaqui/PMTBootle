from bottle import get, run, request, post, error
import sqlite3
@error(404)
def error():
	return "error pagina no encontrada"
def login_form():
	return '''<form method="POST" action="/login">
		<input type="text"name="name"/>
		<input type="password"  name="password"/>
		<input type="submit"/>
		<a href="/registro">Registrate</a>
		</form>'''

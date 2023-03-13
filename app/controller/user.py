from db import connection
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import datetime

class User:
    def set_password(self, password):
        password_hash = generate_password_hash(password)
        return password_hash


    def check_password(self, password_hash, password):
        return check_password_hash(password_hash, password)


    def get_user(self, email):
        query = f"SELECT * FROM user WHERE email = '{email}'"
        result = connection(query, 'select')
        return result


    def login(self):
        email = request.form['email']
        password = request.form['password']

        user = self.get_user(email)

        if not user:
            response = {
                'message': 'Email tidak terdaftar'
            }
            return response

        if not self.check_password(user[0]['password'], password):
            response = {
                'message': 'Password tidak tepat'
            }
            return response

        data = {
            "id_user": user[0]['id_user'],
            "name": user[0]['name'],
            "email": user[0]['email'],
            "role": user[0]['role']
        }

        expires = datetime.timedelta(days=1)
        access_token = create_access_token(data, fresh=True, expires_delta=expires)

        response = {
            'message': 'Login berhasil',
            'access_token': access_token,
        }

        return response
    

    def insert_user(self, name, email, password, role):
        query = f"INSERT INTO user (name, email, password, role) VALUES ('{name}', '{email}', '{password}', {role})"
        connection(query, 'insert')


    def register(self):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        secure_password = self.set_password(password)

        self.insert_user(name, email, secure_password, role)

        return {
            'name': name,
            'email': email,
            'role': role,
            'password': secure_password
        }

# import aplikasi flask, OS, flash, jsonify, redirect, dan render_template untuk dipakai di web kita
import os
# import SQL untuk akses database
from cs50 import SQL
# import flash untuk notifikasi pada web
# import jsonify untuk memformat data
# import redirect dan render_template untuk berpimdah halaman web
# import request dan session untuk mengakses data
from flask import Flask

#mengatur nama aplikasi
app = Flask(__name__)

#mengatur URI (Universal resource Identifier), dan apa yang ditampilkan jika URI tsb diakses 
@app.route('/') #ketika alamat http://127.0.0.1:5000/ dipanggil, maka server akan mengeksekusi hello()
def hello(): # function dengan nama hello
    return 'hello, world!'

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return 'halaman login'   
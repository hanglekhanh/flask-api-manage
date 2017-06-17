'''./main.py'''
from model.meeting import Meeting
from  controller import controller
from flask import Flask
from flask import request
# app = Flask(__name__)


# @app.route('/')
# # hello world
# def hello_world():
#     return 'Hello, World!'


# @app.route('/meeting', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def controller_meeting():
#     if request.method == 'GET':
#         curr_meeting = Meeting(
#             start_time="0:00 AM", end_time="12:00 AM", id_meeting="123", name_meeting="hello")
#         return curr_meeting.print_info_meeting()
#     if request.method == 'POST':
#         return 'POST'
#     if request.method == 'PUT':
#         return 'PUT'
#     if request.method == 'DELETE':
#         return 'DELETE'

print('Welcome to Management Controller Application')
controller.controller()

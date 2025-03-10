from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

from waitress import serve

import graphene
from graphene import ObjectType, String, Int, JSONString, Float

import json

import threading

import time

import JoyStick
import Serial


joystick_instance = JoyStick.JoyStick()
port = Serial.choose_serial_port()
serial_instance = Serial.SerialProtocolHandler(port, 115200)


class JoystickField(ObjectType):
    available = graphene.Boolean()
    axes = graphene.List(graphene.Float)
    buttons = graphene.List(graphene.Int)
    hats = graphene.List(graphene.Int)


class AttitudeField(ObjectType):
    pitch = graphene.Float()
    roll = graphene.Float()
    yaw = graphene.Float()


class JointField(ObjectType):
    left_thruster_joint = graphene.Float()
    right_thruster_joint = graphene.Float()
    end_joint_2 = graphene.Float()
    end_joint_1 = graphene.Float()


class Query(ObjectType):
    joystick = graphene.Field(JoystickField)
    attitude = graphene.Field(AttitudeField)
    joint = graphene.Field(JointField)
    depth = graphene.Float()

    def resolve_joystick(self, info):
        global joystick_instance

        if not joystick_instance.available:
            joystick_instance.init()
            return {"available": False, "axes": {}, "buttons": {}, "hats": {}}

        data = joystick_instance.get()
        return data

    def resolve_attitude(self, info):
        global serial_instance
        data = serial_instance.get_data(Serial.Data.ATTITUDE)
        available = data[1]
        if not available:
            return {"pitch": 0, "roll": 0, "yaw": 0}

        data = data[0]
        return {"pitch": data[1], "roll": data[0], "yaw": data[2]}

    def resolve_joint(self, info):
        global serial_instance
        data = serial_instance.get_data(Serial.Data.SERVO)
        available = data[1]
        if not available:
            return {
                "left_thruster_joint": 0,
                "right_thruster_joint": 0,
                "end_joint_2": 0,
                "end_joint_1": 0,
            }
        data = data[0]
        return {
            "left_thruster_joint": data[0],
            "right_thruster_joint": data[1],
            "end_joint_2": data[2],
            "end_joint_1": data[3],
        }

    def resolve_depth(self, info):
        global serial_instance
        data = serial_instance.get_data(Serial.Data.DEPTH)
        available = data[1]
        if not available:
            return 0
        return data[0][0]


# 定义一个 GraphQL Schema
schema = graphene.Schema(query=Query)


app = Flask(__name__)

CORS(app)

# 添加 GraphQL 视图，指定 schema
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


def serialReceive():
    global serial_instance
    while True:
        serial_instance.receive_data()
        time.sleep(0.01)


if __name__ == "__main__":
    app_thread = threading.Thread(
        target=serve, kwargs={"app": app, "host": "0.0.0.0", "port": 5000}, daemon=True
    )
    app_thread.start()
    while True:
        time.sleep(0.01)
        joystick_instance.update()

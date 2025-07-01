from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

from waitress import serve

import graphene

import threading

import time

import json

import JoyStick
import Client
# import Client


joystick_instance = JoyStick.JoyStick()
client_instance = Client.UDPClient("192.168.1.101", 4567)


class JoystickField(graphene.ObjectType):
    available = graphene.Boolean()
    axes = graphene.List(graphene.Float)
    buttons = graphene.List(graphene.Int)
    hats = graphene.List(graphene.Int)


class AtitudeField(graphene.ObjectType):
    available = graphene.Boolean()
    pitch = graphene.Float()
    roll = graphene.Float()
    yaw = graphene.Float()


class JointField(graphene.ObjectType):
    available = graphene.Boolean()
    left_thruster_joint = graphene.Float()
    right_thruster_joint = graphene.Float()
    end_joint_2 = graphene.Float()
    end_joint_1 = graphene.Float()


class Query(graphene.ObjectType):
    joystick = graphene.Field(JoystickField)
    altitude = graphene.Field(AtitudeField)
    joint = graphene.Field(JointField)
    depth = graphene.Float()
    temperature = graphene.Float()

    def resolve_joystick(self, info):
        del info
        global joystick_instance

        if not joystick_instance.available:
            joystick_instance.init()
            return {"available": False, "axes": {}, "buttons": {}, "hats": {}}

        data = joystick_instance.get()
        return data

    def resolve_altitude(self, info):
        del info
        global client_instance
        data = client_instance.get_data(Client.Data.ATTITUDE)
        available = data[1]
        if not available:
            return {"available": False, "pitch": 0, "roll": 0, "yaw": 0}

        data = data[0]
        return {"available": True, "pitch": data[1], "roll": data[0], "yaw": data[2]}

    def resolve_joint(self, info):
        del info
        global client_instance
        data = client_instance.get_data(Client.Data.SERVO)
        available = data[1]
        if not available:
            return {
                "available": False,
                "left_thruster_joint": 0,
                "right_thruster_joint": 0,
                "end_joint_2": 0,
                "end_joint_1": 0,
            }
        data = data[0]
        return {
            "available": True,
            "left_thruster_joint": data[0],
            "right_thruster_joint": data[1],
            "end_joint_2": data[2],
            "end_joint_1": data[3],
        }

    def resolve_depth(self, info):
        del info
        global client_instance
        data = client_instance.get_data(Client.Data.DEPTH)
        available = data[1]
        if not available:
            return 0
        return data[0][0]

    def resolve_temperature(self, info):
        del info
        global client_instance
        data = client_instance.get_data(Client.Data.TEMPERATURE)
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


# def serialReceive():
#     global client_instance
#     while True:
#         client_instance.receive_data()
#         time.sleep(0.01)


if __name__ == "__main__":
    app_thread = threading.Thread(
        target=serve, kwargs={"app": app, "host": "0.0.0.0", "port": 5000}, daemon=True
    )
    app_thread.start()

    def on_recv(self, data, addr):
        print(f"Received from {addr}: {data}")
        type = json.loads(data.decode("utf-8")).get("type", "str")
        self.data[type] = data
    client_instance.start(on_recv)
    while True:
        time.sleep(0.01)
        joystick_instance.update()
        joystick_data = joystick_instance.get()



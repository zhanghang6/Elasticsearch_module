import time
from flask import Flask, request
from flask_cors import CORS
import json
import backend
import q_first_backend
import q_third_backend

app = Flask(__name__)
CORS(app)


@app.route("/time")
def get_current_time():
    return {"time": time.time()}


@app.route("/get_q_first_list", methods=["GET", "POST"])
def get_q_first_list():
    # 前端数据为b'', 需要先转为字符串，再json解码之后转为字典
    # new_dict = json.loads(request.get_data().decode())
    # print(new_dict['params'])
    """
    get_q_first_list: 获取1、2题的基本数据
    无参数
    return: 数据list, 以node升序排列
    """

    # 从q_first_backend.py函数中调用get_first_all_node()函数返回所有节点的列表信息，新的更改
    q_list = q_first_backend.get_first_all_node()
    return q_list


@app.route("/get_q_first_shard_node", methods=["GET", "POST"])
def get_q_first_shard_node():
    # 前端数据为b'', 需要先转为字符串，再json解码之后转为字典
    new_dict = json.loads(request.get_data().decode())
    print(new_dict["params"])
    """
    get_q_first_shard_node: 根据sh++___ard_node值, 返回对应shard_node结点数据
    name: 结点名字, 值为index&prirep&shard
    params: {
                name: index&prirep&shard
            }
    return: get_q_first_shard_node结点对象的列表(此处应只有一个节点对象)
    """
    # shard_node_list = backend.select_first_shard_node(new_dict["params"]["name"])
    # print(shard_node_list)

    # 从q_first_backend.py函数中调用get_first_selected_index(params)函数返回选取index节点的信息
    shard_node_list = q_first_backend.get_first_shard_node(new_dict["params"]["name"])

    return shard_node_list


@app.route("/get_q_first_index_node", methods=["GET", "POST"])
def get_q_first_index_node():
    # 前端数据为b'', 需要先转为字符串，再json解码之后转为字典
    new_dict = json.loads(request.get_data().decode())
    print("所传递的index参数为：")
    print(new_dict["params"])
    """
    get_q_first_index_node: 根据index, 返回对应index_node结点数据
    name: index
    params: {
                name: index
            }
    return: get_q_first_index_node结点对象的列表
    """

    # index_node_list = backend.select_first_index_node(new_dict["params"]["name"])
    index_node_list = q_first_backend.get_first_index_node(new_dict["params"])
    return index_node_list


@app.route("/get_q_second_connect_list", methods=["GET", "POST"])
def get_q_second_connect_list():
    # 前端数据为b'', 需要先转为字符串，再json解码之后转为字典
    # new_dict = json.loads(request.get_data().decode())
    # print(new_dict['params'])
    """
    get_q_second_connect_list: 返回连线, index = 0存起点index&prirep&shard, index = 1存终点node
    return: 结点对象的列表
    """

    connect_list = [
        ["es_taig_key_20220624&r&0", "data-node-05"],
        ["es_taig_key_20220624&p&0", "data-node-06"],
    ]
    return connect_list


@app.route("/get_q_third_list", methods=["GET", "POST"])
def get_q_third_list():
    """
    get_q_third_list: index_node结点数据, 以physics升序排列
    return: 以physics升序排列结点对象的列表, 如物理机上无虚拟机, 虚拟机数据请用字符串'None'替代
    """
    # q_third_list = backend.get_third_question_list()
    # 调用q_third_backend.py文件中的get_third_question_list()函数，返回虚拟机分配
    # 结果信息
    q_third_list = q_third_backend.get_third_question_list()
    return q_third_list


@app.route("/get_q_physics_node", methods=["GET", "POST"])
def get_q_physics_node():
    # 前端数据为b'', 需要先转为字符串，再json解码之后转为字典
    new_dict = json.loads(request.get_data().decode())
    print(new_dict["params"])
    """
    get_q_physics_node: 根据physics, 返回对应physics结点数据
    params: {
                name: physics
            }
    return: physics_node结点对象的列表
    """
    # physics_node = backend.get_third_q_physics_node(new_dict["params"])
    # 调用q_third_backend.py中的get_third_q_physics_node(params)函数返回指定物理机
    # 上的所有虚拟机的信息
    physics_node = q_third_backend.get_third_q_physics_node(new_dict["params"])
    return physics_node

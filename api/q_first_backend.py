import pandas as pd
import os


"""
本文件为实现第一题返回全部节点信息及指定index节点信息的后端代码实现代码
"""


# 将所有节点分片的信息以列表的形式返回，列表中每个元素为字典
def get_first_all_node():
    # 获取文件的绝对路径
    absolute_path = os.path.abspath("first_second_data.xlsx")
    # 读取excel文件"索引数据"表中第二行作为表头
    df1 = pd.read_excel(
        absolute_path,
        sheet_name="索引数据",
        header=1,
    )
    # 将读取的数据对象转换为字典组成的列表
    index_node = df1.to_dict("records")

    return index_node


# 返回指定节点某一个分片信息的函数
def get_first_shard_node(params):
    # 返回的参数为形如'index&prirep&shard'的字符串，需要先进行分割处理
    list_params = params.split("&")
    # print(list_params)
    # 将参数存储在一个字典中
    conditions = {
        "index": "none",
        "shard": "none",
        "prirep": "none",
    }
    conditions["index"] = list_params[0]
    conditions["shard"] = list_params[2]
    conditions["prirep"] = list_params[1]

    # 调用get_first_all_node()函数得到所有节点分片的信息
    all_node = get_first_all_node()
    # 查询符合conditions中条件的节点信息，并保存在一个新的列表中
    selected_shard_node = [
        d
        for d in all_node
        if all(k in d and str(d[k]) == str(v) for k, v in conditions.items())
    ]
    return selected_shard_node


# 返回某一个index对应的所有分片信息的函数
def get_first_index_node(params):
    # 传递过来的参数形如'{'name': 'es_taig_key_20220626', 'type': 1}'
    conditions = {"index": "none"}
    conditions["index"] = params["name"]
    # 调用get_first_all_node()函数返回所有节点信息
    all_node_list = get_first_all_node()
    selected_index_node = [
        d
        for d in all_node_list
        if all(k in d and d[k] == v for k, v in conditions.items())
    ]

    return selected_index_node

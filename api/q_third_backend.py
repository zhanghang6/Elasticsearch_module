import pandas as pd
import os

"""
本文件为实现第三题计算如何在20台物理机上分配虚拟机达到最大化利用物理机资源的代码实现代码
"""


# 第三问在20台物理机上分配虚拟机来实现最大化资源利用率的后端代码实现
def get_third_question_list():
    # 获取文件的绝对路径
    absolute_path = os.path.abspath("third_data.xlsx")
    # 读取first_second_data.xlsx文件中虚拟机表中的信息，将第一行作为表头
    df1 = pd.read_excel(
        absolute_path,
        sheet_name="虚拟机VM",
        header=0,
    )
    # 将读取的数据的列名设置为"name", "disk", "cpu" 和 "memory"
    df1.columns = ["name", "disk", "cpu", "memory"]

    # 将数据转换为列表的形式
    virtual_machines = df1.to_dict("records")

    # 初始化每台物理机的标准配置
    physical_machine = {"name": "BM-NEW", "cpu": 120, "memory": 512, "disk": 12516}
    # 从excel表中读取物理机的信息

    df2 = pd.read_excel(
        absolute_path,
        sheet_name="物理机BM",
        header=0,
    )
    # 将读取数据的列名依次设置为"name", "disk", "cpu", "memory"
    df2.columns = ["name", "disk", "cpu", "memory"]
    # 将数据转换为列表的形式，其中的元素为字典
    physics_machine = df2.to_dict("records")

    # 分配虚拟机到物理机
    allocation_list = []
    allocation_result = {}
    for vm in virtual_machines:
        allocated = False
        for pm_index, pm in enumerate(physics_machine):
            if all(vm[k] <= pm[k] for k in ("cpu", "memory", "disk")):
                # 分配虚拟机到物理机
                for k in ("cpu", "memory", "disk"):
                    pm[k] -= vm[k]
                # allocation_result[vm["name"]] = pm['name']
                allocation_list.append(
                    {
                        "physics": pm["name"],
                        "virtual": vm["name"],
                        "physics_storage": "126gb",
                        "physics_cpu": "120",
                        "physics_memory": "32768mb",
                        "virtual_storage": str(vm["disk"]),
                        "virtual_cpu": str(vm["cpu"]),
                        "virtual_memory": str(vm["memory"]),
                        "storage_Occupancy": str(
                            round(pm["cpu"] / physical_machine["cpu"] * 100, 2)
                        )
                        + "%",
                        "cpu_Occupancy": str(
                            round(pm["cpu"] / physical_machine["cpu"] * 100, 2)
                        )
                        + "%",
                        "memory_Occupancy": str(
                            round(pm["memory"] / physical_machine["memory"] * 100, 2)
                        )
                        + "%",
                    }
                )
                allocated = True
                break
        if not allocated:
            # 当前物理机没有足够的剩余资源可以分配给虚拟机，
            # 需要寻找其他未被分配的虚拟机看是否又能放入当前的物理机中的
            for pm in physics_machine:
                for vm in virtual_machines:
                    if all(vm[k] <= pm[k] for k in ("cpu", "memory", "disk")):
                        for k in ("cpu", "memory", "disk"):
                            pm[k] -= vm[k]
                        # 向列表中加入当前已经分配好的虚拟机对应的相关信息
                        allocation_list.append(
                            {
                                "physics": pm["name"],
                                "virtual": vm["name"],
                                "physics_storage": "12516gb",
                                "physics_cpu": "120",
                                "physics_memory": "512gb",
                                "virtual_storage": str(vm["disk"]) + "gb",
                                "virtual_cpu": str(vm["cpu"]),
                                "virtual_memory": str(vm["memory"]) + "gb",
                                "storage_Occupancy": str(
                                    round(
                                        pm["disk"] / physical_machine["disk"] * 100, 2
                                    )
                                )
                                + "%",
                                "cpu_Occupancy": str(
                                    round(pm["cpu"] / physical_machine["cpu"] * 100, 2)
                                )
                                + "%",
                                "memory_Occupancy": str(
                                    round(
                                        pm["memory"] / physical_machine["memory"] * 100,
                                        2,
                                    )
                                )
                                + "%",
                            }
                        )
                        allocated = True
                        break

                if not allocated:
                    # 已有的物理机都分配满了，无法再创建新的物理机来分配该虚拟机
                    # print(
                    #     "No available physical machine to allocate VM: {}".format(
                    #         vm["name"]
                    #     )
                    # )
                    break

    # 循环遍历已分配的虚拟机列表，计算每台虚拟机所在物理机的最终的资源利用率
    for vm in allocation_list:
        pm = [pm for pm in physics_machine if pm["name"] == vm["physics"]][0]
        vm["storage_Occupancy"] = (
            str(round((1 - pm["disk"] / physical_machine["disk"]) * 100, 2)) + "%"
        )
        vm["cpu_Occupancy"] = (
            str(round((1 - pm["cpu"] / physical_machine["cpu"]) * 100, 2)) + "%"
        )
        vm["memory_Occupancy"] = (
            str(round((1 - pm["memory"] / physical_machine["memory"]) * 100, 2)) + "%"
        )

    # 将虚拟机分配的结果列表根据'physics'升序排列，方便前端能够正确进行数据展示
    sorted_allocated_vms = sorted(
        allocation_list, key=lambda x: int(x["physics"].split("-")[1])
    )
    # 返回已排序好的虚拟机分配的结果
    count3 = len(sorted_allocated_vms)
    print(f"{count3}台虚拟机已被分配")
    return sorted_allocated_vms


# 返回指定的物理机上的所有虚拟机信息的函数
def get_third_q_physics_node(params):
    # 更改参数中的键名'name'为'physics'
    value = params.pop("name")
    params["physics"] = value
    # 将get_third_question_list()返回值中满足参数中'physics'对应的的元素保存在列表中
    all_node_list = get_third_question_list()
    physics_node_list = [
        d for d in all_node_list if all(k in d and d[k] == v for k, v in params.items())
    ]

    return physics_node_list

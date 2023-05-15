import  pandas
import pandas as pd
from itertools import groupby

df =pd.read_excel("data.xlsx")
data=df.to_dict('records')
#print(data)
#将存储格式转换为同一单位
def transfer_data_format(list):
    for item in list:
        str1 = str(item.get('store'))[-2:-1]

        if str1 == 'g':
            num = float((item.get('store')[0:-2])) * 1024
            str2 = str(num) + 'mb'
            item['store'] = str2

            return list
data=transfer_data_format(data)
#print(data)
sorted_list=sorted(data,key=lambda x:x['ip'])
#物理机分成四个大组
Nm=[list(group) for key, group in groupby(sorted_list, lambda x: x['ip'])]
#对大列表进行排序，从小到大
def sort_by_length(my_list):
    return sorted(my_list, key=len)

Nm=sort_by_length(Nm)

keys_to_extract='node'
#获得节点列表
def get_node_list(list,keys_to_extract):

     return [d[keys_to_extract] for d in list]




#找到主副分片在同一台物理机的分片所在节点
def find_node(Nm1):
    for i in range(len(Nm1)):
         for j in range(i+1,len(Nm1)):
             if Nm1[i]['index_name']==Nm1[j]['index_name'] and Nm1[i]['shard']==Nm1[j]['shard']:
                 #if Nm1[i]['prirep']!=Nm1[j]['prirep']:
                     #if Nm1[i]['store']<= Nm1[j]['store']:
                        return Nm1[i]
# for i in range(len(Nm)):
#    print(find_node(Nm[i]))#N1 -n4分别为NOne
#如果有索引集中的情况优先考虑移动
def find_same_suoyin(Nm1):
    for i in range(len(Nm1)):
        for j in range(i + 1, len(Nm1)):
            if Nm1[i]['index_name'] == Nm1[j]['index_name'] :
                if Nm1[i]['store'] <= Nm1[j]['store']:
                      return Nm1[i]
                else:
                    return Nm1[j]
            else:
                return None
#如果没有就移动最小的那个

def find_fenpian_by_size(Nm1):
    if(find_same_suoyin(Nm1)==None):

        Nm1=sorted(Nm1,key=lambda x:x['store'])


        return Nm1[0]

    else:
        return find_same_suoyin(Nm1)

#每个节点的分片尽可能均衡 ,求每个节点平均下来最好放几个分片


keys_to_remove = ['index_name', 'shard']
remove_none_list_data=[d for d in data if not any(d.get(key) == 'none' for key in keys_to_remove)]#去掉空节点所在的索引分片
#去除空节点
fenpian_number=len(remove_none_list_data)

new_list_num=[('node',d.get('node')) for d in data]
node_number=len(set(new_list_num))
#有一个空节点  求的是节点数有七个
#print(new_list_num)

#每个节点最理想的分片数
best_node=round(fenpian_number/node_number)

#print(best_node)

sorted_list_node=sorted(data,key=lambda x:x['node'])
#把节点开始按小型 正常 大型分组

#先找到每个节点都有哪几个分片 按节点为分片分组
Fenpian_node=[list(group) for key, group in groupby(sorted_list_node, lambda x: x['node'])]

#将大于3的节点分成一组more_  小于3的分成一组less 正常的
more_list=[]
normal_list=[]
less_list=[]
for i in Fenpian_node:

    if len(i)>best_node:

        more_list.append(i)
    elif len(i)<best_node:
        less_list.append(i)
    else:normal_list.append(i)

# print(len(Fenpian_node))
# #print(f"超大节点是{more_list)[::-1]}")#问题出在它列表里套的是列表
# print("morelist",(more_list))
# print(less_list)
# print(len(normal_list))
# print(len(less_list))

need_move_fenpian=[]
#将大节点挪到小节点，根据索引相同
def move_node_lenths(sublist,less_list):
    for sublist in more_list:
            lislen=len(sublist)
            while(lislen > best_node):
                 new_node_dict=find_fenpian_by_size(sublist)


                 strconzip=str(new_node_dict['index_name'])+'&'+str(new_node_dict['prirep'])+'&'+str(new_node_dict['shard'])[0]
                 #print(strconzip)

                 one_new_node=[strconzip,assign_node(less_list)]
                 need_move_fenpian.append(one_new_node)
                 # more_list.pop(j)
                 # j = j + 1

            # new_node_dict['ip']=get_node_ip(assign_node(less_list))#只修改了其中一个节点
                 lislen=lislen-1
                 sublist = [d for d in sublist if d != new_node_dict]#必须从子列表中删去该字典，否则排序还是把它排在第一位




             # index=more_list.index(sublist)
             # del more_list[index]


def assign_node(list):
    list=sort_by_length(list)
    for sublist in  list:
       i=0
       node=sublist[0]['node']#如果一个分片都没有，按照数据表的存储格式至少有一个占位的
       #print(f"被加入的节点是{node}")
       sublist.append(node)
       #print(len(sublist))
       if len(sublist)>=best_node:
           list.pop(i)
           i=i+1
           #print(f"i的值为{i}")
       return node
#获取每个节点所对应的IP物理机
def get_node_ip(node):

        iplist= [{d.get('node'):d.get('ip')} for d in data]

        for subdict in iplist:
            return subdict[node]
#print(get_node_ip('data-node-05'))将新移入的节点的分片IP和节点号修改后，再看有没有主副分片矛盾的情况



move_node_lenths(more_list,less_list)

print(f"总的结果是{need_move_fenpian}")
#返回值：need_move_fenpian 一个对象数组, 对象字段：索引名&主副分片&分片编号，目标节点
<template>
  <el-main class="el_main">
    <el-row>
      <el-col :span="24" id="help_position_parent" class="help_position_parent">

        <div id="node_view" class="grid-content bg-purple flex_layout">
          <div class="node_node" v-for="item in node_view_list" :key="item.title" :title="item.title">
            <span>{{ item.name }}</span>
            <div class="node_node_container flex_layout">
              <div class="shard_node" v-for="item in item.child" :key="item.title"
                @click="_click(item.node_name, item.node_type)" :title="item.title">{{ item.name }}</div>
            </div>
          </div>
        </div>

        <div id="index_view" class="grid-content bg-purple flex_layout">
          <div class="index_node" v-for="item in index_view_list" :key="item.title"
            @click="_click(item.node_name, item.node_type)" :title="item.title">{{ item.name }}</div>
        </div>

      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <div class="grid-content bg-purple-light">
          <el-table :data="tableData" style="width: 100%; padding:20px 20px">
            <el-table-column prop="index" label="索引" width="190">
            </el-table-column>
            <el-table-column prop="shard" label="分片" width="100">
            </el-table-column>
            <el-table-column prop="prirep" label="主副情况" width="100">
            </el-table-column>
            <el-table-column prop="state" label="状态" width="100">
            </el-table-column>
            <el-table-column prop="docs" label="文档数量" width="120">
            </el-table-column>
            <el-table-column prop="store" label="分片大小" width="120">
            </el-table-column>
            <el-table-column prop="ip" label="服务器ip" width="140">
            </el-table-column>
            <el-table-column prop="node" label="集群节点" width="140">
            </el-table-column>
          </el-table>
        </div>
      </el-col>
    </el-row>
  </el-main>
</template>

<style>
.el_main {
  min-height: 100%;
  min-width: 100%;
  padding: 0;
}

.el-row {
  margin-bottom: 0px;
}

.el-col {
  border-radius: 4px;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 0px;
  min-height: 36px;
}

.grid-title {
  min-height: 30px;
}

.row-bg {
  padding: 0px 0;
  background-color: #f9fafc;
}

#node_view {
  padding-top: 20px;
  color: #303133;
  font-size: 20px;
}

#index_view {
  padding-top: 140px;
  padding-bottom: 20px;
  color: #303133;
  font-size: 20px;
}

.flex_layout {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: baseline;
}

.node_node {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  background-color: #40a0ff58;
  border-radius: 5px;
  margin: 20px 10px;
  min-width: 80px;
  min-height: 120px;
  text-align: center;
  border: 1px solid #303133;
}

.node_node span {
  align-self: center;
}

.node_node_container {
  align-self: center;
  padding: 0 10px;
}

.shard_node {
  background-color: #409eff;
  border-radius: 5px;
  padding: 0 0px;
  min-width: 40px;
  height: 60px;
  margin: 0px 2px;
  line-height: 60px;
  text-align: center;
  border: 1px solid #303133;
  font-size: 14px;
}

.shard_node:hover {
  background-color: #006edb;
}

.index_node {
  background-color: #40a0ff58;
  border-radius: 5px;
  width: 120px;
  height: 60px;
  margin: 0px 20px 20px 20px;
  line-height: 60px;
  text-align: center;
  border: 1px solid #303133;
}

.index_node:hover {
  background-color: #006edb;
}

.help_position_parent {
  position: relative;
}
</style>
<script>
export default {
  data() {
    return {
      // 数据列表
      tableData: [/* 与后端数据一致 */],
      // 分片数据
      node_view_list: [
        /* { name: 'node-1', title: 'data-node-04',
          child: [{ name: 'node-2', node_name: 'index&prirep&shard', node_type: '0', title: 'index&prirep&shard' },
          { name: 'node-3', node_name: 'index&prirep&shard', node_type: '0', title: 'index&prirep&shard' }]
        }*/
      ],
      // 索引数据
      index_view_list: [
        /* { name: 'index-A', node_name: 'es_taig_key_20220625', node_type: '1', title: 'es_taig_key_20220625' },
        { name: 'index-B', node_name: 'es_taig_key_20220625', node_type: '1', title: 'es_taig_key_20220625' } */
      ]
    }
  },
  methods: { // 方法
    _click(name, type) {
      this.BtnClick(name, type)
    },
    // 点击事件，更新表格
    BtnClick(name, type) {
      // console.log(name, type)
      if (type == 0) {
        this.$ajax.post('/get_q_first_shard_node', {
          params: {
            name: name,
            type: type
          }
        }).then(res => {
          this.tableData = []
          let arr = res.data
          for (let i of arr) {
            let node = {
              index: i["index"], shard: i["shard"], prirep: i["prirep"], state: i["state"], docs: i["docs"], store: i["store"], ip: i["ip"], node: i["node"]
            }
            this.tableData.push(node)
          }
        })
      } else if (type == 1) {
        this.$ajax.post('/get_q_first_index_node', {
          params: {
            name: name,
            type: type
          }
        }).then(res => {
          this.tableData = []
          let arr = res.data
          for (let i of arr) {
            let node = {
              index: i["index"], shard: i["shard"], prirep: i["prirep"], state: i["state"], docs: i["docs"], store: i["store"], ip: i["ip"], node: i["node"]
            }
            this.tableData.push(node)
          }
        })
      } else {
        console.log(name, type)
      }
    },
    // 加载图表
    load_data() {
      this.$ajax.post('/get_q_first_list', {
        params: {
          load: 'true'
        }
      }).then(res => {
        let arr = res.data
        // console.log(arr);
        // 绑定node_view_list
        let node_view_list = []
        let last_node = " "
        let count = 0
        for (let p = 0; p < arr.length;) {
          last_node = arr[p]["node"]
          let node_node = { name: "node-" + count++, title: arr[p]["node"], child: [] }
          while (p < arr.length && arr[p]["node"] == last_node) {
            if (arr[p]["index"] != "None") {
              let shard_node = {
                name: arr[p]["prirep"] + arr[p]["shard"], node_name: arr[p]["index"] + "&" + arr[p]["prirep"] +
                  "&" + arr[p]["shard"], node_type: '0', title: arr[p]["index"] + "&" + arr[p]["prirep"] +
                    "&" + arr[p]["shard"]
              }
              node_node.child.push(shard_node)
            }
            p++;
          }
          node_view_list.push(node_node)
        }
        this.node_view_list = node_view_list
        // 绑定index_view_list
        let index_view_list = []
        let arr_set = new Set();
        count = 0;
        // 去重
        for (let i in arr) {
          arr_set.add(arr[i]["index"]);
        }
        for (let i of arr_set) {
          let index_node = { name: "index-" + String.fromCharCode(65 + count), node_name: i, node_type: 1, title: i }
          index_view_list.push(index_node)
          count++
        }
        // 更新数据
        this.index_view_list = index_view_list
        // console.log(this.index_view_list, this.node_view_list)
      })
    }
  },
  mounted() { // 声明初始化时可以调用方法
    // we can implement any method here like
    this.load_data()
    this.$nextTick().then(function () {
      setTimeout(() => {
        // 可以使用回调函数的写法
        // 这个函数中DOM必定渲染完成
        // 索引与分片连线
        let shard_node_object = []
        let node_view_object = document.getElementById("node_view").children
        for (let i of node_view_object) {
          for (let j of i.children[1].children) {
            shard_node_object.push(j)
          }
        }
        let index_view_object = document.getElementById("index_view").children
        let plumbIns = jsPlumb.getInstance()
        plumbIns.setContainer("#help_position_parent")
        let arr_color = ['black', 'red', 'blue', 'green', 'white']
        let m = 0
        for (let i of index_view_object) {
          for (let j of shard_node_object) {
            // 如果索引相同，则添加连线
            // console.log(i, j)
            if (i.title == j.title.split("&")[0]) {
              plumbIns.ready(function () {
                plumbIns.connect({
                  // 对应上述基本概念
                  source: j,
                  target: i,
                  endpoint: 'Blank',
                  anchor: ['Top', 'Bottom'],
                  connector: ['Straight'],
                  paintStyle: { stroke: arr_color[m], strokeWidth: 3 },
                })
              })
            }
          }
          m++
        }
      }, 500);
    })
  }
}
// 下面部分是纯JS加载组件，功能已全部由methods实现，下文不再使用，仅供参考
/* function create_element(element_, element_parent, class_list) {
  let element_elecol = document.createElement(element_);
  element_parent.appendChild(element_elecol);
  for (let i in class_list) {
    element_elecol.classList.add(class_list[i]);
  }
  return element_elecol;
}
function create_element_node_node(shard_node_list) {
  shard_node_list = objArraySort(shard_node_list, "node");
  let last_node = " ";
  let count = 0;
  for (let p = 0; p < shard_node_list.length; p++) {
    count++;
    last_node = shard_node_list[p]["node"];
    let element_parent = document.getElementById("node_view");
    let element_node_node = create_element("div", element_parent, ["node_node"]);
    element_node_node.setAttribute("title", shard_node_list[p]["node"]);
    let element_node_span = create_element("span", element_node_node, ["node_span"]);
    element_node_span.innerHTML = "node-" + count;
    let element_node_container = create_element("div", element_node_node, [
      "node_node_container",
      "flex_layout",
    ]);
    while (p < shard_node_list.length && shard_node_list[p]["node"] == last_node) {
      let element_shard_node = create_element("div", element_node_container, [
        "shard_node",
      ]);
      element_shard_node.innerHTML = "A-p1";
      element_shard_node.setAttribute(
        "title",
        shard_node_list[p]["index"] +
        "&" +
        shard_node_list[p]["prirep"] +
        "&" +
        shard_node_list[p]["shard"]
      );
      p++;
    }
  }
}
function create_element_index_node(index_node_list) {
  let element_parent = document.getElementById("index_view");
  let arr_set = new Set();
  let count = 0;
  // 去重
  for (let i in index_node_list) {
    arr_set.add(index_node_list[i]["index"]);
  }
  // 设置title 和 文本 绑定事件
  for (let i of arr_set) {
    let element_node_node = create_element("div", element_parent, ["index_node"]);
    element_node_node.setAttribute("title", i);
    element_node_node.innerHTML = "index-" + String.fromCharCode(65 + count);
    count++;
  }
}
function get_data() {
  var arr = ["test"];
  var formData = new FormData();
  for (var i = 0; i < arr.length; i++) {
    formData.append("temp" + i, arr[i]);
  }
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function () {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      // console.log(xmlHttp.responseText)
      let arr = JSON.parse(xmlHttp.responseText);
      console.log(arr);
      create_element_node_node(arr);
      create_element_index_node(arr);
    }
  };
  xmlHttp.open("post", "http://127.0.0.1:5000/q_first_list");
  xmlHttp.send(formData);
}
// 对象按key排序
function objArraySort(objArr, key) {
  let result = objArr.slice(0);
  return result.sort((a, b) => a[key] - b[key]);
}
get_data(); */
</script>

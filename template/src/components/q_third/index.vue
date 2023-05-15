<template>
	<el-main class="el_main">
		<el-row>
			<el-col :span="24">
				<div>
					<div class="Occupancy_0 color_view">0%</div>
					<div class="Occupancy_20 color_view">1%~19%</div>
					<div class="Occupancy_40 color_view">20%~39%</div>
					<div class="Occupancy_60 color_view">40%~59%</div>
					<div class="Occupancy_80 color_view">60%~79%</div>
					<div class="Occupancy_90 color_view">80%~89%</div>
					<div class="Occupancy_95 color_view">90%~100%</div>
				</div>
			</el-col>
		</el-row>
		<el-row>
			<el-col :span="24">
				<div id="physics_view" class="grid-content bg-purple flex_layout_3">
					<div class="physics_node" v-for="item in physics_view_list" :key="item.key" :title="item.title"
						@click="_click(item.node_name)">
						<span>{{ item.name }}</span>
						<div class="physics_node_container flex_layout_3">
							<div class="virtual_node" v-for="item in item.child" :title="item.title">{{ item.name }}</div>
						</div>
					</div>
				</div>
			</el-col>
		</el-row>
		<el-row>
			<el-col :span="24">
				<div class="grid-content bg-purple-light">
					<el-table :data="tableData" style="width: 100%; padding:20px 20px">
						<el-table-column prop="physics" label="物理机" width="80">
						</el-table-column>
						<el-table-column prop="virtual" label="虚拟机" width="80">
						</el-table-column>
						<el-table-column prop="physics_storage" label="物理机存储" width="100">
						</el-table-column>
						<el-table-column prop="physics_cpu" label="物理机CPU" width="100">
						</el-table-column>
						<el-table-column prop="physics_memory" label="物理机内存" width="100">
						</el-table-column>
						<el-table-column prop="virtual_storage" label="虚拟机存储" width="100">
						</el-table-column>
						<el-table-column prop="virtual_cpu" label="虚拟机CPU" width="100">
						</el-table-column>
						<el-table-column prop="virtual_memory" label="虚拟机内存" width="100">
						</el-table-column>
						<el-table-column prop="storage_Occupancy" label="存储占用率" width="100">
						</el-table-column>
						<el-table-column prop="cpu_Occupancy" label="CPU占用率" width="100">
						</el-table-column>
						<el-table-column prop="memory_Occupancy" label="内存占用率" width="100">
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

#physics_view {
	padding-top: 20px;
	color: #303133;
	font-size: 20px;
	min-height: 300px;
}

.flex_layout_3 {
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: center;
	align-items: baseline;
}

.physics_node {
	background-color: #40a0ff58;
	border-radius: 5px;
	margin: 40px 20px;
	min-width: 95.125px;
	min-height: 120px;
	text-align: center;
	border: 1px solid #303133;
}

.physics_node span {
	display: inline-block;
	margin-top: 10px;
	align-self: center;
}

.physics_node_container {
	margin-top: 10px;
	padding: 0 0px;
}

.virtual_node {
	background-color: #409eff70;
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

.physics_node:hover {
	background-color: #006edb90;
}

.Occupancy_0 {
	background-color: #b2ff5970;
}

.Occupancy_20 {
	background-color: #76FF0370;
}

.Occupancy_40 {
	background-color: #C6FF0070;
}

.Occupancy_60 {
	background-color: #FFFF0070;
}

.Occupancy_80 {
	background-color: #FFC40070;
}

.Occupancy_90 {
	background-color: #ff910070;
}

.Occupancy_95 {
	background-color: #ff3c0070;
}

.color_view {
	display: inline-block;
	width: 13.8%;
	margin: 4px 0px;
}
</style>
<script>
export default {
	data() {
		return {
			// 数据列表
			tableData: [/* 与后端数据一致 */],
			// 分片数据
			physics_view_list: [
				/* { name: 'BM-1', key: 'physics', title: '存储占用率&CPU占用率&内存占用率', node_name: 'BM-1',
				  child: [{ name: 'VM-1', key: 'virtual', title: '存储占用率&CPU占用率&内存占用率' },
				  { name: 'VM-2', key: 'virtual', title: '存储占用率&CPU占用率&内存占用率' }]
				}*/
			]
		}
	},
	methods: { // 方法
		_click(name) {
			this.BtnClick(name)
		},
		// 点击事件，更新表格
		BtnClick(name) {
			// console.log(name)
			this.$ajax.post('/get_q_physics_node', {
				params: {
					name: name
				}
			}).then(res => {
				this.tableData = []
				let arr = res.data
				// console.log(arr);
				for (let i of arr) {
					let node = {
						physics: i["physics"], virtual: i["virtual"], physics_storage: i["physics_storage"], physics_cpu: i["physics_cpu"], physics_memory: i["physics_memory"], virtual_storage: i["virtual_storage"], virtual_cpu: i["virtual_cpu"], virtual_memory: i["virtual_memory"], storage_Occupancy: i["storage_Occupancy"], cpu_Occupancy: i["cpu_Occupancy"], memory_Occupancy: i["memory_Occupancy"]
					}
					this.tableData.push(node)
				}
			})
		},
		// 加载图表
		load_data() {
			this.$ajax.post('/get_q_third_list', {
				params: {
					load: 'true'
				}
			}).then(res => {
				let arr = res.data
				// console.log(arr);
				// 绑定physics_view_list
				let physics_view_list = []
				let last_node = " "
				for (let p = 0; p < arr.length;) {
					last_node = arr[p]["physics"]
					let physics_node = { name: arr[p]["physics"], key: arr[p]["physics"], title: arr[p]["storage_Occupancy"] + "&" + arr[p]["cpu_Occupancy"] + "&" + arr[p]["memory_Occupancy"], node_name: arr[p]["physics"], child: [] }
					while (p < arr.length && arr[p]["physics"] == last_node) {
						if (arr[p]["virtual"] != 'None') {
							let virtual_node = {
								name: arr[p]["virtual"], title: arr[p]["virtual"]
							}
							physics_node.child.push(virtual_node)
						}
						p++
					}
					physics_view_list.push(physics_node)
				}
				this.physics_view_list = physics_view_list
				// console.log(this.physics_view_list)
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
				// 改变物理机前端样式，表明占用率
				let physics_view_object = document.getElementById("physics_view").children
				for (let i of physics_view_object) {
					// console.log(i.title.split("&")[0])
					if (i.title.split("&")[0] == "0%" && i.title.split("&")[1] == "0%" && i.title.split("&")[1] == "0%") {
						i.classList.add("Occupancy_0")
					} else if (i.title.split("&")[0] < "20%" && i.title.split("&")[1] < "20%" && i.title.split("&")[1] < "20%") {
						i.classList.add("Occupancy_20")
					} else if (i.title.split("&")[0] < "40%" && i.title.split("&")[1] < "40%" && i.title.split("&")[1] < "40%") {
						i.classList.add("Occupancy_40")
					} else if (i.title.split("&")[0] < "60%" && i.title.split("&")[1] < "60%" && i.title.split("&")[1] < "60%") {
						i.classList.add("Occupancy_60")
					} else if (i.title.split("&")[0] < "80%" && i.title.split("&")[1] < "80%" && i.title.split("&")[1] < "80%") {
						i.classList.add("Occupancy_80")
					} else if (i.title.split("&")[0] < "90%" && i.title.split("&")[1] < "90%" && i.title.split("&")[1] < "90%") {
						i.classList.add("Occupancy_90")
					} else {
						i.classList.add("Occupancy_95")
					}
				}
			}, 500);
		})
	}
}
</script>
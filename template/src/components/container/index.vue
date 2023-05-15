<template>
	<el-container style="min-height: 789px; border: 1px solid #eee">
		<el-aside width="200px" style="background-color: rgb(238, 241, 246)">
		<el-menu :default-openeds="['1', '3']">
			<el-submenu index="1">
			<template slot="title"><i class="el-icon-menu"></i>查看</template>
			<el-menu-item-group>
				<!-- <template slot="title">第一题</template> -->
				<router-link id="FirstPart" to="/" style="text-decoration: none;">
					<el-menu-item index="1-1">第一问</el-menu-item>
				</router-link>
				<router-link id="SecondPart" to="/q_second" style="text-decoration: none;">
					<el-menu-item index="1-2">第二问</el-menu-item>
				</router-link>
				<router-link id="ThirdPart" to="/q_third" style="text-decoration: none;">
					<el-menu-item index="1-3">第三问</el-menu-item>
				</router-link>
			</el-menu-item-group>
			</el-submenu>
		</el-menu>
		</el-aside>
	
		<el-container>
			<el-header style="text-align: right; font-size: 16px">
				<!-- <i class="el-icon-refresh-right" style="margin-left: 0px"></i>
				<el-dropdown>
					
					<i class="el-icon-setting" style="margin-right: 15px"></i>
					<el-dropdown-menu slot="dropdown">
						<el-dropdown-item>查看</el-dropdown-item>
						<el-dropdown-item>新增</el-dropdown-item>
						<el-dropdown-item>删除</el-dropdown-item>
					</el-dropdown-menu>
				</el-dropdown> -->
				<span>管理员</span>
			</el-header>
		
			<el-main style="padding:0px;">
				<!-- <el-table :data="tableData">
				<el-table-column prop="date" label="日期" width="140">
				</el-table-column>
				<el-table-column prop="name" label="姓名" width="120">
				</el-table-column>
				<el-table-column prop="address" label="地址">
				</el-table-column>
				</el-table> -->
				<router-view> </router-view>
			</el-main>
		</el-container>
  	</el-container>
</template>

  
<style>
.el-header {
	background-color: #B3C0D1;
	color: #333;
	line-height: 60px;
}

.el-aside {
	color: #333;
}
</style>
  
<!-- <script>
export default {
	data() {
		const item = {
			date: '2016-05-02',
			name: '王小虎',
			address: '上海市普陀区金沙江路 1518 弄'
		};
		return {
			tableData: Array(1).fill(item)
		}
	}
};
</script> -->
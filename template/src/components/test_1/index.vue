<template>
	<div id="wrapper">
		<div id="node_view" class="grid-content bg-purple flex_layout">
			<div class="node_node">
				<span>node-1</span>
				<div class="node_node_container flex_layout">
					<div class="shark_node">A-p1</div>
					<div class="shark_node">A-p2</div>
				</div>
			</div>	
			<div class="node_node">
				<span>node-1</span>
				<div class="node_node_container flex_layout">
					<div class="shark_node">A-p1</div>
					<div class="shark_node">A-p2</div>
				</div>
			</div>
		</div>
		<div id="index_view" class="grid-content bg-purple flex_layout">
			<a class="button_a_node">
				<div class="index_node">index-A</div>
			</a>
			<a class="button_a_node">
				<div class="index_node">index-A</div>
			</a>
			<a class="button_a_node">
				<div class="index_node">index-A</div>
			</a>
		</div>
	</div>
</template>

<style>
#wrapper {
	background: #d3dce6;
}
#node_view {
	padding-top: 20px;
	color: #303133;
	font-size: 20px;
}
#index_view {
	padding-top: 20px;
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
	margin: 20px 20px;
	min-width: 40px;
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
.shark_node {
	background-color: #409EFF;
	border-radius: 5px;
	padding: 0 10px;
	height: 60px;
	margin: 0px 10px;
	line-height: 60px;
	text-align: center;
	border: 1px solid #303133;
	font-size: 14px;
}
.shark_node:hover {
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
</style>

<script>
export default {
	name: 'landing-page',
	mounted() {
		
	}
}
</script>
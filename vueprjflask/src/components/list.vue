<template>
	<table width="500">
		<tr>
			<th>编号</th>
			<th>姓名</th>
			<th>密码</th>
			<th>操作</th>
		</tr>
		<tr v-for='(item,index) in listaccount' align='center'>
			<td>{{item.id}}</td>
			<td>{{item.username}}</td>
			<td>{{item.password}}</td>
			<td><button @click="detail(item.id)">查看用户详情</button></td>
			<td><button @click="del(item.id)">删除</button></td>
		</tr>
	</table>
</template>

<script>
		import axios from 'axios'
	export default {
		name: 'list',
		data() {
			return {
				listaccount: [], //列表数据
			}
		},
		created() {
			//发起请求
			axios.get('http://127.0.0.1:5000/getaccounts')
				.then(res => {
					this.listaccount = res.data.accounts;
				})
				.catch(err => {
					console.log(err);
				})
		},
		methods: {
			del:function(aids){
				let params = {
					aid: aids
				};
				axios.post('http://127.0.0.1:5000/delete',params).then(
					response=>{
						if(response.data.code==200){
							this.$router.push('/list');
						}
					}
				)
				.catch(function(error){
					console.log(error)
				})
			},
			detail: function(aids) {
				let params = {
					aid: aids
				};
				//编程式路由
				this.$router.push({
					path: '/edit',
					query: {
						aid: aids
					}
				});
//				axios.get('http://127.0.0.1:5000/editaccount?aid=' + aids).then(
//						response => {
//							if(response.data.code == 200) {
//								this.$router.push({
//									path: '/edit',
//									query: {
//										ac: response.data.ac
//									}
//								});
//							}
//						}
//					)
//					.catch(function(error) {
//						console.log(error)
//					})
			}
		}
	}
</script>

<style>

</style>
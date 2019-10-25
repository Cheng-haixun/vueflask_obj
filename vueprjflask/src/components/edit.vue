<template>
	<!--模板-->
	<form novalidate>
		<label for="username">用户名</label>
		<input type="text" id="aid" value="" v-model="aid"/>
		<input type="text" id='username' v-model="username"/>
		<br />
		<label for="password">密码</label>
		<input type="password" id='password' v-model='password' />
		<br />
		<button type="button" v-on:click="update">update</button>
		
	</form>
</template>

<script>
	import axios from 'axios'
	export default{
		name:'edit',
		data:function(){
			return{
				aid:'',
				username:'',
				password:''
			}
		},
		created(){
			//发起请求
			axios.get('http://127.0.0.1:5000/editaccount?aid='+this.$route.query.aid)
			//服务端响应之后,返回了json参数
			.then(res=>{
				this.aid=res.data.ac.id;
				this.username=res.data.ac.username;
				this.password=res.data.ac.password;
			})
			.catch(err=>{
				console.log(err);
			})
		},
		methods:{
			update:function(){
				//请求参数json数据
				let params={
					aid:this.aid,
					username:this.username,
					password:this.password,
				};
				axios.post('http://127.0.0.1:5000/editaccount',params).then(
					response=>{
						if(response.data.code==200){
							this.$router.push('/list');
						}
					}
				)
				.catch(function(error){
					console.log(error)
				})
			}
		}
	}
</script>

<style>

</style>
<template>
	<!--模板-->
	<!--用户名密码验证-->
	<form action="">
		<label for="username">用户名</label>
		<input type="text" placeholder="Please enter your username" id="username" v-model="username" />
		<br />
		<label for="password">密码</label>
		<input type="password" placeholder="Please enter your password" id="password" v-model="password" />
		<br />
		<button v-on:click="login" type="button">Login</button>
	</form>
</template>

<script>
	import axios from 'axios'
	export default{
		name:'login',
		data:function(){
			return{
				username:'',
				password:''
			}
		},
		methods:{
			login:function(){
				let params={
					username:this.username,
					password:this.password,
				};
				axios.post('http://127.0.0.1:5000/login',params).then(
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
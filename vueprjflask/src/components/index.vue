<template>
	<div class='container'>
		<button type="button" class="btn btn-primary">{{msg}}</button>
	</div>
</template>

<script>
//import axios from 'axios'	
export default{
	name:'index',
	data(){
		return{
			msg:'Hello!',
		};
	},
	methods:{
		getMessage(){
			//服务端的接口地址
			const path='http://localhost:5000/';
			this.$axios.get(path)
			.then((res)=>{
				this.msg=res.data;
			})
			.catch((error)=>{
				console.error(error);
			});
			
		},
	},
	created(){
		this.getMessage();
	},
};
</script>

<style>
</style>
<template>
    <div>
        <Navbar />
        <div class="text-center my-4" >
            <h3>Store Manager Requests</h3>
        </div>
        <div class="container mb-4">               
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="row" >
                                <div class="col-2 text-center">
                                    <h5>Name</h5>
                                </div>
                                <div class="col-8 text-center">
                                    <h5>Username</h5>
                                </div>
                                <div class="col-2 text-center">
                                    <h5>Action</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>               
        </div>
        <!-- loop for products in specific category -->
        <div v-if="users.length > 0" class="container mb-4">
                <div v-for="user in users" :key="user.id">
                    <div class="row">
                        <div class="col">
                            <div class="card">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-2 text-center">
                                            {{ user.fname }} {{ user.lname }}
                                        </div>
                                        <div class="col-8 text-center">
                                            {{ user.username }}
                                        </div>
                                        <div class="col-1 text-center">
                                            <a @click="approveUser(user.id)" class="btn btn-success btn-md mx-auto d-grid col-12" type="submit">Approve</a>
                                        </div>
                                        <div class="col-1 text-center">
                                            <a @click="deleteUser(user.id)" class="btn btn-danger btn-md mx-auto d-grid col-12" type="submit">Reject</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
        <div v-else class="container mb-4">
            <h6>No manager approval requests currently.</h6>
        </div>

        <div class="text-center my-4" >
            <h3>Category Management Requests</h3>
        </div>
        <div class="container mb-4">
                    <div class="row">
                        <div class="col">
                            <div class="card">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-2 text-center">
                                            <h5>Category Name</h5>
                                        </div>
                                        <div class="col-8 text-center">
                                            <h5>Request</h5>
                                        </div>
                                        <div class="col-2 text-center">
                                            <h5>Action</h5>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
        </div>
        <!-- loop for products in specific category -->
        <div v-if="categories.length > 0" class="container mb-4">
                <div v-for="category in categories" :key="category.id">
                    <div class="row">
                        <div class="col">
                            <div class="card">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-2 text-center">
                                            {{ category.cname }}
                                        </div>
                                        <div class="col-8 text-center">
                                            Update
                                        </div>
                                        <div class="col-1 text-center">
                                            <a @click="approveCategory(category.id)" class="btn btn-success btn-md mx-auto d-grid col-12" type="submit">Approve</a>
                                        </div>
                                        <div class="col-1 text-center">
                                            <a @click="deleteCategory(category.id)" class="btn btn-danger btn-md mx-auto d-grid col-12" type="submit">Reject</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
        <div v-else class="container mb-4">
            <h6>No requests currently.</h6>
        </div>
    </div>

</template>
<script>
import Navbar from './Navbar.vue';
import axios from "axios";

export default {
    components: {
        Navbar,
    },
    data() {
        return {
            categories: [],
            users: []
        }
    },
    methods: {
        async fetchCategories() {
            await axios
            .get("http://127.0.0.1:1430/admin-api/approval/categories")
                .then((response) => response)
                .then((response) => response.data)
                .then((results) => {
                    this.categories = results;
                })
                .catch((error)=>{
                    console.error("Category fetch error: ", error)
                });
        },
        async fetchUsers() {
            await axios
            .get("http://127.0.0.1:1430/admin-api/approval/users")
                .then((response) => response)
                .then((response) => response.data)
                .then((results) => {
                    this.users = results;
                })
                .catch((error)=>{
                    console.error("User fetch error: ", error)
                });
        },
        async approveUser(user_id){
            await axios
            .get("http://127.0.0.1:1430/admin-api/approval/user/"+user_id)
                .then((response)=>response)
                .then((response)=>response.data)
                .then((results)=>{alert(results)})
        },
        async deleteUser(user_id){
            await axios
            .delete("http://127.0.0.1:1430/admin-api/approval/user/"+user_id)
                .then((response)=>response)
                .then((response)=>response.data)
                .then((results)=>{
                    this.users = this.users.filter(user => user.id !== user_id);
                    console.log(results)
                    })
        },
        async approveCategory(approval_id){
            await axios
            .get("http://127.0.0.1:1430/admin-api/approval/category/"+approval_id)
                .then((response)=>response)
                .then((response)=>response.data)
                .then((results)=>{
                    this.categories = this.categories.filter(category => category.category_id !== approval_id);
                    console.log(results)
                    })
        },
        async deleteCategory(approval_id){
            await axios
            .delete("http://127.0.0.1:1430/admin-api/approval/category/"+approval_id)
                .then((response)=>response)
                .then((response)=>response.data)
                .then((results)=>{
                    if ("error" in results){
                        throw results
                    }else{
                        this.categories = this.categories.filter(category => category.category_id !== approval_id);
                        console.log(results)
                    }
                })
        }
    },
    async beforeMount() {
        await this.fetchCategories();
        await this.fetchUsers();
    },
    mounted() {
		document.title = "Admin Approvals";
	}
}
</script>
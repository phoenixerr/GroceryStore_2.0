<template>
    <div>
        <Navbar />
            <!-- Button trigger modal -->
        <div class="text-center my-4" >
            <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#AddCategoryModal"><i class="fa fa-plus"></i> Add Category</button>
        </div>
        <AddCategoryModal />

        <div v-if="categories.length > 0" class="container mb-4">
            <div v-for="category in categories" :key="category">
                <div  class="row">
                    <h5 class="col-3" style="margin-top: 6px; font-family: 'Bangers';font-size: 28px;">{{ category.cname }}</h5>
                    <div class="d-flex col-2 align-items-center">
                        <button class="btn btn-dark mx-2" type="button" data-bs-toggle="modal" :data-bs-target="'#'+ category.cid + 'EditCategoryModal'"><i class="fa-solid fa-pen"></i></button>
                        <EditCategoryModal :category="category" />
                        <a :href="'/delete/category/'+category.cid" class="btn btn-danger" type="submit"><i class="fa-solid fa-trash-can"></i></a>
                    </div>
                    <div class="d-flex col-7 align-items-center">
                        <button class="btn btn-dark ms-auto" type="button" data-bs-toggle="modal" :data-bs-target="'#'+ category.cid +'AddProductModal'"><i class="fa-solid fa-circle-plus"></i> Add Product</button>
                    </div>
                    <AddProductModal :category_id="category.cid" />
                </div>
                <hr>
                <div   v-if="category.products.length>0" class="row row-cols-2 row-cols-md-3 row-cols-lg-5  g-4">
                    <!-- loop for products in specific category -->
                    <!-- {% for product in category['products'] %} -->
                    <div v-for="product in category.products" :key="product" class="col">
                        <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">{{ product.pname }}</h5>
                            Quantity: {{ product.quantity }}<br>
                            Rate: Rs. {{ product.rateperunit }}
                        </div>
                        <div class="card-footer d-flex justify-content-center">                    
                            <button class="btn btn-outline-dark btn-sm mx-2" type="button" data-bs-toggle="modal" :data-bs-target="'#'+ product.pid + 'EditProductModal'"><i class="fa-solid fa-pen"></i></button>
                            <!-- EditProductModal -->
                            <EditProductModal :product="product" />
                            <a @click="deleteProduct(product.pid)" class="btn btn-outline-danger btn-sm" type="submit"><i class="fa-solid fa-trash-can"></i></a>                    
                        </div>
                        </div>
                    </div>
                    <!-- {% endfor %} -->
                </div>
                <h6 v-else >No items here yet. Click on Add Product to add items!</h6>
            </div>
        </div>
        <div v-else class="container mb-4">
            <h6>No categories created yet. Click on Add Category to create one!</h6>
        </div>
        <!-- {% endfor %} -->

    </div>
    
</template>

<script>
import Navbar from './Navbar.vue';
import AddProductModal from './modals/AddProductModal.vue';
import EditProductModal from './modals/EditProductModal.vue';
import AddCategoryModal from './modals/AddCategoryModal.vue';
import EditCategoryModal from './modals/EditCategoryModal.vue';
import axios from "axios";


export default {
    components: {
        Navbar,
        AddProductModal,
        EditProductModal,
        AddCategoryModal,
        EditCategoryModal
    },
    data() {
        return {
            categories: []
        }
    },
    methods: {
        async fetchCategories() {
            await axios
            .get("http://127.0.0.1:1430/api/categories")
                .then((response) => response)
                .then((response) => response.data)
                .then((results) => {
                    this.categories = results;
                })
                .catch(()=>{
                    console.error("Category error: ", error)
                });
        },
        async deleteProduct(pid){
            await axios
            .delete("http://127.0.0.1:1430//manager-api/product/"+pid)
            .then((response)=>response)
            .then((response)=>response.data)
            .then((results)=>{
                // this.categories = this.categories.filter(category => category.cid !== cid);
                console.log(results)
                })
        }
    },
    computed:{
        getCategories(){return this.categories;}
    },
    async beforeMount() {
        await this.fetchCategories();
    },
    mounted() {
		document.title = "Manager Dashboard";
	}
}
</script>

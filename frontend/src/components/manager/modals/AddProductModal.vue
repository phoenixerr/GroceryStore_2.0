<template>
    <div class="modal fade" :id="this.category_id +'AddProductModal'">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5">Add Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form>
                    <div class="modal-body">
                        <div class="form-floating mb-3">
                            <input v-model="pname" name="ProductName" type="text" class="form-control" id="ProductName" placeholder="For Eg.: Chilli Powder" required>
                            <label for="ProductName">Product Name</label>
                        </div>
                        <div class="form-floating mb-3">
                            <input v-model="manf_date" name="manf_date" type="date" class="form-control" id="manf_date" required>
                            <label for="manf_date">Manufacture Date</label>
                        </div>
                        <div class="form-floating mb-3">
                            <input v-model="exp_date" name="exp_date" type="date" class="form-control" id="exp_date" required>
                            <label for="exp_date">Expiry Date</label>
                        </div>
                        <div class="form-floating mb-3">
                            <select v-model="unit" name="Unit" class="form-select" id="Unit" aria-label="Floating label select example" required>
                            <option value="kg">kg</option>
                            <option value="gm">gm</option>
                            <option value="litre">litre</option>
                            <option value="dozen">dozen</option>
                            <option value="piece">piece</option>
                            </select>
                            <label for="Unit">Unit</label>
                        </div>
                        <div class="form-floating mb-3">
                            <input v-model="rateperunit" name="Rate/unit" type="number" class="form-control" id="Rate/unit" min="1" required>
                            <label for="Rate/unit">Rate/unit</label>
                        </div>
                        <div class="form-floating mb-3">
                            <input v-model="quantity" name="Quantity" type="number" class="form-control" id="Quantity" min="1" required>
                            <label for="Quantity">Quantity</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button @click="addProduct()" type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
    export default {
        props: {
            category_id:{
                type: Number,
                required: true
            }
        },
        data(){
            return {
                pname:"",
                manf_date:"",
                exp_date:"",
                unit:"",
                rateperunit:"",
                quantity:""
            }
        },
        methods:{
            async addProduct(){
                await axios
                .post("http://127.0.0.1:1430/manager-api/product/add",{
                    category_id:this.category_id,
                    pname:this.pname,
                    manf_date:this.manf_date,
                    exp_date:this.exp_date,
                    unit:this.unit,
                    rateperunit:this.rateperunit,
                    quantity:this.quantity
                })
                .then((response)=>response.data)
                .then((response)=>{alert(response)})
            }
        }
}
</script>
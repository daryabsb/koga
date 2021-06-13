<template>
    <!-- Start Facility Area -->
    <section class="facility-area">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="facility-box" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="loadCategories">
                        <div class="icon">
                            <i class="fas fa-plus-square"></i>
                        </div>
                        <h3>Add New Asset</h3>
                    </div>
                </div>
                <!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add New Asset</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
    
            <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Asset Code</label>
    <input v-model="code" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="nameHelp">
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Asset Name</label>
    <input 
        v-model="name" 
        type="text" 
        class="form-control" 
        id="exampleInputEmail1" 
        aria-describedby="nameHelp">
    <div id="nameHelp" class="form-text">Make sure you don't add too much text.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Category</label>
    <!-- <input type="password" class="form-control" id="exampleInputPassword1"> -->
 
    <select v-model="type" class="form-select" aria-label="Default select example">
        <option 
            v-for="category in getCategories" 
            :key="category.id" :value="category.id"
            
            >{{category.name}}
        </option>
    </select>
  </div>

  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Office</label>
    <!-- <input type="password" class="form-control" id="exampleInputPassword1"> -->

    <select v-model="office" class="form-select" aria-label="Default select example">
        <option 
            v-for="office in getOffices" 
            :key="office.id" :value="office.id"
            >{{office.name}}
        </option>
    </select>
  </div>


      </div>
      <div class="modal-footer">
        <button @click.prevent="emptyFields" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click.prevent="addAsset" type="button" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
      </div>
    </div>
  </div>
</div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="facility-box">
                        <div class="icon">
                            <i class="fas fa-scroll"></i>
                        </div>
                        <h3>Reports</h3>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="facility-box">
                        <div class="icon">
                            <i class="far fa-credit-card"></i>
                        </div>
                        <h3>Many payment gatways</h3>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="facility-box">
                        <div class="icon">
                            <i class="fas fa-headset"></i>
                        </div>
                        <h3>24/7 online support</h3>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Facility Area -->
</template>

<script>
import { mapGetters} from 'vuex';
export default {
    data() {
        return {
            code: "",
            type: 1,
            name: "",
            office: 1,
        }
    },
    methods: {
        async loadCategories() {
		
		 let categoriesUrl = "/categories/";
		 let officesUrl = "/offices/";

        //  console.log(assetsUrl)
      

        try {
            const categoriesData = await this.$axios.get(categoriesUrl);
            const officesData = await this.$axios.get(officesUrl);

            console.log(officesData.data)
            
    
            this.$store.commit("GET_CATEGORIES", categoriesData.data);
            this.$store.commit("GET_OFFICES", officesData.data);
            
            // store.commit("GET_ALL_APPOINTMENTS", allAppointmentsData.data.results);
           

        } catch (err) {
            console.log(err);
        }
        },
        addAsset() {
            let data = {
                   code: this.code,
            type: this.type,
            name: this.name,
            office: this.office,
            }
            console.log(data)
            this.emptyFields()
        },
        emptyFields() {
            this.code = "";
            this.type = 1;
            this.name = "";
            this.office = 11;

        }
        
    },
    computed: {
        ...mapGetters(['getCategories', 'getOffices'])
    }
}
</script>
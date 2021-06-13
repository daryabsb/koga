<template>
    <div>
        <!-- Start Page Title Area -->
        <div class="page-title-area">
            <div class="container">
                <ul>
                    <li><nuxt-link to="/">Home</nuxt-link></li>
                    <li>Electronics</li>
                </ul>
            </div>
        </div>
        <!-- End Page Title Area -->

        <!-- Start Collections Area -->
        <section class="products-collections-area ptb-60">
            <div class="container">
                <div class="section-title row">
                    <h2 class="col-sm-1"><span class="dot"></span><span>Electronics</span></h2>
                    <span class="col-sm-3"></span>
                    <div class="col-8">
                        	<search
									:input="true"
									:date="false"
									:pagination="false"
									url="/assets/"
									moduleState="ASSETS"
								></search>
                    </div>
                    
                </div>
               

                <div class="row">
                    <Sidebar />
                    <AllProducts />
                </div>
            </div>
        </section>
        <!-- End Collections Area -->
    </div>
</template>

<script>
import Sidebar from '~/components/all-products/Sidebar';
import Search from '~/components/landing-one/Search';
import SearchBox from '~/components/landing-one/SearchBox';
import AllProducts from '~/components/all-products/AllProducts';
export default {
    async asyncData({ $axios, app, store, redirect }) {
		
		 let assetsUrl = "/assets/";
		 let categoriesUrl = "/categories/";

        //  console.log(assetsUrl)
      

        try {
            const assetsData = await $axios.get(assetsUrl);
            const categoriesData = await $axios.get(categoriesUrl);

            // console.log(categoriesData.data)
            
           

            store.commit("GET_ALL_ASSETS", assetsData.data);
            store.commit("GET_CATEGORIES", categoriesData.data);
            
            // store.commit("GET_ALL_APPOINTMENTS", allAppointmentsData.data.results);
           

        } catch (err) {
            console.log(err);
        }
    },
    components: {
        Sidebar, AllProducts, Search, SearchBox
    }
}
</script>
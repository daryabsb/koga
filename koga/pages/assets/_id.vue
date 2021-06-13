<template>
    <div>
        <!-- Start Page Title Area -->
        <div class="page-title-area">
            <div class="container">
                <ul>
                    <li><nuxt-link to="/">Home</nuxt-link></li>
                    <li><nuxt-link to="/assets/electronics">Electronics</nuxt-link></li>
                    <li>{{product.name}}</li>
                </ul>
            </div>
        </div>
        <!-- End Page Title Area -->

        <!-- Start Products Details Area -->
        <section class="products-details-area ptb-60">
            <div class="container">
                <div class="row">
                    <ProductImages :images=product.image />
                    <Details 
                        :id="product.id"
                        :name="product.name" 
                        :type="product.type" 
                        :barcode="product.barcode" 
                        price="120$"
                        :image="product.image"
                    />
                    <DetailsInfo />
                    <!-- <RelatedProducts :id="product.id" /> -->
                </div>
            </div>
        </section>
    </div>
</template>



<script>
import ProductImages from '~/components/products/ProductImages';
import Details from '~/components/products/Details';
import DetailsInfo from '~/components/products/DetailsInfo';
import RelatedProducts from '~/components/products/RelatedProducts';
export default {
    async asyncData({ $axios, store, params }) {
		
		let id = params.id;
		// console.log("Page Loaded: ", id);
		// store.dispatch('loadPatientData', id);
		// mutations.togglePatientHistoryTab();
		// console.log("Function is loaded and the ID is: ", id);
		// await store.dispatch('loadPatient',id);
		let productURL = "/assets";
		// let attachmentsURL = '/attachments'

		try {

            let singleProduct = await $axios.$get(`${productURL}/${id}/`);
            
			const [productLoaded] = await Promise.all([singleProduct]);
            // store.state.pimage = patientLoaded.image;
            
            // this.img = patientLoaded.image;
			return {
				product: productLoaded,
            };
			// console.log('?')
            
            
		} catch (err) {
			console.log(err);
		}
	},
    components: {
        ProductImages, Details, DetailsInfo, RelatedProducts
    },
    data(){
        return {
            images: [],
            id: this.$route.params.id
        }
    },
    computed: {
     
    }
}
</script>
<template>
    <div>
        <div class="modal-backdrop" v-if="isQuickViewOpen"></div>
        <transition name="slide-fade">
            <!-- Start Products QuickView Modal Area -->
            <div v-if="isQuickViewOpen" class="modal fade productQuickView" id="productQuickView" tabindex="-1" role="dialog" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <button 
                            type="button" 
                            class="close" 
                            @click="closeQuickView"
                        >
                            <span aria-hidden="true"><i class="fas fa-times"></i></span>
                        </button>
                        <div class="row align-items-center">
                            <div class="col-lg-6 col-md-6">
                                <div class="productQuickView-image">
                                    <img :src="selProduct.image" alt="image">
                                </div>
                            </div>

                            <div class="col-lg-6 col-md-6">
                                <div class="product-content">
                                    <h3>
                                        <nuxt-link :to="`/assets/${selProduct.id}`">
                                            <span @click="closeQuickView">{{selProduct.name}}</span>
                                        </nuxt-link>
                                    </h3>

                                    <div class="price">
                                        <!-- <span class="new-price">$191.00</span> -->
                                    </div>

                                    <div class="product-review">
                                        <div class="rating">
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star-half-alt"></i>
                                        </div>
                                        <a href="#" class="rating-count">3 reviews</a>
                                    </div>

                                    <ul class="product-info">
                                        <li><span>Vendor:</span> <a href="#">Lereve</a></li>
                                        <li><span>Availability:</span> <a href="#">In stock (7 items)</a></li>
                                        <li><span>Product Type:</span> <a href="#">T-Shirt</a></li>
                                    </ul>

                                    <div class="product-color-switch">
                                        <h4>Color:</h4>

                                        <ul>
                                            <li><a href="#" title="Black" class="color-black"></a></li>
                                            <li><a href="#" title="White" class="color-white"></a></li>
                                            <li class="active"><a href="#" title="Green" class="color-green"></a></li>
                                            <li><a href="#" title="Yellow Green" class="color-yellowgreen"></a></li>
                                            <li><a href="#" title="Teal" class="color-teal"></a></li>
                                        </ul>
                                    </div>


                                    <div class="card mt-3" style="width: 18rem;">
                                        <img :src="selProduct.barcode" class="card-img-top" alt="...">
                   
                                    </div>
                                   

                                    <nuxt-link :to="`/assets/${selProduct.id}`" class="view-full-info">
                                    <span @click="closeQuickView">View full info</span>
                                    </nuxt-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        <!-- End Products QuickView Modal Area -->
        </transition>
    </div>
</template>

<script>
import { store, mutations } from '../../utils/sidebar-util';
import { mapGetters, mapActions } from 'vuex';
export default {
    name: 'QuckView',
    data() {
        return{
            quantity: 1,
            item: {
                id: 4,
                name: 'Criss-cross V neck bodycon',
                price: 200.00,
                offer: false,
                offerPrice: 7,
                latest: true,
                bestSellers: false,
                trending: false,
                image: require('../../assets/img/img4.jpg'),
                imageHover: require('../../assets/img/img-hover4.jpg'),
                timePeriod: false,
                dateTime: new Date("December 19, 2020 17:00:00 PDT")
            }
        }
    },
    methods: {
        closeQuickView: mutations.toggleQuickView,
        addToCart(item){
            const product = [{
                id: item.id,
                name: item.name,
                price: item.price,
                image: item.image,
                quantity: this.quantity
            }]

            if(this.cart.length > 0){
                let id = item.id 
                this.getExistPId = id
                let cartIndex = this.cart.findIndex(cart => {
                    return cart.id == id
                })

                if(cartIndex == -1){
                    this.$store.dispatch('addToCart', product);
                    this.$toast("Added to cart", {
                        icon: 'fas fa-cart-plus'
                    });
                } else {
                    this.$store.dispatch('updateCart', {
                        id, unit: 1, cart: this.cart
                    });
                    this.$toast.info("Already added to the cart and update with one");
                }
            } else {
                this.$store.dispatch('addToCart', product)
                this.$toast("Added to cart",{
                    icon: 'fas fa-cart-plus'
                });
            }

            this.closeQuickView()
        },
        increaseQuantity(){
            if(this.quantity > 9){
                this.$toast.error("Can't add more than 10",{
                    icon: 'fas fa-cart-plus'
                });
            } else {
                this.quantity++
            }
        },
        decreaseQuantity() {
            if(this.quantity < 2){
                this.$toast.error("Can't add less than 1",{
                    icon: 'fas fa-cart-plus'
                });
            } else {
                this.quantity--;
            }
        },
    },
    computed: {
        isQuickViewOpen(){
            return store.isQuickViewOpen
        },
        cart(){
            return this.$store.getters.cart
        },
          ...mapGetters(['selProduct'])
    }
}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/styles/_transitions.scss";
</style>
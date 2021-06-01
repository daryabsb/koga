<template>
    <!-- Start Cart Area -->
		<section class="cart-area ptb-60">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 col-md-12">
                       
                     
                            <div class="cart-table table-responsive">
                                <table class="table table-bordered">
                                    <thead>
                                        <tr>
                                            <!-- <th scope="col">Product</th> -->
                                            <th scope="col">Name</th>
                                            <th scope="col">Category</th>
                                            <th scope="col">Office</th>
                                            <th scope="col">Department</th>
                                        </tr>
                                    </thead>

                                    <tbody>

                                        <tr v-for="(product, i) in products" :key="i">
                                            <!-- <td class="product-thumbnail">
                                                <nuxt-link :to="`/assets/${product.id}`">
                                                    <img :src="product.image" :alt="product.name" />
                                                </nuxt-link>
                                            </td> -->

                                            <td class="product-name">
                                                <nuxt-link :to="`/assets/${product.id}`">
                                                    {{product.name}}
                                                </nuxt-link>
                                                <ul>
                                                    <li>Color: <strong>Light Blue</strong></li>
                                                    <li>Size: <strong>XL</strong></li>
                                                    <li>Material: <strong>Cotton</strong></li>
                                                </ul>
                                            </td>

                                            <td class="product-price">
                                                <!-- <span class="unit-amount">${{product.price}}</span> -->
                                                <span class="unit-amount">{{findCategory(product.type)}}</span>
                                            </td>

                                            <td class="product-quantity">
                                                <!-- <div class="input-counter"> -->
                                                    <!-- <span @click="onDecrement(cart.id, cart.quantity)" class="minus-btn"><i class="fas fa-minus"></i></span> -->
                                                    <!-- {{cart.quantity}} -->
                                                    <!-- <span @click="onIncrement(cart.id)" class="plus-btn"><i class="fas fa-plus"></i></span> -->
                                                <span class="unit-amount">{{product.office_name}}</span>

                                                <!-- </div> -->
                                            </td>

                                            <td class="product-subtotal">
                                                <!-- <span class="subtotal-amount">${{product.price * cart.quantity}}</span> -->
                                                <span class="unit-amount">{{product.department_name}}</span>

                                                <a href="javascript:void(0)" @click="removeItemFromCart(product.id)" class="remove"><i class="far fa-trash-alt"></i></a>
                                            </td>
                                        </tr>
                                        
                                    </tbody>
                                </table>
                            </div>

                            <div class="cart-buttons">
                                <div class="row">
                                    <div class="col-lg-7 col-md-7">
                                        <div class="continue-shopping-box">
                                            <nuxt-link to="/products" class="btn btn-light">Continue Shopping</nuxt-link>
                                        </div>
                                    </div>

                                    <div class="col-lg-5 col-md-5 text-right">
                                        <div class="cart-totals">
                                            <h3>Cart Totals</h3>

                                            <ul>
                                                <li>Subtotal <span>${{cartTotal}}</span></li>
                                                <li>Shipping <span>$10.00</span></li>
                                                <li>Total <span><b>${{parseFloat(cartTotal + 10).toFixed(2)}}</b></span></li>
                                            </ul>
                                            <nuxt-link to="/checkout" class="btn btn-light">Proceed to Checkout</nuxt-link>
                                        </div>
                                    </div>
                                </div>
                            </div>
                      
                    </div>
                </div>
            </div>
        </section>
		<!-- End Cart Area -->
</template>

<script>
export default {
    props: ["products",'categories'],
    computed: {
        cart(){
            return this.$store.getters.cart
        },
        cartTotal(){
            return this.$store.getters.totalAmount
        }
    }, 
    methods: {
        findCategory(id){
            let category = this.categories.find(cat => cat.id === id)
            return category.name;
        },
        removeItemFromCart(id){
            this.$store.dispatch('deleteCart', id)
        },
        onIncrement(id){
            this.$store.dispatch('updateCart', {
                id,
                unit: 1,
                cart: this.cart
            })
        },
        onDecrement(id, quantity){
            if (quantity > 1) {
                this.$store.dispatch('updateCart', {
                    id,
                    unit: -1,
                    cart: this.cart
                })
            } else {
                this.removeItemFromCart(id);
                this.$toast.warning("Item deleted!");
            }
        },
    }
}
</script>
<template>
    <div>
        <div class="related-products-area">
            <div class="container">
                <div class="section-title">
                    <h2><span class="dot"></span> Related Products</h2>
                </div>

                <div class="row">
                    <asset-item-grid
                        v-for="product in relatedProducts"
                        :product="product"
                        :key="product.id"
                        @clicked="toggle"
                        :className="`col-lg-3 col-md-6 col-6`"
                    ></asset-item-grid>
                </div>
            </div>
        </div>
        <QuckView />
    </div>
</template>

<script>
import { mutations } from '../../utils/sidebar-util';
import QuckView from '../modals/QuckView';
export default {
    components: {
        QuckView
    },
    props: ['id'],
    methods: {
        toggle() {
            mutations.toggleQuickView()
        }
    },
    computed: {
        relatedProducts(){
            return this.$store.state.products.all.filter(product => product.id !== parseInt(this.id)).slice(0, 4);
        }
    }
}
</script>
<template>
    <div class="col-lg-8 col-md-12">
        <div class="products-filter-options">
            <div class="row align-items-center">
                <div class="col d-flex">
                    <p>Showing 22 of 102 results</p>
                </div>

                <div class="col d-flex">
                    <span @click="grid=false"><i class="fas fa-list"></i></span>
                    <span @click="grid=false" class="mx-2"><i class="fas fa-th-large"></i></span>
                      <span>|</span>
                    <span class="ml-3">Show:</span>

                    <div class="show-products-number">
                        <select>
                            <option value="1">22</option>
                            <option value="2">32</option>
                            <option value="3">42</option>
                            <option value="4">52</option>
                            <option value="5">62</option>
                        </select>
                    </div>
                    <span>|</span>
                    <span>Sort:</span>

                    <div class="products-ordering-list">
                        <select>
                            <option value="1">Featured</option>
                            <option value="2">Best Selling</option>
                            <option value="3">Price Ascending</option>
                            <option value="4">Price Descending</option>
                            <option value="5">Date Ascending</option>
                            <option value="6">Date Descending</option>
                            <option value="7">Name Ascending</option>
                            <option value="8">Name Descending</option>
                        </select>
                    </div>
                    
                     
                </div>
            </div>
        </div>
        <div id="products-filter" class="products-collections-listing row" v-if="grid">
            <asset-item-grid
                v-for="(product, index) in products"
                :product="product"
                :key="index"
                @clicked="toggle"
                :className="`col-lg-3 col-md-3 products-col-item`"
            ></asset-item-grid>
        </div>
         <div id="products-filter" class="products-collections-listing row" v-else>
            <asset-item-list
                :products="getAssets"
                :categories="getCategories"
                @clicked="toggle"
            ></asset-item-list>
        </div>


        <nav class="woocommerce-pagination">
            <ul>
                <li><a href="#" class="page-numbers">1</a></li>
                <li><span class="page-numbers current">2</span></li>
                <li><a href="#" class="page-numbers">3</a></li>
                <li><a href="#" class="page-numbers">4</a></li>
                <li><span class="page-numbers dots">…</span></li>
                <li><a href="#" class="page-numbers">11</a></li>
                <li><a href="#" class="page-numbers">12</a></li>
                <li><a href="#" class="next page-numbers"><i class="fas fa-chevron-right"></i></a></li>
            </ul>
        </nav>

        <QuckView />
    </div>
</template>

<script>
import QuckView from '~/components/modals/QuckView';
import AssetItemGrid from '~/components/landing-one/AssetItemGrid';
import AssetItemList from '~/components/landing-one/AssetItemList';
import { mutations } from '../../utils/sidebar-util';
import { mapGetters, mapActions } from 'vuex';
export default {
    
    components: {
        QuckView,
        AssetItemGrid,
        AssetItemList
    },
    data() {
        return {
            grid: false,
        }
    },
    methods: {
        toggle() {
            mutations.toggleQuickView();
        }
    },
    computed: {
        products(){
            return this.$store.state.products.all
        },
         ...mapGetters(['getAssets','getCategories'])
    },
}
</script>
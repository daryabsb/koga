<template>
    <div>
        <!-- Start Navbar Area -->
        <div :class="['navbar-area', {'is-sticky': isSticky}]">
            <div class="comero-nav">
                <div class="container">
                    <nav class="navbar navbar-expand-md navbar-light">
                        <nuxt-link class="navbar-brand" to="/">
                            <img src="../assets/koga/logo.png" alt="logo">
                        </nuxt-link>

                        <!-- <b-navbar-toggle target="navbarSupportedContent"></b-navbar-toggle> -->
                        <!-- <button class="navbar-toggler" type="button" 
                                data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" 
                                aria-controls="navbarTogglerDemo01" 
                                aria-expanded="false" 
                                aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                        </button> -->
                         <button 
                                class="navbar-toggler"
                                data-bs-toggle="collapse" 
                                data-bs-target="#navbarTogglerDemo02" 
                                aria-expanded="false" 
                                aria-controls="navbarTogglerDemo02"
                                ><span class="navbar-toggler-icon"></span>
                                </button>

                        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                            <ul class="navbar-nav">
                                
                                <li class="nav-item p-relative"><nuxt-link to="/" class="nav-link">Home</nuxt-link>
                                    <!-- <ul class="dropdown-menu">
                                        <li class="nav-item">
                                            <nuxt-link to="/" class="nav-link active">Home Style One</nuxt-link>
                                        </li>

                                        <li class="nav-item">
                                            <nuxt-link to="/diction-two" class="nav-link active">Home Style Two</nuxt-link>
                                        </li>
                                        <li class="nav-item">
                                            <nuxt-link to="/diction-three" class="nav-link active">Home Style Three</nuxt-link>
                                        </li>
                                    </ul> -->
                                </li>

                                <li class="nav-item p-relative"><a href="#" class="nav-link">Assets <i class="fas fa-chevron-down"></i></a>
                                    <ul class="dropdown-menu">
                                        <li class="nav-item"><nuxt-link to="/assets/electronics" class="nav-link">Electronics</nuxt-link></li>

                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Furniture</nuxt-link></li>
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Supplies</nuxt-link></li>
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Vehicles</nuxt-link></li>
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Buildings</nuxt-link></li>
                                    </ul>
                                </li>

                                <li class="nav-item p-relative">
                                    <nuxt-link to="/gallery-one" class="nav-link">Offices  <i class="fas fa-chevron-down"></i></nuxt-link>
                                     <ul class="dropdown-menu">
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Main Office</nuxt-link></li>
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Parwezkhan</nuxt-link></li>
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Pishta</nuxt-link></li>
                                        <li class="nav-item"><nuxt-link to="/assets/1" class="nav-link">Fig</nuxt-link></li>
                                    </ul>
                                </li>

                                <li class="nav-item p-relative"><a href="#" class="nav-link">Miscellaneous <i class="fas fa-chevron-down"></i></a>
                                    <ul class="dropdown-menu">
                                        <li class="nav-item">
                                            <nuxt-link to="/gallery-one" class="nav-link">Used Items</nuxt-link>
                                        </li>

                                        <li class="nav-item">
                                            <nuxt-link to="/cart" class="nav-link">Old Lists</nuxt-link>
                                        </li>

                                        <li class="nav-item">
                                            <nuxt-link to="/checkout" class="nav-link">Notes</nuxt-link>
                                        </li>

                                        <li class="nav-item">
                                            <nuxt-link to="/login" class="nav-link">Departments</nuxt-link>
                                        </li>

                                        <li class="nav-item">
                                            <nuxt-link to="/signup" class="nav-link">Employees</nuxt-link>
                                        </li>

                                    </ul>
                                </li>

                                <li class="nav-item">
                                    <nuxt-link to="/contact" class="nav-link">Contact</nuxt-link>
                                </li>
                            </ul>
                            <div class="others-option" v-if="isAuthenticated">
                                <div class="option-item" >
                                    <a href="javascript:void(0)" @click.prevent="onLogout">Logout</a>
                                </div></div>
                            <div class="others-option" v-else>
                                <div class="option-item" >
                                  
                                    <span><nuxt-link to="/login" >Login</nuxt-link></span>
                                </div>
                               
                                <div class="option-item">
                                    <a @click.prevent="toggle" href="#">
                                        Cart(3) <i class="fas fa-shopping-bag"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </nav>
                </div>
            </div>
        </div>
        <!-- End Navbar Area -->

        <SidebarPanel></SidebarPanel>
    </div>
</template>

<script>
import SidebarPanel from '../layouts/SidebarPanel';
import { mutations } from '../utils/sidebar-util';
import {mapGetters} from 'vuex';
export default {
    components: {
        SidebarPanel
    },
    data(){
        return {
            isSticky: false
        }
    },
    mounted(){
        const that = this;
        window.addEventListener('scroll', () => {
            let scrollPos = window.scrollY;
            if(scrollPos >= 100){
                that.isSticky = true;
            } else {
                that.isSticky = false;
            }
        })
    },
    computed: {
        cart(){
            // return this.$store.getters.cart
        }
    },
    methods: {
        toggle() {
            mutations.toggleNav()
        },
        async onLogout() {
        await this.$auth.logout()
    }
    },
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser'])
    }
}
</script>
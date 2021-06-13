// import axios from '@nuxtjs/axios';
const state = () => ( {
    cart: [],
    totalAmount: 0,
    totalQuantity: 0,
    orders: [],
    assets: [],
    categories: [],
    offices: [],
    selProduct: [],

});

export const totals = (paylodArr) => {
    const totalAmount = paylodArr.map(cartArr => {
        return cartArr.price * cartArr.quantity
    }).reduce((a, b) => a + b, 0);

    const totalQuantity = paylodArr.map(cartArr => {
        return cartArr.quantity;
    }).reduce((a, b) => a + b, 0);

    return {
        amount: totalAmount.toFixed(2),
        qty: totalQuantity
    }
};
const mutations = {
    'GET_ALL_ASSETS'(state, payload) {
        state.assets = payload;
    },
    'GET_CATEGORIES' (state, payload) {
        state.categories = payload;
    },
    'GET_OFFICES' (state, payload) {
        state.offices = payload;
    },
    'SELECT_PRODUCT'(state,payload) {
        state.selProduct = payload;
    },
    'GET_ORDER'(state, payload){
        state.orders = payload
    },
    'GET_CART'(state, payload){
        state.cart = payload
        state.totalAmount = totals(payload).amount
        state.totalQuantity = totals(payload).qty
    },
    'ADD_TO_CART'(state, payload){
        state.cart = [...state.cart, ...payload]
        state.totalAmount = totals(state.cart).amount
        state.totalQuantity = totals(state.cart).qty
    },
    'DELETE_CART'(state, id){
        const currentCartToDelete = state.cart
        const indexToDelete = currentCartToDelete.findIndex(cart => {
            return cart.id == id
        })

        state.cart = [...currentCartToDelete.slice(0, indexToDelete), ...currentCartToDelete.slice(indexToDelete + 1)]
        state.totalAmount = totals(state.cart).amount
        state.totalQuantity = totals(state.cart).qty
    },
    'UPDATE_CART'(state, payload){
        state.cart = payload

        state.totalAmount = totals(payload).amount
        state.totalQuantity = totals(payload).qty
    }, 
    'CART_EMPTY'(state){
        state.cart = []
        state.totalAmount = 0
        state.totalQuantity = 0
    }
};

const actions = {
    // getOrder({commit}){
    //     axios.get('c').then(res => {
    //         if(res.data == 'no data'){
    //             return []
    //         }
    //         commit('GET_ORDER', res.data)
    //     })
    // },

    addToCart({ commit }, payload){
        commit('ADD_TO_CART', payload)
    },

    deleteCart({ commit }, id){
        commit('DELETE_CART', id)
    },

    updateCart({ commit }, payload){
        // console.log(payload.unit)
        const currentCartToUpdate = payload.cart
        const indexToUpdate = currentCartToUpdate.findIndex(cart => {
            return cart.id == payload.id
        })

        const newCart = {
            ...currentCartToUpdate[indexToUpdate],
            quantity: currentCartToUpdate[indexToUpdate].quantity + payload.unit
        }

        // console.log(newCart)

        const cartUpdate = [...currentCartToUpdate.slice(0, indexToUpdate), newCart, ...currentCartToUpdate.slice(indexToUpdate + 1)]
        commit('UPDATE_CART', cartUpdate)
    }, 
    cartEmpty({commit}){
        commit('CART_EMPTY')
    },
    async onFilter({ state, commit }, payload) {

        let url = payload.url;
        let query = '';

       

            query = `?input=${payload.searchInput}`;


        let filterUrl = `${url}${query}`

        console.log(filterUrl)

        try {
            // console.log(Array.from(payload));
            const filterData = await this.$axios.get(filterUrl);
            commit(`GET_ALL_${payload.module}`, filterData.data);
        } catch (err) {
            console.log(err);
        }

    },
};

const getters = {
    cart(state){
        return state.cart
    },
    totalAmount(state){
        return state.totalAmount
    },
    totalQuantity(state){
        return state.totalQuantity
    },
    getOrders(state){
        return state.orders
    },
    isAuthenticated(state) {
        return state.auth.loggedIn;
    },
    loggedInUser(state) {
        return state.auth.user;
    },
    getAssets(state) {
        return state.assets;
    },
    getCategories(state) {
        return state.categories;
    },
    getOffices(state) {
        return state.offices;
    },
    selProduct(state) {
        return state.selProduct;
    },
};

export default{
    state, mutations, actions, getters
};
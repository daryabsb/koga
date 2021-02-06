export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'LOX-STORE',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
            { rel: "stylesheet", type: "text/css", href: " https://www.rudaw.net/styles/cssAr?v=g9_LRHaRUnSkO-tlSvy6WdNhlC6eRHdcSyzvwqILEYI1" }

        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        '~assets/search.css'
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        '~/plugins/globalComponents.cient.js'
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/bootstrap
        'bootstrap-vue/nuxt',
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
        // https://go.nuxtjs.dev/pwa
        '@nuxtjs/pwa',
    ],

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        baseURL: 'http://127.0.0.1:8000/api'
    },

    // PWA module configuration: https://go.nuxtjs.dev/pwa
    pwa: {
        manifest: {
            lang: 'en'
        }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {}
}
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
        { src: "~/plugins/globalComponents.cient.js", ssr: false }
       
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: ["@nuxtjs/style-resources"],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // "@nuxtjs/style-resources",
        '@nuxtjs/auth',
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
    auth: {
        strategies: {
            local: {
                endpoints: {
                    login: {
                        url: 'http://127.0.0.1:8000/api/user/token/',
                        // url: 'http://172.16.10.8:8000/api/user/token/',
                        method: "POST",
                        propertyName: "token",
                        altProperty: 'refresh'
                    },
                    logout: true,
                    user: {
                        url: 'http://127.0.0.1:8000/api/user/me/',
                        // url: `${process.env.baseUrl}:8000/api/user/me`,
                        // url: 'http://172.16.10.8:8000/api/user/me',
                        method: "get",
                        propertyName: false
                    }
                },
                tokenType: "Token "
            }
        },
        redirect: {
            login: '/login',
            logout: '/login',
            callback: false,
            home: '/'
        },
        watchLoggedIn: true
    },

    // PWA module configuration: https://go.nuxtjs.dev/pwa
    pwa: {
        manifest: {
            lang: 'en'
        }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {},
    server: {
        port: 8080 // default: 3000
      }
}
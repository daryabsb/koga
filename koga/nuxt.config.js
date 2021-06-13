export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'koga',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script: [
      { src: "/bootstrap/js/bootstrap.bundle.min.js", type: "text/javascript"}
    ]
  },

  loading: { color: '#fff' },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    './assets/scss/styles/animate.min.css',
    './assets/scss/styles/fontawesome.min.css',
    './assets/scss/styles/style.scss',
    './assets/scss/styles/admin.scss',
    './assets/scss/styles/responsive.scss',
    './assets/bootstrap/css/bootstrap.min.css',
    './assets/bootstrap/css/headers.css',
    './assets/bootstrap/css/sidebars.css' 
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/vue-carousel', ssr: false },
    { src: '~/plugins/vue-backtotop', ssr: false },
    { src: '~/plugins/vue-toastification', ssr: false },
    { src: '~/plugins/vueperslides', ssr: false },
    // { src: '~/plugins/firebase' },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/auth',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // proxy: true
    baseURL: 'http://127.0.0.1:8000/api'
  },

  router: {
    linkActiveClass: 'active',
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

//   auth: {
//     strategies: {
//         local: {
//             endpoints: {
//                 login: {
//                     // url: process.env.LOGIN_URL,
//                     url: 'http://172.16.10.8:8000/api/user/token/',
//                     method: "POST",
//                     propertyName: "token",
//                     altProperty: 'refresh'
//                 },
//                 logout: true,
//                 user: {
//                     // url: process.env.USER_URL,
//                     // url: `${process.env.baseUrl}:8000/api/user/me`,
//                     url: 'http://172.16.10.8:8000/api/user/me',
//                     method: "get",
//                     propertyName: false
//                 }
//             },
//             tokenType: "Token "
//         }
//     },
//     redirect: {
//         login: '/login',
//         logout: '/login',
//         callback: false,
//         home: '/'
//     },
//     watchLoggedIn: true
// },

auth: {
  strategies: {
    local: {
      endpoints: {
        login: {
          url: "http://127.0.0.1:8000/api/user/token/",
          method: "POST",
          propertyName: "token"
        },
        logout: true,
        user: {
          url: "http://127.0.0.1:8000/api/user/me",
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
  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend (config, ctx) {
    }
  },
  server: {
    port: 8080,
    host: '0.0.0.0'
  }
}

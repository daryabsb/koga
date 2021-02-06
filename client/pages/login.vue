<template>
	<div>
     <!-- Page content -->
    <b-container class="mt-3 pb-5">
      <b-row class="justify-content-center">
        <b-col lg="5" md="7">
          <b-card no-body bg-variant="light" header="Login" class="text-center border-0 mb-0">
            <b-card-body class="px-lg-5 py-lg-5">
              
                <!-- <b-form role="form" @submit.prevent="handleSubmit(onSubmit)"> -->
                  <b-form-input 
                              class="mb-3"
                             
                             
                              prepend-icon="ni ni-email-83"
                              placeholder="Email"
                              v-model="email">
                  </b-form-input>

                  <b-form-input 
                              class="mb-3"
                              type="password"
                             
                             
                             
                              placeholder="Password"
                              v-model="password">
                  </b-form-input>
                  <b-form-checkbox style="padding-right:10px;" v-model="rememberMe"> Remember Me</b-form-checkbox>
               
                  <div class="text-center">
                    <b-button @click="onLogin" variant="primary" class="my-4">Sign in</b-button>
                  </div>
                <!-- </b-form> -->
            
            </b-card-body>
          </b-card>
          <b-row class="mt-3">
            <b-col cols="6">
              <router-link to="/dashboard" class="text-light"><small>Forgot password?</small></router-link>
            </b-col>
            <b-col cols="6" class="text-right">
              <nuxt-link to="/register" class="text-light"><small>Create new account</small></nuxt-link>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
	</div>
</template>
<script>
  export default {
    auth: 'guest',
    data() {
      return {
        email: '',
        password: '',
        rememberMe: false
      };
    },
    methods: {
      onSubmit() {
        // this will be called only after form is valid. You can do api call here to login
      },
      async onLogin() {
      try {
        //   console.log(this.email, ' / ', this.password)
        let loginfo = this.$auth.loginWith('local', {
          data: {
            email: this.email,
            password: this.password
          }
          
        });
        // console.log(Loginfo)
        // this.$router.push({ path: '/' })
       
      } catch (err) {
        console.log(err)
      }
       this.$router.push({ path: '/' })
    }
    }
  };
</script>

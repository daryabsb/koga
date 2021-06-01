<template>
    <div>
        <div class="page-title-area">
            <div class="container">
                <ul>
                    <li><nuxt-link to="/">Home</nuxt-link></li>
                    <li>Login</li>
                </ul>
            </div>
        </div>

        <section class="login-area ptb-60">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-md-12">
                        <div class="login-content">
                            <div class="section-title">
                                <h2><span class="dot"></span> Login</h2>
                            </div>

                            <div class="login-form">
                                <div class="form-group">
                                    <label>Email</label>
                                    <input v-model="email" type="email" class="form-control" placeholder="Enter your name" id="name" name="name">
                                </div>

                                <div class="form-group">
                                    <label>Password</label>
                                    <input v-model="password" type="password" class="form-control" placeholder="Enter your password" id="password" name="password">
                                </div>

                                <button @click="onLogin" class="btn btn-primary">Login</button>

                                <nuxt-link to="/" class="forgot-password">Lost your password?</nuxt-link>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-6 col-md-12">
                        <div class="new-customer-content">
                            <div class="section-title">
                                <h2><span class="dot"></span> New Customer</h2>
                            </div>

                            <span>Create a Account</span>
                            <p>Sign up for a free account at our store. Registration is quick and easy. It allows you to be able to order from our shop. To start shopping click register.</p>
                            <nuxt-link to="/signup" class="btn btn-light">Create A Account</nuxt-link>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    auth: 'guest',
  data() {
    return {
      email: '',
      password: ''
    }
  },
    methods: {
          async onLogin() {
      try {
        //   console.log(this.email, ' / ', this.password)
        let loginfo = this.$auth.loginWith('local', {
          data: {
            email: this.email,
            password: this.password
          }
          
        });
        console.log(loginfo)
        // this.$router.push({ path: '/' })
       
      } catch (err) {
        console.log(err)
      }
       this.$router.push({ path: '/' })
    }
    }
}
</script>
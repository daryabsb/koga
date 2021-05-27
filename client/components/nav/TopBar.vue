<template>
    <div>
      <b-navbar style="background-color:#eee;" toggleable="lg" type="light" class="row">

     
       

    <b-navbar-brand href="/" class="col-4">
       <b-img left src="~/assets/images/lox-logo.png" alt="Left image" class="logo-main" height="10"></b-img>
    </b-navbar-brand>
       
 
 <b-card no-border class="container mt-5 border-0 text-center col-4 bg-transparent">
 <search-bar></search-bar>
    </b-card>
       
       
           <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
           <b-navbar-nav class=" mt-5 ml-auto col-4">
 <b-nav-item-dropdown text="Lang" left>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown left>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item @click="onLogout">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav> 
      </b-collapse>
       
     
  
   

   
   

      <!-- Right aligned nav items -->
     
        <!-- <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form> -->
 <!-- <b-nav-item>
   <search-bar></search-bar>
 </b-nav-item> -->
 
       
   
  </b-navbar>
 
</div>
</template>
<script>
export default {
  methods: {
    onLogout() {
      this.$auth.logout();
    },
}
}
</script>

<style>
.logo-main {
  height: 7rem;
}

</style>
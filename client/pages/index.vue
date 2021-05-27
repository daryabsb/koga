<template>
  <b-container fluid>
<!-- <b-row>
  <b-col>
    <b-card no-border class="container border-0 text-center">
 <search-bar></search-bar>
    </b-card>
   
  </b-col>
</b-row> -->

<b-row class="mt-3">
  <b-col cols="3">
     <b-card class="mb-3" header="Filter By:">
       <b-form-select v-model="selectedDept" :options="deptOptions" class="mb-3">
      <!-- This slot appears above the options from 'options' prop -->
      <template #first>
        <b-form-select-option :value="null">-- Filter By Department --</b-form-select-option>
      </template>
      <b-form-select-option value="0">Clear Filter</b-form-select-option>
    </b-form-select>
     <b-form-select v-model="selectedDept" :options="deptOptions" class="mb-3">
      <!-- This slot appears above the options from 'options' prop -->
      <template #first>
        <b-form-select-option :value="null">-- Filter By Type --</b-form-select-option>
      </template>
      <b-form-select-option value="0">Clear Filter</b-form-select-option>
    </b-form-select>
     <b-form-select v-model="selectedDept" :options="deptOptions" class="mb-3">
      <!-- This slot appears above the options from 'options' prop -->
      <template #first>
        <b-form-select-option :value="null">-- Filter By Condition --</b-form-select-option>
      </template>
      <b-form-select-option value="0">Clear Filter</b-form-select-option>
    </b-form-select>
   
    <b-form-checkbox><span class="ml-3">Small</span></b-form-checkbox>
  <b-form-checkbox><span class="ml-3">Medium</span></b-form-checkbox>
  <b-form-checkbox><span class="ml-3">Large</span></b-form-checkbox>
     </b-card>
   <b-card no-body header="Card with flush list group">
    <b-list-group flush>
      <b-list-group-item href="#">Cras justo odio</b-list-group-item>
      <b-list-group-item href="#">Dapibus ac facilisis in</b-list-group-item>
      <b-list-group-item href="#">Vestibulum at eros</b-list-group-item>
    </b-list-group>

    <b-card-body>
      Quis magna Lorem anim amet ipsum do mollit sit cillum voluptate ex nulla tempor. Laborum
      consequat non elit enim exercitation cillum aliqua consequat id aliqua. Esse ex consectetur
      mollit voluptate est in duis laboris ad sit ipsum anim Lorem.
    </b-card-body>
  </b-card>
  </b-col>
  <b-col cols="9">
    <!-- {{assets}} -->
    <b-card>
      <b-table hover :items="assets" :fields="fields">
        <template #cell(name)="row">
            <div >
              <nuxt-link :to="`/${row.item.id}`">{{row.item.name}}</nuxt-link>
              	
            </div>
								
							</template>
        <template #cell(barcode)="row">
            <div >
              	<img style="height:80px;" :src="row.item.barcode" />
            </div>
								
							</template>
      </b-table>
    </b-card>
  </b-col>
</b-row>
  </b-container>
</template>

<script>
export default {
  async asyncData({$axios}) {

    let departmentsUrl = '/departments/';
    let categoriesUrl = '/categories/';
    let assetsUrl = '/assets/';
    try {

      const departmentsRes = await $axios.$get(departmentsUrl);
      const categoriesRes = await $axios.$get(categoriesUrl);
      const assetsRes = await $axios.$get(assetsUrl);

      // const [departmentsData,categoriesData,assetsData] = await Promise.all(departmentsRes,categoriesRes,assetsRes)
    // console.log(assetsRes)

    return {
      departments: departmentsRes,
      categories: categoriesRes,
      assets: assetsRes
    }
   
   } catch (error) {
      console.log(error)
    }
   

  },

  data() {
      return {
        selectedDept:null,
        deptOptions: [
          { value: 'A', text: 'Option A (from options prop)' },
          { value: 'B', text: 'Option B (from options prop)' }
        ],
        selected: [],
        filterOptions: [
          { item: 'A', name: 'Option A' },
          { item: 'B', name: 'Option B' },
          { item: 'D', name: 'Option C', notEnabled: true },
          { item: { d: 1 }, name: 'Option D' }
        ],
        fields: ['id','type','name','condition','barcode'],
        itemsin: [
          { 
            age: 40, 
            first_name: 'Dickerson', 
            last_name: 'Macdonald',
            _rowVariant: `${this.age < 50 ? 'danger' : '?'}`
            },
          { 
            
            age: 21, 
            first_name: 'Larsen', 
            last_name: 'Shaw',
            _rowVariant: `${this.age < 50 ? 'danger' : '?'}`
             },
          {
            age: 89,
            first_name: 'Geneva',
            last_name: 'Wilson',
            _rowVariant: `${this.age < 50 ? 'danger' : '?'}`
          },
          {
            age: 40,
            first_name: 'Thor',
            last_name: 'MacDonald',
            _cellVariants: { age: 'info', first_name: 'warning' }
          },
          { age: 29, first_name: 'Dick', last_name: 'Dunlap' }
        ]
      }
  },
  mounted() {
    
      this.assets.forEach(item => {
        let itemDept = this.departments.find(dept=>dept.id===item.department)
        let itemType = this.categories.find(cat=>cat.id===item.type)
        item.department = itemDept.name
        item.type = itemType.name


      })
    
  } 

}
</script>

<style>

</style>

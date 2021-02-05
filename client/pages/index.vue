<template>
  <b-container fluid>


<b-row class="mt-3">
  <b-col cols="3">
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
</b-card-group>
  </b-col>
  <b-col cols="9">
    <b-card>
      <b-table hover :items="items"></b-table>
    </b-card>
  </b-col>
</b-row>
  </b-container>
</template>

<script>
export default {
  data() {
      return {
        items: [
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
  }
}
</script>

<style>

</style>

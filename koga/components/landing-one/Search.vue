<template>
<div class="searchbnb">
 <svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol xmlns="http://www.w3.org/2000/svg" id="sbx-icon-search-23" viewBox="0 0 40 40">
    <path d="M21.728 22.597c-2.308 2.1-5.374 3.38-8.74 3.38C5.815 25.977 0 20.162 0 12.987 0 5.816 5.815 0 12.988 0c7.174 0 12.99 5.815 12.99 12.988 0 3.366-1.28 6.433-3.38 8.74 1.943-1.516 4.76-1.376 6.542.404l9.41 9.41c1.934 1.934 1.928 5.074-.003 7.005-1.935 1.935-5.077 1.93-7.004.004l-9.41-9.41c-1.787-1.786-1.918-4.602-.405-6.543zm-8.74-.235c5.177 0 9.374-4.197 9.374-9.374 0-5.176-4.197-9.373-9.374-9.373-5.176 0-9.373 4.197-9.373 9.373 0 5.177 4.197 9.374 9.373 9.374zm11.687 4.975c-.732-.733-.735-1.917.005-2.657.735-.735 1.93-.732 2.657-.005l9.104 9.104c.733.73.736 1.916-.004 2.656-.735.735-1.93.73-2.657.005l-9.105-9.103z"
    fill-rule="evenodd" />
  </symbol>
  <symbol xmlns="http://www.w3.org/2000/svg" id="sbx-icon-clear-3" viewBox="0 0 20 20">
    <path d="M8.114 10L.944 2.83 0 1.885 1.886 0l.943.943L10 8.113l7.17-7.17.944-.943L20 1.886l-.943.943-7.17 7.17 7.17 7.17.943.944L18.114 20l-.943-.943-7.17-7.17-7.17 7.17-.944.943L0 18.114l.943-.943L8.113 10z" fill-rule="evenodd" />
  </symbol>
</svg>

  <div role="search" class="sbx-airbnb__wrapper">
    <input 
      type="search"
      @keyup.prevent="onSearchInput"
			v-model="searchInput"
      name="search" 
      placeholder="Search your website" 
      autocomplete="off" 
      required="required" 
      class="sbx-airbnb__input">
    <button title="Submit your search query." class="sbx-airbnb__submit">
      <svg role="img" aria-label="Search">
        <use xlink:href="#sbx-icon-search-23"></use>
      </svg>
    </button>
    <button type="reset" title="Clear the search query." class="sbx-airbnb__reset">
      <svg role="img" aria-label="Reset">
        <use xlink:href="#sbx-icon-clear-3"></use>
      </svg>
    </button>
  </div>
</div>
</template>

<script>
export default {
  props: ['input', 'date', 'pagination', 'url', 'moduleState'],

	data() {
		return {
			searchInput: "",
			dateSelect: "",
			dateInput: "",
			data: {
				searchInput: "",
				date: "",
				url: "",
				module: "",
				pagination: false,
			},
		
		};
	},
	methods: {
		onSearchInput() {

      console.log(this.url)
			// 1. WE GET THE INPUT SEARCH IF ANY

			if (this.input) {
				this.data.searchInput = this.searchInput;
			}

			// 2. WE GET THE DATE IF ANY
		
			if (this.pagination) {
				this.data.pagination = true;
			}
			if (this.url) {
				this.data.url = this.url;
			}
			if (this.moduleState) {
				this.data.module = this.moduleState;
			}

			// CHECK TO SEE IF DATE IS INCLUDED

			this.$store.dispatch("onFilter", this.data);

			// console.log(this.searchInput)
		},
		onDateSelect() {},
	},
};
</script>

<style scoped>
.searchbnb {
  position: relative;
}
.sbx-airbnb {
  display: inline-block;
  position: relative;
  width: 100%;
  height: 33px;
  white-space: nowrap;
  box-sizing: border-box;
  font-size: 14px;
}

.sbx-airbnb__wrapper {
  width: 100%;
  height: 100%;
}

.sbx-airbnb__input {
  display: inline-block;
  -webkit-transition: box-shadow .4s ease, background .4s ease;
  transition: box-shadow .4s ease, background .4s ease;
  border: 0;
  border-radius: 1px;
  box-shadow: inset 0 0 0 0px #CCCCCC;
  background: #FFFFFF;
  padding: 0;
  padding-right: 42px;
  padding-left: 51px;
  width: 100%;
  height: 100%;
  vertical-align: middle;
  white-space: normal;
  font-size: inherit;
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
}

.sbx-airbnb__input::-webkit-search-decoration, .sbx-airbnb__input::-webkit-search-cancel-button, .sbx-airbnb__input::-webkit-search-results-button, .sbx-airbnb__input::-webkit-search-results-decoration {
  display: none;
}

.sbx-airbnb__input:hover {
  box-shadow: inset 0 0 0 0px #b3b3b3;
}

.sbx-airbnb__input:focus, .sbx-airbnb__input:active {
  outline: 0;
  box-shadow: inset 0 0 0 0px #D6DEE3;
  background: #FFFFFF;
}

.sbx-airbnb__input::-webkit-input-placeholder {
  color: #9AAEB5;
}

.sbx-airbnb__input::-moz-placeholder {
  color: #9AAEB5;
}

.sbx-airbnb__input:-ms-input-placeholder {
  color: #9AAEB5;
}

.sbx-airbnb__input::placeholder {
  color: #9AAEB5;
}

.sbx-airbnb__submit {
  position: absolute;
  top: 0;
  right: inherit;
  left: 0;
  margin: 0;
  border: 0;
  border-radius: 0px 0 0 0px;
  background-color: white;
  padding: 0;
  width: 41px;
  height: 100%;
  vertical-align: middle;
  text-align: center;
  font-size: inherit;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

.sbx-airbnb__submit::before {
  display: inline-block;
  margin-right: -4px;
  height: 100%;
  vertical-align: middle;
  content: '';
}

.sbx-airbnb__submit:hover, .sbx-airbnb__submit:active {
  cursor: pointer;
}

.sbx-airbnb__submit:focus {
  outline: 0;
}

.sbx-airbnb__submit svg {
  width: 27px;
  height: 27px;
  vertical-align: middle;
  fill: #CDD0CC;
}

.sbx-airbnb__reset {
  display: none;
  position: absolute;
  top: 7px;
  right: 7px;
  margin: 0;
  border: 0;
  background: none;
  cursor: pointer;
  padding: 0;
  font-size: inherit;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
  fill: rgba(0, 0, 0, 0.5);
}

.sbx-airbnb__reset:focus {
  outline: 0;
}

.sbx-airbnb__reset svg {
  display: block;
  margin: 4px;
  width: 11px;
  height: 11px;
}

.sbx-airbnb__input:valid ~ .sbx-airbnb__reset {
  display: block;
  -webkit-animation-name: sbx-reset-in;
          animation-name: sbx-reset-in;
  -webkit-animation-duration: .15s;
          animation-duration: .15s;
}

@-webkit-keyframes sbx-reset-in {
  0% {
    -webkit-transform: translate3d(-20%, 0, 0);
            transform: translate3d(-20%, 0, 0);
    opacity: 0;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}

@keyframes sbx-reset-in {
  0% {
    -webkit-transform: translate3d(-20%, 0, 0);
            transform: translate3d(-20%, 0, 0);
    opacity: 0;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}

</style>
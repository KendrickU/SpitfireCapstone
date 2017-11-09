new Vue({
  el:"#first",
})

Vue.use(VueTabs);
new Vue({
  el:"#mainTabs",
  data:{
    tabs: ['Show List', 'Item List', 'Calendar View', 'Daily Tasks'], 
  },
  methods: {
    removeTab(x){
      for (let i = 0; i < this.tabs.length; i++) {
          if (this.tabs[i] === x) {
            this.tabs.splice(i, 1);
          }
        }
    },
    addGearTab(){
      this.tabs.push('Gear List')
    }
  }
})

new Vue({
  el:"#showTabs",
  data:{
    tabs: ['Main View'], 
	title: ''
  },
  methods: {
    removeTab(x){
      for (let i = 0; i < this.tabs.length; i++) {
          if (this.tabs[i] === x) {
            this.tabs.splice(i, 1);
          }
        }
    }, 
	addShowTab: function (message) {
	  this.title = message;
      this.tabs.push(message);
    }
  }
})
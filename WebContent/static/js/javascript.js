new Vue({
  el:"#first",
})

Vue.use(VueTabs);
new Vue({
  el:"#mainTabs",
  data:{
    tabs: ['Show List', 'Item List', 'Calendar View', 'To Do List'], 
  },
  methods: {
    removeTab(x){
      for (let i = 0; i < this.tabs.length; i++) {
          if (this.tabs[i] === x) {
            this.tabs.splice(i, 1);
          }
        }
    },
    addTab(){
      this.tabs.push('Show List')
    }
  }
})

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
    }, 
	addDailyTab(){
		this.tabs.push('Daily Tasks')
	}, 
	addGanttTab(){
		this.tabs.push('Gantt View')
	}, 
	addCalendarTab(){
		this.tabs.push('Calendar View')
	}, 
	addShowTab: function (message) {
	  this.title = message;
      this.tabs.push(message);
    }, 
	addItemTab() {
	  this.tabs.push('Item List')
    }, 
  }
})

new Vue({
	el:"#addGear", 
	data:{
		show: false
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

new Vue({
  el:"#dropdown",
  data: {
    master_category: '',
    sub_category: '',
    list: {
            'Lighting': [{sub_category: 'Adapters'}, {sub_category: 'Bolts/Pins/Tools'}, {sub_category: 'Cases'}, {sub_category: 'Data Cable'},
                {sub_category: 'Desks-Moving Lights'}, {sub_category: 'Dimmers'}, {sub_category: 'Distros'}, {sub_category: 'F1 Moving Lights'},
                {sub_category: 'F2 Led Lights'}, {sub_category: 'F3 Static Lights'}, {sub_category: 'F4 Strobe Lights'},
                {sub_category: 'F5 Spotlights'}, {sub_category: 'Lamps'}, {sub_category: 'Fans'}, {sub_category: 'Feeder'},
                {sub_category: 'Foggers'}, {sub_category: 'Hardware'}, {sub_category: 'Hazers'}, {sub_category: 'Intercom/Radio'},
                {sub_category: 'Lifts'}, {sub_category: 'Multicable'}, {sub_category: 'Pipe'}, {sub_category: 'Power Cable (A/C)'},
                {sub_category: 'Snakes'}, {sub_category: 'Softgoods'}],
            'Truss': [{sub_category: 'Truss 12"'}, {sub_category: 'Truss 16"'}, {sub_category: 'Truss 20.5"'}, {sub_category: 'Truss Floor Bases'},
                {sub_category: 'Truss GT'}, {sub_category: 'Truss Pre-Rig 30"'}, {sub_category: 'Truss Tri-Truss'}],
            'Rigging & Motors': [{sub_category: 'Fall Arrest'}, {sub_category: 'Motors'}, {sub_category: 'Motor Cable'},
                {sub_category: 'Motor Controls'}, {sub_category: 'Rigging'}],
    }
  }
})

 Vue.component('date-picker', VueBootstrapDatetimePicker.default);
  
  new Vue({
    el: '#app',
    data: {
      date1: null,
	  date2: null,
	  date3: null,
	  date4: null,
	  use24hours: true,
	  config: {
		format: 'YYYY-MM-DD HH:mm'
		}
    },    
  });
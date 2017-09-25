new Vue({
  el: '#login',
  data: {
    message: 'Welcome to Spitfire\'s Application!',
    credentials:{	
    	user: '',
    	pass: ''
    }
  },
  methods: {
	    submit: function () {
	      window.location = 'Home.html';
	    }
	  }
})

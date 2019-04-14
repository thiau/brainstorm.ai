(function () {
	"use strict";

	const Vue = require("vue");
	const App = require("./components/app.vue");

	new Vue({
		"el": "#app",
		"render": function (h) {
			return h(App);
		}
	});
}())
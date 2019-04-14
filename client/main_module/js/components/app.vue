<template>
	<div id="app">
		<div class="header">
			<div class="header-center">
				<div class="header-center-text">NEW SESSION</div>
				<div class="header-center-text">JOIN SESSION</div>
				<div class="header-center-text">HOW IT WORKS</div>
			</div>
		</div>
		<div class="center-text">Brainstorm.AI</div>
	</div>
</template>

<script>
(function() {
  "use strict";

  module.exports = {
    props: [],
    data: function() {
      return {};
    },
    components: {},
    methods: {},
    computed: {}
  };
})();
</script>


<style scoped>
#app {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-image: linear-gradient(
    to right top,
    #6cdadf,
    #00c3ea,
    #00a7f6,
    #0085f6,
    #6458dd
  );
  justify-content: center;
  align-items: center;
}

.center-text {
  display: flex;
  color: white;
  font-weight: bold;
  font-size: 40pt;
  font-family: azoBold;
}

.header {
  height: 70px;
  width: 100%;
  position: absolute;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
}

.header-center {
  display: flex;
  justify-content: center;
  flex-direction: row;
  width: 500px;
  display: flex;
  justify-content: space-around;
  font-family: azoRegular;
  letter-spacing: 1px;
}

.header-center-text {
  cursor: pointer;
}

@font-face {
  font-family: azoRegular;
  src: url("../client/fonts/azo-regular.otf");
}

@font-face {
  font-family: azoBold;
  src: url("../client/fonts/azo-bold.otf");
}
</style>
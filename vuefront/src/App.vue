<template>

  <div class="container-fluid mt-3 pt-3 text-center">
    <div v-if="$store.state.isAuthenticated" class="logout text-center">
      <form @submit.prevent="logoutForm">
        <button type="submit" class="mt-3 btn btn-dark btn-lg rounded-5 col-2 text-light fw-bold fs-5"
          style="background: linear-gradient(to right,red,black)">Log out <font-awesome-icon
            icon="fa-solid fa-right-from-bracket" /></button>
      </form>
    </div>

  </div>

  <router-view />

</template>


<script>

import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const access = this.$store.state.access

    const user = this.$store.state.isAuthenticated
    console.log(access, 'no token found:( in app.vue')

    if ((access) && (user)) {
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },

  mounted() {

    const user = this.$store.state.isAuthenticated
    if (user) {
      this.$router.push('/apidata')
      setInterval(() => {
        this.getAccess()
      }, 30000)
    }
    else {
      this.$router.push('/')
    }


  },
  methods: {

    logoutForm(e) {
      this.$store.commit('removeAccess');
      localStorage.setItem('access', '');
      localStorage.setItem('refresh', '');
      axios.defaults.headers.common['Authorization'] = ''
      const user = this.$store.state.isAuthenticated
      if (!user) {
        this.$router.push('/log-in')
      }
    },


    getAccess(e) {
      const accessData = {
        refresh: this.$store.state.refresh
      }

      axios.post('/security/jwt/refresh/', accessData)
        .then(response => {
          const access = response.data.access
          console.log(response.data)
          localStorage.setItem('access', access)
          this.$store.commit('setAccess', access)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}


</script>


<style lang="scss">
body {
  padding-top: 70px;
  background: linear-gradient(to right, cyan, blue, black);
}

html {
  height: 100%;
}

.navbar {
  border-bottom: .4vh solid white;
  background: linear-gradient(to right, white, cyan, rgb(0, 230, 255), rgb(0, 180, 255), rgb(0, 160, 255), rgb(0, 130, 255), rgb(0, 100, 255));
}
</style>

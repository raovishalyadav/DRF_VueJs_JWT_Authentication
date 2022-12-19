<template>

  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div id="liveToast" class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true"
      data-bs-delay="2500">
      <div class="toast-header">
        <font-awesome-icon icon="fa-solid fa-triangle-exclamation" style="color:red" />
        <strong class="me-auto text-dark fs-5 ps-2">Error!</strong>
      </div>
      <div class="toast-body">
      </div>
    </div>
  </div>

  <div class="container-fluid mt-4 pt-4 text-center">
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
      }, 29000)
    }
    else {
      this.$router.push('/')
    }

  },
  methods: {

    logoutForm(e) {
      this.$store.commit('removeAccess');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
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
  margin-top: 13vh;
  background: linear-gradient(to right, cyan, blue, black);
}

html {
  height: 100%;
}

.navbar {
  height: 15vh;
  border-bottom: .4vh solid white;
  background: linear-gradient(to right, white, cyan, rgb(0, 230, 255), rgb(0, 180, 255), rgb(0, 160, 255), rgb(0, 130, 255), rgb(0, 100, 255));
}
</style>

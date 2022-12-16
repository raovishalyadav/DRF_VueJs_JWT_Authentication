<template>

    <div class="login shadow-lg rounded-3 col-3 p-5 text-center bg-light text-dark centerlogin">
        <form @submit.prevent="submitForm">
            <font-awesome-icon icon="fa-solid fa-circle-user" size="6x" style="color:purple" />
            <p class="mb-4 fw-bold fs-2" style="font-family: Verdana,monospace ">USER LOGIN</p>
            <div class="input text-start">
                <font-awesome-icon icon="fa-solid fa-envelope" /> <label for="email" class="fs-6">Email
                    Address</label>
                <input class="form-control bg-info bg-opacity-10 border-0 border-bottom border-info" type="email"
                    name="username" v-model="username" placeholder=" Type your email" />
            </div>
            <div class="input text-start mt-1">
                <font-awesome-icon icon="fa-solid fa-key" /> <label for="password" class="fs-6">Password</label>
                <input class="form-control bg-info bg-opacity-10 border-0 border-bottom border-info" type="password"
                    name="password" v-model="password" placeholder=" Type your password" />
            </div>

            <button type="submit" class="mt-4 btn btn-dark rounded-5 col-12 text-light fw-bold fs-5"
                style="background: linear-gradient(to right,blue,purple)">
                Sign in
                <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
            </button>

            <router-link to="/sign-up">
                <button type="submit" class="mt-4 btn btncolor rounded-5 col-12 fw-bold fs-5" style="">
                    Sign up ?
                    <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
                </button></router-link>

        </form>
    </div>


</template>
    
<script>
import axios from 'axios';

export default {
    name: 'login',

    data() {
        return {
            username: '',
            password: ''
        }
    },

    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                password: this.password
            }
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('access')

            axios
                .post('/security/jwt/create/', formData)
                .then(response => {
                    const access = response.data.access
                    const refresh = response.data.refresh

                    this.$store.commit('setAccess', access)
                    this.$store.commit('setRefresh', refresh)

                    axios.defaults.headers.common['Authorization'] = 'JWT ' + access
                    localStorage.setItem('access', access)
                    localStorage.setItem('refresh', refresh)

                    const user = this.$store.state.isAuthenticated
                    if (user) {
                        this.$router.push('/apidata')
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}

</script>

<style scoped>
.centerlogin {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.btncolor {
    color: black;
    background-image: linear-gradient(to right, blue, purple);
    background-origin: border-box;
    box-shadow: 2px 1000px 1px #fff inset;
}

.btncolor:hover {
    box-shadow: none;
    color: white;
}
</style>

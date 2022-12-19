<template>

    <div class="login rounded-3 col-3 px-5 py-3 text-center bg-light text-dark centerlogin">
        <form @submit.prevent="submitForm">
            <font-awesome-icon icon="fa-solid fa-circle-user" style="color:purple;height: 12vh;" />
            <p class="fw-bold fs-3" style="font-family: Verdana,monospace ;margin-top: 1vh;height: 5vh;">USER LOGIN</p>

            <div class="input text-start col-12" style="margin-top: 1vh;height: 8vh;">
                <font-awesome-icon icon="fa-solid fa-envelope" /> <label for="email" class="fs-6">Email
                    Address</label>
                <input class="form-control bg-info bg-opacity-10 border-0 border-bottom border-info input-txt"
                    type="email" name="username" v-model="username" placeholder=" Type your email" required />
            </div>

            <div class="input text-start" style="margin-top: 1vh;height: 8vh;">
                <font-awesome-icon icon="fa-solid fa-key" /> <label for="password" class="fs-6">Password</label>
                <div style="display: flex; align-items: center">
                    <input
                        class="col-10 form-control bg-info bg-opacity-10 border-0 border-bottom border-info me-2 input-txt"
                        type="password" name="password" id="password" v-model="password"
                        placeholder=" Type your password" required />
                    <font-awesome-icon :icon="passwordHidden ? 'fa-solid fa-eye' : 'fa-solid fa-eye-slash'"
                        @click="togglePasswordVisibility" />
                </div>
            </div>

            <button type="submit" class="btn btn-dark rounded-5 col-12 text-light fw-bold fs-5"
                style="background: linear-gradient(to right,blue,purple);margin-top: 4vh;height: 6.5vh;">
                Sign in
                <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
            </button>

            <router-link to="/sign-up">
                <button type="submit" class="btn btncolor rounded-5 col-12 fw-bold fs-5"
                    style="margin-top: 1vh;height: 6.5vh;">
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
            password: '',
            passwordHidden: false,
        }
    },

    methods: {

        togglePasswordVisibility() {
            this.passwordHidden = !this.passwordHidden;
            const passwordInput = document.getElementById('password');
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
            } else {
                passwordInput.type = 'password';
            }
        },


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
                    const toastLiveExample = document.getElementById('liveToast')
                    const element = document.querySelector('.toast-body');
                    element.innerHTML = 'You have entered an invalid username or password.';
                    const toast = new bootstrap.Toast(toastLiveExample)
                    toast.show()
                })


        }

    }
}

</script>

<style scoped>
.centerlogin {
    margin-top: 7.5vh;
    height: 60vh;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.centerlogin:hover {
    box-shadow: 0 0 3vw cyan;
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

.input-txt::placeholder {
    font-size: 0.8rem;
}
</style>

<template>

  <div class="row pt-2">
    <div class="col-12 mx-auto">
      <div class="input-group my-2 mb-3">
        <div class="col-1 me-2 ms-1">
          <input type="text" v-model="first" class="form-control" placeholder=" Text">
        </div>
        <div class="col-1 me-2">
          <input type="number" v-model="third" class="form-control" placeholder=" Integer">
        </div>
        <div class="col-2 me-2">
          <input type="email" v-model="fourth" class="form-control" placeholder=" Email">
        </div>
        <label class="me-2 my-auto fw-bold text-dark">Boolean:</label>
        <input type="checkbox" v-model="fifth" class="form-check-input me-2 my-auto" value="">
        <button @click="$refs.image.click()" class="border-light rounded-2 me-2 btn btn-light">Choose Image
          <font-awesome-icon icon="fa-solid fa-image" /></button>
        <input style="display: none" type="file" ref="image" v-on:change="handleImageUpload()">
        <button @click="$refs.file.click()" class="border-light rounded-2 me-2 btn btn-light">Choose File
          <font-awesome-icon icon="fa-solid fa-file" /></button>
        <input style="display: none" type="file" ref="file" v-on:change="handleFileUpload()">
        <textarea class="form-control me-2 rounded-2" rows="1" v-model="eight" placeholder="Comments"></textarea>
        <select v-model="nine" class="rounded-2 me-2">
          <option value="TODO">TODO</option>
          <option value="DONE">DONE</option>
        </select>

        <button class='btn btn-block btn-success me-1' @click="saveCRUD()">Save
          <font-awesome-icon icon="fa-solid fa-cloud-arrow-up" /></button>
      </div>

    </div>
    <div class="col-12 tableFixHead">
      <table class="table table-hover table-dark table-striped">
        <thead class="text-dark">
          <tr>
            <th class="text-center align-middle px-5">Text</th>
            <th class="text-center align-middle px-5">Timestamp</th>
            <th class="text-center align-middle px-4">Integer</th>
            <th class="text-center align-middle px-5">Email</th>
            <th class="text-center align-middle px-2">Boolean</th>
            <th class="text-center align-middle px-5">Image</th>
            <th class="text-center align-middle px-5">File</th>
            <th class="text-center align-middle px-5">Comments</th>
            <th class="text-center align-middle px-1">Dropdown</th>
            <th class="text-center align-middle px-5">Url</th>
            <th class="text-center align-middle px-1">Edit</th>
            <th class="text-center align-middle px-1">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for='blog in blogs' :key='blog.url'>
            <td class="text-center align-middle text-light">{{ blog.first }}</td>
            <td class="text-center align-middle text-light">{{ blog.second }}</td>
            <td class="text-center align-middle text-light">{{ blog.third }}</td>
            <td class="text-center align-middle text-light">{{ blog.fourth }}</td>
            <td class="text-center align-middle text-light">{{ blog.fifth }}</td>
            <td class="text-center align-middle py-3 px-2"><img :src="blog.sixth" alt="Image Not Found"></td>
            <td class="text-center align-middle " v-if="blog.seventh"> {{
                getFileName(blog.seventh)
            }}<a v-bind:href="blog.seventh"> DOWNLOAD</a></td>
            <td class="text-center align-middle text-light" v-else></td>
            <td class="text-center align-middle text-light">{{ blog.eight }}</td>
            <td class="text-center align-middle text-light">{{ blog.nine }}</td>
            <td class="text-center align-middle"><a v-bind:href="blog.url">{{ blog.url }}</a></td>
            <td class="text-center align-middle">
              <button class="btn btn-warning" @click='editCRUD(blog)'>
                <font-awesome-icon icon="fa-solid fa-pen-to-square" />
              </button>
            </td>
            <td class="text-center align-middle">
              <button class="btn btn-outline-danger" @click='deleteCRUD(blog)'>
                <font-awesome-icon icon="fa-solid fa-trash-can" />
              </button>
            </td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>

</template>
  
<script>
import axios from 'axios';

export default {
  name: 'apidata',
  props: {},
  data() {
    return {
      base_url: 'http://127.0.0.1:8000/CRUD/',
      blogs: null,
      url: '',
      first: '',
      third: '',
      fourth: '',
      fifth: '',
      sixth: '',
      seventh: '',
      eight: '',
      nine: ''
    }
  },
  methods: {

    getFileName(filePath) {
      return filePath.split('/').pop();
    },

    handleImageUpload() {
      this.image = this.$refs.image.files[0];
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },

    getCRUD() {
      axios.get(this.base_url)
        .then(APIdata => {
          this.blogs = APIdata.data;
          this.url = '';
          this.first = '';
          this.third = '';
          this.fourth = '';
          this.fifth = '';
          this.sixth = '';
          this.seventh = '';
          this.eight = '';
          this.nine = '';
        });
    },

    saveCRUD() {
      if (this.url == '') {

        let formData = new FormData();
        formData.append('first', this.first);
        formData.append('third', this.third);
        formData.append('fourth', this.fourth);
        formData.append('fifth', this.fifth);
        if ((typeof this.image) == 'object') {
          formData.append('sixth', this.image, this.image.name);
        }
        if ((typeof this.file) == 'object') {
          formData.append('seventh', this.file, this.file.name);
        }
        formData.append('eight', this.eight);
        formData.append('nine', this.nine);
        // You should have a server side REST API 
        axios.post(this.base_url,
          formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
        ).then(() => {
          this.image = '',
            this.file = '',
            this.sixth = '',
            this.seventh = '',
            this.getCRUD();
          console.log('SUCCESS!!');
        })
          .catch(function () {
            this.getCRUD();
            console.log('FAILURE!!');
          })
      } else {
        let formData = new FormData();
        formData.append('first', this.first);
        formData.append('third', this.third);
        formData.append('fourth', this.fourth);
        formData.append('fifth', this.fifth);
        if ((((typeof this.image) != 'undefined') && ((typeof this.image) != 'string') && ((this.sixth) != null)) || (
          typeof this.image == 'object')) {
          formData.append('sixth', this.image, this.image.name);
        }
        if ((((typeof this.file) != 'undefined') && ((typeof this.file) != 'string') && ((this.seventh) != null)) || (
          typeof this.file == 'object')) {
          formData.append('seventh', this.file, this.file.name);
        }
        formData.append('eight', this.eight);
        formData.append('nine', this.nine);
        axios.patch(this.url,
          formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
        ).then(() => {
          this.image = '',
            this.file = '',
            this.sixth = '',
            this.seventh = '',
            this.getCRUD();
          formData = {};
          console.log('patch SUCCESS!!');
        })
          .catch((error) => {
            this.getCRUD();
            if (error.response) {

              console.log('response error!!');
            } else if (error.request) {

              console.log('request error!!');
            } else if (error.message) {

              console.log('message error!!');
            }
          })

      }
    },

    editCRUD(blog) {
      this.url = blog.url;
      this.first = blog.first;
      this.third = blog.third;
      this.fourth = blog.fourth;
      this.fifth = blog.fifth;
      this.sixth = blog.sixth;
      this.seventh = blog.seventh;
      this.eight = blog.eight;
      this.nine = blog.nine;

    },

    deleteCRUD(blog) {
      axios.delete(blog.url)
        .then(() => {
          this.getCRUD();
        });
    }

  },
  mounted() {
    const user = this.$store.state.isAuthenticated

    if (user) {
      this.$router.push('/apidata');
      this.getCRUD();
    }
    else {
      this.$router.push('/')
    }

  }
}
</script>
  
<style scoped>
img {
  width: 12vw;
  height: 15vh;
  border-radius: 10px;
  box-shadow: 1px 1px 10px 1px rgba(255, 255, 255, 0.5);
}

.tableFixHead {
  overflow-y: auto;
  height: 65.5vh;
}

.tableFixHead th {
  position: sticky;
  top: 0vh;
  background-color: cyan;
}

.table {
  border-collapse: separate;
  border-spacing: 0;
}

table th {
  border: .13rem solid black;
}

table td {
  border: .1rem solid cyan;
}
</style>

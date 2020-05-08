<script src="https://apis.google.com/js/platform.js" async defer></script>
<template>
  <v-container class="fill-height" fluid>
    <!-- <HeaderItem/> -->
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-img
          alt="OICJOB Logo"
          src="../assets/logo.png"
          transition="scale-transition"
          class="mb-5 ml-1"
        />
        <GoogleLogin
          :params="params"
          :renderParams="renderParams"
          :onSuccess="onSuccess"
          :onFailure="onFailure"
          align="center"
        ></GoogleLogin>
        <GoogleLogin :params="params" :logoutButton="true">Logout</GoogleLogin>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
// import HeaderItem from '@/components/HeaderItem.vue'
import GoogleLogin from "vue-google-login";

export default {
  name: "Login",
  data() {
    return {
      params: {
        client_id: process.env.VUE_APP_CLIENT_ID
      },
      renderParams: {
        width: 250,
        height: 50,
        longtitle: true
      }
    };
  },
  components: {
    GoogleLogin
  },
  methods: {
    onSuccess: function(googleUser) {
      // var profile = googleUser.getBasicProfile();
      // console.log("ID: " + profile.getId());
      // console.log("Name: " + profile.getName());
      // console.log("Image URL: " + profile.getImageUrl());
      // console.log("Email: " + profile.getEmail());
      this.$axios
        .post("/oicjob/api/oauth/login", {
          id_token: googleUser.getAuthResponse().id_token
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(err => {
          console.log(err);
        });
      // this.$router.replace("/create_account");
    },
    onFailure: function() {
      console.log("failed...");
    }
  }
};
</script>
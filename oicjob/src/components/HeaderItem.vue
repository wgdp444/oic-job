<template>
  <v-app-bar app color="blue lighten-3" dark>
    <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
    <div class="d-flex align-center">
      <v-img
        alt="OICJOB Logo"
        class="shrink mr-2"
        contain
        src="../assets/logo.png"
        transition="scale-transition"
        width="150"
      />
    </div>
    <v-spacer></v-spacer>
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-avatar color="teal" size="48" style="cursor:pointer;" v-on="on">
          <!-- <span class="white--text headline">aaa</span> -->
          <img :src="userImage" alt />
        </v-avatar>
      </template>
      <v-layout justify-center>
        <v-avatar class="center" color="teal" size="60">
          <!-- <span class="white--text headline">aaa</span> -->
          <img :src="userImage" alt />
        </v-avatar>
      </v-layout>
      <p class="text-center mt-1">{{ userFirstName }} {{ userLastName }}</p>
      <v-divider></v-divider>
      <v-list>
        <v-list-item v-for="(item, index) in userMenuItems" :key="index" @click="item.route">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>


<script>
import Vue from "vue";
export default {
  name: "HeaderItem",
  data: function() {
    return {
      userImage: "None",
      userFirstName: "None",
      userLastName: "None",
      userMenuItems: [{ title: "プロフィール", route: this.Logout }, { title: "ログアウト", route: this.Logout }]
    };
  },
  // components: {
  //   HeaderItem
  // },
  created() {
    // view が作られた時にデータを取得し、
    // そのデータは既に監視されています
    this.getUserProfile();
  },
  watch: {
    // ルートが変更されたらこのメソッドを再び呼び出します
    $route: "getUserProfile"
  },
  methods: {
    getUserProfile() {
      Vue.GoogleAuth.then(auth2 => {
        let user = auth2.currentUser.get();
        let userProfile = user.getBasicProfile();
        this.userImage = userProfile.getImageUrl();
        this.userFirstName = userProfile.getFamilyName();
        this.userLastName = userProfile.getGivenName();
      });
    },
    Logout() {
      Vue.GoogleAuth.then(auth2 => {
        auth2.signOut()
    })
      this.$router.replace("/login");
      this.$router.go({path: this.$router.currentRoute.path, force: true});
    }
  }
};
</script>
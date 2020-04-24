<template>
  <v-app-bar
      app
      color="blue lighten-3"
      dark
    >
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
      <v-avatar color="teal" size="48">
        <!-- <span class="white--text headline">aaa</span> -->
        <img src="../assets/test.jpg" alt="">
      </v-avatar>
    </v-app-bar>
</template>


<script>
export default {
  name: 'HeaderItem'
}
</script>
<template>
  <v-content>
    <HeaderItem/>
  </v-content>
</template>

<script>
// @ is an alias to /src
import HeaderItem from '../components/HeaderItem'

export default {
  name: "Home",
  components: {
    HeaderItem
  }
};
</script>
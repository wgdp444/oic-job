<template>
  <v-content>
    <HeaderItem/>
    <v-container class="fill-height" fluid>
      <v-card
    class="mx-auto"
    max-width="344"
  >
      <v-text-field
            value="John Doe"
            label="Outlined"
            outlined
            readonly
            append_icon="place"
          ></v-text-field>
          <v-text-field
            filled
            label="Prepend inner"
            prepend-inner-icon="place"
          ></v-text-field>
          <v-icon>fas fa-search</v-icon>
      </v-card>
      <v-text-field
            v-model="message1"
            label="Regular"
            clearable
          ></v-text-field>
          <v-text-field
            label="Prepend inner"
            prepend-inner-icon="place"
          ></v-text-field><v-text-field
            filled
            label="Prepend inner"
            prepend-inner-icon="place"
          ></v-text-field>
          <v-icon>fas fa-search</v-icon>
          <v-icon>fas fa-search</v-icon>
          <v-icon>fas fa-search</v-icon>
          <v-icon>fas fa-search</v-icon>
          <v-icon>fas fa-search</v-icon>
    </v-container>
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
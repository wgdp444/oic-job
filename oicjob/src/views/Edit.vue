<template>
  <v-content>
    <HeaderItem/>
    <v-container class="fill-height" fluid>

    <v-row>
    <v-card  class="mx-auto mt-12" width="80%">
        <v-card-text>
            <v-container>
                <v-row>
                <v-col cols="12" sm="3" md="3">
                    <v-card-text style="color: black; font-weight: bold; background-color: #eeeeee;">業界</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">職種</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">求人番号</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">本社</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">募集人数</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">初任給</v-card-text>
                </v-col>

                <v-col cols="12" sm="6" md="6">
                    <v-card-text style="color: black; background-color: #eeeeee">IT業界</v-card-text>
                    <v-card-text style="color: black">システムエンジニア</v-card-text>
                    <v-card-text style="color: black">002</v-card-text>
                    <v-card-text style="color: black">岡山県都窪郡早島町早島777-3</v-card-text>
                    <v-card-text style="color: black">10～12</v-card-text>
                    <v-card-text style="color: black">18万5680円</v-card-text>
                </v-col>
                </v-row>

            </v-container>
        </v-card-text>
    </v-card>
    </v-row>

    <v-icon>fas fa-search</v-icon>
    </v-container>
  </v-content>
</template>

<script>
// @ is an alias to /src
import HeaderItem from '../components/HeaderItem'

export default {
  data: () => ({
    
  }),

  name: "Edit",
  components: {
    HeaderItem
  }
};
</script>
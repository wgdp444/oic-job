<template>
  <v-content>
    <HeaderItem/>
    <v-container class="fill-height" fluid>
    <v-row>
      <v-card 
        class="mx-auto"
        width="100%"
        color="primary"
      >
      <v-card-text>
        <v-container>
            <v-row class="my-auto" align-content="center">
                <v-col cols="12" sm="3" md="3">
                    <h1 class="mt-2" style="color: white">株式会社Daizo</h1>
                </v-col>
                <v-col cols="12" sm="5" md="5"></v-col>
                <v-col cols="12" sm="2" md="2" align="center">
                    <v-btn width="80%" color="#76FF03">編集</v-btn>
                </v-col>
                <v-col cols="12" sm="2" md="2" align="center">
                    <v-btn width="80%" color="#F50057">削除</v-btn>
                </v-col>
            </v-row>
        </v-container>
      </v-card-text>

      </v-card>
    </v-row>

    <v-row>
    <v-card  class="mx-auto mt-12" width="80%">
        <v-card-text>
            <v-container>
                <v-row>
                <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold">業界</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">職種</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">求人番号</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">本社</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">募集人数</v-card-text>
                    <v-card-text style="color: black; font-weight: bold">初任給</v-card-text>
                </v-col>

                <v-col cols="12" sm="6" md="6">
                    <v-card-text style="color: black">IT業界</v-card-text>
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

    <v-row>
    <v-card  class="mx-auto mt-12" width="80%">
        <v-card-text>
            <v-container>
                ここにPDFを表示
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

  name: "VerboseSdreen",
  components: {
    HeaderItem
  }
};
</script>
<template>
  <v-content>
    <HeaderItem/>
    <v-container class="fill-height" fluid>

    <v-row>
    <v-card  class="mx-auto mt-12" width="80%">
        <v-card-text>
            <v-container>

                <!-- 企業名 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">企業名</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field label="" value="" single-line></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="1" md="1">
                    <v-card-text style="color: red; font-weight: bold; font-size: small" class="mt-2">必須</v-card-text>
                  </v-col>
                </v-row>
                
                <!-- 業界 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">業界</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="4" md="4">
                    <v-select :items="items" label="業界選択"></v-select>
                  </v-col>
                  <v-col cols="12" sm="1" md="1">
                    <v-card-text style="color: red; font-weight: bold; font-size: small" class="mt-2">必須</v-card-text>
                  </v-col>
                </v-row>

                <!-- 職種 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">職種</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="4" md="4">
                    <v-select :items="items" label="職種選択"></v-select>
                  </v-col>
                  <v-col cols="12" sm="1" md="1">
                    <v-card-text style="color: red; font-weight: bold; font-size: small" class="mt-2">必須</v-card-text>
                  </v-col>
                </v-row>

                <!-- 郵便番号 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">郵便番号</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="2" md="2">
                    <v-text-field label="○○○-○○○○" single-line></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="1" md="1">
                    <v-card-text style="color: red; font-weight: bold; font-size: small" class="mt-2">必須</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="2" md="2" align="center" class="mt-3">
                    <v-btn width="80%" color="#dddddd">住所自動入力</v-btn>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-card-text style="color: orange; font-weight: bold; font-size: small" class="mt-2">※市町村までが自動入力されます</v-card-text>
                  </v-col>
                </v-row>

                <!-- 住所 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">本社住所</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field label="都道府県から番地まで" single-line></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="1" md="1">
                    <v-card-text style="color: red; font-weight: bold; font-size: small" class="mt-2">必須</v-card-text>
                  </v-col>
                </v-row>

                <!-- 事業所 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">事業所</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field label="都道府県(○○、○○、○○)" single-line></v-text-field>
                  </v-col>
                </v-row>

                <!-- 募集人数 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">募集人数</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field label="" single-line></v-text-field>
                  </v-col>
                </v-row>

                <!-- 初任給 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">初任給</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="4" md="4">
                    <v-text-field label="" single-line></v-text-field>
                  </v-col>
                </v-row>

                <!-- 求人票 -->
                <v-row>
                  <v-col cols="12" sm="2" md="2">
                    <v-card-text style="color: black; font-weight: bold; font-size: large" class="mt-2">求人票</v-card-text>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field label="" single-line></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="2" md="2" align="center" class="mt-3">
                    <v-btn width="80%" color="#76FF03">ファイル選択</v-btn>
                  </v-col>
                  <v-col cols="12" sm="1" md="1">
                    <v-card-text style="color: red; font-weight: bold; font-size: small" class="mt-2">必須</v-card-text>
                  </v-col>
                </v-row>

                <v-row class="mt-12">
                  <v-col cols="12" sm="2" md="2" align="center">
                    <v-btn width="80%" color="primary">戻る</v-btn>
                  </v-col>
                  <v-col cols="12" sm="2" md="2" align="center" class="offset-6">
                    <v-btn width="80%" color="#cccccc">キャンセル</v-btn>
                  </v-col>
                  <v-col cols="12" sm="2" md="2" align="center">
                    <v-btn width="80%" color="primary">登録</v-btn>
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
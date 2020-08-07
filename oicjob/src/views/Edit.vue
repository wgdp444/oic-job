<template>
  <v-content>
    <HeaderItem />
    <v-container class="fill-height" fluid>
      <v-row>
        <v-card class="mx-auto mt-12" width="80%">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >企業名</v-card-text>
                </v-col>
                <v-col cols="12" sm="6" md="6">
                  <v-text-field
                    label="企業名"
                    :value="jobofferDetail.company_name"
                    single-line
                    :rules="[v => !!v || '記入してください']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="1" md="1">
                  <v-card-text
                    style="color: red; font-weight: bold; font-size: small"
                    class="mt-2"
                  >必須</v-card-text>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >業界</v-card-text>
                </v-col>
                <v-col cols="12" sm="4" md="4">
                  <v-select
                    v-model="industrySelect"
                    item-text="name"
                    item-value="id"
                    :items="industryItems"
                    :rules="[v => !!v || '選択してください']"
                    required
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="1" md="1">
                  <v-card-text
                    style="color: red; font-weight: bold; font-size: small"
                    class="mt-2"
                  >必須</v-card-text>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >職種</v-card-text>
                </v-col>
                <v-col cols="12" sm="4" md="4">
                  <v-text-field
                    label="企業名"
                    :value="jobofferDetail.occupation"
                    single-line
                    :rules="[v => !!v || '記入してください']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="1" md="1">
                  <v-card-text
                    style="color: red; font-weight: bold; font-size: small"
                    class="mt-2"
                  >必須</v-card-text>
                </v-col>
              </v-row>

              <!-- <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >郵便番号</v-card-text>
                </v-col>
                <v-col cols="12" sm="2" md="2">
                  <v-text-field label="○○○-○○○○" value="701-0304" single-line></v-text-field>
                </v-col>
                <v-col cols="12" sm="1" md="1">
                  <v-card-text
                    style="color: red; font-weight: bold; font-size: small"
                    class="mt-2"
                  >必須</v-card-text>
                </v-col>
                <v-col cols="12" sm="2" md="2" align="center" class="mt-3">
                  <v-btn width="80%" color="#dddddd">住所自動入力</v-btn>
                </v-col>
                <v-col cols="12" sm="3" md="3">
                  <v-card-text
                    style="color: orange; font-weight: bold; font-size: small"
                    class="mt-2"
                  >※市町村までが自動入力されます</v-card-text>
                </v-col>
              </v-row> -->

              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >募集エリア(複数選択可)</v-card-text>
                </v-col>
                <v-col cols="12" sm="4" md="4">
                  <v-select
                    v-model="jobofferDetail.areas"
                    item-text="name"
                    item-value="id"
                    multiple
                    :items="areaItems"
                    :rules="[v => !!v || '選択してください']"
                    required
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="1" md="1">
                  <v-card-text
                    style="color: red; font-weight: bold; font-size: small"
                    class="mt-2"
                  >必須</v-card-text>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >募集人数</v-card-text>
                </v-col>
                <v-col cols="12" sm="3" md="3">
                  <v-text-field label :value="jobofferDetail.max_appicants" single-line></v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >初任給</v-card-text>
                </v-col>
                <v-col cols="12" sm="4" md="4">
                  <v-text-field label :value="jobofferDetail.starting_salary" single-line></v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text
                    style="color: black; font-weight: bold; font-size: large"
                    class="mt-2"
                  >求人票</v-card-text>
                </v-col>
                <v-col cols="12" sm="3" md="3">
                  <v-file-input show-size label="File input" @change="getFile" :rules="[isPDF]"></v-file-input>
                </v-col>
                <v-col cols="12" sm="1" md="1">
                  <v-card-text
                    style="color: red; font-weight: bold; font-size: small"
                    class="mt-2"
                  >必須</v-card-text>
                </v-col>
              </v-row>

              <v-row class="mt-12">
                <v-col cols="12" sm="2" md="2" align="center">
                  <v-btn
                    width="80%"
                    color="primary"
                    @click="(data) => { $router.push(`/verbose_screen/` + jobofferDetail.id) }"
                  >戻る</v-btn>
                </v-col>
                <v-col cols="12" sm="2" md="2" align="center" class="offset-6">
                  <v-btn width="80%" color="#cccccc">キャンセル</v-btn>
                </v-col>
                <v-col cols="12" sm="2" md="2" align="center">
                  <v-btn width="80%" color="primary">確定</v-btn>
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
import HeaderItem from "../components/HeaderItem";
import Vue from "vue";

export default {
  data: () => ({
    jobofferDetail: {},
    industryItems: [],
    areaSelect: ["岡山県", "秋田県"],
    industrySelect: null,
    isPDF: file => file.name.match(/^.*.pdf$/i) || "pdfファイルしか送れません。",
    areaItems: [
      "北海道",
      "青森県",
      "岩手県",
      "宮城県",
      "秋田県",
      "山形県",
      "福島県",
      "茨城県",
      "栃木県",
      "群馬県",
      "埼玉県",
      "千葉県",
      "東京都",
      "神奈川県",
      "新潟県",
      "富山県",
      "石川県",
      "福井県",
      "山梨県",
      "長野県",
      "岐阜県",
      "静岡県",
      "愛知県",
      "三重県",
      "滋賀県",
      "京都府",
      "大阪府",
      "兵庫県",
      "奈良県",
      "和歌山県",
      "鳥取県",
      "島根県",
      "岡山県",
      "広島県",
      "山口県",
      "徳島県",
      "香川県",
      "愛媛県",
      "高知県",
      "福岡県",
      "佐賀県",
      "長崎県",
      "熊本県",
      "大分県",
      "宮崎県",
      "鹿児島県",
      "沖縄県",
    ],
  }),
  methods: {
    getJobofferDetail: function () {
      //求人票データ取得
      Vue.GoogleAuth.then((auth2) => {
        let user = auth2.currentUser.get();
        this.$axios
          .post(
            "/oicjob/api/joboffer/get/" + this.$route.params.id,
            {
              token: user.getAuthResponse().id_token,
            },
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("access_token")}`,
              },
            }
          )
          .then((response) => {
            // 求人がない場合は終了
            this.jobofferDetail = {
              id: response.data["id"],
              company_name: response.data["company_name"],
              industry: response.data["industry"][0]["name"],
              occupation: response.data["occupation"],
              max_appicants: response.data["max_appicants"],
              starting_salary: response.data["starting_salary"],
              areas: response.data["area"]["prefecture"].split(","),
            };
            // 初期値設定
            this.industrySelect = response.data["industry"][0]["id"]
            console.log(this.jobofferDetail);
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    getIndustry: function () {
      //業界データ取得
      Vue.GoogleAuth.then((auth2) => {
        let user = auth2.currentUser.get();
        this.$axios
          .post("/oicjob/api/industry/gets", {
            token: user.getAuthResponse().id_token,
          })
          .then((response) => {
            console.log(response.data["industrys"]);
            for (let subject of response.data["industrys"]) {
              console.log(subject);
              this.industryItems.push({
                id: subject["id"],
                name: subject["name"],
              });
            }
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    getArea: function () {
      //業界データ取得
      Vue.GoogleAuth.then((auth2) => {
        let user = auth2.currentUser.get();
        this.$axios
          .post("/oicjob/api/area/gets", {
            token: user.getAuthResponse().id_token,
          })
          .then((response) => {
            console.log(response.data["areas"]);
            for (let subject of response.data["industrys"]) {
              console.log(subject);
              this.industryItems.push({
                id: subject["id"],
                name: subject["name"],
              });
            }
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    getFile(f) {
      console.log(f)
    }
  },
  mounted: function () {
    this.getJobofferDetail();
    this.getIndustry();
  },

  name: "Edit",
  components: {
    HeaderItem,
  },
};
</script>
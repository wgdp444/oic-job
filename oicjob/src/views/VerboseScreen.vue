<template>
  <v-content>
    <HeaderItem />
    <v-container class="fill-height" fluid>
      <v-row>
        <v-card class="mx-auto" width="100%" color="primary">
          <v-card-text>
            <v-container>
              <v-row class="my-auto" align-content="center">
                <v-col cols="12" sm="3" md="3">
                  <h1 class="mt-2" style="color: white">{{ joboffer_detail.company_name }}</h1>
                </v-col>
                <v-col cols="12" sm="1" md="1" class="offset-6">
                  <v-btn
                    width="100%"
                    color="white"
                    @click="(data) => { $router.push(`/`) }"
                    style="font-weight: bold"
                  >ホームへ</v-btn>
                </v-col>
                <v-col cols="12" sm="1" md="1" align="center">
                  <v-btn
                    width="100%"
                    color="#76FF03"
                    @click="(data) => { $router.push(`/edit/` + joboffer_detail.id) }"
                    style="font-weight: bold"
                  >編集</v-btn>
                </v-col>
                <v-col cols="12" sm="1" md="1" align="center">
                  <v-btn
                    @click="openModal = true"
                    width="100%"
                    color="#F50057"
                    style="color: white; font-weight: bold"
                  >削除</v-btn>
                  <modal v-if="openModal" @close="openModal = false"></modal>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
      </v-row>

      <v-row>
        <v-card class="mx-auto mt-12" width="80%">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" sm="2" md="2">
                  <v-card-text style="color: black; font-weight: bold">業界</v-card-text>
                  <v-card-text style="color: black; font-weight: bold">職種</v-card-text>
                  <v-card-text style="color: black; font-weight: bold">本社</v-card-text>
                  <v-card-text style="color: black; font-weight: bold">募集人数</v-card-text>
                  <v-card-text style="color: black; font-weight: bold">初任給</v-card-text>
                </v-col>

                <v-col cols="12" sm="6" md="6">
                  <v-card-text style="color: black">{{ joboffer_detail.industry }}</v-card-text>
                  <v-card-text style="color: black">{{ joboffer_detail.occupation }}</v-card-text>
                  <v-card-text style="color: black">岡山県都窪郡早島町早島777-3</v-card-text>
                  <v-card-text style="color: black">{{ joboffer_detail.max_appicants }}人</v-card-text>
                  <v-card-text style="color: black">{{ joboffer_detail.starting_salary.toLocaleString() }}円</v-card-text>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
      </v-row>

      <v-row>
        <v-card class="mx-auto mt-12" width="80%">
          <v-card-text>
            <v-container>ここにPDFを表示</v-container>
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
import Modal from "../components/Modal.vue";
import Vue from "vue";

export default {
  data: () => ({
    openModal: false,
    joboffer_detail: {},
  }),
  mounted: function () {
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
          this.joboffer_detail = {
            id: response.data["id"],
            company_name: response.data["company_name"],
            industry: response.data["industry"][0]["name"],
            occupation: response.data["occupation"],
            max_appicants: response.data["max_appicants"],
            starting_salary: response.data["starting_salary"],
            eria: "test県",
          };
          console.log(this.joboffer_detail);
        })
        .catch((err) => {
          console.log(err);
        });
    });
  },
  components: {
    Modal,
    HeaderItem,
  },

  name: "VerboseScreen",
};
</script>
<template>
  <v-app>
    <v-card width="500px" class="mx-auto mt-12">
      <v-card-title>
        <h1 class="display-1">基本情報の登録</h1>
      </v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-select
            v-model="subjectSelect"
            item-text="name"
            item-value="id"
            :items="subjectList"
            :rules="[v => !!v || '選択してください']"
            label="学科"
            required
          ></v-select>

          <v-select
            v-model="classSelect"
            :items="classList"
            :rules="[v => !!v || '選択してください']"
            label="クラス"
            required
          ></v-select>

          <v-btn :disabled="!valid" class="info" @click="validate">登録</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
    <!-- <v-content>
      <HeaderItem />
    </v-content>-->
  </v-app>
</template>

<script>
// @ is an alias to /src
// import HeaderItem from "../components/HeaderItem";
import Vue from "vue";

export default {
  data: () => ({
    subjectList: [],
    classList: ["無し", 1, 2, 3, 4],
    valid: true,
    classSelect: null,
    subjectSelect: null,
  }),
  methods: {
    //入力チェック
    validate() {
      if (this.$refs.form.validate()) {
        Vue.GoogleAuth.then((auth2) => {
          let user = auth2.currentUser.get();
          this.$axios
            .post("/oicjob/api/user/create", {
              token: user.getAuthResponse().id_token,
              is_admin: false,
              subject_id: this.subjectSelect,
              class_number: this.classSelect,
            })
            .then((response) => {
              console.log(response.data);
            })
            .catch((err) => {
              console.log(err);
            });
        });
        // location.href = "/";
      }
    },
  },
  mounted: function () {
    //学科データ取得
    Vue.GoogleAuth.then((auth2) => {
      let user = auth2.currentUser.get();
      this.$axios
        .post("/oicjob/api/subject/gets", {
          token: user.getAuthResponse().id_token,
        })
        .then((response) => {
          console.log(response.data["subjects"]);
          for (let subject of response.data["subjects"]) {
            console.log(subject);
            this.subjectList.push({
              id: subject["id"],
              name: subject["name"],
            });
          }
          console.log(Object.values(this.subjectList));
        })
        .catch((err) => {
          console.log(err);
        });
    });
  },
  name: "CreateAccount",
  // components: {
  //   HeaderItem
  // }
};
</script>
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

          <v-btn
            :disabled="!valid"
            class="info"
            @click="validate" 
            >登録
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
    <v-content>
      <HeaderItem/>
    </v-content>
  </v-app>
</template>

<script>
// @ is an alias to /src
import HeaderItem from '../components/HeaderItem'

export default {
  data: () => ({
    subjectList: [],
    classList: [],
    valid: true,
    classSelect:null,
    subjectSelect:null,
  }),
  methods:{
    //入力チェック
    validate () {
        if(this.$refs.form.validate()){
          this.$axios
          .post("/oicjob/api/create_account",{
            classData: 'classSelect',
            subjectData: 'subjectSelect',

          })
          .then(response => {
          console.log(response.data);
          })
          .catch(err => {
          console.log(err);
          });
          location.href = "/"
        }
      },
  },
    mounted:function() {
      //学科データ取得
      this.$axios.get('/oicjob/api/getsubject')
      .then(response => {
       // console.log(response.data)
        this.subjectList = response.data;
      })
      .catch( err => {
        console.log(err);
      });
    //クラスデータ取得
      this.$axios.get('/oicjob/api/getclass')
      .then(response => {
        //console.log(response.data)
        this.classList = response.data;
      })
      .catch( err => {
        console.log(err);
      });
    },
  
  name: "CreateAccount",
  components: {
    HeaderItem
  }

};
</script>
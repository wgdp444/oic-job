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
            :items="subjectItems"
            :rules="[v => !!v || '選択してください']"
            label="学科"
            required
          ></v-select>

          <v-select
            v-model="classSelect"
            :items="classItems"
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
    valid: true,
    classSelect:null,
    classItems:[
      '1',
      '2',
      '3'
    ],
    subjectSelect:null,
    subjectItems:[
      '情スぺ',
      
    ],
    required: value => !!value || "必ず選択"
  }),
  methods:{
    validate () {
        if(this.$refs.form.validate()){
          this.$axios
          .post("/oicjob/api/create_account",{
            classData: 'classSelect',
            subjectData: 'subjectSelect'
          })
          .then(response => {
          console.log(response.data);
          })
          .catch(err => {
          console.log(err);
          });
         // location.href = "/"
        }
      },
  },
  name: "CreateAccount",
  components: {
    HeaderItem
  }
};
</script>
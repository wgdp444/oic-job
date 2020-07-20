<template>
  <v-content>
    <HeaderItem/>
    <v-container class="fill-height" fluid>
    <v-row>
      <v-card 
        class="mx-auto"
        width="70%"
      >
      <v-card-text>

      <v-container>
        <v-row>
          <v-col cols="12" sm="6" md="6">
            <v-text-field
              v-model="search"
              label="企業名を入力"
              append-icon="mdi-magnify"
              outlined
            ></v-text-field>
          </v-col>
          
          <v-col cols="12" sm="3" md="3">
            <v-btn x-large color="primary">検索</v-btn>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" sm="4" md="4">
            <v-overflow-btn
              class="my-2"
              :items="dropdown_edit"
              label="業界"
              editable
              item-value="text"
            ></v-overflow-btn>
          </v-col>
          
          <v-col cols="12" sm="4" md="4">
            <v-overflow-btn
              class="my-2"
              :items="dropdown_edit"
              label="職種"
              editable
              item-value="text"
            ></v-overflow-btn>
          </v-col>

          <v-col cols="12" sm="4" md="4">
            <v-overflow-btn
              class="my-2"
              :items="dropdown_edit"
              label="エリア"
              editable
              item-value="text"
            ></v-overflow-btn>
          </v-col>
        </v-row>
      </v-container>
      </v-card-text>

      </v-card>
      </v-row>

      <v-row>
        <v-card width="1400px" class="mx-auto mt-12">
          <v-card-title>
            検索結果
            <v-spacer></v-spacer>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="desserts"
            :search="search"
          ></v-data-table>
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
    headers: [
      { text: '番号', sortable: false, width: 50,},
      { text: '企業名', sortable: false, },
      { text: '業界', sortable: false, },
      { text: '業種', sortable: false, },
      { text: 'エリア', sortable: false, }
    ]
  }),

  name: "Home",
  components: {
    HeaderItem
  }
};
</script>
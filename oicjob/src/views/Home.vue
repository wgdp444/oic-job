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
              label="検索"
              append-icon="mdi-magnify"
              outlined
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" sm="4" md="4">
            <v-overflow-btn
              v-model="search"
              class="my-2"
              :items="dropdown_industry"
              label="業界"
              editable
              item-value="text"
            ></v-overflow-btn>
          </v-col>
          
          <v-col cols="12" sm="4" md="4">
            <v-overflow-btn
              class="my-2"
              :items="dropdown_industries"
              label="職種"
              editable
              item-value="text"
            ></v-overflow-btn>
          </v-col>

          <v-col cols="12" sm="4" md="4">
            <v-overflow-btn
              class="my-2"
              :items="dropdown_eria"
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
            :items="items"
            item-key="name"
            :search="search"
            @click:row="
              (data) => {
                $router.push(`/verbose_screen`)
              }
            "
            id="table"
          ></v-data-table>
        </v-card>
      </v-row>

      <v-icon>fas fa-search</v-icon>
    </v-container>
  </v-content>
</template>

<style>
#table td {
  cursor: hand;
  cursor: pointer;
}
</style>

<script>
// @ is an alias to /src
import HeaderItem from '../components/HeaderItem'

export default {
  data: () => ({
    dropdown_industry: ['IT'],
    dropdown_industries: ['システムエンジニア'],
    dropdown_eria: [
      '北海道','青森','岩手','宮城','秋田','山形','福島','茨城','栃木','群馬',
      '埼玉','千葉','東京','神奈川','新潟','富山','石川','福井','山梨','長野',
      '岐阜','静岡','愛知','三重','滋賀','京都','大阪','兵庫','奈良','和歌山',
      '鳥取','島根','岡山','広島','山口','徳島','香川','愛媛','高知','福岡',
      '佐賀','長崎','熊本','大分','宮崎','鹿児島','沖縄',
    ],
    search: '',
    headers: [
      { text: '番号', value: 'number', sortable: false, width: 50,},
      { text: '企業名', value: 'name', sortable: false, },
      { text: '業界', value: 'industry', sortable: false, },
      { text: '業種', value: 'industries', sortable: false, },
      { text: 'エリア', value: 'eria', sortable: false, }
    ],
    items: [
      { number: '001', name: '株式会社Daizo1', industry: 'IT', industries: 'システムエンジニア', eria: '岡山県' },
      { number: '002', name: '株式会社Daizo2', industry: 'IT', industries: 'システムエンジニア', eria: '大阪府' },
      { number: '003', name: '株式会社Daizo3', industry: 'IT', industries: 'システムエンジニア', eria: '東京都' },
      { number: '004', name: '株式会社Daizo4', industry: 'IT', industries: 'システムエンジニア', eria: '沖縄県' },
      { number: '005', name: '株式会社Daizo5', industry: 'IT', industries: 'システムエンジニア', eria: '北海道' },
      { number: '006', name: '株式会社Daizo6', industry: 'IT', industries: 'システムエンジニア', eria: '広島県' },
      { number: '007', name: '株式会社Daizo7', industry: 'IT', industries: 'システムエンジニア', eria: '鳥取県' },
      { number: '008', name: '株式会社Daizo8', industry: 'IT', industries: 'システムエンジニア', eria: '島根県' },
    ]
  }),
  

  name: "Home",
  components: {
    HeaderItem
  }
};
</script>
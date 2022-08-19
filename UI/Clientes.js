const clientes = { template: '<table class="table table-striped"><thead><tr><th>ClienteId</th><th>ClienteNome</th><th>ClienteEmail</th> <th>ClienteTelefone</th><th>ClienteEndereco</th><th>ClienteProfissao</th><th>ClinteCurriculo</th></tr><tbody><tr v-for="dep in clientes"></tbody></thead></table>',

data(){
  return{
    Clientes:[]
  }
},
methods:{
  refreshData(){
    axios.get(variables.API_URL+"Clientes")
    .then((response)=>{
      this.clientes=response.data;
    });
  }
},
mounted:functions(){
  this.refreshData();
}

}



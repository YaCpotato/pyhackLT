$(window).load(function(){
    var app = new Vue({
        el:'#app',
        data:{
            list:[]
        },
        methods:{
            getAllList:function(){
                var _this = this
                $.ajax({
                    type:'POST',
                    url:'/postText',
                    data:textData,
                    contentType:'application/json',
                    success:function(data) {
                      var result = JSON.parse(data.ResultSet).result;
                      console.log(result)
                      _this.list = result
                      return
                    }
                })
            }
        }
    })
});//windowをロードしたらinitをロードする

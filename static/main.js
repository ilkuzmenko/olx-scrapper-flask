$(document).ready(function(){

    $('.btn').click(function(){
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function (response) {
                $.each(response, function(index) {
                    $('.list').append(
                        '<div><h3>' + response[index].name + '</h3><h3>' + response[index].price + '</h3>' +
                        '<img src="' + response[index].image + '" alt="image" width="350" height="auto"><br>' +
                        '<button class="btn btn-danger" onClick="onClickHandler()">Видалити</button><br><br></div>'
                    )
                })
            }
        })
    })
})

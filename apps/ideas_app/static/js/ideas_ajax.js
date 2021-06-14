$(document).ready(function(){
    $('#submit-btn').click(ajax_add)

    $('.like-form').submit(function(e){
        e.preventDefault()
        //const post_id = $(this).attr('id')
        const url = $(this).attr('action')

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                //'post_id': post_id,
            },
            success: function(response){
                $('.all_ideas').html(response['form'])
                //console.log('success', response)
            },
            error: function(response){
                console.log('error')
            }
        })
    })
    
})

function ajax_add(e){
    e.preventDefault()
    var data = $('#ideaForm').serialize()
    $.ajax({
        type: 'post',
        url: $(this).attr('ajax/add'),
        //url: 'ideas_brillantes/ajax/add',
        data: data,
        success: function(response){
            $('.all_ideas').html(response['form'])
            $("#id_idea").val('');
        },
        error: function(re, e){
            console.log(re.responseText)
        }
      })
    //alert('Felicidades!! Agregaste una idea')
    console.log(data)
}

function ajax_like(e){
    e.preventDefault()
    $.ajax({
        type: 'post',
        url: $(this).attr('add'),
        //url: 'ideas_brillantes/ajax/add',
        //data: data,
        success: function(response){
            $('.all_ideas').html(response['form'])
        },
        error: function(re, e){
            console.log(re.responseText)
        }
      })
    alert('Ajax testing')
    console.log(data)
}

//$(document).ready(function(){
//    $('#submit-unlike').click(ajax_unlike)
//})

//$(document).ready(function(){
//    $('#submit-delete').click(ajax_delete)
//})

$(document).ready(function () {
    event.preventDefault();
    // global variables
    var numbers = []
    var operator = []

    // $(".number").click(function(){ 
    //     curValue = $("input").val();
    //     console.log(curValue);
    //     numbers.push(curvalue);
    //     if (curValue <= 1) {
    //         $("input[name='x']").val($(this).text());
    //     }
    //     else {
    //         $("input[name='x']").val(curValue + $(this).text());
    //     }
    // })
      
    $(".operate").click(function(event){ 
        num1 = $("input[name='x']").val();
        num2 = $("input[name='y']").val();
        operator = $(this).prop('value');

        $.ajax({
            type: "POST",
            url: "/",
            data: {
                'num1': num1,
                'num2': num2,
                'operator': operator
            },
            success: function(result) {
                console.log(result);
                $.each(result, function(idx, obj) {
                    console.log(obj);
                    $('.output').text(obj)
                });
            },
            error: function(error) {
                console.log(error);
            }
        });

    });
      
    $(".clear").click(function(){ 
        console.log("clear");
        $("input").val('');
        $(".output").text('');
    }); 
      
    $(".equals").click(function(){ 
        console.log('equals');
    }); 

});
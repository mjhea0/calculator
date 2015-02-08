$(document).ready(function () {
    event.preventDefault();
    // global variables
    var numbers = []
    var operator = []

    $(".number").click(function(){ 
        curValue = $("input").val();
        console.log(curValue);
        numbers.push(curvalue);
        if (curValue <= 1) {
            $("input[name='x']").val($(this).text());
        }
        else {
            $("input[name='x']").val(curValue + $(this).text());
        }
    })
      
    // $(".operate").click(function(){ 
    //     num1 = $("input[name='x']").val();
    //     num2 = $("input[name='y']").val();
    //     $("input").val('');

    //     // console.log(number)
    //     numbers.push(num1);
    //     numbers.push(num2);
    //     operator = $(this).prop('name');
    //     console.log(operator);
    //     console.log(numbers);

    //     $.ajax({
    //         type: "POST",
    //         url: "/",
    //         data : { 'num1': num1, 'num2': num2, 'numbers': numbers, 'operator': operator },
    //         success: function(result) {
    //             console.log(result);
    //         },
    //         error: function(error) {
    //             console.log(error);
    //         }
    //     });
    //     return false;
    // });
      
    $(".clear").click(function(){ 
        $("input").val('');
    }); 
      
    $(".equals").click(function(){ 
        console.log('equals');
    }); 

});
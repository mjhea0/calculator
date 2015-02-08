$(document).ready(function () {
    event.preventDefault();
    // global variables
    var numbers = []
    var operator = []

    $(".number").click(function(){ 
        curValue = $("input").val();
        if (curValue != 0) {
            num1 = curValue;
        }
        console.log(numbers);
        if (curValue <= 1) {
            $("input[name='x']").val($(this).text());
        }
        else {
            $("input[name='x']").val(curValue + $(this).text());
        }
    })

    $(".operate").click(function(event){ 
        num1 = $("input[name='x']").val();
        numbers.push(num1);
        console.log(numbers);
        operator = $(this).prop('value');
        console.log(operator);
        $("input").val('');
    });
      
    $(".equals").click(function(event){ 
        num1 = numbers[0];
        num2 = $("input[name='x']").val();
        numbers.push(num2);
        console.log(numbers);
        console.log(operator);

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
                    numbers = []
                    $("input").val('');
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
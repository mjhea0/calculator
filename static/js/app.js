$(document).ready(function () {
    event.preventDefault();

    // global variables
    var numbers = []
    var operator = []

    function grabOperator() {
        input = $("input[name='x']").val();
        if (input == "") {
            num1 = $('.output').text();
            console.log(num1);
        }
        else {
            num1 = $("input[name='x']").val();
            console.log(num1);
        }
        numbers.push(num1);
        console.log(numbers);
        console.log(operator);
        $("input").val('');
    }

    function calculate() {
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
    }

    $(".number").click(function(){ 
        curValue = $("input").val();
        if (curValue != 0) {
            num1 = curValue;
        }
        console.log(numbers);
        if (curValue < 1) {
            $("input[name='x']").val($(this).text());
        }
        else {
            $("input[name='x']").val(curValue + $(this).text());
        }
    })

    $(".operate").click(function(event){ 
        operator = $(this).prop('value');
        grabOperator();
    });

    $(document).keydown(function(e) {
        if (e.keyCode == 107) {
        console.log('addition pressed');
        operator = 'add';
        grabOperator();
        }
        if (e.keyCode == 109) {
        console.log('subtraction pressed');
        operator = 'subtract';
        grabOperator();
        }
        if (e.keyCode == 106) {
        console.log('multiplication pressed');
        operator = 'multiply';
        grabOperator();
        }
        if (e.keyCode == 111) {
        console.log('division pressed');
        operator = 'divide';
        grabOperator();
        }
        if (e.keyCode == 13) {
        console.log('equals pressed');
        calculate();
        }
    });
      
    $(".equals").click(function(event){ 
        calculate();
    });
    
    function clear() {
         console.log("clear");
        $("input").val('');
        $(".output").text('');
        numbers = []
    }
    $(".clear").click(function(){ 
        clear();
    }); 

});
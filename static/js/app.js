$(document).ready(function () {
    $("#calc").on("submit", function (event) {
        event.preventDefault();
        calculate();
    });
    $("input").change(function(){
        calculate();
    });
    $("select").change(function(){
        calculate();
    });

    function calculate() {
        var form = document.getElementById("calc");
        var answer = form.elements["out"];
        var x = parseInt(form.elements["x"].value);
        var y = parseInt(form.elements["y"].value);
        var operator = parseInt(form.elements["operator"].value);

        switch(operator) {
            case 0:
            answer.value = x+y;
            break;
            case 1:
            answer.value = x-y;
            break;
            case 2:
            answer.value = x*y;
            break;
            case 3:
            answer.value = (x/y).toFixed(2);
            break;
            default: 
            break;
        }
    }
});
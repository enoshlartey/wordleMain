document.addEventListener("DOMContentLoaded", function () {
    var inputs = document.querySelectorAll(".input-field");

    inputs.forEach(function (input, index) {
        input.addEventListener("input", function () {
            if (this.value.length >= 1) {
                for (var i = index + 1; i < inputs.length; i++) {
                    if (inputs[i].value.length === 0 && !inputs[i].classList.contains('read-only')) {
                        inputs[i].focus();
                        break;
                    }
                }
            }
        });

        input.addEventListener("keydown", function (event) {
            if (event.key === "Backspace" && this.value.length === 0) {
                for (var i = index - 1; i >= 0; i--) {
                    if (inputs[i].value.length === 0 && !inputs[i].classList.contains('read-only')) {
                        inputs[i].focus();
                        break;
                    }
                }
            }
        });
    });

    
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === '' && !inputs[i].classList.contains('read-only')) {
            inputs[i].focus();
            break;
        }
    }
});

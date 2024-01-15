document.addEventListener("DOMContentLoaded", function () {
    var inputs = document.querySelectorAll(".input-field");

    inputs.forEach(function (input, index) {
        input.addEventListener("input", function () {
            if (this.value.length >= 1) {
                // Move to the next input field if available
                var nextInput = inputs[index + 1];
                if (nextInput) {
                    nextInput.focus();
                }
            }
        });

        input.addEventListener("keydown", function (event) {
            if (event.key === "Backspace" && this.value.length === 0) {
                // Move to the previous input field if available
                var prevInput = inputs[index - 1];
                if (prevInput) {
                    prevInput.focus();
                }
            }
        });
    });
});
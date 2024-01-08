// function capitalize(id) {
//     let inputField = document.getElementById(id);
//     let inputValue = inputField.value;

//     inputValue = inputValue.toUpperCase();
//     inputField.value = inputValue;
// }


function capitalize(inputField) {
    let inputValue = inputField.value || '';
    inputValue = inputValue.toUpperCase();
    inputField.value = inputValue;
}

document.addEventListener("DOMContentLoaded", function() {
    let existingInputs = document.querySelectorAll('.input');
    existingInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            capitalize(input);
        });
    });
});

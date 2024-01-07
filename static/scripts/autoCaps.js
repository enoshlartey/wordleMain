// function capitalize(id) {
//     let inputField = document.getElementById(id);
//     let inputValue = inputField.value;

//     inputValue = inputValue.toUpperCase();
//     inputField.value = inputValue;
// }


function capitalize(id) {
    let inputField = document.getElementById(id);
    let inputValue = inputField.value;

    inputValue = inputValue.toUpperCase();
    inputField.value = inputValue;
}

document.addEventListener("DOMContentLoaded", function() {
    // Capitalize all existing input fields
    let existingInputs = document.querySelectorAll('.input');
    existingInputs.forEach(input => {
        input.addEventListener('input', function() {
            capitalize(input.id);
        });
    });

    // Capitalize all new form input fields if applicable (consider a proper way to target these)
    let newInputs = document.querySelectorAll('.new-input');
    newInputs.forEach(input => {
        input.addEventListener('input', function() {
            capitalize(input.id);
        });
    });
});
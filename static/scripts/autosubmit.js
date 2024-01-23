document.addEventListener('DOMContentLoaded', () => {
    const intake = document.querySelectorAll("input:not([disabled]):not([type='hidden'])");

    intake.forEach(input => {
        input.addEventListener('input', () => {
            const writableIntake = [...intake].filter(field => !field.classList.contains('read-only'));
            const filledWritableIntake = writableIntake.filter(field => field.value !== '');

            if (filledWritableIntake.length === writableIntake.length) {
                document.getElementById('submitForm').submit();
            }
        });
    });
});
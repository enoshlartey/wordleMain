document.addEventListener('DOMContentLoaded', () => {
    const intake = document.querySelectorAll("input:not([disabled]):not([type='hidden'])");

    intake.forEach(input => {
        input.addEventListener('input', () => {
            const filledIntake = [...intake].filter(field => field.value !== '');
            if (filledIntake.length === intake.length) {
                document.getElementById('submitForm').submit();
            }
        });
    });
});

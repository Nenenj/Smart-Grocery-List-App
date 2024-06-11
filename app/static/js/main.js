document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("registerForm");

    if (registerForm) {
        registerForm.addEventListener("submit", function(event) {
            const password = document.querySelector('input[name="password"]').value;
            const confirmPassword = document.querySelector('input[name="confirm_password"]').value;

            if (password !== confirmPassword) {
                event.preventDefault();
                alert("Passwords do not match!");
            }
        });
    }
});

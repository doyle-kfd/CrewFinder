/* jshint esversion: 6 */
/* Javascript to provide captain function to toggle applicants for trips */
document.addEventListener("DOMContentLoaded", function () {
    const toggleButtons = document.querySelectorAll('[data-bs-toggle="collapse"][data-bs-target^="#applicants"]');

    toggleButtons.forEach(function (button) {
        const targetId = button.getAttribute("data-bs-target");
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            const updateButtonText = function (text) {
                button.textContent = text;
                button.setAttribute("aria-expanded", text === "Hide Applicants");
            };

            targetElement.addEventListener("shown.bs.collapse", function () {
                updateButtonText("Hide Applicants");
            });

            targetElement.addEventListener("hidden.bs.collapse", function () {
                updateButtonText("Show Applicants");
            });
        } else {
            console.warn("No element found for target ID:", targetId);
        }
    });
});

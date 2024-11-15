document.addEventListener("DOMContentLoaded", function () {
    // Select only "Show Applicants" buttons, avoiding the navbar toggle button
    const toggleButtons = document.querySelectorAll('[data-bs-toggle="collapse"][data-bs-target^="#applicants"]');

    toggleButtons.forEach(button => {
        const targetId = button.getAttribute("data-bs-target"); // Get the target collapse ID
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            // Listen for the collapse being shown
            targetElement.addEventListener("shown.bs.collapse", function () {
                button.textContent = "Hide Applicants";
            });

            // Listen for the collapse being hidden
            targetElement.addEventListener("hidden.bs.collapse", function () {
                button.textContent = "Show Applicants";
            });
        }
    });
});

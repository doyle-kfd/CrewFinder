document.addEventListener("DOMContentLoaded", function () {
    // Select all "Show More" buttons
    const toggleButtons = document.querySelectorAll('[data-bs-toggle="collapse"]');

    toggleButtons.forEach(button => {
        const targetId = button.getAttribute("data-bs-target"); // Get the target collapse ID
        const targetElement = document.querySelector(targetId);

        // Listen for the collapse being shown
        targetElement.addEventListener("shown.bs.collapse", function () {
            button.textContent = "Show Less";
        });

        // Listen for the collapse being hidden
        targetElement.addEventListener("hidden.bs.collapse", function () {
            button.textContent = "Show More";
        });
    });
});

function toggleButtonText(button) {
    if (button.getAttribute("aria-expanded") === "true") {
        button.textContent = "Show More";
    } else {
        button.textContent = "Show Less";
    }
}
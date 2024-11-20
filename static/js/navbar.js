document.addEventListener('click', function(event) {
    // Get the navbar collapse element
    const navbarCollapse = document.getElementById('navbarNav');
    // Get the toggle button
    const toggleButton = document.querySelector('.navbar-toggler');
    
    // Check if the click is outside both the navbar and toggle button
    if (!navbarCollapse.contains(event.target) && !toggleButton.contains(event.target)) {
        // If navbar is expanded (has show class)
        if (navbarCollapse.classList.contains('show')) {
            // Remove the show class
            navbarCollapse.classList.remove('show');
            // Update the toggle button's aria-expanded attribute
            toggleButton.setAttribute('aria-expanded', 'false');
        }
    }
});
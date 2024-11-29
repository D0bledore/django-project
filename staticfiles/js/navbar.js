document.addEventListener('DOMContentLoaded', () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const body = document.body;
    const navbarCollapse = document.getElementById('navbarNav');

    function toggleNavbar() {
        const isExpanded = navbarCollapse.classList.toggle('show');
        body.classList.toggle('navbar-open');
        navbarToggler.setAttribute('aria-expanded', isExpanded);
        navbarToggler.classList.toggle('collapsed');
    };

    navbarToggler.addEventListener('click', (event) => {
        event.stopPropagation();
        toggleNavbar();
    });

    document.addEventListener('click', (event) => {
        if (!navbarCollapse.contains(event.target) && !navbarToggler.contains(event.target)) {
            if (navbarCollapse.classList.contains('show')) {
                toggleNavbar();
            }
        }
    });
});
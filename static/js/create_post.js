document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('createPostForm');
    form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            showStep(currentStep);
            return;
        }

        const postData = {
            title: form.title.value,
            category: form.category.value,
            condition: form.condition.value,
            content: form.content.value,
            price: form.price.value,
            sale_handling: form.sale_handling.value,
            email: form.email ? form.email.value : null
        };

        localStorage.setItem('postData', JSON.stringify(postData));
    });

    // Redirect to registration page if user is not authenticated
    const isAuthenticated = form.getAttribute('data-is-authenticated') === 'True';
    if (!isAuthenticated) {
        const guestFormStep = document.querySelector('.form-step:nth-last-child(2)');
        if (guestFormStep) {
            const registerUrl = form.getAttribute('data-register-url');
            if (!registerUrl) {
                console.error('Register URL is not defined');
                return;
            }
            guestFormStep.querySelector('button').addEventListener('click', function () {
                if (validateStep(currentStep)) {
                    window.location.href = registerUrl;
                }
            });
        }
    }
});
function showStep(step) {
    const formSteps = document.querySelectorAll('.form-step');
    formSteps.forEach((formStep, index) => {
        formStep.style.display = index === step ? 'block' : 'none';
    });
}

function validateStep(step) {
    const formSteps = document.querySelectorAll('.form-step');
    const inputs = formSteps[step].querySelectorAll('input, textarea, select');
    for (let input of inputs) {
        if (!input.checkValidity()) {
            input.reportValidity();
            return false;
        }
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function () {
    const formSteps = document.querySelectorAll('.form-step');
    let currentStep = 0;

    // Ensure the first step is visible
    showStep(currentStep);

    window.nextStep = function () {
        if (validateStep(currentStep)) {
            currentStep++;
            if (currentStep < formSteps.length) {
                showStep(currentStep);
            }
        }
    };

    // Ensure the email field is visible before form submission
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        if (!validateStep(currentStep)) {
            event.preventDefault();
            showStep(currentStep);
        }
    });

    // Redirect to registration page if user is not authenticated
    const isAuthenticated = form.getAttribute('data-is-authenticated') === 'True';
    if (!isAuthenticated) {
        const guestFormStep = document.querySelector('.form-step:nth-last-child(2)');
        if (guestFormStep) {
            const registerUrl = form.getAttribute('data-register-url');
            guestFormStep.querySelector('button').addEventListener('click', function () {
                if (validateStep(currentStep)) {
                    window.location.href = registerUrl;
                }
            });
        }
    }
});
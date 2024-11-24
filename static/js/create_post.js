document.addEventListener('DOMContentLoaded', function () {
    const formSteps = document.querySelectorAll('.form-step');
    let currentStep = 0;

    // Ensure the first step is visible
    showStep(currentStep);

    window.nextStep = function () {
        if (validateStep(currentStep)) {
            showStep(++currentStep);
        }
    };

    function showStep(step) {
        formSteps.forEach((formStep, index) => {
            formStep.style.display = index === step ? 'block' : 'none';
        });
    }

    function validateStep(step) {
        const inputs = formSteps[step].querySelectorAll('input, textarea, select');
        for (let input of inputs) {
            if (!input.checkValidity()) {
                input.reportValidity();
                return false;
            }
        }
        return true;
    }
});
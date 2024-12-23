// Function to show the current form step
function showStep(step) {
    const formSteps = document.querySelectorAll('.form-step');
    formSteps.forEach((formStep, index) => {
        formStep.style.display = index === step ? 'block' : 'none';
    });
}

// Function to validate form inputs
function validateStep(step) {
    const formSteps = document.querySelectorAll('.form-step');
    const inputs = formSteps[step].querySelectorAll('input, textarea, select');
    let isValid = true;

    for (let input of inputs) {
        if (!input.checkValidity()) {
            input.reportValidity();
            isValid = false;
        }
    }

    // Disable/enable next button based on validation
    const nextButton = formSteps[step].querySelector('.next-step');
    if (nextButton) {
        nextButton.disabled = !isValid;
    }

    return isValid;
}

// Function to validate image files
function validateImage(file) {
    const maxSize = 5 * 1024 * 1024; // 5MB
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];

    if (file.size > maxSize) {
        return 'Image file too large (> 5MB)';
    }
    if (!allowedTypes.includes(file.type)) {
        return 'Unsupported file type';
    }
    return null;
}

// Function to preview images
function previewImages() {
    const imagePreview = document.getElementById('image-preview');
    const imageUpload = document.getElementById('image-upload');
    let errorDisplay = document.querySelector('.alert.alert-danger');
    if (errorDisplay) {
        imagePreview.parentNode.insertBefore(errorDisplay, imagePreview);
    }

    if (!errorDisplay) {
        errorDisplay = document.createElement('div');
        errorDisplay.className = 'alert alert-danger';
        errorDisplay.style.display = 'none';
        imagePreview.parentNode.insertBefore(errorDisplay, imagePreview);
    }

    imageUpload.addEventListener('change', function(event) {
        imagePreview.innerHTML = '';
        errorDisplay.innerHTML = '';
        const files = event.target.files;
        let hasError = false;

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const error = validateImage(file);
            if (error) {
                errorDisplay.innerHTML += `<p>${file.name}: ${error}</p>`;
                hasError = true;
            } else {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.style.width = '100px';
                    img.style.margin = '10px';
                    imagePreview.appendChild(img);
                };
                reader.readAsDataURL(file);
            }
        }

        if (hasError) {
            errorDisplay.style.display = 'block';
        } else {
            errorDisplay.style.display = 'none';
        }

        // Disable next/submit button if there are errors
        const nextButton = imagePreview.closest('.form-step').querySelector('.next-step, [type="submit"]');
        if (nextButton) {
            nextButton.disabled = hasError;
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const formSteps = document.querySelectorAll('.form-step');
    let currentStep = 0;

    // Ensure the first step is visible
    showStep(currentStep);

    // Initialize image preview functionality
    previewImages();

    // Add event listeners to next step buttons
    const nextStepButtons = document.querySelectorAll('.next-step');
    nextStepButtons.forEach(button => {
        button.addEventListener('click', function () {
            if (validateStep(currentStep)) {
                currentStep++;
                if (currentStep < formSteps.length) {
                    showStep(currentStep);
                }
            }
        });
    });
});
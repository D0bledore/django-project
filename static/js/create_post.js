// Function to update review section
function updateReview() {
    document.getElementById('review-title').innerText = document.getElementById('id_title').value;
    document.getElementById('review-category').innerText = document.getElementById('id_category').value;
    document.getElementById('review-condition').innerText = document.getElementById('id_condition').value;
    document.getElementById('review-price').innerText = document.getElementById('id_price').value;
    document.getElementById('review-sale_handling').innerText = document.getElementById('id_sale_handling').value;
    document.getElementById('review-location').innerText = document.getElementById('id_location').value;
    document.getElementById('review-content').innerText = document.getElementById('id_content').value;

    // For images, display a message or image preview if available
    const imageUpload = document.getElementById('id_image');
    if (imageUpload.files.length > 0) {
        document.getElementById('review-image').innerText = imageUpload.files[0].name;
    } else {
        document.getElementById('review-image').innerText = 'No images uploaded';
    }
}

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

    inputs.forEach(input => {
        if (!input.checkValidity()) {
            input.reportValidity(); // Show validation message
            isValid = false;
        }
    });

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
        return 'Unsupported file type. (JPEG, PNG, GIF only)';
    }
    return null;
}

// Function to preview images
function previewImages() {
    const imagePreview = document.getElementById('image-preview');
    const imageUpload = document.getElementById('id_image');

    let errorDisplay = document.querySelector('.alert.alert-danger');

    errorDisplay.style.display = 'none';
    
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

        errorDisplay.style.display = hasError ? 'block' : 'none';

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
            const isValidStep = validateStep(currentStep);
            
            if (isValidStep) {
                // Update review before moving to next step if it's the last step
                if (currentStep === formSteps.length - 2) { // Second to last step is where we update review
                    updateReview();
                }
                currentStep++;
                if (currentStep < formSteps.length) {
                    showStep(currentStep);
                }
            } else {
                const firstInvalidInput = formSteps[currentStep].querySelector(':invalid');
                if (firstInvalidInput) {
                    firstInvalidInput.focus();
                }
            }
        });
    });

    // Add event listeners to previous step buttons
    const previousStepButtons = document.querySelectorAll('.previous-step');
    previousStepButtons.forEach(button => {
        button.addEventListener('click', function () {
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        });
    });

    // Add event listener to enforce maximum length of 8 digits for price input (must be 8 + 2 decimal places)
    const priceInput = document.getElementById('id_price');
    if (priceInput) {
        priceInput.addEventListener('input', function () {
            if (priceInput.value.length > 8) {
                priceInput.value = priceInput.value.slice(0, 8);
            }
        });
    }
});
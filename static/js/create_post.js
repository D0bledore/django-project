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
    for (let input of inputs) {
        if (!input.checkValidity()) {
            input.reportValidity();
            return false;
        }
    }
    return true;
}

// Function to preview images
function previewImages() {
    const imagePreview = document.getElementById('image-preview');
    const imageUpload = document.getElementById('image-upload');
    
    imageUpload.addEventListener('change', function(event) {
        imagePreview.innerHTML = ''; // Clear any existing previews

        const files = event.target.files;
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const reader = new FileReader();

            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                img.style.width = '100px'; // Set thumbnail size
                img.style.margin = '10px';
                imagePreview.appendChild(img);
            };

            reader.readAsDataURL(file);
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
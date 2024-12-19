document.addEventListener('DOMContentLoaded', function () {
    const emailField = document.querySelector('#id_email');
    const usernameField = document.querySelector('#id_username');
    const bioField = document.querySelector('#id_bio');
    const emailDisplay = document.querySelector('#email-display');
    const usernameDisplay = document.querySelector('#username-display');
    const bioDisplay = document.querySelector('#bio-display');
    const changeEmailBtn = document.querySelector('#change-email-btn');
    const changeUsernameBtn = document.querySelector('#change-username-btn');
    const changeBioBtn = document.querySelector('#change-bio-btn');

    changeEmailBtn.addEventListener('click', function () {
        const isHidden = emailField.style.display === 'none';
        emailField.style.display = isHidden ? 'block' : 'none';
        emailDisplay.style.display = isHidden ? 'none' : 'block';
    });

    changeUsernameBtn.addEventListener('click', function () {
        const isHidden = usernameField.style.display === 'none';
        usernameField.style.display = isHidden ? 'block' : 'none';
        usernameDisplay.style.display = isHidden ? 'none' : 'block';
    });

    changeBioBtn.addEventListener('click', function () {
        const isHidden = bioField.style.display === 'none';
        bioField.style.display = isHidden ? 'block' : 'none';
        bioDisplay.style.display = isHidden ? 'none' : 'block';
    });

    // Initially hide email, username, and bio fields
    emailField.style.display = 'none';
    usernameField.style.display = 'none';
    bioField.style.display = 'none';
});
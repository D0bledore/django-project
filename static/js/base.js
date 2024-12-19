document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var message = document.querySelector('.django-message');
        if (message) {
            message.style.transition = "opacity 1s ease-out";
            message.style.opacity = 0;
            setTimeout(function() {
                message.style.display = "none";
            }, 1000);
        }
    }, 5000);
});
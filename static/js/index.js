document.addEventListener('DOMContentLoaded', function () {
    const answers = document.querySelectorAll('.answer');

    answers.forEach(button => {
        button.addEventListener('click', function () {
            const currentQuestion = this.closest('.question-container');
            const nextQuestionId = this.getAttribute('data-next');

            // Hide the current question
            currentQuestion.classList.remove('active');

            // Show the next question
            document.getElementById(nextQuestionId).classList.add('active');
        });
    });
});

document.querySelectorAll('.answer').forEach(wrapper => {
    wrapper.addEventListener('click', function () {
        this.scrollIntoView({ behavior: 'smooth' });
    });
});
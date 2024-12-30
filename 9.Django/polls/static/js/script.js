document.addEventListener('DOMContentLoaded', () => {
    const questions = document.querySelectorAll('.question-item');
    questions.forEach((question, index) => {
        question.style.opacity = 0;
        setTimeout(() => {
            question.style.transition = 'opacity 0.5s ease-in-out';
            question.style.opacity = 1;
        }, index * 200); // تأخیر برای هر سوال
    });
});

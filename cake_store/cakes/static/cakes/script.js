document.addEventListener("DOMContentLoaded", function() {
    const button1 = document.querySelectorAll(".button1");
    
    button1.forEach(button => {
        button.addEventListener("click", function() {
            window.location.href = "/";
        });
    });
});
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');
    console.log('Hello');

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener("submit", event => {
            if (!form.checkValidity() || languageFrom == languageTo) {
                event.preventDefault();
                event.stopPropagation();
            }

            form.classList.add("was-validated");
        }, false)
    })
})()
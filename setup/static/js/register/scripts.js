function disable_alert() {
    tarja = document.getElementById("tarja-user");
    tarja.style.display = "None";
    //tarja.remove();
}
function activate_alert() {
    tarja = document.getElementById("tarja-user");
    tarja.style.display = "Block";
}

window.onload = function() {
    var already_exists_user = document.getElementById("user_exists").innerText;
    if (already_exists_user == "False") {
        disable_alert();
    } else {
        activate_alert();
    }
}

function formsValidation(event) {
    var inputUsername = document.getElementById("username");
    var inputEmail = document.getElementById("email");
    var inputPassword = document.getElementById("password");
    var inputPasswordConfirm = document.getElementById("confirm-password");

    var listItensInput = [inputUsername, inputEmail, inputPassword, inputPasswordConfirm];
    
    var hasError = false;

    listItensInput.forEach(function(input) {
        input.classList.remove("field-empty");
    });

    listItensInput.forEach(function(input) {
        if (input.value.trim() == '') {
            input.classList.add("field-empty");
            hasError = true;
        }
    });

    if (hasError) {
        alert("Existem Campos Vazios!");
        event.preventDefault();
    } else {
        // Valida Email
        if (inputEmail.value.trim() !== '' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inputEmail.value)) {
            alert("Digite um email válido!")
            inputEmail.classList.add("field_empty");
            hasError = true;
            event.preventDefault();
        }
        // Valida Senha
        if (inputPassword.value !== inputPasswordConfirm.value) {
            alert("As senhas não estão iguais")
            inputPasswordConfirm.classList.add("field_empty");
            hasError = true;
            event.preventDefault();
        }

        return true;
    }


}
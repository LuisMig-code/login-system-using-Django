window.onload = function() {
    credentials_status = document.getElementById("credentials_status").innerText;
    div_erro_login = document.getElementById("credentials_user");
    
    if(credentials_status == "Usuário ou Senha incorretos") {
        div_erro_login.style.display = "Block";
    } else {
        div_erro_login.remove();
    }
}
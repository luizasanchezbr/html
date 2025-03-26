function onRecaptchaSuccess(token) {
    // O token do reCAPTCHA está disponível aqui
    console.log('reCAPTCHA token:', token);
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('loginForm');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const username = form.querySelector('input[name="username"]');
        const password = form.querySelector('input[name="password"]');
        const captchaResponse = grecaptcha.getResponse();
        
        if (!username.value || !password.value) {
            alert('Todos os campos são obrigatórios!');
            return;
        }
        
        if (!captchaResponse) {
            alert('Por favor, complete o captcha!');
            return;
        }
        
        // Se tudo estiver ok, envia o formulário
        form.submit();
    });
}); 
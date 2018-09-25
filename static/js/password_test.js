$(document).ready(function(){
    // находим форму
    var form = $('#password_test');
    //выводим в консоль должно высветится:  a.fn.init [form#password_test.form-inline]
    console.log(form);
    // назначаем действие на отправку
    var password_before = $('#password_before').val(); 
    console.log(password_before);
    if(password_before == 0){$('.posts_and_video').removeClass('del')
        $('.form_password').addClass('del');}
    form.on('submit', function(e){ //e блокируем перезагрузку
        e.preventDefault();
        //alert('+');
        var password_from_input = $('#password').val();
        var submit_btn = $('#submit_btn');
        var password_from_bd =  submit_btn.data("password_from_bd");
        console.log(password_from_bd);
        console.log(password_from_input);
        
                        
        if (password_from_input == (password_from_bd/3)){$('.posts_and_video').removeClass('del');
        //alert('пароль верный');
        $('.form_password').addClass('del');
        
        }
        });
        
});
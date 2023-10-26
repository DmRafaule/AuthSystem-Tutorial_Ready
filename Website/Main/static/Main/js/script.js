$(document).ready(function() {
    $('.nav__bur').click(function(event){
        $('.nav__bur,.nav').toggleClass('active');//Для добавления класов со стилями для  навигационного бургера
    }),
    $('.title-of-section').click(function(event){
        $('.title-of-section,.futureprod__row2').toggleClass('active2');//Для добавления класов со стилями для бургера внизу
    });
});
$(document).ready(function(){//For displaying img
    $('.f_l').click(function(event){
        $('.choise_img').toggleClass('all'),
        $('.choise_img').removeClass('printTm'),
        $('.choise_img').removeClass('webTm'),
        $('.choise_img').removeClass('UI'),
        $('.choise_img').removeClass('MockUp');
    });
    $('.s_l').click(function(event){
        $('.choise_img').toggleClass('printTm');
        $('.choise_img').removeClass('all'),
        $('.choise_img').removeClass('webTm'),
        $('.choise_img').removeClass('UI'),
        $('.choise_img').removeClass('MockUp');
    });
    $('.t_l').click(function(event){
        $('.choise_img').toggleClass('webTm');
        $('.choise_img').removeClass('all'),
        $('.choise_img').removeClass('printTm'),
        $('.choise_img').removeClass('UI'),
        $('.choise_img').removeClass('MockUp');
    });
    $('.f1_l').click(function(event){
        $('.choise_img').toggleClass('UI'),
        $('.choise_img').removeClass('all'),
        $('.choise_img').removeClass('printTm'),
        $('.choise_img').removeClass('webTm'),
        $('.choise_img').removeClass('MockUp');
        
    });
    $('.f2_l').click(function(event){
        $('.choise_img').toggleClass('MockUp'),
        $('.choise_img').removeClass('all'),
        $('.choise_img').removeClass('printTm'),
        $('.choise_img').removeClass('webTm'),
        $('.choise_img').removeClass('UI');
    });
});

$('.nav__link').on('click', function(){//For switching buttons in nav
    $('.nav__link').removeClass('selected_nav');
    $('.nav__link').removeClass('nav__link_first');
    $(this).addClass('selected_nav');
});

$('.futureprod__row2_link').on('click',function(){//for switching ref in futureprod
    $('.futureprod__row2_link').removeClass('selected_submenu');
    $('.futureprod__row2_link').removeClass('red');
    $(this).addClass('selected_submenu');

});
$('.socnet_act').on('click',function(){//for choose a socnet
    $('.socnet_act').removeClass('selected_socnet');
    $(this).addClass('selected_socnet');
});
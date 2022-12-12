$('.tab .menus li').each(function(){
    $('.tab .menus li').click(function(){
        $('.tab .menus li').removeClass('bg');
        $(this).addClass('bg');
        var index = $(this).index();
        $('.tab .scroll').css('margin-top', - index * 900+'px');
    })
})
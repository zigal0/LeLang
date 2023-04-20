function setActiveNav(navId) {
    $('.nav-link.active').each(function() {
        $(this).removeClass('active');
    });
    $(navId).addClass('active');
}
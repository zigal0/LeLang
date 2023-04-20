$("#msg").each(function(i, msg) {
    setTimeout(function() {
        msg.remove();
    }, 3000);
});
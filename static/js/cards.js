var i = 0;
changeTerm(0);

$('#card').click(function(){
    flipCard(i);
});

$('#prev').click(function(){
    i--;
    changeTerm(i);
});

$('#next').click(function(){
    i++;
    changeTerm(i);
});

function changeTerm(i) {
    attr = $('#content').attr('translation');

    // For some browsers, `attr` is undefined; for others,
    // `attr` is false.  Check for both.
    if (typeof attr !== 'undefined' && attr !== false) {
        $('#content').removeAttr('translation');
    }

    $('#content').empty();
    $('#content').append(terms[i].word);

    $('#counter').empty();
    $('#counter').append(i + 1);

    if (i == 0) {
        $('#prev').prop('disabled', true);
    } else {
        $('#prev').prop('disabled', false);
    }

    if (i == terms.length-1) {
        $('#next').prop('disabled', true);
    } else {
        $('#next').prop('disabled', false);
    }
}

function flipCard(i) {
    attr = $('#content').attr('translation');

    let content = ""

    // For some browsers, `attr` is undefined; for others,
    // `attr` is false.  Check for both.
    if (typeof attr !== 'undefined' && attr !== false) {
        $('#content').removeAttr('translation');
        content = terms[i].word
    } else {
        $('#content').attr('translation', '');
        content = terms[i].translation
    }

    $('#content').empty();
    $('#content').append(content);
}


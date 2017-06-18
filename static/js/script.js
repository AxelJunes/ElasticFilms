// AJAX Functions
$( document ).ready(function() {
    /* Set cursor at the end of input */
    var searchInput = $('#query');

    // Multiply by 2 to ensure the cursor always ends up at the end;
    // Opera sometimes sees a carriage return as 2 characters.
    var strLength = searchInput.val().length * 2;

    searchInput.focus();
    searchInput[0].setSelectionRange(strLength, strLength);
});
// Submits the form on keyup
$('#query').keyup(function(e) {
    $('#target').submit();
});

window.onkeydown=function(event){
    if(event.keyCode==13){
        sendNew();
        if(event.preventDefault) event.preventDefault();
        return false;
    }
}
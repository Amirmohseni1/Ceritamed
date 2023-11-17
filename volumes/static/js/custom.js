function ShowMessage(title, text, theme) {
    $(document).ready(function () {
        window.createNotification({
            closeOnClick: true,
            displayCloseButton: false,
            positionClass: 'nfc-bottom-right',
            showDuration: 7000,
            theme: theme !== '' ? theme : 'success',
        })({
            title: title !== '' ? title : 'إعلان',
            message: text
        });
    });
}


$(document).ready(function(){
    $('.support-content').hide();
    $('a.btn-support').click(function(e){
      e.stopPropagation();
      $('.support-content').slideToggle();
    });
    $('.support-content').click(function(e){
      e.stopPropagation();
    });
    $(document).click(function(){
      $('.support-content').slideUp();
    });
});

(function(){
  $("img").attr("height", "100%");
  $("img").attr("width", "100%");
}());
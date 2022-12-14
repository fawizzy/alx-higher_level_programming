$(document).ready(function () {
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      headers: {
        'Access-Control-Allow-Origin': '*'
      },
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
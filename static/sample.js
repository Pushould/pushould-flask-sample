$(function() {
  $('input').click(function() {
    $.ajax({
      type: 'POST',
      url: '/comment',
      data: {
        msg: 'new comment'
      }
    });
  })
});

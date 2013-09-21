// Once the api loads call enable the search box.
function handleAPILoaded() {
  $('#search-button').attr('disabled', false);
}

// Search for a given string.
function search() {
  alert("HERE");
  var q = $('#query').val();
  var request = gapi.client.youtube.search.list({
    q: q,
    part: 'snippet'
  });

  request.execute(function(response) {
    var str = JSON.stringify(response.result);
    $('#search-container').html('<pre>' + str + '</pre>');
  });
}
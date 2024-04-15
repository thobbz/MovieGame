function getQuote() {
  axios.get('/get_quote')
    .then(function (response) {
      document.getElementById('quote').innerHTML = response.data.quote;
      document.getElementById('result').innerHTML = ''; // Clear any previous result
    })
    .catch(function (error) {
      console.log(error);
    });
}

function checkGuess() {
  var guess = document.getElementById('guess').value;
  var movieId = document.getElementById('quote').getAttribute('data-movie-id');

  axios.post('/check_guess', {
    guess: guess,
    movie_id: movieId
  })
    .then(function (response) {
      if (response.data.correct) {
        document.getElementById('result').innerHTML = response.data.message;
      } else {
        document.getElementById('quote').innerHTML = response.data.quote;
        document.getElementById('result').innerHTML = 'Incorrect guess. Try again!';
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}
function getQuestion() {
  axios.get('/get_question')
    .then(function (response) {
      document.getElementById('question').innerHTML = response.data.question;
      document.getElementById('question').setAttribute('data-movie-id', response.data.movie_id);
      document.getElementById('result').innerHTML = ''; // Clear any previous result
    })
    .catch(function (error) {
      console.log(error);
    });
}

function checkGuess() {
  var guess = document.getElementById('guess').value;
  var movieId = document.getElementById('question').getAttribute('data-movie-id');

  axios.post('/check_guess', {
    guess: guess,
    movie_id: movieId
  })
    .then(function (response) {
      if (response.data.correct) {
        document.getElementById('result').innerHTML = response.data.message;
      } else {
        document.getElementById('question').innerHTML = response.data.question;
        document.getElementById('result').innerHTML = 'Incorrect guess. Try again!';
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}
function validateForm() {
  var query = document.getElementById('query-input').value;
  var errorMessage = document.getElementById('error-message');
  var loadingSpinner = document.getElementById('loading-spinner');
  var searchBtn = document.getElementById('search-btn');
  var searchText = document.getElementById('search-text');
  var searchAnimation = document.getElementById('search-animation');
  var noResults = document.getElementById('no-results');

  var isNumeric = /^\d+$/.test(query);

  if (query.length < 4 || !isNumeric) {
    errorMessage.classList.remove('hidden');
    return false;
  }

  errorMessage.classList.add('hidden');
  searchText.classList.add('hidden');
  loadingSpinner.classList.remove('hidden');
  searchBtn.disabled = true;

  searchAnimation.classList.remove('hidden');

  if (noResults) {
    noResults.classList.add('hidden');
  }

  return true;
}

  document.getElementById('back-button').addEventListener('click', function() {
    document.getElementById('back-animation').classList.remove('hidden');
    
    // Sahifani orqaga qaytarishdan oldin animatsiya 1 soniya davom etadi
    setTimeout(function() {
      window.history.back();  // Sahifa orqaga qaytadi
    }, 1000);  // Animatsiya ko'rsatilish muddati (1 soniya)
  });

const splashScreen = document.getElementById("splash");

// Function to hide the splash screen
function hideSplashScreen() {
    splashScreen.style.visibility = "hidden";
    splashScreen.style.opacity = 0;
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            duration: 10000,
        });
    });
});

// Hide the splash screen after 5 seconds
setTimeout(hideSplashScreen, 5000);


// Validating that form has input

function validateForm() {
    // Check if any input field has a value
    let inputs = document.querySelectorAll('input[type="text"], input[type="number"], select');
    for (let input of inputs) {
        if (input.value.trim() !== '') {
            return true;  // Allow form submission
        }
    }
    
    // If no input has value, prevent form submission
    alert('Please fill in at least one search field.');
    return false;
}


// live search

document.addEventListener('DOMContentLoaded', function() {
    const locationSearch = document.getElementById('location_search');
    const suggestionsElement = document.getElementById('suggestions');

    function fetchSuggestions() {
        const query = locationSearch.value.trim();
        if (query.length < 3) {
            clearSuggestions();
            return;
        }

        fetch(`/suggest_locations/?query=${encodeURIComponent(query)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                renderSuggestions(data.suggestions);
            })
            .catch(error => {
                console.error('Error fetching suggestions:', error);
                displayError();
            });
    }

    function renderSuggestions(suggestions) {
        suggestionsElement.innerHTML = '';
        suggestions.forEach(item => {
            const div = document.createElement('div');
            div.textContent = item;
            div.classList.add('suggestion-item');
            div.onclick = () => selectSuggestion(item);
            suggestionsElement.appendChild(div);
        });
        suggestionsElement.style.visibility = 'visible';
        suggestionsElement.style.opacity = '1';
    }

    function clearSuggestions() {
        suggestionsElement.innerHTML = '';
        suggestionsElement.style.visibility = 'hidden';
        suggestionsElement.style.opacity = '0';
    }

    function displayError() {
        suggestionsElement.innerHTML = '<p>Failed to fetch suggestions. Please try again later.</p>';
        suggestionsElement.style.visibility = 'visible';
        suggestionsElement.style.opacity = '1';
    }

    function selectSuggestion(item) {
        locationSearch.value = item;
        clearSuggestions();
    }

    locationSearch.addEventListener('input', fetchSuggestions);
});

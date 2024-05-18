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
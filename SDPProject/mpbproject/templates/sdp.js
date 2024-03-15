// Define constants
const HOME_MODULE = "home";
const PAWNBROKERS_MODULE = "pawnbrokers";
const USERS_MODULE = "users";
const ADMIN_MODULE = "admin";

// Get elements from HTML
const homeBtn = document.getElementById("home");
const pawnbrokersBtn = document.getElementById("pawnbrokers");
const usersBtn = document.getElementById("users");
const adminBtn = document.getElementById("admin");
const contentDiv = document.getElementById("content");

// Define functions for each module
function showHome() {
    contentDiv.innerHTML = "<h1>Welcome to PAWNSHOP MORTGAGE</h1>";
}

function showPawnbrokers() {
    promptForCredentials(PAWNBROKERS_MODULE);
}

function showUsers() {
    promptForCredentials(USERS_MODULE);
}

function showAdmin() {
    promptForCredentials(ADMIN_MODULE);
}

function promptForCredentials(module) {
    const username = prompt(`Please enter your username for the ${module} module:`);
    const password = prompt(`Please enter your password for the ${module} module:`);
    // Check if credentials are valid
    if (checkCredentials(username, password)) {
        authenticateUser();
        redirectToYouTube();
    } else {
        alert("Invalid credentials, please try again.");
    }
}

function checkCredentials(username, password) {
    // Replace these with actual credentials for each module
    if (username === "admin" && password === "admin123") {
        return true;
    } else if (username === "user" && password === "user123") {
        return true;
    } else if (username === "pawnbroker" && password === "pawnbroker123") {
        return true;
    } else {
        return false;
    }
}

function authenticateUser() {
    // Set a flag to indicate that the user is authenticated
    isAuthenticated = true;
}

function redirectToYouTube() {
    // Redirect the user to YouTube
    window.location.href = "https://www.youtube.com";
}

// Add event listeners to buttons
homeBtn.addEventListener("click", showHome);
pawnbrokersBtn.addEventListener("click", showPawnbrokers);
usersBtn.addEventListener("click", showUsers);
adminBtn.addEventListener("click", showAdmin);

// Check if user is authenticated
let isAuthenticated = false; // change this to true if user is authenticated



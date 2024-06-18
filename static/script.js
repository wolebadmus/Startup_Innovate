// Function to toggle the visibility of sections
function toggleSection(id) {
    const element = document.getElementById(id);
    if (element.classList.contains('expanded')) {
        element.classList.remove('expanded');
    } else {
        element.classList.add('expanded');
    }
}

// Function to handle the typewriter effect
function typeWriter() {
    const welcomeText = document.getElementById('typingEffect');
    const statements = [
        "Welcome to the inaugural edition of the Startup Innovation",
        "Contest!",
        "",
        "Turn your ideas into reality and shape the future",
        "of entrepreneurship.",
        "",
        "Share innovative solutions, compete for prizes,",
        "and connect with visionaries.",
        "",
        "Seize the chance to make your mark. Ignite creativity,",
        "drive innovation and build a brighter tomorrow.",
        "",
        "Join us."
    ];
    let statementIndex = 0;
    let charIndex = 0;

    function type() {
        if (statementIndex < statements.length) {
            if (charIndex < statements[statementIndex].length) {
                if (statements[statementIndex].charAt(charIndex) === ' ') {
                    welcomeText.innerHTML += '&nbsp;'; // Non-breaking space for correct formatting
                } else {
                    welcomeText.innerHTML += statements[statementIndex].charAt(charIndex);
                }
                charIndex++;
                setTimeout(type, 30); // Adjust typing speed (milliseconds)
            } else {
                welcomeText.innerHTML += '<br>'; // Add paragraph break
                statementIndex++;
                charIndex = 0;
                setTimeout(type, 200); // Delay before typing the next statement (milliseconds)
            }
        }
    }

    type();
}

// Initialize typewriter effect on page load
document.addEventListener("DOMContentLoaded", typeWriter);

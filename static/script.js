document.addEventListener("DOMContentLoaded", function() {
    function toggleSection(id) {
        const element = document.getElementById(id);
        const arrow = element.previousElementSibling.querySelector('.arrow');
        if (element.classList.contains('expanded')) {
            element.classList.remove('expanded');
            arrow.innerHTML = '&#9662;'; // Down arrow
        } else {
            element.classList.add('expanded');
            arrow.innerHTML = '&#9652;'; // Up arrow
        }
    }

    // Function to initialize the typing effect
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

    function typeWriter() {
        if (statementIndex < statements.length) {
            if (charIndex < statements[statementIndex].length) {
                if (statements[statementIndex].charAt(charIndex) === ' ') {
                    welcomeText.innerHTML += '&nbsp;'; // Non-breaking space for correct formatting
                } else {
                    welcomeText.innerHTML += statements[statementIndex].charAt(charIndex);
                }
                charIndex++;
                setTimeout(typeWriter, 30); // Adjust typing speed (milliseconds)
            } else {
                welcomeText.innerHTML += '<br>'; // Add paragraph break
                statementIndex++;
                charIndex = 0;
                setTimeout(typeWriter, 200); // Delay before typing the next statement (milliseconds)
            }
        }
    }

    // Call the typeWriter function to start the typing effect
    typeWriter();

    // Event delegation for toggling sections
    const sidebar = document.querySelector('.sidebar');
    sidebar.addEventListener('click', function(event) {
        if (event.target.classList.contains('arrow')) {
            const sectionId = event.target.parentElement.nextElementSibling.id;
            toggleSection(sectionId);
        }
    });

    // Word count functionality
    const descriptionField = document.getElementById('description');
    const wordCountMessage = document.getElementById('word-count-message');
    const maxWords = 150;

    descriptionField.addEventListener('input', function(event) {
        let words = descriptionField.value.trim().split(/\s+/);
        if (words.length > maxWords) {
            words = words.slice(0, maxWords);
            descriptionField.value = words.join(' ');
            wordCountMessage.textContent = `You have reached the ${maxWords} words limit.`;
            wordCountMessage.style.color = 'red';
        } else {
            wordCountMessage.textContent = `Current word count: ${words.length}`;
            wordCountMessage.style.color = 'green';
        }
    });
});

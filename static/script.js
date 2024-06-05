document.getElementById('submissionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    const response = await fetch('/submit', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        alert('Your idea has been submitted successfully!');
        this.reset();
    } else {
        alert('There was an error submitting your idea. Please try again.');
    }
});

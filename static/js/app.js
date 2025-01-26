document.getElementById('fetchPlaylist').addEventListener('click', () => {
    const mood = document.getElementById('mood').value;
    const limit = document.getElementById('limit').value;

    // Validate inputs
    if (!mood || !limit) {
        alert('Please select a mood and enter a limit.');
        return;
    }

    // Show the terminal loader and set the initial text
    const terminalText = document.getElementById('terminalText');
    terminalText.innerHTML = "Wait a moment...";

    document.getElementById('terminalLoader').style.display = 'block';

    // Fetch the playlist
    fetch(`/playlist?mood=${mood}&limit=${limit}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            setTimeout(() => {
                terminalText.innerHTML = "Playlist Loaded: -<br>"; // After 4 seconds, show the loaded message
                if (data.length === 0) {
                    terminalText.innerHTML += "No songs found for the selected mood.";
                    return;
                }

                // Output each song with numbering and a line break
                data.forEach((song, index) => {
                    terminalText.innerHTML += `${index + 1}. ${song.title} by ${song.artist}<br>`;
                });
            }, 4000); // Delay for 4 seconds before showing the playlist
        })
        .catch(error => {
            terminalText.innerHTML = `Error fetching playlist: ${error.message}`;
        });
});

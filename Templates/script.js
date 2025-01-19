document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("user-input-form"); // Ensure the form exists

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Get values from form inputs
        const genre = document.getElementById("genre").value;
        const playtime = document.getElementById("playtime").value;
        const difficulty = document.getElementById("difficulty").value;

        try {
            // Send data to the backend via POST
            const response = await fetch("/recommendations", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    genre: genre,
                    playtime: playtime,
                    difficulty: difficulty,
                }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            const results = await response.json();
            const resultsDiv = document.getElementById("results");

            // Clear previous results
            resultsDiv.innerHTML = "";

            // Render the game recommendations
            if (results.length > 0) {
                results.forEach((game) => {
                    const gameElement = document.createElement("div");
                    gameElement.innerHTML = `
                        <div>
                            <img src="${game[4]}" alt="${game[0]}" width="100">
                            <p><strong>${game[0]}</strong> (${game[2]})</p>
                            <p>Genre: ${game[1]} | Playtime: ${game[3]} hours</p>
                        </div>
                    `;
                    resultsDiv.appendChild(gameElement);
                });
            } else {
                resultsDiv.innerHTML = "<p>No games found. Try different filters!</p>";
            }
        } catch (error) {
            console.error("Error fetching recommendations:", error);
            const resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "<p>Something went wrong. Please try again later.</p>";
        }
    });
});

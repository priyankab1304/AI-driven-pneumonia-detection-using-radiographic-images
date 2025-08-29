document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const predictionText = document.getElementById('prediction');
    const loadingDiv = document.getElementById('loading');

    // Check if a file has been selected
    if (fileInput.files.length > 0) {
        // Show loading message
        loadingDiv.style.display = "block";
        predictionText.textContent = "";
        predictionText.className = ""; // Clear any previous class

        // Simulate a delay for "processing"
        setTimeout(function() {
            // Hide loading message
            loadingDiv.style.display = "none";

            // Simulate a random prediction result (either 'Pneumonia' or 'Normal')
            const isPneumonia = Math.random() > 0.5;

            if (isPneumonia) {
                predictionText.textContent = "Prediction: Pneumonia detected.";
                predictionText.classList.add('prediction-pneumonia'); // Add red color
            } else {
                predictionText.textContent = "Prediction: No pneumonia detected.";
                predictionText.classList.add('prediction-normal'); // Add green color
            }

        }, 2000); // Simulate 2-second delay
    } else {
        // If no file is selected, show a message to prompt the user
        predictionText.textContent = "Please upload an image.";
        predictionText.className = ""; // Reset class
    }
});



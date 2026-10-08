document.getElementById('uploadForm').onsubmit = async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    document.getElementById('predictionResult').innerText = 'Predicting... 🔍';

    const res = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    const data = await res.json();
    if (data.prediction) {
        document.getElementById('predictionResult').innerText = "Prediction: " + data.prediction;
    } else {
        document.getElementById('predictionResult').innerText = "❌ Error: " + (data.error || "Unknown error");
    }
};

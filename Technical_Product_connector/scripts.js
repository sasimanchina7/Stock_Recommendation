document.addEventListener("DOMContentLoaded", function() {
    var popup = document.querySelector('.popup');
    var closeBtn = document.querySelector('.close');
    var predictionData = document.getElementById('prediction-data');

    // Mock prediction data
    var stockPrediction = {
    stockName: 'AAPL',
    predictedPrice: '$150.25',
    confidenceLevel: 'High'
    };

    // Construct HTML for prediction data
    var predictionHTML = `
    <p>Stock: ${stockPrediction.stockName}</p>
    <p>Predicted Price: ${stockPrediction.predictedPrice}</p>
    <p>Confidence Level: ${stockPrediction.confidenceLevel}</p>
    `;
    // Set prediction data into the div
    predictionData.innerHTML = predictionHTML;
  
    // Show popup when the extension icon is clicked
    safari.extension.toolbarItems.addEventListener('command', function(event) {
      popup.style.display = "block";
    });
  
    // Close popup when close button is clicked
    closeBtn.addEventListener('click', function() {
      popup.style.display = "none";
    });
  
    // Close popup when user clicks outside of it
    window.addEventListener('click', function(event) {
      if (event.target == popup) {
        popup.style.display = "none";
      }
    });
  });
  
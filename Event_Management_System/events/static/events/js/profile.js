// Function to animate the bar graph
function animateBarGraph() {
    const bars = document.querySelectorAll('.bar');
    const barValues = [80, 65, 90]; // Replace with the actual percentage values for each year
  
    bars.forEach((bar, index) => {
      setTimeout(() => {
        bar.style.width = `${barValues[index]}%`;
        bar.nextElementSibling.textContent = `${barValues[index]}%`;
      }, (index + 1) * 1000); // Adjust the delay for a smooth animation (optional)
    });
  }
  
  // Call the animateBarGraph function when the document is ready
  document.addEventListener('DOMContentLoaded', animateBarGraph);
  
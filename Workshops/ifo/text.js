const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");

const textArray = ["Press Release: ifo Institute: German Manufacturing Sector Demonstrates Strong Improvement in Latest Business Climate Index. Munich, Germany – The ifo Institute, a leading German economic research organization, has released its latest Business Climate Index for the German manufacturing sector, revealing a significant improvement in the industry's outlook. The index rose to 103.3 points in April 2023, up from 101.2 points in the previous month, signaling a positive trend for the country's economy. The manufacturing industry is a key contributor to the German economy, and its positive performance is critical for the country's continued economic growth. The sector accounts for approximately 22% of the country's GDP and employs millions of people across the country. Therefore, the ifo Business Climate Index serves as a reliable predictor of the overall economic health of Germany. 'The strong improvement in the ifo Business Climate Index for the German manufacturing sector is a clear indication of the robustness of the industry,' said Prof. Clemens Fuest, President of the ifo Institute. 'This positive trend is expected to have a significant impact on the overall economic growth of Germany in the coming months.' The improved outlook for the manufacturing sector can be attributed to several factors, including increased demand from global markets, particularly from the United States and China. Furthermore, German manufacturers have demonstrated exceptional resilience, innovation, and adaptability in the face of various economic and political challenges. 'The German manufacturing sector has shown an impressive ability to navigate through turbulent economic conditions, and its continued success is a testament to the hard work and dedication of the industry's stakeholders,' added Prof. Fuest. The ifo Business Climate Index has a long history of accurately predicting German GDP growth, making it an essential tool for policymakers, business leaders, and investors. The positive outlook for the manufacturing sector, as indicated by the latest index, suggests a continued positive trend for the country's economy, highlighting the critical importance of the sector for the world economy."];
const typingDelay = 50;
const erasingDelay = 0;
const newTextDelay = 10000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < textArray[textArrayIndex].length) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
  	setTimeout(erase, newTextDelay);
  }
}

function erase() {
	if (charIndex > 0) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
    charIndex--;
    setTimeout(erase, erasingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
    textArrayIndex++;
    if(textArrayIndex>=textArray.length) textArrayIndex=0;
    setTimeout(type, typingDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function() { // On DOM Load initiate the effect
  if(textArray.length) setTimeout(type, newTextDelay + 250);
});
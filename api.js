function sendWhatsApp() {
  const msg = `
🐄 CareNode Alert
Cattle ID: #A1023
Health Score: 82/100
Temperature: 38.6°C
Respiratory: Normal
Requesting veterinary consultation.
  `;
  window.open(`https://wa.me/?text=${encodeURIComponent(msg)}`);
}

function playVoice() {
  alert("Voice explanation will be played in selected language.");
}

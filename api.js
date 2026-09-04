// ================= AUTH =================
function signup() {
  localStorage.setItem("user", email.value);
  localStorage.setItem("pass", password.value);
  alert("Account created");
}

function login() {
  if (
    email.value === localStorage.getItem("user") &&
    password.value === localStorage.getItem("pass")
  ) {
    localStorage.setItem("loggedIn", "true");
    location.href = "dashboard.html";  // redirect only
  } else {
    alert("Invalid credentials");
  }
}

function checkAuth() {
  if (localStorage.getItem("loggedIn") !== "true") {
    location.href = "auth.html";
  }
}

function logout() {
  localStorage.removeItem("loggedIn");
  location.href = "auth.html";
}

// ================= UTIL =================
function sendWhatsApp() {
  const msg = "CareNode Alert: Requesting veterinary consultation.";
  location.href = `https://wa.me/?text=${encodeURIComponent(msg)}`;
}

function playVoice() {
  alert("Voice explanation in selected language plays here");
}

// ================= DASHBOARD UPDATE =================
function updateDashboard(data) {
  document.getElementById("cow_id").innerText = data.cow_id;
  document.getElementById("temperature").innerText = data.temperature + " °C";
  document.getElementById("breathing").innerText = data.breathing_rate + " bpm";
  document.getElementById("audio").innerText = data.audio_rms;
  document.getElementById("zcr").innerText = data.zcr;

  document.getElementById("normal_prob").innerText = data.probabilities.normal;
  document.getElementById("monitor_prob").innerText = data.probabilities.monitor;
  document.getElementById("critical_prob").innerText = data.probabilities.critical;

  document.getElementById("prediction").innerText = data.prediction;
  document.getElementById("confidence").innerText = data.confidence;
}

// ================= DATA FETCH =================
let fetchInterval;

function startFetching() {
  if (fetchInterval) return; // prevent duplicate intervals

  fetchInterval = setInterval(fetchData, 2000);
}

async function fetchData() {
  try {
    const res = await fetch("http://localhost:8000/data");
    const data = await res.json();

    console.log("Received:", data);

    if (Object.keys(data).length !== 0) {
      updateDashboard(data);
    }
  } catch (err) {
    console.error("Error:", err);
  }
}
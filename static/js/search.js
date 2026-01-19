const API_BASE = "http://127.0.0.1:8000/api/v1/";

document.addEventListener("DOMContentLoaded", () => {

    const resultsGrid = document.getElementById("resultsGrid");
    const bedsContainer = document.getElementById("beds-container");
    const bloodContainer = document.getElementById("blood-container");
    const searchBtn = document.getElementById("searchPageBtn");

    function getQueryParam(param) {
        return new URLSearchParams(window.location.search).get(param);
    }

    const hospitalId = getQueryParam("hospital");
    if (hospitalId) {
        fetchHospitalDetails(hospitalId);
    }

    searchBtn.addEventListener("click", () => {
        const city = document.getElementById("searchCity").value;
        const resource = document.getElementById("searchResource").value;

        resultsGrid.innerHTML = "";
        bedsContainer.innerHTML = "";
        bloodContainer.innerHTML = "";

        fetch(`${API_BASE}hospitals/?city=${encodeURIComponent(city)}`)
            .then(r => r.json())
            .then(data => {
                if (!data.length) {
                    resultsGrid.innerHTML = "<p>No hospitals found.</p>";
                    return;
                }

                data.forEach(h => {
                    const div = document.createElement("div");
                    div.className = "hospital";
                    div.innerHTML = `
                        <strong>${h.name}</strong><br>
                        ${h.address}, ${h.city}<br>
                        📞 ${h.phone_number}<br>
                        <button onclick="fetchHospitalDetails(${h.id}, '${resource}')">
                          View ${resource === "beds" ? "Beds" : "Blood"}
                        </button>
                    `;
                    resultsGrid.appendChild(div);
                });
            });
    });
});

function fetchHospitalDetails(hospitalId, resource = "beds") {

    const bedsContainer = document.getElementById("beds-container");
    const bloodContainer = document.getElementById("blood-container");

    bedsContainer.innerHTML = "";
    bloodContainer.innerHTML = "";

    if (resource === "beds") {
        fetch(`${API_BASE}hospitals/${hospitalId}/beds/`)
            .then(r => r.json())
            .then(beds => {
                if (!beds.length) {
                    bedsContainer.innerHTML = "<p>No bed data.</p>";
                    return;
                }

                beds.forEach(b => {
                    bedsContainer.innerHTML += `
                        <div>
                          ${b.bed_type} —
                          <strong>${b.available ? "Available" : "Full"}</strong>
                        </div>
                    `;
                });
            });
    }

    if (resource === "blood") {
        fetch(`${API_BASE}blood/`)
            .then(r => r.json())
            .then(blood => {
                if (!blood.length) {
                    bloodContainer.innerHTML = "<p>No blood data.</p>";
                    return;
                }

                blood.forEach(b => {
                    bloodContainer.innerHTML += `
                        <div>
                          ${b.blood_group}: ${b.units_available} units
                        </div>
                    `;
                });
            });
    }
}


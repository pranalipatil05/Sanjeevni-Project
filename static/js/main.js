const API_BASE = "http://127.0.0.1:8000/api/v1/";

document.addEventListener("DOMContentLoaded", () => {
    const hospitalListDiv = document.getElementById("hospital-list");

    if (!hospitalListDiv) return;

    fetch(`${API_BASE}hospitals/`)
        .then(r => r.json())
        .then(data => {
            hospitalListDiv.innerHTML = "";
            if (!Array.isArray(data) || data.length === 0) {
                hospitalListDiv.innerHTML = `<div style="color:#6b7280;font-style:italic">No hospitals found.</div>`;
                return;
            }

            data.forEach(hospital => {
                const div = document.createElement("div");
                div.className = "hospital-item";
                div.innerHTML = `
                    <div style="font-weight:800; font-size:16px;">${hospital.name}</div>
                    <div style="font-size:14px; color:#6b7280; margin-top:4px;">
                        ${hospital.address}, ${hospital.city}
                    </div>
                    <div style="margin-top:8px; font-size:14px; color:#16a34a;">
                        📞 <a href="tel:${hospital.phone_number}" style="color:#16a34a;text-decoration:none;">
                            ${hospital.phone_number}
                        </a>
                    </div>
                `;
                div.addEventListener("click", () => {
                    window.location.href = `/search/?hospital=${hospital.id}`;
                });
                hospitalListDiv.appendChild(div);
            });
        })
        .catch(err => {
            console.error(err);
            hospitalListDiv.innerHTML = `<div style="color:#ef4444">Failed to load hospitals.</div>`;
        });
});


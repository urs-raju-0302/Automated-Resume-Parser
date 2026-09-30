document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("resumeForm");
    const fileInput = document.getElementById("resumeFile");
    const statusEl = document.getElementById("status");
    const result = document.getElementById("result");

    if (!form) {
        console.error("resumeForm was not found.");
        return;
    }

    form.addEventListener("submit", async function (event) {

        event.preventDefault();

        console.log("✅ Parse button clicked");

        if (!fileInput || fileInput.files.length === 0) {
            statusEl.textContent = "Please select a PDF or DOCX resume.";
            return;
        }

        const file = fileInput.files[0];

        console.log("📄 Selected:", file.name);

        const formData = new FormData();
        formData.append("file", file);

        statusEl.textContent = "Parsing resume...";
        result.classList.add("hidden");

        try {

            const response = await fetch("/api/parse", {
                method: "POST",
                body: formData
            });

            console.log("API status:", response.status);

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "Failed to parse resume.");
            }

            document.getElementById("name").textContent =
                data.name || "-";

            document.getElementById("email").textContent =
                data.email || "-";

            document.getElementById("phone").textContent =
                data.phone || "-";

            document.getElementById("linkedin").textContent =
                data.linkedin || "-";

            document.getElementById("github").textContent =
                data.github || "-";

            document.getElementById("skills").textContent =
                data.skills && data.skills.length
                    ? data.skills.join(", ")
                    : "-";

            document.getElementById("education").textContent =
                data.education || "-";

            document.getElementById("experience").textContent =
                data.experience || "-";

            statusEl.textContent =
                "✅ Resume parsed successfully.";

            result.classList.remove("hidden");

        } catch (error) {

            console.error("❌ Parser error:", error);

            statusEl.textContent =
                "❌ " + error.message;
        }
    });
});
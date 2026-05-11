const API_URL = "http://127.0.0.1:8000/generate";

async function generateContent() {

    const category = document.getElementById("category").value;
    const topic = document.getElementById("topic").value;
    const audience = document.getElementById("audience").value;
    const tone = document.getElementById("tone").value;

    const output = document.getElementById("output");

    output.value = "Generating content...";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                category,
                topic,
                audience,
                tone
            })
        });

        const data = await response.json();

        if (!response.ok) {
            output.value = data.detail || "Request failed.";
            return;
        }

        if (data.success === false) {
            output.value = data.error || "Failed to generate content.";
            return;
        }

        output.value = data.content || "No content received.";

    } catch (error) {
        output.value = "Server error occurred.";
    }
}

function copyContent() {
    const output = document.getElementById("output");
    output.select();
    document.execCommand("copy");
    alert("Content copied!");
}

document.getElementById("contactForm").addEventListener("submit", async function(event) {
    event.preventDefault();  // Prevent default form submission

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    if (name && email && message) {
        // Update UI before sending the request
        document.getElementById("statusMessage").innerHTML = "Sending your message...";

        // Prepare form data
        let formData = new FormData();
        formData.append("name", name);
        formData.append("email", email);
        formData.append("message", message);

        try {
            let response = await fetch("https://marissa-loya.com/contact", {
                method: "POST",
                body: formData
            });

            let result = await response.json();  // Get response body

            if (response.ok) {
                // Display success message on UI
                document.getElementById("statusMessage").innerHTML = result.status;
                document.getElementById("statusMessage").style.color = "green";
                document.getElementById("contactForm").reset();  // Reset form after success
            } else {
                throw new Error(result.message || "Something went wrong. Please email me directly.");
            }
        } catch (error) {
            // Handle errors properly on the frontend
            console.error("Error:", error);
            document.getElementById("statusMessage").innerHTML = error.message;
            document.getElementById("statusMessage").style.color = "red";
        }
    } else {
        document.getElementById("statusMessage").innerHTML = "Please fill out all fields.";
        document.getElementById("statusMessage").style.color = "red";
    }
});

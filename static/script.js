document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");
    
    window.addEventListener("scroll", function() {
        let scrollPos = window.scrollY;
        
        sections.forEach(section => {
            if (scrollPos >= section.offsetTop - 50) {
                section.style.transform = "translateY(0)";
                section.style.opacity = "1";
            }
        });
    });

    // Smooth Scroll for links
    document.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", function(event) {
            if (this.getAttribute("href").startsWith("#")) {
                event.preventDefault();
                const targetId = this.getAttribute("href").substring(1);
                const targetSection = document.getElementById(targetId);
                targetSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});

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
            // Send data to Flask API on Render
            let response = await fetch("https://resume-website-b1kh.onrender.com/contact", {
                method: "POST",
                body: formData
            });
        
            // Get response
            let result = await response.json();
        
            if (response.ok) {
                document.getElementById("statusMessage").innerHTML = result.status; //Show success message
                document.getElementById("statusMessage").style.color = "green";
                document.getElementById("contactForm").reset(); // Reset form
            } else {
                throw new Error(result.message || "Something went wrong. Please email me directly at mloya1207@gmail.com");
            }
        
        } catch (error) {
            console.error("Error:", error);
            document.getElementById("statusMessage").innerHTML = error.message;
            document.getElementById("statusMessage").style.color = "red";
        }
    } else {
        document.getElementById("statusMessage").innerHTML = "Please fill out all fields.";
        document.getElementById("statusMessage").style.color = "red";
    }
});
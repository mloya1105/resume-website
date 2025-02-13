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

document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;
    
    if (name && email && message) {
        document.getElementById("statusMessage").innerHTML = "Thank you for your message, " + name + "! I'll be in touch soon.";
        document.getElementById("contactForm").reset();
    } else {
        document.getElementById("statusMessage").innerHTML = "Please fill out all fields.";
    }
});

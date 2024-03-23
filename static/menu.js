
function toggleServices() {
    var servicesDropdownContent = document.getElementById("servicesDropdownContent");
    var servicesArrow = document.getElementById("servicesArrow");

    if (servicesDropdownContent.style.display === "block") {
        servicesDropdownContent.style.display = "none";
        servicesArrow.innerHTML = "&#9650;"; // Change to up arrow
    } else {
        servicesDropdownContent.style.display = "block";
        servicesArrow.innerHTML = "&#9660;"; // Change to down arrow
    }
}

function toggleContact() {
    var contactDropdownContent = document.getElementById("contactDropdownContent");
    var contactArrow = document.getElementById("contactArrow");

    if (contactDropdownContent.style.display === "block") {
        contactDropdownContent.style.display = "none";
        contactArrow.innerHTML = "&#9650;"; // Change to up arrow
    } else {
        contactDropdownContent.style.display = "block";
        contactArrow.innerHTML = "&#9660;"; // Change to down arrow
    }
}

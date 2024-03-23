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

function toggleLanguages() {
    var languagesDropdownContent = document.getElementById("languagesDropdownContent");
    var languagesArrow = document.getElementById("languagesArrow");

    if (languagesDropdownContent.style.display === "block") {
        languagesDropdownContent.style.display = "none";
        languagesArrow.innerHTML = "&#9650;"; // Change to up arrow
    } else {
        languagesDropdownContent.style.display = "block";
        languagesArrow.innerHTML = "&#9660;"; // Change to down arrow
    }
}

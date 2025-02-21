document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("prediction-form").addEventListener("submit", function (event) {
        let cgpa = parseFloat(document.getElementById("cgpa").value);
        let iq = parseInt(document.getElementById("iq").value);

        if (cgpa < 0 || cgpa > 10) {
            alert("CGPA must be between 0 and 10");
            event.preventDefault();
        } else if (iq < 50 || iq > 200) {
            alert("IQ must be between 50 and 200");
            event.preventDefault();
        }
    });
});

function showSuccessMessage(event) {
    

    var form = document.getElementById("ServicesForm");

    
    if (form.checkValidity()) {
        var messageElement = document.getElementById("successMessage");
        messageElement.classList.remove("hidden");

      
    }
}


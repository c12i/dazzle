// copy image url to clipboard function
function copyToClipboard(id) {
    var grabText = document.getElementById(id);
    var toCreateAttribute = grabText.textContent;
    console.log(toCreateAttribute);
    
    var inputElement = document.createElement("input");
    document.body.appendChild(inputElement);
    inputElement.setAttribute("value", toCreateAttribute);
    inputElement.setAttribute("hidden", true);
    inputElement.select();
    document.execCommand("copy");
    alert("Image url copied");

    // document.removeChild(inputElement);
  }
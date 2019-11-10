$(function () {
    $(window).scroll(function () {              
        $(".backtop").show(4000)
    })

    $(".backtop").click(function(){                  
        $(this).hide()
    })
})


// copy image url to clipboard function
function copyToClipboard(id) {
    var grabText = document.getElementById(id);
    var toCreateAttribute = grabText.textContent;
    console.log(toCreateAttribute);
    
    var inputElement = document.createElement("input");
    document.body.appendChild(inputElement);
    inputElement.setAttribute("value", toCreateAttribute);
    inputElement.select();
    inputElement.setSelectionRange(0, 99999);
    document.execCommand("copy");
    alert("Image url copied");
    inputElement.setAttribute("hidden", true);
    document.removeChild(inputElement);
  }
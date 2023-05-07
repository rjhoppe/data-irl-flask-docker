$('#app__form').each(function() {
    var hasRequired = $(this).attr('required');
    if (typeof hasRequired !== "undefined" && hasRequired !== false) {
        // This is required inputs.
    } else {
        let popup = document.getElementById("popup");
        function openPopup(){
            popup.classList.add("open-popup");
        }

        function closePopup(){
            popup.classList.remove("open-popup");
        }
    }
}


let popup = document.getElementById("popup");
function openPopup(){
    popup.classList.add("open-popup");
}

function closePopup(){
    popup.classList.remove("open-popup");
}
</script>
{% endblock %}



let popup = document.getElementById("popup");
function openPopup(){
    $("input").each(function() {
        var hasRequired = $(this).attr('required');
        if (typeof hasRequired !== "undefined" && hasRequired !== false) {
        } else {
            popup.classList.add("open-popup");
        }
    });
}

function closePopup(){
    popup.classList.remove("open-popup");
}






///

let popup = document.getElementById("popup");
function openPopup(){
    popup.classList.add("open-popup");
}

function closePopup(){
    popup.classList.remove("open-popup");
}

let popup = document.getElementById("popup");
let corp_email = document.getElementById("corp_email");
let survey_id = document.getElementById("survey_id");
let numb_of_resp = document.getElementById("numb_of_resp");
let resp_type = document.getElementById("resp_type");

if (corp_email != "" || survey_id != "" || numb_of_resp != "" || resp_type != "" ) {
    function openPopup(){
        popup.classList.add("open-popup");
    }

    function closePopup(){
        popup.classList.remove("open-popup");
    }
}

///

$('#check').on("click", function(){
    let valid = true;
    $('[required]').each(function() {
      if ($(this).is(':invalid') || !$(this).val()) valid = false;
    })
    if (!valid) alert("error please fill all fields!");
    else alert('valid');
  })




  let popup = document.getElementById("popup");
  $('#app__form').each(function() {
      var hasRequired = $(this).attr('required');
      if (typeof hasRequired !== "undefined" && hasRequired !== false) {
          // This is required inputs.
      } else {
          function openPopup(){
              popup.classList.add("open-popup");
          }
  
          function closePopup(){
              popup.classList.remove("open-popup");
          }
      }
  }
  </script>









  function validateForm() {
    let email = document.forms["app__fields"]["corp_email_input"].value;
    if (email == "Please enter your email") {
        alert("Name must be filled out");
        return false;
    }

    let surveyId = document.forms["app__fields"]["survey_id_input"].value;
    if (surveyId == "Enter an anonymous link") {
        alert("Please enter an anonymous link");
        return false;
    }

    let numOfResponses = document.forms["app__fields"]["numb_of_resp_input"].value;
    if (numOfResponses == "Enter in a number of responses") {
        alert("Please enter a number of responses");
        return false;
    }

    let responseType = document.forms["app__fields"]["resp_type_select"].value;
    if (responseType == "") {
        alert("Name must be filled out");
        return false;
    }

}



function validateForm() {
    let email = document.forms["app__fields"]["corp_email_input"].value;
    if (email == "Enter in your email") {
        alert("Email must be filled out");
        console.log(email);
        return false;
    }

    let surveyId = document.forms["app__fields"]["survey_id_input"].value;
    if (surveyId == "Enter an anonymous link") {
        alert("Please enter an anonymous link");
        console.log(surveyId);
        return false;
    }

    let numOfResponses = document.forms["app__fields"]["numb_of_resp_input"].value;
    if (numOfResponses == "Enter in a number of responses") {
        alert("Please enter in a number of responses");
        console.log(numOfResponses)
        return false;
    }

    let responseType = document.forms["app__fields"]["resp_type_select"].value;
    if (responseType == "") {
        alert("Response type must be filled out");
        console.log(responseType);
        return false;
    }
}






function validateForm() {
    let email = document.forms["app__fields"]["corp_email_input"].value;
    if (email == "") {
        alert("Please enter in your email");
        console.log(email)
        return false;
    }

    let surveyId = document.forms["app__fields"]["survey_id_input"].value;
    if (surveyId == "") {
        alert("Please enter an anonymous link");
        console.log(surveyId)
        return false;
    }

    let numOfResponses = document.forms["app__fields"]["numb_of_resp_input"].value;
    if (numOfResponses == "") {
        alert("Please enter a number of responses");
        console.log(numOfResponses)
        return false;
    }

    let responseType = document.forms["app__fields"]["resp_type_select"].value;
    if (responseType == "") {
        alert("Please enter a response type");
        console.log(responseType)
        return false;
    }

    let popup = document.getElementById("popup");
    popup.classList.add("open-popup")
}

function closePopup(){
    popup.classList.remove("open-popup");
}
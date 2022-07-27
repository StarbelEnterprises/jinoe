var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
//   set the submit type to the button
  if (n == (x.length)) {
    document.getElementById("nextBtn").setAttribute('type','submit')
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
    // document.getElementById("nextBtn").setAttribute('type','submit')
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
    console.log(n)
    if (n === 1) {
        console.log('can submit form 1 containing')
        const myname1 = document.getElementById('firstname').value
        const myname2 = document.getElementById('lastname').value
        console.log(myname1, myname2)
    }
    if (n === 2){
        const email=document.getElementById('email').value
        const phone= document.getElementById('phone').value
        console.log(email, phone)
    }
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").addEventListener('submit' , (event)=> {
        event.preventDefault();
        console.log('prent form data')
    })
     console.log(' form data here')
     var serializedData = $('#regForm').serialize();
    //  const jsonData = JSON.parse(serializedData)
     console.log(serializedData )
     var formEl = document.forms.regForm;
     var formData = new FormData(formEl);
     var name = formData.get('firstname');

    console.log(formData)

    
    console.log(name)
    ajaxCall(serializedData);

    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

ajaxCall = (data) => {
    $.ajax({
        type : "post", 
        url: window.location.href,
        data: data,
        success: function(data){
          console.log('submited after 2 sec');
          console.log(data.msg)
          const messages = document.getElementById('message')
          messages.innerHTML =`Your account has been created successifully<a href="/login" class="alert-link"> click here to login</a>`
          messages.style.display='block'

        },
        failure: function(error) {
            console.log(error)
        }
    })
}



function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}
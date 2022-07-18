
let level = {}

$('#level').on('change', function(event) {
    console.log(event.type + " event with:", $(this).val());
    level['id'] =$(this).val();
});
console.log('level', level)
  

$('#signupform').on('submit', function(e) {
    const registerData = {}
    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
    registerData['csrfmiddlewaretoken'] = csrfToken;
    registerData['username'] = $('#username').val()
    registerData['email'] = $('#email').val()
    registerData['firstname'] = $('#firstname').val()
    registerData['lastname'] = $('#lastname').val()
    registerData['password'] = $('#password').val()
    registerData['comfirm_password'] = $('#comfirm_password').val()
    registerData['enrolled_to'] = level
    e.preventDefault();
    console.log(registerData)
    ajaxCall(registerData);
    }
);    

ajaxCall = (data) => {
    $.ajax({
        type : "POST", 
        url: window.location.href,
        data: data,
        success: function(data){
          console.log('submited after 2 sec');
          console.log(data.msg)
          const messages = document.getElementById('message')
          messages.style.display='block'
        },
        failure: function(error) {
            console.log(error)
        }
    })
}


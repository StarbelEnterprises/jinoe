const allCurriculumSubtopiclinks = [...document.getElementsByClassName('curriculum-sub-topic-link')]

allCurriculumSubtopiclinks.forEach((element)=>{
 element.addEventListener('click', (event)=>{
    if(event.target.tagName == "A"){
      const subtopicId = event.target.id
      const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
       let subtopicData = {
         'id': subtopicId,
        'csrfmiddlewaretoken':csrfToken
       }

     let mainContentContainer = document.getElementById('main-content-container')
      mainContentContainer.innerHTML=""
      curriculum_ajaxCall(subtopicData);
      mainContentContainer.innerHTML=`
       <div class="col-12 col-lg-9">
      <div class="row">

      </div>
      <div class="row">
          <div class="col-12">
              <div class="card">
                  <div class="card-body video">
                      <video  width="320" height="240" controls autoplay>
                          <source src="/static/dashboard/assets/videos/ukuaji.m4v" type="video/mp4">
                          Your browser does not support the video tag.
                          </video>
                  </div>
                  <div class="row mt-0">
                      <div class="col-md-4">
                          <button  data-toggle="modal" data-target="#staticBackdrop" class="btn btn-brown rounded-pill ms-4 mb-3" >Take Module Assesment</button>
                      </div>
                      <div class="col-md-2 mt-1 d-flex">
                          <span style="font-weight: bold; font-size: 18px;" >300K</span>
                          <i style="font-size:18px;" class="bi bi-hand-thumbs-up text-danger ms-1 " ></i>
          
                      </div>
                      <div class="col-md-2 mt-1 d-flex">
                          
                          <span style="font-weight: bold; font-size: 18px;margin-left: 20px;" >10</span>
                              <i style="font-size:18px;" class="bi bi-hand-thumbs-down text-danger ms-1 mt-1" ></i>
                      </div>
                      <div class="col-md-4">
                          <button class="btn btn-brown rounded-pill ms-4 mb-3" >Add Comment</button>
                      </div>
                  </div>
              </div>
          </div>
      </div>
      <div class="row">
          
          <div class="col-12 col-xl-12">
              <div class="card" >
                  <div class="card-header">
                      <h5>Module Comments and Reviews</h5>
                  </div>
                  <div class="card-body">
                      <div class="row">
                          <div class="col-md-3">
                          <div class="rate-value d-block bg-brown text-center">
                              <br>
                              <div class=" mr-2">
                                  <span></span>
                                  <span >4.6</span>
                              </div>
                              <div class=" mb-2 mt-2 " >
                                  <span><i class="bi bi-star-fill text-warning" ></i></span>
                                  <span><i class="bi bi-star-fill text-warning" ></i></span>
                                  <span><i class="bi bi-star-fill text-warning" ></i></span>
                                  <span><i class="bi bi-star-half text-warning" ></i></span>
                              </div>
                              <div class=" mb-3 mr-2" >
                                  <span>Total Average Reviews</span>
                              </div>
                              <div class="mt-2"><span></span></div>
                          </div>
                          </div>
                          <div class="col-md-7">
                              <div class="progress progress-warning  mb-2">
                                  <div class="progress-bar" role="progressbar" style="width: 35%"
                                      aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="progress progress-warning  mb-2">
                                  <div class="progress-bar " role="progressbar" style="width: 50%"
                                      aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="progress progress-warning  mb-2">
                                  <div class="progress-bar" role="progressbar" style="width: 45%"
                                      aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="progress progress-warning  mb-2">
                                  <div class="progress-bar" role="progressbar" style="width: 30%"
                                      aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="progress progress-warning  mb-2">
                                  <div class="progress-bar" role="progressbar" style="width: 10%"
                                      aria-valuenow="" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                          </div>
                          <div class="col-md-2">
                              <h6>5 stars</h6>
                              <h6>4 stars</h6>
                              <h6>3 stars</h6>
                              <h6>2 stars</h6>
                              <h6>1 stars</h6>
                          </div>
                      </div>
                          <div class="comment-section">
                              <div class="user d-flex mt-3">
                                  <img style="height:50px; width: 50px; border-radius: 50px; " src="" alt="">
                                  <h5 class="ms-3 mt-3" >Isaya Bendera - 10 July, 2022</h5>
                              </div>
                              
                              <div class="comment">
                                  <p class="ms-5 text-brown " >
                                      Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                                      Earum non amet nam quam quae eveniet eius commodi quasi, sit, fugiat fugit recusandae eaque rerum! 
                                      Labore nesciunt libero ad dolor minima?
                                  </p>
                              </div>
                              <div class="reply-section ms-5">
                              <div class="user d-flex mt-3">
                                  <img style="height:50px; width: 50px; border-radius: 50px; " src="" alt="">
                                  <h5 class="ms-3 mt-3" >Isaya Bendera - 10 July, 2022</h5>
                              </div>
                              
                              <div class="reply">
                                  <p class="ms-5 text-brown " >
                                      Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                                      Earum non amet nam quam quae eveniet eius commodi quasi, sit, fugiat fugit recusandae eaque rerum! 
                                      Labore nesciunt libero ad dolor minima?
                                  </p>
                              </div>
                          </div>
                          </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
  <div class="col-12 col-lg-3">
      <div class="card">
          <div class="card-body py-4 px-5">
              <div class="d-flex align-items-center">
                  <div class="ms-0 name">
                      <h6 class="text-muted mb-3">Click subscribe for more</h6>
                          <button style="background-color:#853636;" class="btn text-white rounded-pill" >Subscribe Now </button>
                      
                  </div>
              </div>
          </div>
      </div>
      <div class="card">
          <div class="card-header">
              <h4>Subtopics</h4>
          </div>
          <div id="sub-sub-content-list" class="card-content pb-4 ">
          </div>
      </div>
  </div>`
    }

 })
}) 


curriculum_ajaxCall = (data) => {
   $.ajax({
       type : "POST", 
       url: window.location.href,
       data: data,
       success: function(response){
         console.log('submited after 2 sec');
         const parseJson = JSON.parse(response.data)
         console.log(parseJson);
         let subSubContentList = document.getElementById('sub-sub-content-list');
         subSubContentList.innerHTML = ''
         let html = ''
        if( parseJson.length !== 0){
      
            for (let i = 0; i < parseJson.length; i++) {
                html += `<a id="${parseJson[i].pk}" onclick='handleSubsubTopicDetailModalDisplay(this)'> <div class="recent-message subsubtopic-video d-flex px-4 py-3">
                <div class="avatar avatar-lg">
                    <video width="100" height="50">
                        <source src="/static/dashboard/assets/videos/ukuaji.m4v" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="name ms-4 mt-1">
                    <h6 class="mb-1">${parseJson[i].fields.sub_sub_topic_name}</h6>
                    <small class="text-muted mb-0">@johnducky</small>
                </div>
            </div></a>`
            }
            subSubContentList.innerHTML = html
        }else{
            subSubContentList.innerHTML = `<div class="alert alert-danger" role="alert">No sub topic contents!</div>`
        }
     
       },
       failure: function(error) {
           console.log(error)
       }
   })
}


function handleSubsubTopicDetailModalDisplay(element){
 console.log('clicked', element.id)
 
 $('#subsubmodal').modal('show')
  
}
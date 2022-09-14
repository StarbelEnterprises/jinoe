let videoElem = document.getElementById("intro-video");
let playButton = document.getElementById("intro-video-play-btn");

playButton.addEventListener('click',  handlePlaybtn, false)
if (videoElem.paused) {
  playVideo();
  playButton.style.display="block"
} else {
  playButton.style.display="none"
}


async function playVideo() {
    try {
      playButton.style.display="none"
      await videoElem.play();
      conosole.log(' playing')
    
    } catch(err) {
      console.log('some error happening')
      playButton.classList.remove("playing");
    }
  }
  
function handlePlaybtn(){
    if (videoElem.paused) {
      playVideo();
      playButton.style.display="none"
    } else {
      videoElem.pause();
      playButton.style.display="none"
    }
  }


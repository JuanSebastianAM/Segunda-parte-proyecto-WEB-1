
document.addEventListener("DOMContentLoaded", function () {
  var parent = document.querySelector(".splitview"),
    topPanel = parent.querySelector(".top"),
    handle = parent.querySelector(".handle"),
    skewHack = 0,
    delta = 0;

  // If the parent has .skewed class, set the skewHack var.
  if (parent.className.indexOf("skewed") != -1) {
    skewHack = 1000;
  }

  parent.addEventListener("mousemove", function (event) {
    // Get the delta between the mouse position and center point.
    delta = (event.clientX - window.innerWidth / 2) * 0.5;

    // Move the handle.
    handle.style.left = event.clientX + delta + "px";

    // Adjust the top panel width.
    topPanel.style.width = event.clientX + skewHack + delta + "px";
  });
});










let slide_data = [
    {
      src:
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHaf4_uacFvjUSzSBWEYFpuj2gh7zFjH-iIQ&usqp=CAU",
      
    },
    {
      src:
        "https://m.guiamedica.com.pe/perfiles/descargar/9889",
      
    },
    {
      src:
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDJA023wLNytEMAobC16KVIg3Ok_Iy3ykCUg&usqp=CAU",
     
    },
    {
      src:
      "https://www.elempleo.com/colombia/files/basesempresariales/dentisalud/image/cab_dentisalud.jpg",
      
    }
  ];
  let slides = [],
    captions = [];
  
  let autoplay = setInterval(function () {
    nextSlide();
  }, 5000);
  let container = document.getElementById("container");
  let leftSlider = document.getElementById("left-col");
  // console.log(leftSlider);
  let down_button = document.getElementById("down_button");
  // let caption = document.getElementById('slider-caption');
  // let caption_heading = caption.querySelector('caption-heading');
  
  down_button.addEventListener("click", function (e) {
    e.preventDefault();
    clearInterval(autoplay);
    nextSlide();
    autoplay;
  });
  
  for (let i = 0; i < slide_data.length; i++) {
    let slide = document.createElement("div"),
      caption = document.createElement("div"),
      slide_title = document.createElement("div");
  
    slide.classList.add("slide");
    slide.setAttribute("style", "background:url(" + slide_data[i].src + ")");
    caption.classList.add("caption");
    slide_title.classList.add("caption-heading");
    slide_title.innerHTML = "<h1>" + slide_data[i].title + "</h1>";
  
    switch (i) {
      case 0:
        slide.classList.add("current");
        
        break;
      case 1:
        slide.classList.add("next");
        
        break;
      case slide_data.length - 1:
        slide.classList.add("previous");
        
        break;
      default:
        break;
    }
    
    
    slides.push(slide);
    leftSlider.appendChild(slide);
    container.appendChild(caption);
  }
 
  
  function nextSlide() {
    
    slides[0].classList.remove("current");
    slides[0].classList.add("previous", "change");
    slides[1].classList.remove("next");
    slides[1].classList.add("current");
    slides[2].classList.add("next");
    let last = slides.length - 1;
    slides[last].classList.remove("previous");
  
  
   
   
  
    let placeholder = slides.shift();
    
    slides.push(placeholder);
    
  }
  
  
 
  function whichTransitionEvent() {
    var t,
      el = document.createElement("fakeelement");
  
    var transitions = {
      transition: "transitionend",
      OTransition: "oTransitionEnd",
      MozTransition: "transitionend",
      WebkitTransition: "webkitTransitionEnd"
    };
  
    for (t in transitions) {
      if (el.style[t] !== undefined) {
        return transitions[t];
      }
    }
  }
  
  var transitionEvent = whichTransitionEvent();
  caption.addEventListener(transitionEvent, customFunction);
  
  function customFunction(event) {
    
    console.log("animation ended");
 
  }

  
  
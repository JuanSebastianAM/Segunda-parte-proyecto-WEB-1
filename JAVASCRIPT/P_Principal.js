let slide_data = [
    {
      src:
        "https://images.unsplash.com/photo-1506765336936-bb05e7e06295?ixlib=rb-0.3.5&s=d40582dbbbb66c7e0812854374194c2e&auto=format&fit=crop&w=1050&q=80",
      
    },
    {
      src:
        "https://images.unsplash.com/photo-1496309732348-3627f3f040ee?ixlib=rb-0.3.5&s=4d04f3d5a488db4031d90f5a1fbba42d&auto=format&fit=crop&w=1050&q=80",
      
    },
    {
      src:
        "https://images.unsplash.com/photo-1504271863819-d279190bf871?ixlib=rb-0.3.5&s=7a2b986d405a04b3f9be2e56b2be40dc&auto=format&fit=crop&w=334&q=80",
     
    },
    {
      src:
        "https://images.unsplash.com/photo-1478728073286-db190d3d8ce6?ixlib=rb-0.3.5&s=87131a6b538ed72b25d9e0fc4bf8df5b&auto=format&fit=crop&w=1050&q=80",
      
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
  // console.log(slides);
  
  function nextSlide() {
    // caption.classList.add('offscreen');
  
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
  
  
  // https://jonsuh.com/blog/detect-the-end-of-css-animations-and-transitions-with-javascript/
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

 
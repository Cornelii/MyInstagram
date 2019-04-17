let A = document.querySelector('strong');
A.style.fontWeignt = 'bold';
A.style.color = 'black';

let max_size = "40rem";


// image size correction 

var user_imgs = document.querySelectorAll(".user_image");

user_imgs.forEach((userImg)=>{
    var width = userImg.naturalWidth;
    var height = userImg.naturalHeight;
    
    if (width >= height){
        userImg.style.width=max_size;
        userImg.style.height="auto";
    }else{
        userImg.style.height=max_size;
        userImg.style.width="auto";
    }
})


// this script is for the scroll-fade-in animation in the hompage
window.addEventListener('scroll', reveal);
function reveal(){
    var reveal_items = document.querySelectorAll('.reveal');
    console.log(reveal_items);
    for(var i=0; i<reveal_items.length; i++){
        var windowHeight = window.innerHeight;
        var revealTop = reveal_items[i].getBoundingClientRect().top;
        var revealPoint = 150;

        if(revealTop < windowHeight - revealPoint){
            reveal_items[i].classList.add('active');
        }else{
            reveal_items[i].classList.remove('active');
        }
    }
}
// end of script for homepage animation
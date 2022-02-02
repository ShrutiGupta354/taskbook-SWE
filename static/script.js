
// this script is for the scroll-fade-in animation in the hompage
window.addEventListener('scroll', reveal);
function reveal(){
    var reveal_items = document.querySelectorAll('.reveal');
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


/* API CALLS */
function api_get_tasks(success_function) {

  $.ajax({url:"api/tasks", type:"GET", 
          success:success_function});
}

function api_create_task(task, success_function) {
  $.ajax({url:"api/tasks", type:"POST", 
          data:JSON.stringify(task), 
          contentType:"application/json; charset=utf-8",
          success:success_function});
}

function api_update_task(task, success_function) {
  task.id = parseInt(task.id)
  $.ajax({url:"api/tasks", type:"PUT", 
          data:JSON.stringify(task), 
          contentType:"application/json; charset=utf-8",
          success:success_function});
}

function api_delete_task(task, success_function) {
  task.id = parseInt(task.id)
  $.ajax({url:"api/tasks", type:"DELETE", 
          data:JSON.stringify(task), 
          contentType:"application/json; charset=utf-8",
          success:success_function});
}

//array of numbers so that all numbers are 2 digit for day and month when created in id field
const numbers = ["00",
"01","02","03","04","05","06","07","08","09","10",
"11","12","13","14","15","16","17","18","19","20",
"21","22","23","24","25","26","27","28","29","30",
"31"
];

// this will take the data of the task and send it to the modal
function sendDataToModal(id,desc,date,time,completed){
    document.getElementById("task_id").value = id;
    document.getElementById("new_description").value=desc;
    document.getElementById("new_date").value=date;
    document.getElementById("new_time").value=time;
    document.getElementById("mark_completed").checked = completed === 'true';
    if(completed === 'true'){
        document.getElementById("label_for_completed").innerHTML = "Mark as incomplete";
    }
}

// since we are repeating code:
function makeDescriptionHTML(task,taskDesc){
    taskDesc += `<div class="toast show mb-3 mt-3" role="alert" aria-live="assertive" aria-atomic="true" style="cursor:pointer" onclick="sendDataToModal('${task.id}','${task.description}','${task.date}','${task.time}','${task.completed}')" data-bs-toggle="modal" data-bs-target="#edit_task_modal">`;
        taskDesc += `<div class="toast-header justify-content-between">`;
            // for now I have added the blue sun as the icon but that will change depending on the tag (low, med, high)
            taskDesc += `<strong><i class="bi bi-brightness-high-fill" style="color:blue"></i></strong>`;
            taskDesc += `<span class="fs-6">${task.date} | ${task.time}</span>`;
        taskDesc += `</div>`;
        taskDesc += `<div class="toast-body fs-6 ${task.completed ? "completed" : "" }">`;
            taskDesc += task.description;
        taskDesc += `</div>`;
    taskDesc += `</div>`;
    return taskDesc;
}


//Function to display tasks in day view
function displayDayTasks(key){
    let taskDesc = "";
    let count = 0;
    //fetches tasks
    api_get_tasks(function(result){
        for(const task of result.tasks){
            //if task matches current day, display it
            if(task.date == key){
                taskDesc = makeDescriptionHTML(task,taskDesc);
                document.getElementById("toast-container-today").innerHTML = taskDesc;
                count++;
            }
        }
        if(count==0){
            let task = {
                date:"-",
                time:"-",
                description:"<h4 class='ms-3'>No tasks for today!<h4>",
            }
            taskDesc = makeDescriptionHTML(task,taskDesc);
            document.getElementById("toast-container-today").innerHTML =taskDesc;
        }

    });
}

//Function to display next 10 tasks
function displayNextTasks(key){
    let taskDesc = "";  //building the tasks into this variable
    let count = 0;      //counting up to how many tasks are in this column (10 for time being)

    //fetches tasks and stores them into array to be sorted by date
    api_get_tasks(function(result){
        for(const task of result.tasks){
            //Magic number 10 is how many upcoming tasks can be displayed, may be modified when customization comes in.
            if(count >= 10) break;
            if(task.date > key){
                count++;
                taskDesc = makeDescriptionHTML(task,taskDesc);
                document.getElementById("toast-container-upcoming").innerHTML = taskDesc;
            }
        }
        if(count==0){
            let task = {
                date:"-",
                time:"-",
                description:"<h4 class='ms-3'>No upcoming tasks!<h4>",
            }
            taskDesc = makeDescriptionHTML(task,taskDesc);
            document.getElementById("toast-container-upcoming").innerHTML =taskDesc;
        }
    });
}

// dynamically generate today's date to render in the front-end
// the tricky bit is that, if we are at /task or today then it is the current day but if someone comes to this page from clicking on a date from calendar,
// then, we need to display that date. So I had to look at the URL and then based on that, dynamically generate the date.
// what is does is, if we are at a route /tasks/whatever, then we display that date. If we are at /task then we display today's date.
let urlDate = window.location.href.split("/").length > 4 ? new Date(window.location.href.split("/")[4].replace(/-/g,'/')).toDateString() : new Date().toDateString();
document.getElementById("today-date").innerHTML = urlDate;

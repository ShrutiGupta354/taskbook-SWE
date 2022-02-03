
//array of numbers so that all numbers are 2 digit for day and month when created in id field
const numbers = ["00",
"01","02","03","04","05","06","07","08","09","10",
"11","12","13","14","15","16","17","18","19","20",
"21","22","23","24","25","26","27","28","29","30",
"31"
];

// since we are repeating code:
function makeDescriptionHTML(task,taskDesc){
    taskDesc += `<div class="toast show mb-3 mt-3" role="alert" aria-live="assertive" aria-atomic="true" style="cursor:pointer" onclick="window.location.href='/tasks'">`;
        taskDesc += `<div class="toast-header justify-content-between">`;
            // for now I have added the blue sun as the icon but that will change depending on the tag (low, med, high)
            taskDesc += `<strong><i class="bi bi-brightness-high-fill" style="color:blue"></i></strong>`;
            taskDesc += `<small class="text-muted">${task.date} | ${task.time}</small>`;
        taskDesc += `</div>`;
        taskDesc += `<div class="toast-body ${task.completed ? "completed" : "" }">`;
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
                description:"<h2 class='ms-3'>No tasks for today!<h2>",
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
                description:"<h2 class='ms-3'>No upcoming tasks!<h2>",
            }
            taskDesc = makeDescriptionHTML(task,taskDesc);
            document.getElementById("toast-container-upcoming").innerHTML =taskDesc;
        }
    });
}
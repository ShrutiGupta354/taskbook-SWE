
//array of numbers so that all numbers are 2 digit for day and month when created in id field
const numbers = ["00",
"01","02","03","04","05","06","07","08","09","10",
"11","12","13","14","15","16","17","18","19","20",
"21","22","23","24","25","26","27","28","29","30",
"31"
];


//Function to display tasks in day view
function displayDayTasks(key){
    let taskDesc = "";

    //fetches tasks
    api_get_tasks(function(result){
        for(const task of result.tasks){
            //if task matches current day, display it
            if(task.date == key){
                taskDesc += `<p class="taskdesc`;
                if(task.completed) taskDesc += ` completed`;
                taskDesc += `">` + task.description + `</p>`;
            }
        }
        //once all tasks are in the taskDesc, add them to list
        document.getElementById("today-tasks").innerHTML = taskDesc;
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
                taskDesc += `<p class="taskdesc`;
                if(task.completed) taskDesc += ` completed`;
                taskDesc += `">` + task.description + `</p>`;
            }
        }
        document.getElementById("upcoming-tasks").innerHTML = taskDesc;
    });
}
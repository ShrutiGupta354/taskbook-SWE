
//array of numbers so that all numbers are 2 digit for day and month when created in id field
const numbers = ["00",
"01","02","03","04","05","06","07","08","09","10",
"11","12","13","14","15","16","17","18","19","20",
"21","22","23","24","25","26","27","28","29","30",
"31"
];

//find current day to use as key
d = new Date();

let id = d.getFullYear() + '-' + numbers[d.getMonth()+1] + '-' + d.getDate()

//displays tasks for today
displayDayTasks(id);
//displays next 10 tasks
displayNextTasks(id);

//Function to display tasks in day view
function displayDayTasks(key){
    let taskDesc = "";
    let count = 0;

    //fetches tasks
    api_get_tasks(function(result){
        for(const task of result.tasks){
            //if task matches current day, display it
            if(task.date == key){
                taskDesc += `<p class="taskdesc`;
                if(task.completed) taskDesc += ` completed`;
                taskDesc += `">` + task.description + `</p>`;
                document.getElementById("test").innerHTML = taskDesc;
            }
        }
    });
}

//Function to display next 10 tasks
function displayNextTasks(key){
    let taskDesc = "";
    let count = 0;

    api_get_tasks(function(result){
        for(const task of result.tasks){
            //(bug) this does not account for next 10, its next 10 after the date in order they were added to db
            if(task.date > key){
                count++;
                if(count < 11){
                    taskDesc += `<p class="taskdesc`;
                    if(task.completed) taskDesc += ` completed`;
                    taskDesc += `">` + task.description + `</p>`;
                    document.getElementById("next").innerHTML = taskDesc;
                }
            }
        }
    });
}
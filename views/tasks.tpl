% include("header.tpl")
% include("banner.tpl")

<style>
  .save, .undo, .move, .desc, .edit, .delete {
    cursor: pointer;
  }
  .desc { padding-left:8px }
</style>

<div class="w3-row">
  <div class="w3-col s6 w3-container w3-topbar w3-bottombar w3-leftbar w3-rightbar w3-border-white w3-blue">
    <div class="w3-row w3-xxlarge w3-bottombar w3-border-black w3-margin-bottom">
      <h1><i>Today</i></h1>
    </div>
    <table id="task-list-today" class="w3-table">
      <tr>
        <td style="width:36px"></td>
        <td>
          <input id="input-new-today" 
                 class="w3-input w3-border-bottom w3-blue" 
                 placeholder="Add an item..." 
                 type="text"/>
        </td>
        <td style="width:72px">
          <span id="save-new-today" class="save material-icons">done</span>
          <span id="undo-new-today" class="delete material-icons">unpublished</span>
        </td>
    </table>
    <div class="w3-row w3-bottombar w3-border-black w3-margin-bottom w3-margin-top"></div>
  </div>
  <div class="w3-col s6 w3-container w3-topbar w3-bottombar w3-leftbar w3-rightbar w3-border-white w3-green">
    <div class="w3-row w3-xxlarge w3-bottombar w3-border-black w3-margin-bottom">
      <h1><i>Tomorrow</i></h1>
    </div>
    <table  id="task-list-tomorrow" class="w3-table">
      <tr>
        <td style="width:36px"></td>
        <td>
          <input id="input-new-tomorrow" 
                 class="w3-input w3-border-bottom w3-green" 
                 placeholder="Add an item..." 
                 type="text"/>
        </td>
        <td style="width:72px">
          <span id="save-new-tomorrow" class="save material-icons">done</span>
          <span id="undo-new-tomorrow" class="undo material-icons">unpublished</span>
        </td>
      </tr>
    </table>
    <div class="w3-row w3-bottombar w3-border-black w3-margin-bottom w3-margin-top"></div>
  </div>
</div>
<script>

function save_task(event) {
  console.log("save item")
}

function undo_task(event) {
  console.log("undo item")
}

function move_task(event) {
  console.log("move item")
}

function edit_task(event) {
  console.log("edit item")
}

function delete_task(event) {
  console.log("delete item")
}

function display_task(x) {
  console.log("displaying task",x);
  description = x.completed ? '<s>' + x.description + '</s>' : x.description; 
  t = '<tr class="task">' + 
      '<td><span id="today-'+x.id+'" class="move material-icons">arrow_back</span></td>' +
      '  <td><span id="desc-'+x.id+'" class="desc">' + description + '</td>' +
      '  <td>' +
      '    <span id="edit-'+x.id+'" class="edit material-icons">edit</span>' +
      '    <span id="delete-'+x.id+'" class="delete material-icons">delete</span>' +
      '  </td>' +
      '</tr>';
  $("#task-list-" + x.list).append(t);
}

function display_tasks(tasks) {
  // remove the old tasks
  $(".task").remove();
  // display the new tasks
  for (const task of tasks) {
    console.log("Task = ",task)
    display_task(task)
  }
  $(".move").click(move_task);
  $(".edit").click(edit_task);
  $(".delete").click(delete_task);
}

$(document).ready(function(){
  $(".save").click(save_task);
  $(".undo").click(undo_task);
  display_tasks([
    {"id": 1235, time:0.0, "description":"Do something", "list":"today", "completed":true},
    {"id": 1234, time:0.5, "description":"Do something else", "list":"today", "completed":false},
    {"id": 1235, time:0.3, "description":"Do something", "list":"tomorrow", "completed":false},
    {"id": 1234, time:0.7, "description":"Do something else", "list":"tomorrow", "completed":true}
  ]);
});

</script>
% include("footer.tpl")

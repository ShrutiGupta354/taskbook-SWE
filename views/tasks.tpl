% include("header.tpl")
% include("banner.tpl")

<style>
  .save, .undo, .move, .desc, .edit, .delete {
    cursor: pointer;
  }
  .completed {text-decoration: line-through;}
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
          <span id="undo-new-today" class="undo material-icons">unpublished</span>
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
  input_id = event.target.id.replace("save","input");
  desc = $("#" + input_id).val()
  list = input_id.endsWith("today") ? "today" : "tomorrow";
  if (desc == "") { return; }
  console.log("saving :",input_id," ",$("#" + input_id).val())
  $.ajax({url:"api/tasks", type:"POST", 
          data:JSON.stringify({description:$("#" + input_id).val(),list:list}), 
          contentType:"application/json; charset=utf-8",
          success:function(result){
            console.log("POST result = ",result)
            $("#" + input_id).val("");
            get_current_tasks();
  }});
}

function undo_task(event) {
  input_id = event.target.id.replace("undo","input");
  $("#" + input_id).val("");
}

function move_task(event) {
  console.log("move item", event.target.id )
  id = event.target.id.replace("move-","");
  id = parseInt(id)
  target_list = event.target.className.search("today") > 0 ? "tomorrow" : "today";
  console.log("updating :",{'id':id, 'list':target_list})
  $.ajax({url:"api/tasks", type:"PUT", 
          data:JSON.stringify({'id':id, 'list':target_list}), 
          contentType:"application/json; charset=utf-8",
          success:function(result){
            console.log("PUT result = ",result)
            get_current_tasks();
  }});
}

function complete_task(event) {
  console.log("complete item", event.target.id )
  id = event.target.id.replace("desc-","");
  id = parseInt(id)
  completed = event.target.className.search("completed") > 0;
  console.log("updating :",{'id':id, 'completed':completed==false})
  $.ajax({url:"api/tasks", type:"PUT", 
          data:JSON.stringify({'id':id, 'completed':completed==false}), 
          contentType:"application/json; charset=utf-8",
          success:function(result){
            console.log("PUT result = ",result)
            get_current_tasks();
  }});
}

function edit_task(event) {
  console.log("edit item")
}

function delete_task(event) {
  console.log("delete item")
  id = event.target.id.replace("delete-","");
  id = parseInt(id)
  console.log("deleting :",{'id':id})
  $.ajax({url:"api/tasks", type:"DELETE", 
          data:JSON.stringify({'id':id}), 
          contentType:"application/json; charset=utf-8",
          success:function(result){
            console.log("DELETE result = ",result)
            get_current_tasks();
  }});
}

function display_task(x) {
  arrow = (x.list == "today") ? "arrow_forward" : "arrow_back";
  completed = x.completed ? " completed" : "";
  t = '<tr class="task">' + 
      '<td><span id="move-'+x.id+'" class="move '+x.list+' material-icons">' + arrow + '</span></td>' +
      '  <td><span id="desc-'+x.id+'" class="desc' + completed + '">' + x.description + '</span></td>' +
      '  <td>' +
      '    <span id="edit-'+x.id+'" class="edit material-icons">edit</span>' +
      '    <span id="delete-'+x.id+'" class="delete material-icons">delete</span>' +
      '  </td>' +
      '</tr>';
  $("#task-list-" + x.list).append(t);
}

function get_current_tasks() {
  // remove the old tasks
  $(".task").remove();
  // display the new tasks
  $.ajax({url:"api/tasks", type:"GET", success:function(result){
    for (const task of result.tasks) {
      console.log("Task = ",task)
      display_task(task)
    }
    $(".move").click(move_task);
    $(".desc").click(complete_task)
    $(".edit").click(edit_task);
    $(".delete").click(delete_task);
  }});
}

$(document).ready(function() {
  $(".save").click(save_task);
  $(".undo").click(undo_task);
  get_current_tasks()
});

</script>
% include("footer.tpl")

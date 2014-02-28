var x = 0;

function change(type, y) {
  if (type == "landline") {
    document.getElementById("contactphone["+y+"].dropdown").innerHTML = "<span style='padding:0 5px 0 0;'><img src='/static/img/phone_icon.png' style='position:relative; top:-1px;' /></span> Land Line <span class='caret'></span>"
    document.getElementById("contactphone[0].type").value = type;
  } else if (type == "cell") {
    document.getElementById("contactphone["+y+"].dropdown").innerHTML = "<span style='padding:0 9px 0 3px;'><img src='/static/img/cell_icon.png' style='position:relative; top:-1px;' /></span> Cell Phone <span class='caret'></span>"
    document.getElementById("contactphone["+y+"].type").value = type;
  } else if (type == "fax") {
    document.getElementById("contactphone["+y+"].dropdown").innerHTML = "<span style='padding:0 5px 0 0;'><img src='/static/img/fax_icon.png' style='position:relative; top:-1px;' /></span> Fax <span class='caret'></span>"
    document.getElementById("contactphone["+y+"].type").value = type;
  } else if (type == "other") {
    document.getElementById("contactphone["+y+"].dropdown").innerHTML = "Other <span class='caret'></span>"
    document.getElementById("contactphone["+y+"].type").value = type;    
  }
}

function addnumber() {

  window.x++;
  var x = window.x;
  var insert =  "<div class='input-group'>";
      insert += " <div class='input-group-btn'>";
      insert += "   <button type='button' class='btn btn-default dropdown-toggle' data-toggle='dropdown' id='contactphone["+x+"].dropdown'>";
      insert += "     <span style='padding:0px 5px 0 0;'>";
      insert += "       <img src='/static/img/phone_icon.png' style='position:relative; top:-1px;'/>";
      insert += "     </span> Land Line <span class='caret'></span>";
      insert += "   </button>";
      insert += "   <ul class='dropdown-menu'>";
      insert += "     <li><a onclick='change(\"landline\", "+x+")'>";
      insert += "       <span style='padding:0px 5px 0 0;'>";
      insert += "         <img src='/static/img/phone_icon.png' style='position:relative; top:-1px;' />";
      insert += "       </span> Land line</a>";
      insert += "     </li>";
      insert += "     <li><a onclick='change(\"cell\", "+x+")'>";
      insert += "       <span style='padding:0 9px 0 3px;'>";
      insert += "         <img src='/static/img/cell_icon.png' style='position:relative; top:-1px;' />";
      insert += "       </span> Cell Phone</a></li>";
      insert += "     <li><a onclick='change(\"fax\", "+x+")'>";
      insert += "       <span style='padding:0 5px 0 0;'>";
      insert += "         <img src='/static/img/fax_icon.png' style='position:relative; top:-1px;' />";
      insert += "       </span> Fax</a></li>";
      insert += "     <li class='divider'></li>";
      insert += "     <li><a onclick='change(\'other\', "+x+")'>Other</a></li>";
      insert += "   </ul>";
      insert += " </div><!-- /btn-group -->";
      insert += " <input type='text' class='form-control' name='contactphone["+x+"].number' id='contactphone["+x+"].number' placeholder='(XXX) XXX-XXX xXXX'>";
      insert += "</div><!-- /input-group -->";
      insert += "<input type='text' class='form-control' name='contactphone["+x+"].type' id='contactphone["+x+"].type' placeholder='landline'>";
  document.getElementById("extra").innerHTML += insert;
}
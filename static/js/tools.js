function addinput(obj){
  var htmlObj = obj.parentElement;
  var parent = htmlObj.parentElement;
  var html = htmlObj.innerHTML;
  obj.onclick = function() {return false;};
  obj.style.cursor = "default";
  var div = document.createElement('div');
  div.innerHTML = html;
  div.className = "input-group";
  div.style.padding = "10px";
  parent.appendChild(div);
}

function removeinput(obj){
  var parent = obj.parentElement.parentElement;
  var htmlObj = obj.parentElement;

  htmlObj.remove();
  parent.lastChild.onclick=addinput(this);
  parent.lastChild.style.cursor = "pointer";

}


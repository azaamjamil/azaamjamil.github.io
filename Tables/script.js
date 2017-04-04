function sortTable(col,sortDown, el) {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("myTable");
  //calls vilisbilty function to make all images visible
  visible();
  el.style.visibility = "hidden";
  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("TR");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[col];
      y = rows[i + 1].getElementsByTagName("TD")[col];
      //check if the two rows should switch place:
      if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()&&sortDown==0) {
        //if so, mark as a switch and break the loop:
        shouldSwitch= true;
        break;
      }
      if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()&&sortDown==1) {
        //if so, mark as a switch and break the loop:
        shouldSwitch= true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
  //hides the element you just clicked
}

function visible() {
  //grabs all the images
  var images = document.getElementsByTagName('img'); 
  //goes through them and sets them visible
  for(var i = 0; i < images.length; i++) {
      images[i].style.visibility = "visible";
  }
}
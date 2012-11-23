/* Function getElementsByClassName(node,classname) by Dustin Diaz, found here: 
http://stackoverflow.com/questions/1933602/
how-to-getelementbyclass-instead-of-getelementbyid-with-javascript*/
function getElementsByClassName(node,classname) {
  if (node.getElementsByClassName) { // use native implementation if available
    return node.getElementsByClassName(classname);
  } else {
    return (function getElementsByClass(searchClass,node) {
        if ( node == null )
          node = document;
        var classElements = [],
            els = node.getElementsByTagName("*"),
            elsLen = els.length,
            pattern = new RegExp("(^|\\s)"+searchClass+"(\\s|$)"), i, j;

        for (i = 0, j = 0; i < elsLen; i++) {
          if ( pattern.test(els[i].className) ) {
              classElements[j] = els[i];
              j++;
          }
        }
        return classElements;
    })(classname, node);
  }
}

// --------------------------------------------------------- GLOBAL VARS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

var listObj;
var streamName;

function newFeedFooClose() {
    document.getElementById("newFeedFoo").style.display = 'none';
}
function saveAllChangesClose() {
    document.getElementById("saveAllChanges").style.display = 'none';
}

function addFeedToStream(e) {
    document.getElementById("newFeedFoo").style.display = 'block';
    streamName = e.target.id;
    var listId = "" + e.target.id + "ListReally";
    listObj = document.getElementById(listId);
}

function reallyAddFeed() {
    var fName = document.getElementById('elephant').value;
    var fUrl = document.getElementById('walrus').value;

    var newHtml = "<li><a class='";
    newHtml += streamName;

    newHtml += "' id='";
    newHtml += fName;
    newHtml += "' href='";
    newHtml += fUrl;
    newHtml += "'>";
    newHtml += fName;
    newHtml += "</a> <span class='msg' style='color:blue;font-size:0.8em;'>(New feed: click SAVE at the bottom to save)</span></li>";

    listObj.innerHTML += newHtml;
    newFeedFooClose();    
}

function saveAllChanges() {
    document.getElementById('saveAllChanges').style.left="50px";

    //construct the new JSON file
    var ulArray = getElementsByClassName(document, 'streamTitleList');
    var output = "[";

    for (var i=0; i<ulArray.length; i++) {
        output += "{\"stream_name\":\"";
        output += ulArray[i].id.slice(0,-4);
        output += "\",";
        output += "\"feeds\": [";
        var listItems = getElementsByClassName(document,ulArray[i].id.slice(0,-4));
        for (var j=0; j<listItems.length; j++) {
            output += "{\"name\":\"";
            output += listItems[j].getAttribute('id');
            output += "\", \"url\":\"";
            output += listItems[j].getAttribute('href');
            output += "\"}";
            var c = j+1;
            if (c < listItems.length) {
                output += ",";
            }
        }
        output += "]}";
        var d = i+1;
        if (d < ulArray.length) {
            output += ",";
        }
    }
    output += "]";

    //encodeURIComponent(content);
    var uriFoo = "data:text/json;UTF-8," + output;
    saveAllChangesClose();

}

function init() {

    var kobjs = getElementsByClassName(document, 'addFeedToStream');
    for (var i=0; i<kobjs.length; i++) {
        kobjs[i].addEventListener('click', function (e) {
            addFeedToStream(e);
        }, false);
    }

    var objs = getElementsByClassName(document, 'remove_stream');
    for (var i=0; i<objs.length; i++) {
        objs[i].addEventListener('click', function (e) {
            e.target.parentNode.parentNode.innerHTML = "STREAM REMOVED (if you didn't want to do that, just reload the page.)";
        }, false);
    }

    var fobjs = getElementsByClassName(document, 'remove_feed');
    for (var j=0; j<fobjs.length; j++) {
        fobjs[j].addEventListener('click', function (e) {
            e.target.parentNode.innerHTML = "FEED REMOVED (if you didn't want to do that, just reload the page.)";
        }, false);
    }

    var gobjs = getElementsByClassName(document, 'add_feed');
    for (var k=0; k<gobjs.length; k++) {
        gobjs[k].addEventListener('click', function (e) {

            var parentDiv = e.target.parentNode;
            var childArray = parentDiv.childNodes;
            var feedName = childArray[1].value;
            var feedUrl = childArray[3].value;

            var fooObj = parentDiv.parentNode;
            fooObj.innerHTML += "FOO!!";

 
        }, false);
    }
}


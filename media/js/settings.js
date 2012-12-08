function init() {
    loadStreams();
    addListeners();
}

function loadStreams() {
    var html = "";

    for (var i=0; i<jsonStreams.length; i++) {
        var number = i+1;
        html += "<div class='stream'>";


        html += "<span class='remove_stream'>(remove the entire set)</span>";

        html += "<h3>";
        html += "Set of feeds ";
        html += number;
        html += "</h3>";


        html += "<span class='streamTitleList' id='";
        html += jsonStreams[i]['stream_name'];
        html += "List'>";
        html += "<h3>Name:</h3> <input type='text' class='streamNameInput' value='";
        html += jsonStreams[i]['stream_name'];
        html += "'>";
        html += "</span>";

        html += "<h3>Feeds:</h3>";
        html += "<ul id='";
        html += jsonStreams[i]['stream_name'];
        html += "ListReally'>";

        for (var j=0; j<jsonStreams[i]['feeds'].length; j++) {
            html += "<li><a class='";
            html += jsonStreams[i]['stream_name'];
            html += "' id='";
            html += jsonStreams[i]['feeds'][j]['name'];
            html += "' href='";
            html += jsonStreams[i]['feeds'][j]['url'];
            html += "'>";
            html += jsonStreams[i]['feeds'][j]['name'];
            html += "</a> <span class='remove_feed'>(remove feed)</span></li>";
        }
        html += "</ul>";
        html += "<button class='addFeedToStream' id='";
        html += jsonStreams[i]['stream_name'];
        html += "'>Add a feed to this set</button>";
        html += "</div> <!--.stream-->";
    }
    document.getElementById('streamsGoHere').innerHTML = html;
}


/* ----- GLOBAL VARS ----- */

var listObj;
var streamName;

function newFeedFooClose() {
    document.getElementById("newFeedFoo").style.display = 'none';
}
function addStreamClose() {
    document.getElementById('addStream').style.display = 'none';
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
    var fUrl = document.getElementById('feedNameButton').value;

    var newHtml = "<li><a class='newFeed' href='";
    newHtml += streamName;
    newHtml += fUrl;
    newHtml += "'>";
    newHtml += fUrl;
    newHtml += "</a> <p class='msg'>Not yet saved: to finish adding this feed, you'll have to save your settings by clicking the SAVE ALL button at the bottom of this page.</p></li>";

    listObj.innerHTML += newHtml;
    newFeedFooClose();    
}
function addStream() {
    document.getElementById('addStream').style.display = "block";
}
function reallyAddStream() {
    var newStreamName = document.getElementById('newStreamName').value;
    var myDiv = document.getElementById("streamsGoHere");
    var html = "<div class='stream'> <h2><a class='streamTitleList' id='";
    html += newStreamName;
    html += "List' href=''>";
    html += newStreamName;
    html += "</a> <span class='remove_stream'>(remove stream)</span></h2> <ul id='";
    html += newStreamName;
    html += "ListReally'>  </ul>  <button class='addFeedToStream' id='";
    html += newStreamName;
    html += "'>Add a feed to this stream </button></div> <!--.stream-->";
    myDiv.innerHTML += html;
    addListeners();
    addStreamClose();
}

function saveAllChanges() {

    //construct the new JSON file
    var ulArray = getElementsByClassName(document, 'streamTitleList');
    var output = "var jsonStreams = /*STARTJSON*/[";

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
    output += "]/*ENDJSON*/;";

    //encodeURIComponent(content);
    var uriFoo = "data:text/json;UTF-8," + output;
    document.getElementById('saveAllChangesLink').setAttribute('href', uriFoo);
    document.getElementById('saveAllChanges').style.display="block";
}


function renameThisFunction1(e) {
    e.target.parentNode.innerHTML += "<p class='msg'>This feed has been marked for removal: to complete the removal process this, click SAVE at the bottom of this page.</p>";
}
function renameThisFunction2(e) {
    e.target.parentNode.parentNode.innerHTML += "<p class='msg'>This stream has been marked for removal: to complete the removal process this, click SAVE at the bottom of this page.</p>";
}


function addListeners() {

    var kobjs = getElementsByClassName(document, 'addFeedToStream');
    for (var f=0; f<kobjs.length; f++) {

        // Only add event listener if the isn't one already
        if (typeof(kobjs[f].onclick) != "function") {
            kobjs[f].addEventListener('click', function (e) {
                addFeedToStream(e);
            }, false);
        }
    }

    var objs = getElementsByClassName(document, 'remove_stream');
    for (var i=0; i<objs.length; i++) {

        // Only add event listener if the isn't one already
        if (typeof(objs[i].onclick) != "function") {
            objs[i].addEventListener('click', function (e) {
                renameThisFunction2(e);
            }, false);
        }
    }

    var fobjs = getElementsByClassName(document, 'remove_feed');
    for (var j=0; j<fobjs.length; j++) {

        // Only add event listener if the isn't one already
        if (typeof(fobjs[j].onclick) != "function") {
            fobjs[j].addEventListener('click', function (e) {
                renameThisFunction1(e);
            }, false);
        }
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




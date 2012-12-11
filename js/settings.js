function getFeedHtml(stream_name, feed_name, feed_url) {
    var html = "<li><a class='";
    html += stream_name;
    html += "' id='";
    html += feed_name;
    html += "' href='";
    html += feed_url;
    html += "'>";
    html += feed_name;
    html += "</a> <span class='remove_feed'>(remove feed)</span></li>";
    return html;
}

function getStreamHtml(number, streamName, feedsArray) {
    var html = "";
    html += "<div class='stream'>";
    html += "<span class='remove_stream'>(remove the entire set)</span>";
    html += "<h3>";
    html += "Set of feeds ";
    html += number;
    html += "</h3>";
    html += "<span class='streamTitleList' id='";
    html += streamName;
    html += "List'>";
    html += "<h3>Name:</h3> <input type='text' class='streamNameInput' id='";
    html += streamName;
    html += "NameInput' value='";
    html += streamName;
    html += "'>";
    html += "</span>";
    html += "<h3>Feeds:</h3>";
    html += "<ul id='";
    html += streamName;
    html += "ListReally'>";
    for (var j=0; j<feedsArray.length; j++) {
        var newHtml = getFeedHtml(streamName, feedsArray[j]['name'], feedsArray[j]['url']);
        html += newHtml;
    }
    html += "</ul>";
    html += "<button class='addFeedToStream' id='";
    html += streamName;
    html += "'>Add a feed to this set</button>";
    html += "</div> <!--.stream-->";
    return html;
}

function loadStreams() {
    var html = "";

    for (var i=0; i<jsonStreams.length; i++) {
        var number = i+1;
        var newHtml = getStreamHtml(number, jsonStreams[i]['stream_name'], jsonStreams[i]['feeds']);
        html += newHtml;
    }
    document.getElementById('streamsGoHere').innerHTML = html;
}

function init() {
    loadStreams();
    addListeners();
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
                markStreamForRemoval(e);
            }, false);
        }
    }
    var fobjs = getElementsByClassName(document, 'remove_feed');
    for (var j=0; j<fobjs.length; j++) {

        // Only add event listener if the isn't one already
        if (typeof(fobjs[j].onclick) != "function") {
            fobjs[j].addEventListener('click', function (e) {
                markFeedForRemoval(e);
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


/* ---  Functions to open divs --- */

function displayAddStream() {
    document.getElementById('addStream').style.display = "block";
}
function displayAddFeed() {
    document.getElementById("newFeed").style.display = 'block';
}


/* --- Functions to close divs by setting them to display:none --- */

function newFeedClose() {
    document.getElementById("newFeed").style.display = 'none';
}
function addStreamClose() {
    document.getElementById('addStream').style.display = 'none';
}
function saveAllChangesClose() {
    document.getElementById("saveAllChanges").style.display = 'none';
}

/* --- */

function markFeedForRemoval(e) {
    e.target.parentNode.innerHTML = "<p>MARKED FOR REMOVAL</p>";
}
function markStreamForRemoval(e) {
    e.target.parentNode.innerHTML = "<p>MARKED FOR REMOVAL</p>";
}

function addFeedToStream(e) {
    var streamName = e.target.id;
    document.getElementById("newFeedStreamName").value = streamName;
    displayAddFeed();
}
function addFeed() {
    var feed_url = document.getElementById('feedNameButton').value;
    var streamName = document.getElementById('newFeedStreamName').value;
    var newHtml = getFeedHtml(streamName, 'New feed', feed_url);
    var targetId = streamName + "ListReally";
    document.getElementById(targetId).innerHTML += newHtml;
    newFeedClose();    
}
function addStream() {
    var newStreamName = document.getElementById('newStreamName').value;
    var myDiv = document.getElementById("streamsGoHere");
    var emptyArray = [];
    var ulArray = getElementsByClassName(document, 'streamTitleList');
    var number = ulArray.length + 1;
    var html = getStreamHtml(number, newStreamName, emptyArray);
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
        var tempName = ulArray[i].id.slice(0,-4);
        tempName += "NameInput";
        var streamName = document.getElementById(tempName).value;

        output += streamName;







        //output += ulArray[i].id.slice(0,-4);
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


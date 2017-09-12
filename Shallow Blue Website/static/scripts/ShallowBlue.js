/*
Notes:
console.log() print to the brouser console
 */

function example()
{
    //action;
};

function get_news()
{
    var xhttp = new XMLHttpRequest();
    
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rawData = this.responseText;
            //alert(rawData)
            document.getElementById("news-bar").innerHTML = rawData;
        }
    };
    xhttp.open("GET", "/data/news-bar", true);
    xhttp.send();
}
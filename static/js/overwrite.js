function goToSubreddit(){
    // Selecting the input element and get its value 
    var inputVal = document.getElementById("subredditSearch").value;
    var baseURL = window.location.hostname.concat('/r/');

    var url = baseURL.concat(inputVal)
    alert(url);
    window.location.href = url;
}
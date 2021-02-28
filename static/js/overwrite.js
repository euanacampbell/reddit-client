function goToSubreddit(){
    // Selecting the input element and get its value 
    var inputVal = document.getElementById("subredditSearch").value;
    var baseURL = '/r/';

    var url = baseURL.concat(inputVal)
    window.location.href = url;
}
function goToSubreddit(){
    // Selecting the input element and get its value 
    var inputVal = document.getElementById("subredditSearch").value;
    var baseURL = "https://reddit.euan.app/r/";

    var url = baseURL.concat(inputVal)
    console.log(url)
    alert(url);
    window.location.href = url;
}
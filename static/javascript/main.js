function changeActive(id){
    var body = document.body.id;
    var itemId = "item-" + body;
    var element = document.getElementById(itemId);
    // window.alert(element.textContent);
    element.classList.add("active");
}
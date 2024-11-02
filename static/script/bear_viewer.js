document.getElementById("view-bear-button").addEventListener("click", () => {
    document.getElementById("bv-element").classList.toggle("hidden-viewer");

    let e = document.createElement("div");
    e.id = "bv-backdrop";
    e.classList.add("bv-backdrop");
    e.classList.add("hidden-backdrop");
    document.getElementById("bv-element").parentNode.insertBefore(e, document.getElementById("bv-element"));
    
    setTimeout(() => { e.classList.remove("hidden-backdrop"); }, 0);
});



document.getElementById("bv-close").addEventListener("click", () => {
    document.getElementById("bv-element").classList.add("hidden-viewer");
    document.getElementById("bv-backdrop").classList.add("hidden-backdrop");
    
    setTimeout(() => {
        document.getElementById("bv-backdrop").remove();
    }, 300);
});

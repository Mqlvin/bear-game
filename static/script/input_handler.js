

async function takeInput(values, question, socket) {
return new Promise((resolve) => {

    let inputSelector = document.getElementById("input-selector");
    inputSelector.style.paddingTop = "150px";
    inputSelector.style.opacity = "0";

    let questionElement = document.createElement("div");
    questionElement.classList.add("tektur-700");
    questionElement.classList.add("text-glow");
    questionElement.classList.add("select-option");
    questionElement.textContent = question;
    inputSelector.append(questionElement);

    let optionElements = [];
    let selectedIdx = 0;

    for(let i = 0; i < values.length; i++) {
        let option = document.createElement("div");
        option.classList.add("tektur-500");
        option.classList.add("text-glow");
        option.classList.add("select-option");
        option.classList.add("select-unselected");

        inputSelector.append(option);
        option.textContent = values[i];
        optionElements.push(option);
    }

    optionElements[selectedIdx].classList.remove("select-unselected");
    optionElements[selectedIdx].classList.add("select-selected");    
    
    setTimeout(() => {
        document.getElementById("input-decor").classList.add("decor-highlight");
        inputSelector.style.paddingTop = "30px";
        inputSelector.style.opacity = "1";
    }, 1);
    

    const kdFunc = (ev) => {
        switch(ev.key) {
            case "Enter": {
                document.removeEventListener("keydown", kdFunc);

                // fade out other items
                for(let i = 0; i < optionElements.length; i++) {
                    let tempEle = optionElements[i];
                    if(tempEle.classList.contains("select-unselected")) {
                        tempEle.style.opacity = "0";
                    }
                }

                // slide text out
                setTimeout(() => {
                    inputSelector.style.opacity = "0";
                    inputSelector.style.paddingTop = "150px";

                    document.getElementById("input-decor").classList.remove("decor-highlight");
                }, 800);


                // resolve answer and clear inputselector element
                setTimeout(() => {
                    while(inputSelector.lastChild) {
                        inputSelector.removeChild(inputSelector.lastChild);
                    }

                    resolve(selectedIdx);
                }, 1200);

                // put question/choice on terminal
                textToTerminal("\u00A0", 500, false);
                textToTerminal(question, 700, false);
                textToTerminal(values[selectedIdx], 500, true);


                break;
            }

            case "ArrowUp": {
                selectedIdx = Math.max(0, selectedIdx - 1);

                optionElements[selectedIdx].classList.remove("select-unselected");
                optionElements[selectedIdx].classList.add("select-selected");
                optionElements[selectedIdx + 1].classList.remove("select-selected");
                optionElements[selectedIdx + 1].classList.add("select-unselected");


                break;
            }

            case "ArrowDown": {
                selectedIdx = Math.min(values.length - 1, selectedIdx + 1);

                optionElements[selectedIdx].classList.remove("select-unselected");
                optionElements[selectedIdx].classList.add("select-selected");
                optionElements[selectedIdx - 1].classList.remove("select-selected");
                optionElements[selectedIdx - 1].classList.add("select-unselected");

                break;
            }

            default: {
                break;
            }
        }
    };


    document.addEventListener("keydown", kdFunc);

});
}

function textToTerminal(text, weight, italic) {
    let ele = document.createElement("h");
    ele.classList.add("text-glow");
    ele.classList.add("dialogue-text");
    ele.classList.add("tektur-" + weight);
    if(italic) ele.classList.add("font-italic");
    ele.textContent = text;

    document.getElementById("dc").append(ele);
}

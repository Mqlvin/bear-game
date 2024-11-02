const notebook = [];



const socket = new WebSocket('./game_socket');
socket.addEventListener('message', async ev => {
    let message = JSON.parse(ev.data);



    switch(message.event_type) {
        case "take_input": {

            let responseIdx = await takeInput(message.options, message.question, socket);
            socket.send(JSON.stringify({"response":responseIdx, "token":message.token}))
            

            break;
        }


        case "serve_characteristics": {

            let parentContainer = document.getElementById("bv-stats-container");

            for(let bearCharacteristic of message.bears) {
                let container = document.createElement("div");
                container.classList.add("bv-stat-container");

                let nameElement = document.createElement("p");
                nameElement.classList.add("bv-stat-text");
                nameElement.classList.add("bv-bear-name");
                nameElement.classList.add("tektur-500");
                nameElement.classList.add("text-glow");
                nameElement.classList.add("font-large");
                nameElement.textContent = bearCharacteristic.name;

                container.append(nameElement);

                for(let charKey of Object.keys(bearCharacteristic.characteristics)) {
                    let property = document.createElement("p");
                    property.classList.add("bv-stat-text");
                    property.classList.add("tektur-500");
                    property.classList.add("text-glow");
                    property.classList.add("font-medium");
                    property.textContent = bearCharacteristic.characteristics[charKey];
                    container.append(property);
                }

                parentContainer.append(container);
            }

            break;

        }


        case "evidence": {
            let noEvidenceElement = document.getElementById("no-evidence");
            if(noEvidenceElement != undefined) {
                noEvidenceElement.remove();
            }

                let e = document.createElement("div");
                e.classList.add("evidence-entry");
                e.classList.add("font-small");
                e.classList.add("tektur-300");
                e.classList.add("text-glow");
                e.textContent = message.fact_string.substring(0, 60) + "...";
                document.getElementById("evidence-container").appendChild(e);

                notebook.push(message.fact_string);

                e.addEventListener("click", () => {
                    textToTerminal("\u00A0", 500, false);
                    textToTerminal("You take a look in your notebook... it reads:", 500, false);
                    textToTerminal(message.fact_string, 500, true);
                });

            break;
        }


        case "display": {
            let e = document.createElement("h");
            e.classList.add("text-glow")
            e.classList.add("dialogue-text")
            e.classList.add("tektur-500")
            if(message.text != "newline") {
                e.textContent = message.text;
            } else {
                e.textContent = "\u00A0";
            }
            document.getElementById("dc").append(e);

            break;
        }

        
        case "game_init": {
            console.log(message.is_murderer)
            document.getElementById("nameplate-prefix").textContent = "You are:";
            document.getElementById("nameplate").textContent =
                message.player_name +
                " (" + (message.is_murderer ? "murderer" : "innocent") + ")";

            break;
        }

        case "done_question": {
            // document.getElementById("input-selector").style.height = "0px";

            break;
        }

        default: {
            console.log("Unknown event " + message.event_type);
            break;
        }
    }
})


function textToTerminal(text, weight, italic) {
    let ele = document.createElement("h");
    ele.classList.add("text-glow");
    ele.classList.add("dialogue-text");
    ele.classList.add("tektur-" + weight);
    if(italic) ele.classList.add("font-italic");
    ele.textContent = text;

    document.getElementById("dc").append(ele);
}

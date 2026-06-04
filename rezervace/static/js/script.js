function rezervovat(id) {
    const capElement = document.getElementById('cap-' + id);
    let currentCap = parseInt(capElement.innerText);

    if (currentCap > 0) {
        if (confirm("Chcete si zarezervovat místo na této lekci?")) {
            // Snížíme číslo v tabulce o 1
            currentCap--;
            capElement.innerText = currentCap;
            alert("Rezervace byla úspěšně vytvořena!");
        }
    } else {
        alert("Omlouváme se, tato lekce je již plně obsazena.");
    }
}
const formulaire = document.getElementById("formulaire");

formulaire.addEventListener("submit", async (e) => {
    e.preventDefault();

    const message = document.getElementById("message").value;

    const reponse = await fetch("/recevoir", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const resultat = await reponse.json();

    document.getElementById("resultat").textContent = resultat.message;
    document.getElementById("message").value = "";
});
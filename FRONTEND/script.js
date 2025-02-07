// Not ekleme fonksiyonu
function notEkle() {
    let noteInput = document.getElementById("noteInput");
    let notMetni = noteInput.value.trim();

    if (notMetni === "") {
        alert("Lütfen bir not girin!");
        return;
    }

    // Notu listeye ekleme
    let notListesi = document.getElementById("notListesi");
    let li = document.createElement("li");
    li.textContent = notMetni;
    notListesi.appendChild(li);

    // LocalStorage'e kaydetme (tarayıcıda saklama)
    let notlar = JSON.parse(localStorage.getItem("notlar")) || [];
    notlar.push(notMetni);
    localStorage.setItem("notlar", JSON.stringify(notlar));

    // Alanı temizle
    noteInput.value = "";
}

// Sayfa açıldığında kaydedilmiş notları göster
window.onload = function() {
    let notlar = JSON.parse(localStorage.getItem("notlar")) || [];
    let notListesi = document.getElementById("notListesi");
    
    notlar.forEach(not => {
        let li = document.createElement("li");
        li.textContent = not;
        notListesi.appendChild(li);
    });
};

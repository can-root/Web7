function sifreOlustur() {
    const uzunluk = parseInt(document.getElementById('uzunluk').value);
    if (uzunluk < 8 || uzunluk > 256) {
        alert('Lütfen 8-256 arasında bir uzunluk girin.');
        return;
    }

    const karakterler = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';
    let sifre = '';
    for (let i = 0; i < uzunluk; i++) {
        sifre += karakterler.charAt(Math.floor(Math.random() * karakterler.length));
    }

    document.getElementById('sonuc').value = sifre; // Şifreyi metin kutusuna yaz
}

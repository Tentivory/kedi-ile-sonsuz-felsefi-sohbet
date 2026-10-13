#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi ile Sonsuz Felsefi Sohbet Simülatörü
Bu kod, kedilerin aslında evrenin sırlarını bildiğini kanıtlar.
Çalıştırmak için: python kedi_sohbet.py
"""

import random
import time
import sys

def yavas_yaz(metin, gecikme=0.05):
    """Metni karakter karakter yavaşça yazar, çünkü kediler acele etmez."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

insan_sorulari = [
    "Hayatın anlamı nedir, kedi?",
    "Evren neden genişliyor?",
    "Neden her şey boş?",
    "Kahve mi çay mı daha felsefi?",
    "Zaman gerçekten var mı yoksa sadece kedi uykusu mu?",
    "Neden çoraplar kayboluyor?",
    "Eğer bir ağaç düşerse ve kedi duymuyorsa, gerçekten düşmüş müdür?"
]

kedi_cevaplar = [
    "Miyav. Yani, aslında her şey bir yanılsama. Ama mama gerçek.",
    "... (uzun uzun bakar) ... Sen mi sordun yoksa evren mi?",
    "Hrrrr. Bu sorunun cevabı kuyruk ucumda. Yaklaşma.",
    "Neden sormaya devam ediyorsun? Ben sadece uyumak istiyorum.",
    "Evet. Hayır. Belki. Miyav. Şimdi karnımı kaşı.",
    "Varlık, yokluktan daha az ilginç. Özellikle mama yoksa.",
    "Bu sohbetin derinliği, senin kedi severliğinle doğru orantılı.",
    "Hııı. Felsefe yüksek sesle yapılmaz. Sessiz mırla."
]

def sohbet_baslat(tur_sayisi=5):
    yavas_yaz("=== Kedi ile Sonsuz Felsefi Sohbet Simülatörü v1.0 ===")
    yavas_yaz("Uyarı: Bu program ciddi bilimsel araştırma ürünüdür. Sonuçlar garantilidir.")
    yavas_yaz("Kediniz hazır mı? (Aslında hazır değil, ama biz başlıyoruz)\n")
    
    for i in range(tur_sayisi):
        soru = random.choice(insan_sorulari)
        cevap = random.choice(kedi_cevaplar)
        
        yavas_yaz(f"Sen: {soru}")
        time.sleep(1.5)
        yavas_yaz(f"Kedi: {cevap}")
        yavas_yaz("---")
        time.sleep(2)
    
    yavas_yaz("\nSohbet sona erdi. Kediniz hala uyuyor. Felsefe kazandı.")
    yavas_yaz("Tekrar için programı yeniden çalıştır. Sonsuz değil ama neredeyse.")

if __name__ == "__main__":
    sohbet_baslat()

# Gizli not: Bu kodun altında aslında büyük bir sır var. Kayyumlar bile bunu çözemedi. Ama ciddiye alma.

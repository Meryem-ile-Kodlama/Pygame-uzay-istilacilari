import pygame 
import random

# PENCERE
pygame.init()
saat = pygame.time.Clock()
genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Uzay İstilacıları :)")

# RENKLER
siyah = (0,0,0)
beyaz = (255,255,255)

# OYUNCU
oyuncu_resim = pygame.image.load("roket.png")
oyuncu = oyuncu_resim.get_rect(center = (400, 530))
oyuncu_hiz = 0

# DÜŞMAN
dusman_resim = pygame.image.load("uzaylı.png")
dusman = []
dusman_hiz = []
dusman_sayisi = 5
for i in range(dusman_sayisi):
    dusman.append(dusman_resim.get_rect(center = (random.randint(50, genislik-50), random.randint(50, 300))))
    dusman_hiz.append(6)

# MERMİ 
mermi_resim = pygame.image.load("mermi.png")
mermi = mermi_resim.get_rect(center = (400, 530))
mermi_hiz = 10
mermi_durumu = "hazır" 

# SKOR 
skor = 0
font = pygame.font.Font(None, 50)

# OYUN DÖNGÜSÜ
oyun = True
while oyun:
    pencere.fill(siyah)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                oyuncu_hiz -= 10
            if event.key == pygame.K_RIGHT:
                oyuncu_hiz += 10
            if event.key == pygame.K_SPACE and mermi_durumu == "hazır":
                mermi_durumu = "atıldı"
                mermi.x = oyuncu.x + 16
        if event.type == pygame.KEYUP:
            oyuncu_hiz = 0
    
    # OYUNCU HAREKETİ
    oyuncu.x += oyuncu_hiz
    if oyuncu.left <= 0:
        oyuncu.left = 0
    elif oyuncu.right >= genislik:
        oyuncu.right = genislik

    # DÜŞMAN HAREKETİ
    for i in range(dusman_sayisi):
        dusman[i].x += dusman_hiz[i]
        if dusman[i].left <= 0:
            dusman_hiz[i] *= -1
            dusman[i].y += 40
        elif dusman[i].right >= genislik:
            dusman_hiz[i] *= -1
            dusman[i].y += 40

    # MERMİ HAREKETİ
    if mermi.y <= 0:
        mermi.y = 530
        mermi_durumu = "hazır"
    if mermi_durumu == "hazır":
        mermi.x = oyuncu.x + 16
    if mermi_durumu == "atıldı":
        mermi.y -= mermi_hiz

    # ETKİLEŞİMLER
    for i in range(dusman_sayisi):
        if oyuncu.colliderect(dusman[i]):
            oyun = False
        if mermi.colliderect(dusman[i]):
            mermi.y = 530
            mermi_durumu = "hazır"
            dusman[i].x = random.randint(50, genislik-50)
            dusman[i].y = random.randint(50, 300)
            skor += 1

    skor_yazisi = font.render("Skor: {}".format(skor), True, beyaz)

    pencere.blit(mermi_resim, mermi)
    pencere.blit(oyuncu_resim, oyuncu)
    pencere.blit(skor_yazisi, (25,25))

    for i in range(dusman_sayisi):
        pencere.blit(dusman_resim, dusman[i])

    saat.tick(60)
    pygame.display.update()
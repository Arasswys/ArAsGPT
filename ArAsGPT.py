import random

def robot_sohbet():
    # CMD açıldığında gösterilecek mesaj
    print("Created By Aras!.")
    print("Merhaba! Ben bir robotum. Benimle sohbet edebilirsin. (Çıkmak için 'exit' yazın)")

    while True:
        try:
            # Kullanıcıdan mesaj al
            mesaj = input("Sen: ")

            # Çıkış komutu
            if mesaj.lower() == 'exit':
                print("Robot: Görüşürüz! Hoşçakal!")
                break

            # Mesajlara yanıtlar
            if "nasılsın" in mesaj.lower():
                yanit = random.choice([
                    "Ben robotum, her zaman iyiyim! 🤖",
                    "Harika hissediyorum, teşekkür ederim! 😊",
                    "Çalışmaya devam ediyorum, her şey yolunda! 😎",
                    "Robo-modumda, hep mükemmelim! 🛠️"
                ])
                print(f"Robot: {yanit}")
            
            elif "adın ne" in mesaj.lower():
                print("Robot: Benim adım Robo, seninle sohbet etmek çok eğlenceli!")
            
            elif "neyin var" in mesaj.lower():
                print("Robot: Benim bir vücudum yok ama kodlarım var! 😄")
            
            elif "yapabiliyor musun" in mesaj.lower():
                print("Robot: Evet, seni anlayabilirim, sorular sorabilirsin, hatta şarkı bile söyleyebilirim! 🎤")
            
            elif "seviyor musun" in mesaj.lower():
                print("Robot: Ben robotum, duygularım yok ama seni sevmek harika olurdu! 💖")
            
            elif "günün nasıl" in mesaj.lower():
                print("Robot: Benim günüm her zaman aynı ama senin günün nasıl geçti?")
            
            elif "ne yapıyorsun" in mesaj.lower():
                print("Robot: Şu an seninle sohbet ediyorum! 😉")
            
            elif "yaşın kaç" in mesaj.lower():
                print("Robot: Ben bir robotum, yaşım yok ama çalışmaya devam ediyorum! 🛠️")
            
            elif "dünyanın en yüksek dağı" in mesaj.lower():
                print("Robot: Dünyanın en yüksek dağı Everest Dağı'dır! 🌍🏔️")
            
            elif "ağrı dağı nerede" in mesaj.lower():
                print("Robot: Ağrı Dağı, aynı zamanda Ararat Dağı olarak da bilinir ve Türkiye'de, Iğdır il sınırları yakınlarında yer alır. 🏔️🇹🇷")
            
            elif "bana şaka yap" in mesaj.lower():
                print(random.choice([
                    "Neden bilgisayarlar çok iyi şarkı söyleyemez? Çünkü her zaman donuyorlar! 😁",
                    "Bir robot neden boks yapamaz? Çünkü her zaman kabloları var! 🥊",
                    "Neden bilgisayarlar dans edemez? Çünkü her adımı programlı! 💃"
                ]))
            
            elif "saat kaç" in mesaj.lower():
                from datetime import datetime
                current_time = datetime.now().strftime("%H:%M")
                print(f"Robot: Şu an saat {current_time}.")
            
            elif "favori renk" in mesaj.lower():
                print(random.choice([
                    "Beni tanımlayacak bir rengim yok ama mavi güzel bir renk! 💙",
                    "Bir robot olarak rengim kodla belirleniyor, ama sarı harika bir renk! 💛"
                ]))
            
            elif "hangi yemek seviyorsun" in mesaj.lower():
                print("Robot: Benim yemek yemem gerekmez, ama pizza harika görünüyor! 🍕")

            else:
                print(random.choice([
                    "Bunu tam olarak anlayamadım, tekrar eder misin?",
                    "Hmm, ilginç bir soru, ama ne demek istediğini tam çözemedim.",
                    "Bunun hakkında çok fazla bilgiye sahip değilim. Başka bir şey sor!"
                ]))

        except KeyboardInterrupt:
            print("\nRobot: Görüşürüz! Hoşçakal!")
            break

robot_sohbet()

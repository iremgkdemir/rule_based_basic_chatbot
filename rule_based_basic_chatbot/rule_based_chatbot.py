import requests
import random
import re
import os  
import platform
import string  # Noktalama işaretlerini kaldırmak için gerekli
from datetime import datetime  # Tarih ve saat bilgisi için gerekli

class ChatBot:
    API_KEY = 'da8c497f530bea97455b28482b9df8db'  
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    exit_commands = ("çık", "kapat", "exit", "quit", "görüşürüz", "bye", "bb")
    
    # ChatBot sınıfının yapıcı metodu
    def __init__(self):
        # ChatBot'un desteklediği cevaplar ve karşılık gelen regex kalıpları
        # Sınıfın her örneği (nesne) kendi veri üyelerine sahip olabilir. Bu veri üyelerine sınıfın içindeki metodlardan erişmek için self kullanırız.
        self.support_responses = {
            'weather_info': r'\b(hava durumu|hava nasıl|bugün hava nasıl|manisa hava durumu|izmir hava durumu)\b',
            'date_time_info': r'\b(bugün günlerden ne|hangi gündeyiz|tarih nedir|saat kaç|tarih|saat|gün|günler)\b',
            'help': r'\b(yardım|neler yapabiliyorsun|ne yapabilirsin|yapabilirsin|hangi bilgileri verebilirsin|bilgi|bilgiler|yardımcı)\b',
            'chatbot_info': r'\b(merhaba|sen kimsin|kimsin sen| yaşın kaç|cinsiyetin ne|adın ne)\b',
            'chatbot_mood': r'\b(nasılsın|bugün nasılsın|nasıl|naber|naber chatbot|iyi misin|his)\b'
        }

        self.days_of_week = {
            "Monday": "Pazartesi",
            "Tuesday": "Salı",
            "Wednesday": "Çarşamba",
            "Thursday": "Perşembe",
            "Friday": "Cuma",
            "Saturday": "Cumartesi",
            "Sunday": "Pazar"
        }

    def greet(self):
        print("Chatbot'a hoş geldiniz! (Çıkmak için 'çık', 'kapat', 'exit' veya 'quit' yazabilirsiniz.)")
        self.chat() # Chat metodu çağrılır, kullanıcıdan giriş alınır ve cevaplar üretilir.

    # Kullanıcının çıkış yapmak isteyip istemediğini kontrol et
    def make_exit(self, reply):
        for command in self.exit_commands: 
            if command in reply:
                print("Chatbot: Görüşmek üzere!")
                return True
        return False
    def normalize_input(self, user_input):
        # Metni küçük harflere çevir
        user_input = user_input.lower()

        # kullanıcı girdisindeki noktalama işaretlerini çıkararak metnin daha sade ve daha kolay işlenebilir hale gelmesini sağlar
        user_input = user_input.translate(str.maketrans('', '', string.punctuation))

        # Yaygın yazım hatalarını düzelt
        corrections = {
            'hva': 'hava',
            'drmu': 'durumu',
            'bu gün': 'bugün',
            'gnd': 'gün',
            'tarh': 'tarih',
            'nbr': 'naber',
            'naslsn': 'nasılsın',
            'naslsnz': 'nasılsınız',
            'ii': 'iyi',
            'kpat': 'kapat',
            'görüşürz': 'görüşürüz',
            'olr': 'olur',
            'saol': 'sağ ol',
            's.a.': 'selamünaleyküm',
            'slm': 'selam',
            'mrb': 'merhaba',
            'nsl': 'nasıl',
            'tm': 'tamam',
            'akşm': 'akşam',
            'gnydn': 'günaydın',
            'bb': 'bye',
            'mrh': 'merhaba',
            'tsk': 'teşekkür',
            'tşk': 'teşekkür',
            'by': 'bye',
            'gorusuruz': 'görüşürüz',
            'kndm': 'kendim',
            'gidiyom': 'gidiyorum',
            'geliyom': 'geliyorum',
            'gelceğim': 'geleceğim',
            'bişey': 'bir şey',
            'yanlız': 'yalnız',
            'başlıyalım': 'başlayalım',
            'şuanki': 'şu anki',
            'herkez': 'herkes',
            'çünki': 'çünkü',
            'deil': 'değil',
            'hıc': 'hiç',
            'hic': 'hiç',
            'sevdim':'sevdim',
            'niye': 'neden',
            'niyeki': 'nedenki',
            'benimkisi':'benimki',
            'diycem':'diyeceğim',
            'iyimi':'iyi mi',
            'suan':'şu an',
            'baya':'bayağı'
        }

        # Bu döngü, tanımlanan tüm hatalı-doğru çiftlerini metin üzerinde uygular. 
        # re.sub() fonksiyonu, belirli bir desen (regex) ile eşleşen kısımları bulur ve onları belirtilen doğru karşılığıyla değiştirir. 
        # Burada kullanılan regex deseni (\b), sadece tam kelime eşleşmelerini bulur ve değiştirir.
        for wrong, correct in corrections.items():
            user_input = re.sub(r'\b' + wrong + r'\b', correct, user_input)
       
        # normalleştirilmiş metin döndürülür
        return user_input
    
    # Kullanıcı ile sürekli etkileşimde bulunan ana fonksiyon
    def chat(self):
        reply = input("Siz: ").lower()
        while not self.make_exit(reply):
            response = self.match_reply(reply) # Kullanıcının girişine göre cevap üret
            print(f"Chatbot: {response}")
            reply = input("Siz: ").lower()

    # Kullanıcının girişine göre uygun cevabı üret
    def match_reply(self, reply):
        # self.support_responses: ChatBot sınıfının başlatıcısında (constructor) tanımlanmış bir sözlüktür (dictionary). 
        # Bu sözlük, kullanıcıdan gelen mesajların hangi niyete (intent) karşılık geleceğini tanımlayan anahtar-değer çiftlerinden oluşur. 
        # Anahtarlar (intent), kullanıcı mesajlarının niyetini belirtirken, değerler (regex_pattern), bu mesajları yakalamak için kullanılan düzenli ifade (regex) kalıplarıdır.
        # self.support_responses.items(): Sözlüğün tüm anahtar-değer çiftlerini döngüyle işlememizi sağlar. Bu, her döngü adımında bir intent ve ona karşılık gelen bir regex_pattern verir.
        # intent: Bu, sözlükteki anahtar değeridir, örneğin "weather_info", "date_time_info" gibi.
        # regex_pattern: Bu, kullanıcı mesajının bu niyetle eşleşip eşleşmediğini kontrol etmek için kullanılan düzenli ifade kalıbıdır.
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply) #re.search():verilen metin içinde belirtilen kalıbı arar. Yoksa none döner.
            if found_match and intent == 'chatbot_info':
                return self.chatbot_info()
            elif found_match and intent == 'weather_info':
                return self.weather_info(reply)
            elif found_match and intent == 'date_time_info':
                return self.date_time_info()
            elif found_match and intent == 'help':
                return self.help()
            elif found_match and intent == 'chatbot_mood':
                return self.chatbot_mood_conversation()
        return self.no_match_intent()

    def chatbot_mood(self):
        responses = [
            "Teşekkür ederim, iyiyim! Sen nasılsın?",
            "Teşekkür ederim, bugün harika hissediyorum! Sen nasılsınko?",
        ]
        return random.choice(responses)
    
    def chatbot_mood_conversation(self):
        print("Chatbot: Teşekkür ederim, iyiyim! Sen nasılsın?")
        user_response = input("Siz: ").lower()

        if any(word in user_response for word in ["iyi", "iyiyim", "harika"]):
            return "Bunu duyduğuma sevindim! Size nasıl yardımcı olabilirim?"
        elif any(word in user_response for word in ["kötü", "kötüyüm", "mutsuz","üzgün","fena değilim"]):
            return "Üzgünüm bunu duyduğuma, bir şeyler yapmak ister misiniz? Belki biraz hava durumu bilgisi veya günün tarihi hakkında konuşabiliriz."
        else:
            return "Anlıyorum. Başka bir konuda yardımcı olabilir miyim?"

    def chatbot_info(self):
        responses = [
            "Herhangi bir cinsiyete / yaşa sahip olmayan bir AI chatbot'um ve size yardımcı olmak için buradayım.",
        ]
        return random.choice(responses)

    def weather_info(self, reply):
        # Şehir adı girdi içinde geçiyorsa doğrudan bilgiyi al
        city_match = re.search(r"\b(\w+)\s+hava durumu\b", reply)
        if city_match:
            city_name = city_match.group(1)
            return self.get_weather(city_name)
        else:
            # Şehir adı belirtilmediyse kullanıcıdan şehir adı iste
            city_name = input("Hangi şehrin hava durumu bilgisini almak istersiniz? ")
            return self.get_weather(city_name)

    def date_time_info(self):
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        weekday = self.days_of_week[datetime.now().strftime("%A")]
        return f"Bugün {weekday}, şu anki tarih ve saat: {current_time}."

    def help(self):
        responses = [
            "Size çeşitli bilgiler sağlayabilirim. Hava durumu, tarih gibi konularda sorular sorabilirsiniz.",
            "Benimle sohbet edebilir ve basit sorular sorabilirsiniz. Hava durumu, tarih gibi konularda sorular sorabilirsiniz. Elimden geleni yaparım!"     
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "Üzgünüm, bunu tam olarak anlayamadım. Başka bir şey sormak ister misiniz?",
            "Bu konuda bilgiye sahip değilim, ama başka bir şey hakkında konuşabiliriz!",
            "Tam olarak ne demek istediğinizi anlamadım, lütfen farklı bir şekilde sorar mısınız?"
        ]
        return random.choice(responses)

    def get_weather(self, city_name):
        complete_url = f"{self.BASE_URL}q={city_name}&appid={self.API_KEY}&units=metric&lang=tr"
        response = requests.get(complete_url)    # requests kütüphanesinin get metodu, belirtilen URL'ye bir HTTP GET isteği gönderir. Bu istek, API'den hava durumu verilerini almak için kullanılır.

        try:
            data = response.json()  # response.json(): HTTP yanıtını JSON formatına dönüştürür.
        except ValueError:
            return "Hava durumu bilgisi alınamadı, lütfen daha sonra tekrar deneyin."

        if data["cod"] != "404":
            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"{city_name} için hava durumu: Hava {temperature} derece ve {weather_desc}."
        else:
            return "Şehir bulunamadı, lütfen geçerli bir şehir adı girin."

    def clear_terminal(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

# Chatbot'u çalıştır
bot = ChatBot()
bot.greet()

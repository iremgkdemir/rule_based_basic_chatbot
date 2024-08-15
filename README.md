readme_content = """
# ChatBot

Bu proje, Python programlama dili kullanılarak geliştirilmiş basit bir chatbot uygulamasıdır. Chatbot, kullanıcıların hava durumu, tarih/saat bilgileri gibi sorularına cevap verir ve çeşitli sohbet işlevlerini yerine getirir. Kullanıcı girdilerini normalleştirerek daha doğru cevaplar üretebilir ve yaygın yazım hatalarını düzeltebilir.

## Özellikler

- **Hava Durumu Bilgisi**: Belirtilen şehir için güncel hava durumu bilgisini sağlar.
- **Tarih/Saat Bilgisi**: Günün tarihini ve saatini verir.
- **ChatBot Bilgisi**: Chatbot hakkında genel bilgiler sunar.
- **ChatBot Ruh Hali**: Chatbot'un ruh hali hakkında sorular sorabilir ve kullanıcı ile kısa sohbetler gerçekleştirebilirsiniz.
- **Yardım**: Chatbot'un neler yapabileceği konusunda bilgi verir.

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın:

    ```bash
    git clone https://github.com/kullaniciadi/projeadi.git
    ```

2. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install requests
    ```

3. API anahtarını ve şehir adlarını `ChatBot` sınıfının `API_KEY` değişkenine yerleştirin.

4. Chatbot'u çalıştırmak için terminale şu komutu yazın:

    ```bash
    python chatbot.py
    ```

## Kullanım

- Chatbot'u başlattığınızda, kullanıcı girdisini bekler. Hava durumu, tarih/saat bilgisi veya chatbot hakkında sorular sorabilirsiniz.
- Chatbot'a `çık`, `kapat`, `exit`, `quit`, `görüşürüz`, `bye`, `bb` gibi komutlarla veda edebilirsiniz.

## NLP ve Kural Tabanlı Chatbot Farkı

### Kural Tabanlı Chatbotlar

Kural tabanlı chatbotlar, belirli bir dizi kural ve koşula dayalı olarak çalışır. Kullanıcı girişlerine önceden tanımlanmış desenlere (regex) veya ifadelere göre yanıt verirler. Bu tür chatbotlar, belirli bir görev için özelleştirilmiş olabilir ancak esneklikleri sınırlıdır. Kural tabanlı chatbotların en büyük avantajı, belirli ve dar alanlarda çok doğru yanıtlar verebilmeleridir. Ancak, karmaşık veya çok çeşitli konularla başa çıkmakta zorlanırlar.

### NLP (Doğal Dil İşleme) Tabanlı Chatbotlar

NLP tabanlı chatbotlar, kullanıcı girdilerini anlamak için doğal dil işleme tekniklerini kullanır. Bu chatbotlar, makine öğrenimi ve derin öğrenme algoritmaları kullanarak metinleri analiz eder ve anlamaya çalışır. NLP tabanlı chatbotlar, kullanıcı girdilerini anlamada daha esnek ve güçlüdür, çünkü önceden tanımlanmış kalıplara değil, anlamına odaklanırlar. Bu sayede çok daha geniş bir konu yelpazesinde etkili olabilirler. Ancak, eğitim verisi gereksinimi ve daha yüksek işlem gücü gibi zorluklar içerirler.

### Sonuç

Kural tabanlı chatbotlar belirli ve dar alanlarda etkili olabilirken, NLP tabanlı chatbotlar daha geniş ve karmaşık alanlarda esneklik sunar. Bu projede yer alan chatbot kural tabanlı bir chatbot olup, belirli regex desenleri üzerinden çalışmaktadır.
"""

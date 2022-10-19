import speech_recognition as sr
import pyttsx3
import time
from termcolor import colored

r = sr.Recognizer()

mic = sr.Microphone()

engine = pyttsx3.init()

#micList = sr.Microphone.list_microphone_names()

#seslerden gelen cevap ve dönüşüm örnekleri
'''
5
text tipi
<class 'str'>
Sağ
sol
Evet
Hayır
'''
def yildizUcgenYazdir():

    sleepTime=0.5
    
    #----------------------SAYI SORU OKUMA----------------------
    
    print(colored("kaç yıldızlı üçgen basalım? ",'blue'))
    soruOku = "kaç yıldızlı üçgen basalım?"
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    #bilgisayardan bilgisayara değişiklik gösterebilir 1 idsi bende tr dili okunuşu, deneyerek veya voice yazdırarak kendi tr idinizi bulabilirsiniz
    #veya başka dillerde okuma sağlayabilirsiniz
    engine.say(soruOku)
    engine.runAndWait()
    time.sleep(sleepTime)
    
    #----------------------YILDIZ SAYI MİKROFONU----------------------
    
    with mic as source:
        print("Dinliyorum")
        audio = r.listen(source,timeout=2, phrase_time_limit=5)
        
        try:
            yildizSayi_str = r.recognize_google(audio,language='tr-tr')
            print("cevabınız: "+yildizSayi_str)
            
        except sr.WaitTimeoutError:
            print("Sayı için Dinleme zaman aşımına uğradı")

        except sr.UnknownValueError:
            print("Sayı için Ne dediğini anlayamadım")

        except sr.RequestError:
            print("Sayı için İnternete bağlanamıyorum")
    
    #----------------------SAĞ SOL SORU OKUMA----------------------
    print(colored("Sağa mı yaslı olsun yoksa sola mı? ",'blue'))
    soruOku2 = "Sağa mı yaslı olsun yoksa sola mı?"
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(soruOku2)
    engine.runAndWait()
    time.sleep(sleepTime)

    #----------------------SAĞ SOL MİKROFONU----------------------

    with mic as source:
        print("Dinliyorum")
        audio = r.listen(source,timeout=2, phrase_time_limit=5)
        
        try:
            kullaniciCevap = r.recognize_google(audio,language='tr-tr')
            print("cevabınız: "+kullaniciCevap)
            
        except sr.WaitTimeoutError:
            print("Sağ-sol için Dinleme zaman aşımına uğradı")

        except sr.UnknownValueError:
            print("Sağ-sol için Ne dediğini anlayamadım")

        except sr.RequestError:
            print("Sağ-sol için İnternete bağlanamıyorum")    

    #----------------------TİP DÖNÜŞÜMÜ SAĞA SOLA YASLAMAK İÇİN----------------------

    yildizSayi=int(yildizSayi_str)

    #----------------------ÜÇGEN SAĞ SOL YASLAMA----------------------

    def sagaYasliUcgen():
        for i in range(yildizSayi):
            for j in range(i,yildizSayi):
                print(" ",end=" ")
            for j in range(i+1):
                print(colored('*','green'),end=' ')
            print('\r')

    def solaYasliUcgen():
        for i in range(yildizSayi):
            for j in range(i+1):
                print(colored('*','green'),end=' ')
            print('\r')

    #----------------------KULLANICIDAN ALINAN CEVAP SAĞ SOL----------------------

    if kullaniciCevap == 'Sağ':
        sagaYasliUcgen()
    elif kullaniciCevap== 'sol':
        solaYasliUcgen()
    else:
        print("Hatalı giriş sağ - sol sıkıntısı")
    
    #----------------------PROGRAM TEKRAR----------------------

    print(colored("Tekrar denemek ister misiniz?",'blue'))
    soruOku3 = "Tekrar denemek ister misiniz?"
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(soruOku3)
    engine.runAndWait()
    time.sleep(sleepTime)

    #----------------------PROGRAM TEKRAR MİKROFONU----------------------

    with mic as source:
        print("Dinliyorum")
        audio = r.listen(source,timeout=2, phrase_time_limit=5)
        
        try:
            restart = r.recognize_google(audio,language='tr-tr')
            print("cevabınız: "+restart)
        except sr.WaitTimeoutError:
            print("evet-hayır için Dinleme zaman aşımına uğradı")

        except sr.UnknownValueError:
            print("evet-hayır için Ne dediğini anlayamadım")

        except sr.RequestError:
            print("evet-hayır İnternete bağlanamıyorum")
    
    #----------------------PROGRAM TEKRAR CEVABI----------------------

    if restart == "Evet" or restart == "evet" or restart=="e" or restart=="E" or restart=="Y" or restart=="y" or restart=="Ye" or restart=="ye" or restart=="Yes" or restart=="yes" or restart=="nevet" or restart=="Nevet":
        yildizUcgenYazdir()
    if restart == "Hayır" or restart == "hayır" or restart=="h" or restart=="H" or restart=="N" or restart=="n" or restart=="Ne" or restart=="ne" or restart=="No" or restart=="no" or restart=="nayır" or restart=="Nayır":
        print(colored("Program durduruldu Kaçaooovvv",'red'))
        soruOku2 = "Program durduruldu Kaçaooovvv"
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.say(soruOku2)
        engine.runAndWait()
        time.sleep(sleepTime)

#----------------------ANA FONKSİYON----------------------
yildizUcgenYazdir()
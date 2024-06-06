# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:07:33 2021

@author: erdal
"""

!pip install rake-nltk

#%% 

from rake_nltk import Rake
import nltk; nltk.download('stopwords')

#%%


r = Rake()

r.extract_keywords_from_text("Yüksek kaliteli ses alternatifleri ile self servis müşteri hizmetlerini iyileştiren Konuşma Sentezi teknolojisi, otomasyonu artırarak müşteri temsilcilerinin iş yükünü hafifletir. Dinamik içerikleri bile seslendiren yapısı sayesinde otomasyonu artıran teknoloji, tüm diyalogları otomatik olarak seslendirerek stüdyo kayıtlarına duyulan ihtiyacı ortadan kaldırır, zaman ve para tasarrufu sağlar. Yüksek kaliteli ses alternatifleri ile müşterilerin ilgisini çekerek doğal ve kişisel bir etkileşime olanak tanır. Kullanıcıların çeşitli kanallarda tanıdıkları ve güvendikleri bir ses ile karşılanması işletmeye olan bağlılıklarının artmasına katkıda bulunur. Bir dili nasıl konuşulduğunu duymadan ve pratik yapmadan öğrenmek neredeyse olanaksızdır. Konuşma Sentezi teknolojisi, dil eğitiminde hemen her dildeki çeşitli kelimeleri seslendirerek telaffuz gelişimine katkıda bulunur.")
#%%
print(r.get_word_frequency_distribution())
print("*******************************************************\n\n")
print(r.get_ranked_phrases_with_scores())

#%%
import pandas as pd
import nltk
import re
nltk.download('stopwords')
# %%
df = pd.read_csv("reviews.csv", encoding='UTF8', sep="\t")

df.head(10)
# %%
df.iloc[[1]]


df.tail(3)
df['text_lower']  = df['review'].str.lower()
df['text_lower'].head()
df['text_punct'] = df['review'].str.replace('[^\w\s]','')
df['text_punct'].head()


# %%
from nltk.corpus import stopwords



STOPWORDS = set(stopwords.words('russian'))


def stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

df["text_stop"] = df["text_punct"].apply(stopwords)
df["text_stop"].head()

# %%

#Удаление высокочастотных слов
from collections import Counter
cnt = Counter()
for text in df["text_stop"].values:
    for word in text.split():
        cnt[word] += 1
        
cnt.most_common(10)
# %%

#ужаление часто встречающиеся слов в корпусе при помощи tf-idf
# Удаление самых частотных слов
freq = set([w for (w, wc) in cnt.most_common(10)])
# функция удаления слов
def freqwords(text):
    return " ".join([word for word in str(text).split() if word not 
in freq])
# применение функции
df["text_common"] = df["text_stop"].apply(freqwords)
df["text_common"].head()
# %%

#Удаление низкочастотных слов
freq = pd.Series(' '.join(df['text_common']).split()).value_counts()[-10:] # 10 rare words
freq = list(freq.index)
df['text_rare'] = df['text_common'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
df['text_rare'].head()
# %%

# Удаление эмодзи
def emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
#passing the emoji function to 'text_rare'
df['text_rare'] = df['text_rare'].apply(emoji)
# %%

#Удаление цифр
df['text_nonum'] = df['text_common'].str.replace('\d+', '') 
df['text_nonum'].head()
# %%

#Удаление URL
# Function for url's
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)
# Examples
text = "This is my website, https://www.link.com"
remove_urls(text)
#Passing the function to 'text_rare'
df['text_rare'] = df['text_rare'].apply(remove_urls)
# %%

#Удаление HTML-тегов
from bs4 import BeautifulSoup
#Function for removing html
def html(text):
    return BeautifulSoup(text, "lxml").text
# Examples
text = """<div>
<h1> Это </h1>
<p> странца</p>
<a href="https://www.link.com/"> пример</a>
</div>
"""
print(html(text))
# Passing the function to 'text_rare'
df['text_rare'] = df['text_rare'].apply(html)
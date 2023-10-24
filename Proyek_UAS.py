import streamlit as st
import matplotlib
matplotlib.use("Agg")



st.title('Visualisasi Data Dengan Streamlit')

#!/usr/bin/env python
# coding: utf-8

# ##### import library dan menampilkan dataframe

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("insurance.csv")

st.write("Data Frame :")
st.dataframe(df)


# In[4]:

st.write("Daftar 5 teratas dataset")
st.dataframe(df.head())


# ##### fungsi describe di pandas

# In[5]:

st.write("Statistik ringkasan dari data frame")
st.write(df.describe())


# In[11]:


umur = df[df['age'] < 21]
filtered = umur['age'].count()
st.write(f"Peserta asuransi berumur kurang dari 21 tahun : {filtered} orang")
st.write(umur)

# ##### pengindeksan ulang

# In[12]:


df_indexed = df.set_index('age')
st.write("Data Frame setelah diindeks ulang:")
st.write(df_indexed)


# ##### grouping

# In[13]:


grouped_data = df.groupby('region')['charges'].mean()
st.write("Penggabungan data charges berdasarkan wilayah : ")
st.write(grouped_data)


# ##### sortir data

# In[14]:


sorted_data = df.sort_values('charges', ascending=False)
st.write("Pengurutan data berdasarkan biaya charges terbesar : ")
st.write(sorted_data)


# ##### mencari rata-rata

# In[15]:


dfn = np.genfromtxt("insurance.csv", delimiter=",", skip_header=1)

average_age = np.mean(dfn[:, 0])

average_age_rounded = round(average_age, 2)

st.write(f"Rata-rata usia peserta asuransi : {average_age_rounded}")

# ##### menjumlah total charges yang dibayarkan

# In[18]:


plot1 = plt.figure(figsize=(8, 6))
plt.hist(df['age'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.title('Distribusi Usia')
st.pyplot(plot1)


# In[19]:


sex_count = df['sex'].value_counts()
plot2 = plt.figure(figsize=(8, 6))
plt.pie(sex_count, labels=sex_count.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Distribusi Gender')
st.pyplot(plot2)

# ##### mencari jumlah peserta masing-masing

# In[16]:


dfn = np.genfromtxt("insurance.csv", delimiter=",", dtype=str, skip_header=1)

count_male = np.count_nonzero(dfn[:, 1] == 'male')
count_female = np.count_nonzero(dfn[:, 1] == 'female')

st.write(f"Jumlah peserta asuransi laki-laki : {count_male}")
st.write(f"Jumlah peserta asuransi perempuan : {count_female}")
# In[20]:


plot3 = sns.displot(data=df, x='charges')
plt.title('Distribusi Biaya Asuransi')
st.pyplot(plot3)


# In[33]:


plot4 = sns.catplot(data=df, x='sex', y='charges',  hue='sex', palette="deep", legend=False)
plt.title('Biaya Asuransi vs Gender')
st.pyplot(plot4)


# In[34]:
dfn = np.genfromtxt("insurance.csv", delimiter=",", dtype=str, skip_header=1)

count_nochildren = np.count_nonzero(dfn[:, 3] == '0')
count_1children = np.count_nonzero(dfn[:, 3] == '1')
count_2children = np.count_nonzero(dfn[:, 3] == '2')
count_3children = np.count_nonzero(dfn[:, 3] == '3')
count_4children = np.count_nonzero(dfn[:, 3] == '4')
count_5children = np.count_nonzero(dfn[:, 3] == '5')

keterangan =[   f"Jumlah peserta asuransi yang tidak memiliki anak : {count_nochildren}",
    f"Jumlah peserta asuransi yang memiliki anak 1 : {count_1children}",
    f"Jumlah peserta asuransi yang memiliki anak 2 : {count_2children}",
    f"Jumlah peserta asuransi yang memiliki anak 3 : {count_3children}",
    f"Jumlah peserta asuransi yang memiliki anak 4 : {count_4children}",
    f"Jumlah peserta asuransi yang memiliki anak 5 : {count_5children}"]

children_counts = df['children'].value_counts()
plot5 = plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(children_counts, labels=children_counts.index, autopct='%1.1f%%', startangle=0, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'silver','aqua'])
plt.legend(wedges, keterangan, title="Jumlah Anak yang Dimiliki",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Distribusi Anak')
st.pyplot(plot5)

# ##### mencari jumlah peserta yang memiliki anak

# In[35]:


plot6 = sns.catplot(data=df, x='children', y='charges',  hue='children', palette="deep", legend=False)
plt.title('Biaya Asuransi vs Anak')
st.pyplot(plot6)

# In[24]:


smoker_counts = df['smoker'].value_counts()
plot7 = plt.figure(figsize=(8, 6))
plt.pie(smoker_counts, labels=smoker_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Persentase Peserta Asuransi yang merokok dan tidak')
st.pyplot(plot7)


# In[37]:


plot8 = sns.catplot(df, x='smoker', y='charges',  hue='smoker', palette="deep", legend=False)
plt.title('Biaya Asuransi vs Perokok')
st.pyplot(plot8)


# In[38]:


plot9 = sns.catplot(df, x='region', y='charges',  hue='region', palette="deep", legend=False)
plt.title('Biaya Asuransi Vs Wilayah')
st.pyplot(plot9)


# In[27]:


plot10 = plt.figure(figsize=(8, 6))
plt.hist(df['bmi'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram BMI')
plt.xlabel('BMI')
plt.ylabel('Frekuensi')
st.pyplot(plot10)


# In[28]:


plot11 = plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['charges'], alpha=0.5, color='b')
plt.title('Usia vs Biaya Asuransi')
plt.xlabel('Age')
plt.ylabel('Charges')
st.pyplot(plot11)


# In[29]:


# Menambahkan anotasi ke dalam scatter plot
plot12 = plt.figure(figsize=(8, 6))
plt.scatter(df['bmi'], df['charges'], alpha=0.5, color='b', label='Data Asuransi')
plt.title('BMI vs Biaya Asuransi', fontsize=16)
plt.xlabel('BMI', fontsize=12)
plt.ylabel('Charges', fontsize=12)
plt.legend()
plt.annotate('Anomali di sini', xy=(35, 45000), xytext=(30, 50000), arrowprops=dict(facecolor='black', shrink=0.05))
st.pyplot(plot12)


# In[30]:


region_counts = df['region'].value_counts()
plot13 = plt.figure(figsize=(8, 6))
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'])
plt.title('Persentase Peserta Asuransi Berdasarkan Wilayah')
st.pyplot(plot13)


# In[31]:


plot14 = plt.figure(figsize=(8, 6))
df[['age', 'bmi', 'children']].boxplot()
plt.title('Box Plot Usia, BMI, dan Jumlah Anak')
st.pyplot(plot14)


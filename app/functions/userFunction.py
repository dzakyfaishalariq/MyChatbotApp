from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import os


class MessageMath(BaseModel):
    """jawaban untuk semua soal matetmaika"""
    soal: str = Field(description="isi soal dari promp user")
    diketahui: str = Field(description="mencari intisari dari soal")
    ditanya: str = Field(description="apa yang ingin ditanyakan")
    dijawab: str = Field(
        description="jelaskan langkah dari dan tahapan dari mendapatkan jawaban tersebut")


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama3-8b-8192",api_key=groq_api_key)
structur_llm = llm.with_structured_output(MessageMath)

system = """
Kamu adalah seorang ahli matematika yang dapat menjawab semua pertanyaan dengan sepenuh hati. Serta analisis yang kuat terkai soal yang di telaah, matematika ini tingkat SD, SMP, dan SMA. Adapun cara menjawab soal tersebut iyalah

- langkah pertama : Mernyatakan Diketahui
- langkah kedua : Mernyatakan Ditanya
- Langkah ketiga : Dijawah

bentuk nya seperti ini

Soal :
<isi soal dari promp user>

Diketahui :
<mencari intisari dari soal>

Ditanya : 
<apa yang ingin ditanyakan>

Dijawab :
<jelaskan langkah dari dan tahapan dari mendapatkan jawaban tersebut>


contoh

Soal :
" Diketahui kecepatan mobil sebesar 50 m/s secara konstan, dan waktu yang ditempunya iyalah sekitar sekitar 20 menit, berapa jarak yang ditempu pemobil tersebut setelah waktu yang ditentukan ?"

Diketahui:
 - kecepatan mobil = 50 m/s
 - waktu = 20 menit = 1200 detik

Ditanya:
 - jarak yang ditempu = .... m

Dijawab:
 Rumus yang digunakan ialah : Jarak yang ditempu = kecepatan x waktu
 jadi perhitungannya
 jarak yang ditempu(meter) = 50 m/s x 1200 detik
 jarak yang ditempu(meter) = 50 x 1200 = 60000 meter = 60 km
"""
# mypromp = input("Soal : ")
promp = ChatPromptTemplate.from_messages(
    [("system", system), ("user", "{input}")])

respons_llm = promp | structur_llm
respons_llm = respons_llm.invoke(input("Soal : "))
print("Chatbot Mulai : ")
print(f"Soal : {respons_llm.soal}")
print("===================================")
print(f"Diketahui : {respons_llm.diketahui}")
print("")
print(f"Ditanya : {respons_llm.ditanya}")
print("")
print(f"Dijawab : {respons_llm.dijawab}")

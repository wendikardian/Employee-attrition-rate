# Business Understanding

## Latar Belakang 

### Latar Belakang Masalah

Perusahaan **Jaya Jaya Maju** menghadapi tantangan dalam mempertahankan karyawan akibat tingkat keluar karyawan (*attrition rate*) yang tinggi. Masalah ini berdampak pada produktivitas, biaya rekrutmen, dan stabilitas organisasi. Beberapa faktor seperti gaji rendah, beban kerja tinggi akibat lembur, dan kurangnya keseimbangan kerja-hidup (work-life balance) menjadi penyebab utama. Selain itu, karyawan muda dengan pengalaman singkat lebih rentan untuk keluar, sementara pendidikan yang lebih tinggi berkorelasi dengan retensi yang lebih baik. Analisis mendalam diperlukan untuk memahami penyebab dan merancang strategi mitigasi yang efektif.

## Tujuan Utama
Mengidentifikasi faktor-faktor yang memengaruhi tingkat keluar karyawan (attrition rate) di perusahaan **Jaya Jaya Maju**. Langkah-langkah:
1. **Permasalahan Bisnis**:
   - Mengapa karyawan keluar? (misalnya: kepuasan kerja, gaji, perjalanan bisnis).
   - Apa faktor signifikan yang memengaruhi attrition?
   - Bagaimana cara memprediksi karyawan berisiko keluar?
   - Bagaimana monitoring faktor ini secara real-time?

2. **Cakupan Proyek**:
   - Mengembangkan model prediksi untuk mengetahui potensi karyawan keluar.
   - Mengidentifikasi fitur penting untuk pengambilan keputusan HR.
   - Menyediakan dashboard interaktif untuk analisis data real-time.

---

## Persiapan Data
- **Sumber Data**: [Dataset Employee Attrition](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).
- **Struktur Data**:
  - 35 kolom, 1.470 baris data.
  - Kolom utama: 
    - `Attrition` (target variabel): 1 = attrition terjadi, 0 = tidak terjadi.
    - Fitur penting:
      - **Lingkungan Kerja**: `EnvironmentSatisfaction`, `WorkLifeBalance`.
      - **Kompensasi**: `MonthlyIncome`, `PercentSalaryHike`.
      - **Keseimbangan Hidup**: `OverTime`, `BusinessTravel`.
      - **Pengalaman**: `YearsAtCompany`, `TotalWorkingYears`.
      
- **Tugas Awal**:
  1. Visualisasi distribusi target (`Attrition`) untuk melihat rasio distribusi.
  2. Analisis korelasi antar fitur numerik (misalnya: gaji dengan kepuasan kerja).
  3. Analisis fitur kategorikal (seperti `JobRole`, `Department`) menggunakan diagram batang atau pie chart.

---

## Setup Environment

Untuk mempersiapkan lingkungan kerja Anda, gunakan perintah berikut:
### Langkah installasi

```bash
pip install -r requirements.txt
pip list
```


### Langkah Menjalankan Skrip
Gunakan perintah berikut di terminal:
```bash
python prediction.py
```
### Input data untuk melakukan prediction

- Jika menggunakan file CSV, pastikan file tersedia di direktori kerja dengan format yang sesuai.


## Dashboard Interaktif
[Akses Dashboard Tableau](https://public.tableau.com/app/profile/wendi.kardian/viz/DashboardAttritionEmployee-WendiKardian/Dashboard1)

![Wendi Kardian - Dashboard](https://github.com/user-attachments/assets/1315d761-4f71-442a-9320-63227fca8705)


### Temuan Utama
1. **Pendapatan vs. Attrition**: Karyawan berpendapatan rendah memiliki tingkat attrition tinggi.
2. **Distribusi Usia**: Karyawan muda (20-30 tahun) lebih sering mengalami attrition.
3. **Gender dan Attrition**: Perbedaan tingkat attrition berdasarkan gender sangat kecil.
4. **Pengaruh Lembur**: Tingkat attrition lebih tinggi pada karyawan yang sering lembur.
5. **Pendidikan dan Pendapatan**: Pendidikan lebih tinggi berkorelasi dengan pendapatan lebih tinggi, tingkat attrition lebih rendah.
6. **Peran Pekerjaan**: Beberapa peran memiliki tingkat attrition bervariasi, mencerminkan tantangan spesifik.

---

## Conclusion
Hasil analisis menunjukkan faktor utama yang memengaruhi attrition:
- Gaji rendah.
- Work-life balance yang buruk akibat lembur.
- Usia muda dengan pengalaman kerja singkat.
- Pendidikan tinggi berkorelasi dengan retensi lebih baik.

### Rekomendasi Action Items
1. Benchmark gaji terhadap pasar untuk meningkatkan daya saing.
2. Kurangi lembur dengan optimasi alur kerja dan sumber daya.
3. Buat pelatihan & mentoring khusus bagi karyawan muda dan kurang berpengalaman.
4. Tawarkan insentif seperti bonus kinerja, penghargaan, atau kerja fleksibel.
5. Selenggarakan survei & sesi feedback rutin.
6. Berikan program sertifikasi/pelatihan bagi karyawan berpendidikan rendah.

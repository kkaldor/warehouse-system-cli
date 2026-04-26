**Advanced Warehouse Management System (WMS) berbasis Python CLI**

Sistem ini adalah implementasi Warehouse Management System (WMS) versi lightweight yang dirancang menggunakan arsitektur terstruktur dan pola command-line modern.
Walaupun berjalan di CLI, sistem ini mengadopsi konsep **operasional gudang nyata**, termasuk:

* Item Master
* Location Hierarchy (Warehouse → Rack → Aisle → Bin)
* Stock Per Location
* Stock In / Stock Out
* Safety Stock Awareness

Tujuan utama proyek ini adalah memberikan **simulasi WMS tingkat menengah**, yang mudah dipahami pemula tetapi tetap memiliki struktur profesional seperti sistem enterprise.

---

# 🚀 Fitur Utama

### **1. Item Management**

* Membuat master item
* Menyimpan SKU, kategori, UOM, dan safety stock
* Menampilkan daftar item

### **2. Location Management**

* Membuat struktur lokasi gudang yang realistis
* Format lokasi: `Warehouse / Rack / Aisle / Bin`
* Menampilkan semua lokasi

### **3. Stock Management**

* Menambah stok masuk (Receiving / Putaway)
* Mengurangi stok (Picking / Consumption)
* Melihat seluruh stok global
* Melihat stok berdasarkan item
* Melihat stok berdasarkan lokasi

### **4. Arsitektur Modular**

Menggunakan layering:

```
CLI Layer → Service Layer → Repository Layer → JSON Storage
```

Struktur ini memudahkan scaling dan penambahan fitur baru.

---

# 🏗️ Arsitektur Proyek

```
warehouse_system/
│
├── cli/                 # Command & routing layer
│   ├── commands.py
│   ├── item_commands.py
│   ├── location_commands.py
│   └── stock_commands.py
│
├── core/                # Services / business logic
│   ├── item_service.py
│   ├── location_service.py
│   └── stock_service.py
│
├── models/              # Model domain
│   ├── item.py
│   ├── location.py
│   └── stock.py
│
├── repositories/        # JSON persistence layer
│   ├── item_repository.py
│   ├── location_repository.py
│   └── stock_repository.py
│
├── data/                # JSON datasets
│   ├── items.json
│   ├── locations.json
│   └── stocks.json
│
└── main.py              # Entry point CLI
```

Arsitektur ini meniru pola software enterprise agar pemula dapat belajar:

* separation of concerns
* clean code
* modular design
* scalability mindset

---

# 📘 Cara Menjalankan Sistem

### **1. Jalankan CLI**

```bash
python main.py <command> <subcommand>
```

---

# 🔧 Daftar Command Penting

## **Item**

```bash
python main.py item create
python main.py item list
python main.py item show <item_id>
```

## **Location**

```bash
python main.py location create
python main.py location list
```

## **Stock**

```bash
python main.py stock add
python main.py stock list
python main.py stock remove
python main.py stock by-item <item_id>
python main.py stock by-location <location_id>
```

Untuk dokumentasi lengkap, lihat:
📄 **COMMANDS.md**

---

# 📚 Contoh Workflow Gudang (Sederhana)

### **1. Tambah item master**

```bash
python main.py item create
```

### **2. Buat lokasi penyimpanan**

```bash
python main.py location create
```

### **3. Tambah stok barang**

```bash
python main.py stock add
```

### **4. Cek semua stok**

```bash
python main.py stock list
```

### **5. Cek stok berdasarkan item**

```bash
python main.py stock by-item <item_id>
```

---

# 🌟 Keunggulan Proyek Ini (Sangat Cocok untuk Pemula)

### ✔ **1. Menerapkan konsep sistem gudang nyata**

Pemula belajar:

* SKU
* stock movement
* safety stock
* lokasi berhirarki
* penerimaan barang
* penempatan barang

Ini adalah konsep dasar dunia logistik profesional.

---

### ✔ **2. Arsitektur bersih dan mudah dipahami**

Pemula sering kesulitan karena tutorial Python hanya fokus pada “CRUD sederhana”.

Proyek ini mengenalkan:

* layering (CLI → service → repository)
* model domain (item, location, stock)
* workflow operasional
* pemisahan logic bisnis & logic tampilan

---

### ✔ **3. Tidak bergantung pada database sulit**

Menggunakan JSON, sehingga pemula:

* tidak perlu SQL/MySQL/PostgreSQL
* tetap bisa mempelajari persistence layer
* bisa melakukan debugging dengan mudah

---

### ✔ **4. Bisa dikembangkan menjadi sistem besar**

Anda bisa menambahkan:

* Receiving
* Putaway
* Picking
* Transfer stock
* Cycle counting
* Batch/Lot management
* FIFO/LIFO logic

Modul baru dapat dimasukkan tanpa merombak sistem.

---

### ✔ **5. Cocok untuk portfolio teknis / interview**

Proyek ini menunjukkan bahwa Anda memahami:

* domain logistik
* desain software
* CLI application
* data modeling
* structured programming

Perekrut sangat menyukai proyek yang menggabungkan bisnis & engineering.

---

# 🚀 Rencana Pengembangan (Roadmap)

* Receiving module
* Putaway optimizer
* Picking system (FIFO)
* Stock transfer antar lokasi
* User/role authentication
* API REST (FastAPI)
* Dashboard analitik

---

# 🤝 Kontribusi

Pull request sangat diterima.
Silakan membuat issue untuk:

* bug report
* saran fitur
* peningkatan dokumentasi

---

# 📄 Lisensi

Proyek ini dapat menggunakan lisensi MIT, BSD, atau lisensi lain sesuai preferensi Anda.

---

Jika Anda ingin, saya bisa juga membuatkan:

### ✔ Versi README yang lebih visual

### ✔ README dengan badge (Python version, license, stars, workflow)

### ✔ README dengan diagram arsitektur (Mermaid)

### ✔ README versi bahasa Inggris untuk audience internasional

Cukup beri instruksi.

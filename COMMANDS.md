# COMMANDS.md
## Warehouse WMS CLI — Command Reference

Dokumen ini berisi daftar lengkap seluruh command yang tersedia dalam sistem Warehouse Management System (WMS) berbasis Python CLI.

## Struktur Command
Format dasar menjalankan CLI:

```
python main.py <command> <subcommand> [options]
```

## 1. Item Commands

### 1.1 Create Item
```
python main.py item create
```

### 1.2 List Items
```
python main.py item list
```

### 1.3 Show Item Detail (Opsional)
```
python main.py item show <item_id>
```

## 2. Location Commands

### 2.1 Create Location
```
python main.py location create
```

### 2.2 List Locations
```
python main.py location list
```

## 3. Stock Commands

### 3.1 Add Stock
```
python main.py stock add
```

### 3.2 List Stock
```
python main.py stock list
```

### 3.3 Remove Stock (Opsional)
```
python main.py stock remove
```

### 3.4 Stock By Item
```
python main.py stock by-item <item_id>
```

### 3.5 Stock By Location
```
python main.py stock by-location <location_id>
```

## Contoh Workflow Operasional

```
python main.py item create
python main.py location create
python main.py stock add
python main.py stock list
python main.py stock by-item <item_id>
python main.py stock by-location <location_id>
```

## Appendix

```
python main.py --help
python main.py item --help
python main.py stock --help
python main.py location --help
```

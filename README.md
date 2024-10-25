# 🦾 Programming IV (OOP) 🦾

## 🎉 Project: Second Exam - Entity Management System 🎉

This project serves as a creative and dynamic solution for the **Second Exam**, focusing on **Inheritance, Modularity, Encapsulation, Polymorphism, and Data Structures**. It includes three independent modules: 📚 **Book Management**, 🏨 **Hotel Reservations**, and 🛒 **Online Store Orders**. Each module showcases Object-Oriented Programming (OOP) principles and data structures to meet exam requirements.

---

## 📝 Table of Contents
1. [🌱 Requirements](#requirements)
2. [🔧 Installation](#installation)
3. [🚀 Execution](#execution)
4. [📂 Module Descriptions](#module-descriptions)
5. [💻 Usage](#usage)

---

## 🌱 Requirements
- **Python 3.8+**
- Additional libraries:
    - 📋 `tabulate` - for displaying data in table format
    - 📁 `json` - for managing JSON files

> [!NOTE]  
> Isolating dependencies with `venv` is highly recommended.

### ⚙️ Setting up with `venv`
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the environment:
    - **Linux/macOS**:
      ```bash
      source venv/bin/activate
      ```
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
3. Install required packages:
   ```bash
   pip install tabulate
   ```

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adriancho91s/second-exam-programming-IV.git
   cd second-exam-programming-IV
   ```
2. Follow the [Setting up with venv](#setting-up-with-venv) instructions to complete the setup.

> [!TIP]  
> Make sure to activate the virtual environment each time you work on the project!

## 🚀 Execution
Each module operates independently. Start each module using these commands:

```bash
# 📚 For Book Management
python point-1/main.py

# 🏨 For Hotel Reservations
python point-2/parcial_ii_programacion_iv.py

# 🛒 For Online Store Orders
python point-3/main.py
```

---

## 📂 Module Descriptions

### 📚 1. Book Management
This module lets users add and manage books in a JSON-based collection.
- **Entities**: `Book` (title, author, publication year, genre)
- **Features**:
    - Add books through console input.
    - Display all books in a well-organized table.
    - Save and load book data to/from a JSON file.

### 🏨 2. Hotel Reservations
The Hotel Reservations module allows users to handle rooms of various types and make reservations.
- **Classes**:
    - `Room` (base class)
    - `SimpleRoom`, `DoubleRoom`, `Suite` (derived classes)
- **Features**:
    - Display available rooms.
    - Reserve specific rooms.
    - Calculate total price, including extra services for Double and Suite rooms.

### 🛒 3. Online Store Order Management
This module allows product management and order placement for an online store.
- **Entities**:
    - `Product` (base class)
    - `Electronics`, `Clothing`, `Food` (derived classes)
- **Features**:
    - Display available products.
    - Place orders and adjust stock.
    - Calculate total with discounts on bulk purchases.
    - Save updated inventory in a JSON file.

---

## 💻 Usage

### 📚 Book Management
1. Add books by following console prompts.
2. Save books to `library.json`.
3. View all books in a table format.

### 🏨 Hotel Reservations
1. View available rooms.
2. Reserve rooms by selecting their room number.
3. Calculate total for Double or Suite rooms, including any extra services.

### 🛒 Online Store Orders
1. Display product catalog.
2. Place orders by specifying product and quantity.
3. Calculate the total with discounts for bulk purchases.
4. Save updated inventory in `productos.json`.

> [!IMPORTANT]  
> Remember to save all data after each session to prevent data loss.
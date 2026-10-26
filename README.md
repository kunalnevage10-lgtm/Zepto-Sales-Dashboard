# ⚡ Zepto Quick Commerce Sales & Product Analytics Dashboard

An interactive, dark-mode Data Visualization and Business Intelligence dashboard built with **Streamlit**, **Pandas**, and **Plotly**, styled according to **Zepto's** signature brand identity (Deep Purple & Vibrant Magenta/Pink).

![Zepto Dashboard Banner](https://img.shields.io/badge/Zepto-Quick%20Commerce-FF3269?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.20+-3F4F75?style=for-the-badge&logo=Plotly&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=Python&logoColor=white)

---

## 🌟 Key Features

- **🎨 Zepto Brand Identity (Dark Mode Theme)**:
  - Custom UI palette with Zepto's signature Deep Purple (`#0C0214`, `#160526`, `#1F0838`) and Vibrant Magenta / Neon Pink accents (`#FF3269`, `#FF007A`).
  - Glowing KPI cards, custom-styled tabs, interactive badges, and dark Plotly charts.

- **📊 High-Impact Executive KPIs**:
  - **Total Products / SKUs** with real-time category distribution.
  - **Average Original Price (MRP)** with normalized rupee conversions (from paise).
  - **Average Discount Percentage** with peak discount indicators.
  - **Stock In-Stock Rate** showcasing warehouse inventory depth.

- **📈 Core Visualizations**:
  - **Top 10 Product Categories by Volume**: Horizontal bar chart with dynamic toggle (*SKU Count*, *Available Inventory Units*, *Total Weight in kg*).
  - **Original Price (MRP) vs. Discounted Price (Scatter Plot)**: Compares MRP vs Selling Price against a reference $y = x$ (zero discount line), sizing points by discount percentage.
  - **Distribution of Discount Ranges (Donut Chart)**: Visualizes breakdown across *No Discount (0%)*, *Low (1-10%)*, *Moderate (11-20%)*, *High (21-35%)*, and *Super Saver (36%+)*.

- **🎯 Interactive Sidebar Controls**:
  - Full-text keyword product search.
  - Multi-select category filtering with quick *Select All* and *Clear All* actions.
  - Stock availability radio filters (*All*, *In Stock*, *Out of Stock*).
  - Dynamic dual-slider for MRP (₹) and Discount Percentage (%).
  - One-click *Reset Filters* mechanism.

- **🔬 In-Depth Analysis Tabs**:
  - **🏷️ Pricing & Deals Matrix**: Average category discounts, price distribution box plots, and a Top 10 *Super Savers* leaderboard.
  - **📦 Inventory & Stock Intelligence**: Out-of-stock category ratios and restock alerts.
  - **🔍 SKU Data Explorer**: Searchable and sortable catalog table with instant **CSV Export**.

---

## 📁 Repository Structure

```plaintext
Zepto-Sales-Dashboard/
├── .streamlit/
│   └── config.toml          # Custom dark mode brand theme configuration
├── app.py                   # Main Streamlit dashboard application
├── zepto_v2.csv             # Cleaned Zepto retail product catalog dataset
├── requirements.txt         # Production Python dependencies
├── .gitignore               # Ignored system and build files
└── README.md                # Project documentation and guide
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/<YOUR_USERNAME>/Zepto-Sales-Dashboard.git
cd Zepto-Sales-Dashboard
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard
```bash
streamlit run app.py
```
The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## 📊 Dataset Overview (`zepto_v2.csv`)

| Column Name | Description | Units / Format |
|---|---|---|
| `Category` | Retail department (e.g. Cooking Essentials, Munchies, Fruits & Vegetables) | String (14 unique categories) |
| `name` | Item / SKU Title | String (1,681 unique products) |
| `mrp` | Maximum Retail Price | Stored in **paise** (normalized to ₹ in app) |
| `discountPercent` | Applied discount percentage | Integer (0% - 51%) |
| `discountedSellingPrice`| Final checkout price | Stored in **paise** (normalized to ₹ in app) |
| `availableQuantity` | Active stock depth in warehouse | Units (0 to 6) |
| `weightInGms` | Package weight | Grams (g) |
| `outOfStock` | Warehouse inventory availability | Boolean (`True` / `False`) |
| `quantity` | Package unit count | Unit count / pack size |

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - Fast, interactive web app framework
- [Pandas](https://pandas.pydata.org/) - High-performance data manipulation
- [Plotly](https://plotly.com/python/) - Modern, interactive charting library
- [Matplotlib](https://matplotlib.org/) - Colormap engine for styled tabular gradients

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

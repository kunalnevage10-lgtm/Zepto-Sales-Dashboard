# ⚡ Zepto Quick Commerce Sales & Product Analytics Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Zepto-Dark%20Theme-0C0214?style=for-the-badge&logoColor=FF3269" alt="Zepto Theme" />
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Plotly-5.20+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

An enterprise-grade, dark-mode Business Intelligence (BI) and Data Visualization dashboard engineered with **Streamlit**, **Pandas**, and **Plotly**. Built around **Zepto's** signature brand identity (Deep Midnight Purple and Vibrant Magenta/Pink), this application delivers actionable quick-commerce intelligence—from real-time catalog pricing and discount spread analysis to warehouse inventory stock health.

---

## 🎯 Objective

In high-velocity quick-commerce retail, understanding pricing elasticities, catalog distribution, discount trends, and warehouse inventory depth is paramount for operational excellence. 

The primary objectives of this dashboard are:
- **Catalog Visibility**: Provide category managers and supply chain analysts with interactive exploratory data analysis (EDA) across 1,600+ product SKUs.
- **Pricing & Margin Intelligence**: Evaluate how Maximum Retail Price (MRP) correlates with final discounted selling prices to pinpoint aggressive loss-leaders and margin opportunities.
- **Inventory & Out-of-Stock Risk Mitigation**: Surface critical stock deficits, out-of-stock ratios per department, and automated restock alerts.
- **Executive Brand Presentation**: Deliver a seamless, branded dark-mode UI with intuitive controls, dynamic filtering, responsive charts, and instant catalog data export.

---

## ✨ Key Features

### 🎨 1. Zepto Signature Brand Theme
- **Bespoke Color Palette**: Designed strictly according to Zepto's visual identity using Deep Midnight Purple (`#0C0214`, `#160526`), Rich Card Accents (`#1F0838`), and High-Energy Magenta/Pink (`#FF3269`, `#FF007A`).
- **Modern Glassmorphic UI**: Gradient stat badges, translucent glowing KPI containers, clean divider lines, and custom-styled sidebar widgets.
- **Synchronized Visuals**: All Plotly figures are automatically injected with consistent typography, custom hover templates, transparent backgrounds, and neon gridlines.

### 📌 2. Top Executive KPI Cards
At the top of the dashboard, high-level business metrics give an instantaneous pulse check of catalog health:
- **📦 Total SKUs / Products**: Total active catalog volume matching user filters.
- **🏷️ Average Original Price (MRP)**: Converted and normalized to Rupees (`₹`) from paise.
- **🔥 Average Discount Percentage**: Catalog-wide discount rate with highlight badges for maximum discount items.
- **🟢 In-Stock Availability Rate**: Percentage of catalog items currently available for immediate order dispatch.

### 📊 3. Core Visualizations & Analytics Tabs
The dashboard organizes multidimensional analytics into four specialized, interactive tabs:

#### 1️⃣ Tab 1: 📊 Core Visualizations
- **Top 10 Product Categories by Volume**: Interactive horizontal bar chart with a dynamic metric switcher:
  - *Product (SKU) Count*
  - *Available Inventory Stock Units*
  - *Total Weight Volume (kg)*
- **Distribution of Discount Ranges**: Donut chart detailing consumer deal buckets (*No Discount 0%*, *Low 1–10%*, *Moderate 11–20%*, *High 21–35%*, and *Super Saver 36%+*).
- **Original Price (MRP) vs. Discounted Price (Scatter Plot)**: Compares MRP against final Selling Price, sizing nodes by discount percentage, categorized by product department, and overlaying a reference $y = x$ (zero discount parity line).

#### 2️⃣ Tab 2: 🏷️ Pricing & Deals Matrix
- **Category-wise Discount Comparison**: Identifies which retail departments offer the steepest markdowns.
- **Price Spread & Distribution Box Plots**: Visualizes median price, variance, and outlier premiums across categories.
- **Top 10 Super Savers Leaderboard**: Filterable table highlighting the most heavily discounted items for tactical promotions.

#### 3️⃣ Tab 3: 📦 Inventory & Stock Intelligence
- **Stock Depletion Analysis**: Stacked bar charts showing the proportion of In-Stock vs. Out-of-Stock items by category.
- **Warehouse Unit Depth**: Stock level histogram identifying single-item inventory risks.
- **Critical Restock Alert Table**: Immediate tabular view of zero-stock items requiring replenishment.

#### 4️⃣ Tab 4: 🔍 SKU Data Explorer
- **Interactive Data Table**: Searchable, sortable view of all filtered SKU records.
- **One-Click CSV Export**: Instant export button to download the currently filtered dataset for offline reporting and spreadsheet workflows.

### 🎛️ 4. Advanced Sidebar Controls & Multi-Filters
- **Instant Keyword Search**: Real-time substring matching across product names.
- **Category Multi-Select**: Seamless department filtering with convenient `Select All` and `Clear All` quick-action buttons.
- **Stock Availability Filter**: Toggle between *All*, *In Stock*, or *Out of Stock* products.
- **Dual-Slider Range Filters**:
  - MRP Range Slider (`₹0` to `₹Max`)
  - Discount Range Slider (`0%` to `100%`)
- **One-Click Reset**: Resets all filters back to default catalog settings in a single action.

---

## 🛠️ Tech Stack Used

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend Framework** | [Streamlit](https://streamlit.io/) (v1.40+) | Interactive web dashboard framework and reactive component state |
| **Data Processing** | [Pandas](https://pandas.pydata.org/) (v2.0+) | Data cleaning, type transformations, missing-value imputation, aggregation |
| **Numeric Computing** | [NumPy](https://numpy.org/) | Vectorized price conversions and numerical binning |
| **Interactive Charting** | [Plotly](https://plotly.com/python/) (v5.20+) | GPU-accelerated interactive charts (Bar, Donut, Scatter, Box Plots) |
| **Data Visualization & Color** | [Matplotlib](https://matplotlib.org/) | Colormap engine for gradient table styling |
| **Language & Runtime** | [Python](https://www.python.org/) (v3.11+) | Core programming language |
| **Styling & Design** | HTML5, CSS3, Plus Jakarta Sans | Custom Zepto brand injection, glow containers, and responsive cards |

---

## 📂 Repository Structure

```plaintext
Zepto-Sales-Dashboard/
├── .streamlit/
│   └── config.toml          # Custom dark mode brand theme & server configuration
├── app.py                   # Main Streamlit application and analytics engine
├── zepto_v2.csv             # Cleaned Zepto retail product catalog dataset
├── requirements.txt         # Production Python dependencies
├── .gitignore               # Ignored system, virtualenv, and cache files
└── README.md                # Project documentation and setup guide
```

---

## 📋 Dataset Schema (`zepto_v2.csv`)

The underlying dataset contains catalog records extracted and normalized for quick-commerce analytics:

| Column Name | Data Type | Description | Unit / Example |
|---|---|---|---|
| `Category` | `String` | Retail product department | *Fruits & Vegetables, Munchies, Dairy* |
| `name` | `String` | Official SKU title | *Fresh Hybrid Tomato 500g* |
| `mrp` | `Float` | Original Maximum Retail Price | Converted from paise to Rupees (`₹`) |
| `discountPercent` | `Integer` | Applied promotional discount | Percentage (`0%` - `51%`) |
| `discountedSellingPrice` | `Float` | Final consumer checkout price | Converted from paise to Rupees (`₹`) |
| `availableQuantity` | `Integer` | Units currently available in warehouse | Integer count (`0` to `6+`) |
| `weightInGms` | `Float` | Net product weight | Grams (`g`) / Kilograms (`kg`) |
| `outOfStock` | `Boolean` | Real-time stock status flag | `True` / `False` |
| `quantity` | `String` | Unit packaging size description | *1 pc, 500g, 1L* |

---

## ⚙️ Installation Steps

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/kunalnevage10-lgtm/Zepto-Sales-Dashboard.git
cd Zepto-Sales-Dashboard
```

### 2. Create a Virtual Environment
It is recommended to use an isolated Python environment:

* **On Windows (PowerShell / Command Prompt):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

* **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries using the pinned `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Usage Instructions

### 1. Launch the Streamlit Dashboard
Run the following command in your terminal from the project root:
```bash
streamlit run app.py
```

### 2. Access the Application
Once the local development server starts, open your web browser and navigate to:
```text
http://localhost:8501
```

### 3. Interacting with the Dashboard
- **Filter Catalog**: Use the sidebar on the left to slice data by specific categories, set price boundaries, filter discount depths, or search specific product keywords.
- **Toggle Visual Metrics**: On the **Top 10 Categories** bar chart, switch between *SKU Count*, *Available Inventory Units*, and *Weight (kg)* to view volume from operational and inventory perspectives.
- **Inspect Pricing Margins**: Navigate to the **Pricing & Deals Matrix** tab to see category markdowns and the Top 10 Super Savers leaderboard.
- **Monitor Stock**: Open the **Inventory & Stock** tab to check out-of-stock items needing urgent replenishment.
- **Export Data**: In the **SKU Data Explorer** tab, click **📥 Download Filtered Data (CSV)** to export customized reports for your team.

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE) — feel free to modify, distribute, and integrate it into your own data analytics and portfolio projects.

---

## 👨‍💻 Author & Maintainer

**Kunal Nevage**  
- **GitHub**: [@kunalnevage10-lgtm](https://github.com/kunalnevage10-lgtm)
- **Specialization**: AI, Machine Learning & Business Intelligence

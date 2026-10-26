import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Zepto Analytics | Quick Commerce Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ZEPTO BRAND THEMING & CUSTOM CSS
# ==========================================
ZEPTO_PURPLE_DARK = "#0C0214"
ZEPTO_PURPLE_BG = "#160526"
ZEPTO_PURPLE_CARD = "#1F0838"
ZEPTO_PURPLE_BORDER = "rgba(255, 50, 105, 0.28)"
ZEPTO_MAGENTA = "#FF3269"
ZEPTO_PINK_VIBRANT = "#FF007A"
ZEPTO_PINK_LIGHT = "#FF6B8B"
ZEPTO_PURPLE_ACCENT = "#8C1EFF"
ZEPTO_PURPLE_LIGHT = "#B24BF3"
ZEPTO_TEXT_MUTED = "#A89AC0"

st.markdown(f"""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    /* Global reset and typography */
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #FFFFFF;
    }}

    /* Main container background */
    .stApp {{
        background: radial-gradient(circle at 15% 15%, #25063F 0%, #10021D 50%, #07010C 100%);
        background-attachment: fixed;
    }}

    /* Custom Header Banner */
    .zepto-banner {{
        background: linear-gradient(135deg, rgba(43, 4, 76, 0.85) 0%, rgba(26, 3, 48, 0.95) 50%, rgba(255, 50, 105, 0.2) 100%);
        border: 1px solid {ZEPTO_PURPLE_BORDER};
        border-radius: 18px;
        padding: 24px 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 16px;
    }}
    
    .zepto-logo-text {{
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #FFFFFF 0%, #FF6B8B 50%, #FF3269 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .zepto-badge {{
        background: linear-gradient(135deg, #FF3269, #8C1EFF);
        color: white;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 999px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 15px rgba(255, 50, 105, 0.4);
    }}

    .zepto-sub {{
        color: {ZEPTO_TEXT_MUTED};
        font-size: 0.95rem;
        margin-top: 6px;
    }}

    /* Metric Cards */
    .kpi-container {{
        background: linear-gradient(145deg, rgba(35, 8, 62, 0.8), rgba(20, 3, 38, 0.9));
        border: 1px solid rgba(255, 50, 105, 0.22);
        border-radius: 16px;
        padding: 20px 22px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
        position: relative;
        overflow: hidden;
    }}
    .kpi-container:hover {{
        transform: translateY(-3px);
        border-color: rgba(255, 50, 105, 0.55);
        box-shadow: 0 12px 30px rgba(255, 50, 105, 0.2);
    }}
    .kpi-container::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #FF3269, #8C1EFF);
    }}
    .kpi-title {{
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: {ZEPTO_TEXT_MUTED};
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .kpi-value {{
        font-size: 1.95rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.5px;
        line-height: 1.2;
    }}
    .kpi-subtext {{
        font-size: 0.8rem;
        color: #38E54D;
        margin-top: 6px;
        display: flex;
        align-items: center;
        gap: 4px;
        font-weight: 500;
    }}
    .kpi-subtext.magenta {{
        color: #FF3269;
    }}
    .kpi-subtext.violet {{
        color: #B24BF3;
    }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #18032B 0%, #0D0117 100%);
        border-right: 1px solid rgba(255, 50, 105, 0.2);
    }}
    
    section[data-testid="stSidebar"] .stMarkdown h2, 
    section[data-testid="stSidebar"] .stMarkdown h3 {{
        color: #FFFFFF;
    }}

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 12px;
        background-color: transparent;
        padding-bottom: 4px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(35, 8, 62, 0.5);
        border: 1px solid rgba(255, 50, 105, 0.2);
        border-radius: 12px;
        color: {ZEPTO_TEXT_MUTED};
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, rgba(255, 50, 105, 0.25), rgba(140, 30, 255, 0.25)) !important;
        border: 1px solid {ZEPTO_MAGENTA} !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(255, 50, 105, 0.3);
    }}

    /* Chart Container Card */
    .chart-card {{
        background: linear-gradient(145deg, rgba(28, 6, 50, 0.8), rgba(16, 2, 30, 0.9));
        border: 1px solid rgba(255, 50, 105, 0.2);
        border-radius: 18px;
        padding: 20px 22px 14px 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
    }}

    /* Custom Filter Pill Badges */
    .filter-pill {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        background: rgba(255, 50, 105, 0.15);
        border: 1px solid rgba(255, 50, 105, 0.4);
        color: #FF80AB;
        margin: 2px 4px 2px 0;
    }}

    /* Buttons */
    div.stButton > button {{
        background: linear-gradient(135deg, #FF3269 0%, #B21B72 100%);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.45rem 1.1rem;
        transition: all 0.25s ease;
        box-shadow: 0 4px 12px rgba(255, 50, 105, 0.3);
    }}
    div.stButton > button:hover {{
        background: linear-gradient(135deg, #FF527F 0%, #D81B60 100%);
        box-shadow: 0 6px 18px rgba(255, 50, 105, 0.5);
        transform: translateY(-1px);
        color: white;
    }}

    /* Streamlit dataframe styling */
    [data-testid="stDataFrame"] {{
        border: 1px solid rgba(255, 50, 105, 0.2);
        border-radius: 12px;
        overflow: hidden;
    }}
</style>
""", unsafe_allow_html=True)


# ==========================================
# DATA LOADING & PREPROCESSING (CACHE-ENABLED)
# ==========================================
@st.cache_data(show_spinner=False)
def load_and_clean_data(file_path: str = "zepto_v2.csv") -> pd.DataFrame:
    """
    Loads zepto_v2.csv with multi-encoding fallback, handles missing values,
    converts prices from paise to Rupees, and builds analytical dimensions.
    """
    encodings_to_try = ["latin-1", "cp1252", "utf-8", "iso-8859-1"]
    df = None
    
    # Path resolution: check current folder or fallback
    target_path = Path(file_path)
    if not target_path.exists():
        # Search workspace or parent
        matches = list(Path(".").rglob("zepto_v2.csv"))
        if matches:
            target_path = matches[0]
        else:
            raise FileNotFoundError(f"Dataset '{file_path}' not found in workspace.")
            
    for enc in encodings_to_try:
        try:
            df = pd.read_csv(target_path, encoding=enc)
            break
        except (UnicodeDecodeError, Exception):
            continue
            
    if df is None:
        # Ultimate fallback with error replacement
        df = pd.read_csv(target_path, encoding="utf-8", encoding_errors="replace")

    # 1. Clean column strings and handle text missing values
    if "Category" in df.columns:
        df["Category"] = df["Category"].fillna("Uncategorized").astype(str).str.strip()
    else:
        df["Category"] = "Uncategorized"

    if "name" in df.columns:
        df["name"] = df["name"].fillna("Unnamed Product").astype(str).str.strip()
    else:
        df["name"] = "Unnamed Product"

    # 2. Clean and convert numeric fields (stored in paise in raw data)
    numeric_cols = ["mrp", "discountedSellingPrice", "discountPercent", "availableQuantity", "weightInGms", "quantity"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        else:
            df[col] = 0

    # Impute missing numerics
    df["mrp"] = df["mrp"].fillna(0)
    df["discountedSellingPrice"] = df["discountedSellingPrice"].fillna(df["mrp"])
    df["discountPercent"] = df["discountPercent"].fillna(0).clip(lower=0, upper=100)
    df["availableQuantity"] = df["availableQuantity"].fillna(0).clip(lower=0)
    df["weightInGms"] = df["weightInGms"].fillna(0)
    df["quantity"] = df["quantity"].fillna(1)

    # 3. Clean Boolean outOfStock flag
    if "outOfStock" in df.columns:
        df["outOfStock"] = df["outOfStock"].astype(str).str.strip().str.upper().isin(["TRUE", "1", "YES"])
    else:
        df["outOfStock"] = df["availableQuantity"] == 0

    # 4. Computed currency dimensions (paise to INR ₹)
    df["mrp_inr"] = df["mrp"] / 100.0
    df["discounted_price_inr"] = df["discountedSellingPrice"] / 100.0
    df["savings_inr"] = (df["mrp_inr"] - df["discounted_price_inr"]).clip(lower=0)

    # 5. Stock Status Label
    df["Stock_Status"] = df["outOfStock"].apply(lambda x: "Out of Stock" if x else "In Stock")

    # 6. Categorize Discount Ranges for Donut Visualization
    def categorize_discount(pct):
        if pct <= 0:
            return "No Discount (0%)"
        elif pct <= 10:
            return "Low (1% - 10%)"
        elif pct <= 20:
            return "Moderate (11% - 20%)"
        elif pct <= 35:
            return "High (21% - 35%)"
        else:
            return "Super Saver (36%+)"

    df["Discount_Range"] = df["discountPercent"].apply(categorize_discount)

    # 7. Ordered Categorical for consistent visualization ordering
    discount_order = [
        "No Discount (0%)",
        "Low (1% - 10%)",
        "Moderate (11% - 20%)",
        "High (21% - 35%)",
        "Super Saver (36%+)"
    ]
    df["Discount_Range"] = pd.Categorical(df["Discount_Range"], categories=discount_order, ordered=True)

    return df


try:
    df_raw = load_and_clean_data("zepto_v2.csv")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()


# ==========================================
# SIDEBAR FILTERS & INTERACTIVITY
# ==========================================
with st.sidebar:
    # Zepto Brand Header in Sidebar
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <div style="font-size: 2.2rem; font-weight: 900; background: linear-gradient(135deg, #FF3269, #C2185B); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            zepto ⚡
        </div>
        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: #A89AC0;">
            Catalog Filter Engine
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Dynamic Filters")

    # Filter 1: Search by Product Name
    search_query = st.text_input(
        "🔍 Search Products",
        placeholder="e.g. Onion, Amul, Maggi...",
        help="Filter products containing search keywords"
    )

    # Filter 2: Category Multi-Select
    all_categories = sorted(df_raw["Category"].unique().tolist())
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("Select All", use_container_width=True):
            st.session_state["selected_categories"] = all_categories
    with col_btn2:
        if st.button("Clear All", use_container_width=True):
            st.session_state["selected_categories"] = []

    if "selected_categories" not in st.session_state:
        st.session_state["selected_categories"] = all_categories

    selected_categories = st.multiselect(
        "📂 Product Category",
        options=all_categories,
        default=st.session_state["selected_categories"],
        help="Select one or multiple categories to filter"
    )

    # Filter 3: Stock Status Filter
    stock_options = ["All Items", "In Stock Only", "Out of Stock Only"]
    selected_stock = st.radio(
        "📦 Stock Availability",
        options=stock_options,
        index=0,
        horizontal=True
    )

    # Filter 4: Price Range Slider (in INR)
    min_mrp = float(df_raw["mrp_inr"].min())
    max_mrp = float(df_raw["mrp_inr"].max())
    if max_mrp <= min_mrp:
        max_mrp = min_mrp + 1.0
    
    price_range = st.slider(
        "💰 Original Price Range (₹ MRP)",
        min_value=round(min_mrp, 1),
        max_value=round(max_mrp, 1),
        value=(round(min_mrp, 1), round(max_mrp, 1)),
        step=5.0,
        format="₹%.0f"
    )

    # Filter 5: Discount Percentage Slider
    max_disc = int(df_raw["discountPercent"].max())
    if max_disc <= 0:
        max_disc = 1

    discount_range = st.slider(
        "🏷️ Discount Percentage (%)",
        min_value=0,
        max_value=max_disc,
        value=(0, max_disc),
        step=1,
        format="%d%%"
    )

    st.markdown("---")
    
    # Reset All Filters button
    if st.button("🔄 Reset All Filters", use_container_width=True):
        st.session_state["selected_categories"] = all_categories
        st.rerun()

    # Active Filter Summary
    st.markdown("""
    <div style="font-size: 0.78rem; color: #A89AC0; margin-top: 10px; line-height: 1.5;">
        ⚡ <b>Zepto Fast Facts:</b><br>
        • Database: <b>3,732</b> products<br>
        • Categories: <b>14</b> retail segments<br>
        • Prices normalized from paise to INR (₹)
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# APPLY FILTERING LOGIC
# ==========================================
filtered_df = df_raw.copy()

# Apply Category filter
if selected_categories:
    filtered_df = filtered_df[filtered_df["Category"].isin(selected_categories)]
else:
    # If nothing selected, empty dataframe
    filtered_df = filtered_df.iloc[0:0]

# Apply Stock Availability filter
if selected_stock == "In Stock Only":
    filtered_df = filtered_df[~filtered_df["outOfStock"]]
elif selected_stock == "Out of Stock Only":
    filtered_df = filtered_df[filtered_df["outOfStock"]]

# Apply Price Range filter
filtered_df = filtered_df[
    (filtered_df["mrp_inr"] >= price_range[0]) & 
    (filtered_df["mrp_inr"] <= price_range[1])
]

# Apply Discount Percentage filter
filtered_df = filtered_df[
    (filtered_df["discountPercent"] >= discount_range[0]) & 
    (filtered_df["discountPercent"] <= discount_range[1])
]

# Apply Text Search filter
if search_query.strip():
    q = search_query.strip().lower()
    filtered_df = filtered_df[
        filtered_df["name"].str.lower().str.contains(q) | 
        filtered_df["Category"].str.lower().str.contains(q)
    ]


# ==========================================
# MAIN DASHBOARD HEADER
# ==========================================
st.markdown(f"""
<div class="zepto-banner">
    <div>
        <div class="zepto-logo-text">
            <span>zepto</span>
            <span style="font-size: 1.4rem; color: #FF3269;">⚡ 10-Min Analytics</span>
        </div>
        <div class="zepto-sub">
            Interactive Product Intelligence & Pricing Performance Dashboard
        </div>
    </div>
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
        <span class="zepto-badge">Live Store Catalog</span>
        <span class="zepto-badge" style="background: linear-gradient(135deg, #8C1EFF, #4A0E78);">
            {len(filtered_df):,} of {len(df_raw):,} SKUs Shown
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Edge case: If no records match
if filtered_df.empty:
    st.warning("⚠️ No products match your selected filter criteria. Please adjust or reset filters in the sidebar.")
    st.stop()


# ==========================================
# TOP KPIS (KEY PERFORMANCE INDICATORS)
# ==========================================
total_skus = len(filtered_df)
avg_mrp = filtered_df["mrp_inr"].mean()
avg_discount = filtered_df["discountPercent"].mean()
avg_selling = filtered_df["discounted_price_inr"].mean()
in_stock_count = (~filtered_df["outOfStock"]).sum()
in_stock_pct = (in_stock_count / total_skus * 100) if total_skus > 0 else 0
total_savings_pool = filtered_df["savings_inr"].sum()
max_discount_val = filtered_df["discountPercent"].max()

kpi_c1, kpi_c2, kpi_c3, kpi_c4 = st.columns(4)

with kpi_c1:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">📦 Total Products / SKUs</div>
        <div class="kpi-value">{total_skus:,}</div>
        <div class="kpi-subtext violet">
            <span>●</span> {filtered_df['Category'].nunique()} Categories Active
        </div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c2:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">🏷️ Avg. Original Price (MRP)</div>
        <div class="kpi-value">₹{avg_mrp:,.2f}</div>
        <div class="kpi-subtext">
            <span>●</span> Selling Avg: ₹{avg_selling:,.2f}
        </div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c3:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">⚡ Avg. Discount</div>
        <div class="kpi-value">{avg_discount:.1f}%</div>
        <div class="kpi-subtext magenta">
            <span>▲</span> Peak Discount: {max_discount_val:.0f}% OFF
        </div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c4:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">🟢 Stock In-Stock Rate</div>
        <div class="kpi-value">{in_stock_pct:.1f}%</div>
        <div class="kpi-subtext">
            <span>✓</span> {in_stock_count:,} Available | {total_skus - in_stock_count:,} OOS
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)


# ==========================================
# PLOTLY THEME HELPER FUNCTION
# ==========================================
def apply_zepto_theme(fig, title: str = "", height: int = 420):
    """Applies a consistent, polished Zepto dark-mode aesthetic to Plotly figures."""
    fig.update_layout(
        title={
            "text": f"<b>{title}</b>",
            "y": 0.95,
            "x": 0.02,
            "xanchor": "left",
            "yanchor": "top",
            "font": {"size": 17, "color": "#FFFFFF", "family": "Plus Jakarta Sans, sans-serif"}
        },
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=height,
        margin=dict(l=20, r=20, t=55, b=25),
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#E2D9F3"),
        legend=dict(
            bgcolor="rgba(24, 4, 44, 0.6)",
            bordercolor="rgba(255, 50, 105, 0.2)",
            borderwidth=1,
            font=dict(size=11, color="#E2D9F3")
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(255, 255, 255, 0.07)",
            zeroline=False,
            color="#A89AC0",
            tickfont=dict(size=11, color="#C7B8E0")
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255, 255, 255, 0.07)",
            zeroline=False,
            color="#A89AC0",
            tickfont=dict(size=11, color="#C7B8E0")
        ),
        hoverlabel=dict(
            bgcolor="#1F0838",
            bordercolor="#FF3269",
            font=dict(family="Plus Jakarta Sans", size=12, color="#FFFFFF")
        )
    )
    return fig


# ==========================================
# MAIN INTERACTIVE TABS
# ==========================================
tab_overview, tab_pricing, tab_inventory, tab_data = st.tabs([
    "📊 Core Visualizations",
    "🏷️ Pricing & Deals Matrix",
    "📦 Inventory & Stock",
    "🔍 SKU Data Explorer"
])

# ---------------------------------------------------------------------------------
# TAB 1: CORE VISUALIZATIONS (STRICT REQUIREMENTS)
# ---------------------------------------------------------------------------------
with tab_overview:
    # Row 1: Bar Chart (Top 10 Categories by Volume) + Donut Chart (Discount Distribution)
    row1_c1, row1_c2 = st.columns([1.1, 0.9])

    with row1_c1:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        
        # Volume toggle: SKU Count vs Stock Units
        vol_metric_choice = st.radio(
            "Sort Category Volume By:",
            ["Product (SKU) Count", "Available Inventory Stock Units", "Total Weight Volume (kg)"],
            index=0,
            horizontal=True,
            key="vol_metric_toggle"
        )
        
        if vol_metric_choice == "Product (SKU) Count":
            cat_vol = (
                filtered_df.groupby("Category")
                .size()
                .reset_index(name="Volume")
                .sort_values(by="Volume", ascending=True)
                .tail(10)
            )
            val_col_name = "Volume (SKUs)"
            custom_hover = "Category: <b>%{y}</b><br>SKU Count: <b>%{x:,}</b>"
            bar_color_scale = ["#3D075E", "#6B11A6", "#9C27B0", "#D81B60", "#FF3269"]
        elif vol_metric_choice == "Available Inventory Stock Units":
            cat_vol = (
                filtered_df.groupby("Category")["availableQuantity"]
                .sum()
                .reset_index(name="Volume")
                .sort_values(by="Volume", ascending=True)
                .tail(10)
            )
            val_col_name = "Stock Units"
            custom_hover = "Category: <b>%{y}</b><br>Available Units: <b>%{x:,}</b>"
            bar_color_scale = ["#280447", "#5E0F8B", "#8C1EFF", "#E91E63", "#FF3269"]
        else:
            cat_vol = (
                filtered_df.groupby("Category")["weightInGms"]
                .sum()
                .div(1000.0)
                .reset_index(name="Volume")
                .sort_values(by="Volume", ascending=True)
                .tail(10)
            )
            val_col_name = "Total Weight (kg)"
            custom_hover = "Category: <b>%{y}</b><br>Total Weight: <b>%{x:,.1f} kg</b>"
            bar_color_scale = ["#350654", "#7B1FA2", "#C2185B", "#FF007A", "#FF6B8B"]

        # Horizontal Bar Chart for readability of category names
        fig_bar = px.bar(
            cat_vol,
            x="Volume",
            y="Category",
            orientation="h",
            text="Volume",
            color="Volume",
            color_continuous_scale=bar_color_scale
        )
        fig_bar.update_traces(
            texttemplate="%{x:,.0f}" if vol_metric_choice != "Total Weight Volume (kg)" else "%{x:,.1f}k",
            textposition="outside",
            marker=dict(line=dict(color="#FF3269", width=1)),
            hovertemplate=custom_hover + "<extra></extra>"
        )
        fig_bar.update_coloraxes(showscale=False)
        fig_bar = apply_zepto_theme(fig_bar, f"Top 10 Product Categories by {val_col_name}", height=430)
        fig_bar.update_layout(xaxis_title=val_col_name, yaxis_title="")
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with row1_c2:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        
        # Donut Chart: Discount Range Distribution
        discount_dist = (
            filtered_df["Discount_Range"]
            .value_counts()
            .reset_index()
        )
        discount_dist.columns = ["Discount_Range", "Count"]
        
        # Filter out 0 count ranges
        discount_dist = discount_dist[discount_dist["Count"] > 0]
        
        # Palette mapping for discount ranges
        color_map = {
            "No Discount (0%)": "#4A0E78",
            "Low (1% - 10%)": "#7B1FA2",
            "Moderate (11% - 20%)": "#C2185B",
            "High (21% - 35%)": "#FF3269",
            "Super Saver (36%+)": "#FF80AB"
        }
        slice_colors = [color_map.get(cat, "#FF3269") for cat in discount_dist["Discount_Range"]]

        fig_donut = go.Figure(data=[go.Pie(
            labels=discount_dist["Discount_Range"],
            values=discount_dist["Count"],
            hole=0.58,
            marker=dict(
                colors=slice_colors,
                line=dict(color="#160526", width=2.5)
            ),
            textinfo="percent+label",
            textposition="inside",
            insidetextorientation="horizontal",
            insidetextfont=dict(size=11, color="#FFFFFF", family="Plus Jakarta Sans"),
            hovertemplate="<b>%{label}</b><br>SKUs: <b>%{value:,}</b><br>Share: <b>%{percent:.1%}</b><extra></extra>",
            pull=[0.02, 0.02, 0.04, 0.06, 0.08]
        )])

        # Center KPI in Donut
        fig_donut.add_annotation(
            text=f"<b>{total_skus:,}</b><br><span style='font-size:10px; color:#A89AC0;'>TOTAL SKUs</span>",
            x=0.5, y=0.5,
            font=dict(size=16, color="#FFFFFF", family="Plus Jakarta Sans"),
            showarrow=False
        )

        fig_donut = apply_zepto_theme(fig_donut, "Distribution of Discount Ranges", height=465)
        fig_donut.update_layout(
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.22,
                xanchor="center",
                x=0.5
            )
        )
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Row 2: Scatter Plot (Original Price vs Discounted Price)
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    
    col_scat_ctrl1, col_scat_ctrl2 = st.columns([1, 1])
    with col_scat_ctrl1:
        scatter_color_by = st.selectbox(
            "Color Points By:",
            ["Category", "Discount_Range", "Stock_Status"],
            index=0,
            key="scatter_color_select"
        )
    with col_scat_ctrl2:
        total_filtered_pts = len(filtered_df)
        min_scatter_pts = min(100, total_filtered_pts)
        max_scatter_pts_val = total_filtered_pts
        
        # Ensure max_value is always strictly greater than min_value to prevent StreamlitInvalidMinMaxError
        if max_scatter_pts_val <= min_scatter_pts:
            max_scatter_pts_val = min_scatter_pts + 1

        if total_filtered_pts <= 100:
            st.caption(f"⚡ Showing all **{total_filtered_pts:,}** filtered items (no sampling required).")
            max_scatter_pts = total_filtered_pts
        else:
            slider_step = 50 if total_filtered_pts <= 1000 else 100
            default_val = min(1500, max_scatter_pts_val)
            if default_val < min_scatter_pts:
                default_val = min_scatter_pts
            max_scatter_pts = st.slider(
                "Sample Size for Plot (optimizes rendering performance):",
                min_value=min_scatter_pts,
                max_value=max_scatter_pts_val,
                value=default_val,
                step=slider_step
            )

    # Sample if dataset is very large for crisp responsiveness
    if len(filtered_df) > max_scatter_pts:
        df_scatter = filtered_df.sample(max_scatter_pts, random_state=42)
    else:
        df_scatter = filtered_df

    # Zepto-inspired categorical palette
    zepto_cat_palette = [
        "#FF3269", "#8C1EFF", "#00E5FF", "#FFB300", "#00E676",
        "#E040FB", "#FF5252", "#7C4DFF", "#69F0AE", "#FF6E40",
        "#40C4FF", "#EEFF41", "#FF1744", "#D500F9"
    ]

    fig_scatter = px.scatter(
        df_scatter,
        x="mrp_inr",
        y="discounted_price_inr",
        color=scatter_color_by,
        size="discountPercent",
        size_max=14,
        color_discrete_sequence=zepto_cat_palette,
        hover_name="name",
        hover_data={
            "Category": True,
            "mrp_inr": ":.2f",
            "discounted_price_inr": ":.2f",
            "discountPercent": True,
            "savings_inr": ":.2f",
            "availableQuantity": True
        },
        labels={
            "mrp_inr": "Original Price (₹ MRP)",
            "discounted_price_inr": "Discounted Selling Price (₹)",
            "discountPercent": "Discount %",
            "savings_inr": "Savings (₹)",
            "availableQuantity": "Available Qty"
        }
    )

    # Add 1:1 reference line (Zero Discount Line: y = x)
    max_val = max(df_scatter["mrp_inr"].max(), df_scatter["discounted_price_inr"].max()) if not df_scatter.empty else 100
    fig_scatter.add_trace(
        go.Scatter(
            x=[0, max_val],
            y=[0, max_val],
            mode="lines",
            line=dict(color="rgba(255, 255, 255, 0.35)", width=2, dash="dash"),
            name="Zero Discount Line (y = x)",
            hoverinfo="none"
        )
    )

    fig_scatter.update_traces(
        marker=dict(opacity=0.82, line=dict(width=0.6, color="rgba(255, 255, 255, 0.4)"))
    )

    fig_scatter = apply_zepto_theme(
        fig_scatter, 
        f"Original Price (MRP) vs. Discounted Selling Price (Sample: {len(df_scatter):,} SKUs)",
        height=520
    )
    fig_scatter.update_layout(
        xaxis_title="Original Price (₹ MRP)",
        yaxis_title="Discounted Selling Price (₹)",
        legend=dict(orientation="h", yanchor="bottom", y=-0.28, xanchor="center", x=0.5)
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.caption("💡 *Points further below the dashed diagonal line represent greater absolute customer rupee savings.*")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------------
# TAB 2: PRICING & DEALS MATRIX
# ---------------------------------------------------------------------------------
with tab_pricing:
    col_deal_1, col_deal_2 = st.columns(2)

    with col_deal_1:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        # Average Discount % by Category
        cat_discount = (
            filtered_df.groupby("Category")["discountPercent"]
            .mean()
            .reset_index()
            .sort_values(by="discountPercent", ascending=True)
        )
        
        fig_cat_disc = px.bar(
            cat_discount,
            x="discountPercent",
            y="Category",
            orientation="h",
            color="discountPercent",
            color_continuous_scale=["#3D075E", "#8C1EFF", "#FF3269", "#FF80AB"],
            labels={"discountPercent": "Average Discount (%)", "Category": ""},
            text="discountPercent"
        )
        fig_cat_disc.update_traces(
            texttemplate="%{x:.1f}%",
            textposition="outside",
            marker=dict(line=dict(color="#FF3269", width=0.8)),
            hovertemplate="Category: <b>%{y}</b><br>Avg Discount: <b>%{x:.1f}%</b><extra></extra>"
        )
        fig_cat_disc.update_coloraxes(showscale=False)
        fig_cat_disc = apply_zepto_theme(fig_cat_disc, "Average Discount Percentage by Category", height=440)
        fig_cat_disc.update_layout(xaxis_title="Average Discount (%)")
        st.plotly_chart(fig_cat_disc, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_deal_2:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        # Box Plot: Price Distribution across Top Categories
        top_cats = (
            filtered_df["Category"].value_counts().head(8).index.tolist()
        )
        df_box = filtered_df[filtered_df["Category"].isin(top_cats)]
        
        fig_box = px.box(
            df_box,
            x="Category",
            y="discounted_price_inr",
            color="Category",
            color_discrete_sequence=zepto_cat_palette,
            labels={"discounted_price_inr": "Selling Price (₹)", "Category": ""}
        )
        fig_box.update_traces(marker=dict(size=3, opacity=0.7))
        fig_box = apply_zepto_theme(fig_box, "Selling Price Distribution across Top 8 Categories", height=440)
        fig_box.update_layout(showlegend=False, xaxis_tickangle=-30)
        st.plotly_chart(fig_box, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Super Savers: Top 10 Best Deals by Discount Percentage
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.markdown("### 🏆 Top 10 'Super Saver' Deals in Current Selection")
    
    top_deals = (
        filtered_df.sort_values(by=["discountPercent", "savings_inr"], ascending=[False, False])
        .head(10)[["name", "Category", "mrp_inr", "discounted_price_inr", "discountPercent", "savings_inr", "Stock_Status"]]
        .rename(columns={
            "name": "Product Name",
            "mrp_inr": "MRP (₹)",
            "discounted_price_inr": "Selling Price (₹)",
            "discountPercent": "Discount (%)",
            "savings_inr": "Savings (₹)",
            "Stock_Status": "Status"
        })
    )
    
    st.dataframe(
        top_deals.style.format({
            "MRP (₹)": "₹{:,.2f}",
            "Selling Price (₹)": "₹{:,.2f}",
            "Discount (%)": "{:.0f}%",
            "Savings (₹)": "₹{:,.2f}"
        }).background_gradient(subset=["Discount (%)"], cmap="magma"),
        use_container_width=True,
        hide_index=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------------
# TAB 3: INVENTORY & STOCK INTELLIGENCE
# ---------------------------------------------------------------------------------
with tab_inventory:
    inv_c1, inv_c2 = st.columns([1, 1])

    with inv_c1:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        # Out-of-Stock vs In-Stock Breakdown by Category
        stock_summary = (
            filtered_df.groupby(["Category", "Stock_Status"])
            .size()
            .reset_index(name="Count")
        )
        
        fig_stock = px.bar(
            stock_summary,
            x="Count",
            y="Category",
            color="Stock_Status",
            orientation="h",
            barmode="stack",
            color_discrete_map={
                "In Stock": "#00E676",
                "Out of Stock": "#FF3269"
            },
            labels={"Count": "Product Count", "Stock_Status": "Inventory Status"}
        )
        fig_stock = apply_zepto_theme(fig_stock, "In-Stock vs Out-of-Stock Counts by Category", height=450)
        fig_stock.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5))
        st.plotly_chart(fig_stock, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with inv_c2:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        # Available Quantity Distribution for In-Stock Items
        in_stock_df = filtered_df[~filtered_df["outOfStock"]]
        if not in_stock_df.empty:
            avail_counts = (
                in_stock_df["availableQuantity"]
                .value_counts()
                .reset_index()
                .rename(columns={"availableQuantity": "Stock_Units", "count": "SKU_Count"})
                .sort_values(by="Stock_Units")
            )
            avail_counts["Stock_Units_Label"] = avail_counts["Stock_Units"].apply(lambda u: f"{u} Units")

            fig_avail = px.bar(
                avail_counts,
                x="Stock_Units_Label",
                y="SKU_Count",
                color="SKU_Count",
                text="SKU_Count",
                color_continuous_scale=["#3D075E", "#8C1EFF", "#FF3269"],
                labels={"Stock_Units_Label": "Available Inventory Batch Size", "SKU_Count": "SKU Count"}
            )
            fig_avail.update_traces(textposition="outside")
            fig_avail.update_coloraxes(showscale=False)
            fig_avail = apply_zepto_theme(fig_avail, "Batch Inventory Depth (Available Units per SKU)", height=450)
            st.plotly_chart(fig_avail, use_container_width=True)
        else:
            st.info("No in-stock items currently match the filter selection.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Out of Stock High Priority Alert Table
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.markdown("### ⚠️ Out-of-Stock SKUs Requiring Warehouse Replenishment")
    oos_df = filtered_df[filtered_df["outOfStock"]][["name", "Category", "mrp_inr", "discountPercent", "weightInGms"]]
    if not oos_df.empty:
        st.dataframe(
            oos_df.rename(columns={
                "name": "Product Name",
                "Category": "Category",
                "mrp_inr": "MRP (₹)",
                "discountPercent": "Standard Discount (%)",
                "weightInGms": "Weight (g)"
            }).style.format({"MRP (₹)": "₹{:,.2f}", "Standard Discount (%)": "{:.0f}%", "Weight (g)": "{:,.0f} g"}),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("🎉 All filtered items are currently in stock!")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------------
# TAB 4: SKU DATA EXPLORER & CSV EXPORT
# ---------------------------------------------------------------------------------
with tab_data:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.markdown("### 🔍 Searchable Product Catalog Table")

    col_tbl_ctrl1, col_tbl_ctrl2 = st.columns([2, 1])
    with col_tbl_ctrl1:
        st.write(f"Showing **{len(filtered_df):,}** products matching current sidebar filters.")
    with col_tbl_ctrl2:
        # CSV Download button
        csv_export = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=csv_export,
            file_name="zepto_filtered_analytics.csv",
            mime="text/csv",
            use_container_width=True
        )

    # Display clean formatted columns
    display_cols = [
        "name", "Category", "mrp_inr", "discounted_price_inr", 
        "discountPercent", "savings_inr", "Stock_Status", "availableQuantity", "weightInGms"
    ]
    
    st.dataframe(
        filtered_df[display_cols].rename(columns={
            "name": "Product Name",
            "Category": "Category",
            "mrp_inr": "MRP (₹)",
            "discounted_price_inr": "Selling Price (₹)",
            "discountPercent": "Discount (%)",
            "savings_inr": "Savings (₹)",
            "Stock_Status": "Stock Status",
            "availableQuantity": "Available Units",
            "weightInGms": "Weight (g)"
        }).style.format({
            "MRP (₹)": "₹{:,.2f}",
            "Selling Price (₹)": "₹{:,.2f}",
            "Discount (%)": "{:.0f}%",
            "Savings (₹)": "₹{:,.2f}",
            "Weight (g)": "{:,.0f} g"
        }),
        use_container_width=True,
        hide_index=True,
        height=520
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div style="text-align: center; color: #7B6899; font-size: 0.8rem; padding: 30px 0 10px 0; border-top: 1px solid rgba(255, 50, 105, 0.15); margin-top: 40px;">
    ⚡ <b>Zepto Quick Commerce Analytics Dashboard</b> | Crafted with Streamlit, Pandas & Plotly | Dark Mode Brand Theme
</div>
""", unsafe_allow_html=True)

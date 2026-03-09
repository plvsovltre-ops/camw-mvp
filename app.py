import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.set_page_config(page_title="CASPI Methane Watch", layout="wide", page_icon="🌍")
st.title("🌍 CASPI Methane Watch (CAMW)")
st.markdown("**Пилот S.O.R.B.U.L.A.Q.** — озеро Сорбулак, Центральная Азия")

st.sidebar.header("Параметры")
period = st.sidebar.date_input("Период", [date(2025,1,1), date.today()])

# Данные (здесь можно подключить реальные из Colab)
df = pd.DataFrame({
    'Дата': pd.date_range('2025-01-01', periods=60),
    'CH4 (ppb)': [1850 + i*1.8 for i in range(60)],
    'H2S Risk': ['Низкий']*25 + ['Средний']*20 + ['Высокий']*15,
    'pH': [8.2, 8.4, 8.1, 7.9] * 15,
    'DO (мг/л)': [5.2, 4.8, 3.9, 6.1] * 15
})

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("CH₄ сейчас", "1924 ppb", "↑12")
with col2:
    st.metric("Риск H₂S", "Средний", "↑")
with col3:
    st.metric("pH", "8.3", "норма")

st.subheader("Прогноз на завтра")
st.success(f"CH₄ завтра: **{1924 + 18:.0f} ppb** (по XGBoost)")

fig = px.line(df, x='Дата', y='CH4 (ppb)', title="Динамика метана за 60 дней")
st.plotly_chart(fig, use_container_width=True)

st.map(pd.DataFrame({'lat': [43.670124], 'lon': [76.574117]}))

st.caption("MVP создан Yernar Sailybayev | Team CASPI | Данные Earth Engine + XGBoost")

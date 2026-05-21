import streamlit as st
import pandas as pd
import joblib
import time

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Recomendador de OS",
    page_icon="💻",
    layout="centered"
)

# CARGAR MODELO
modelo = joblib.load('modelos/modelo_random_forest.pkl')

# ESTILOS CSS
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0f1117;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* =========================
   TÍTULO PRINCIPAL
========================= */

.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 800;
    color: #00ffe1;
    margin-bottom: 10px;
    text-shadow: 0px 0px 18px #00ffe1;
    letter-spacing: 1px;
}

/* =========================
   SUBTÍTULO
========================= */

.subtitle {
    text-align: center;
    font-size: 27px;
    font-weight: 600;
    color: #d0d0d0;
    margin-bottom: 35px;
}

/* =========================
   CAJAS DE PREGUNTAS
========================= */

.question-box {
    background: #1a1d29;
    padding: 14px 20px;
    border-radius: 16px;
    margin-bottom: 12px;
    border: 1px solid #2f3547;
    box-shadow: 0px 0px 12px rgba(0,255,225,0.08);
    transition: 0.3s;
}

.question-box:hover {
    border: 1px solid #00ffe1;
    box-shadow: 0px 0px 18px rgba(0,255,225,0.2);
}

/* =========================
   TEXTO DE PREGUNTAS
========================= */

.question-box label,
.question-box p,
.stRadio label,
.stSelectSlider label {

    font-size: 23px !important;
    font-weight: 700 !important;
    color: white !important;
    line-height: 1.4;
}

/* =========================
   OPCIONES SÍ / NO
========================= */

.stRadio div[role="radiogroup"] {
    gap: 25px;
}

.stRadio div[role="radiogroup"] label {
    font-size: 20px !important;
    font-weight: 600 !important;
    background: #252938;
    padding: 10px 18px;
    border-radius: 12px;
    border: 1px solid #3b4255;
    transition: 0.3s;
}

.stRadio div[role="radiogroup"] label:hover {
    border: 1px solid #00ffe1;
    box-shadow: 0px 0px 10px rgba(0,255,225,0.25);
}

/* =========================
   BOTÓN PRINCIPAL
========================= */

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00ffe1, #007cf0);
    color: black;
    font-size: 20px;
    font-weight: bold;
    border-radius: 14px;
    border: none;
    padding: 14px;
    transition: 0.3s;
    margin-top: 15px;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 25px #00ffe1;
}

/* =========================
   RESULTADO
========================= */

.result-box {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    padding: 32px;
    border-radius: 22px;
    text-align: center;
    animation: aparecer 0.8s ease-in-out;
    margin-top: 28px;
    box-shadow: 0px 0px 35px rgba(0,255,225,0.4);
}

.result-text {
    font-size: 32px;
    font-weight: bold;
    color: white;
    line-height: 1.5;
}

/* =========================
   ANIMACIÓN
========================= */

@keyframes aparecer {

    from {
        opacity: 0;
        transform: translateY(30px) scale(0.9);
    }

    to {
        opacity: 1;
        transform: translateY(0px) scale(1);
    }
}

/* =========================
   CAJA GOOGLE COLAB
========================= */

.colab-box {
    background: linear-gradient(135deg, #111827, #1f2937);
    border: 1px solid #00ffe1;
    padding: 24px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 35px;
    box-shadow: 0px 0px 20px rgba(0,255,225,0.15);
    animation: aparecer 1s ease-in-out;
    transition: 0.3s;
}

.colab-box:hover {
    transform: scale(1.01);
    box-shadow: 0px 0px 25px rgba(0,255,225,0.25);
}

/* =========================
   EMOJI DEL CUADERNO
========================= */

.colab-emoji {
    font-size: 68px;
    margin-bottom: 10px;
    display: block;
}

/* =========================
   LINK COLAB
========================= */

.colab-box a {
    color: #00ffe1;
    text-decoration: none;
    font-size: 25px;
    font-weight: bold;
}

.colab-box a:hover {
    color: white;
    text-shadow: 0px 0px 12px #00ffe1;
}

/* =========================
   FOOTER / CRÉDITOS
========================= */

.footer {
    margin-top: 60px;
    text-align: center;
    color: #777;
    font-size: 14px;
    line-height: 1.8;
}

/* =========================
   SCROLLBAR MODERNO
========================= */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #111827;
}

::-webkit-scrollbar-thumb {
    background: #00ffe1;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #00c6ff;
}

</style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown('<div class="main-title">💻 Recomendador de OS</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Sistema Inteligente de Recomendación de Sistemas Operativos</div>',
    unsafe_allow_html=True
)

# LINK COLAB DESTACADO
st.markdown("""
<div class="colab-box">
    📘 <br><br>
    <a href="https://colab.research.google.com/drive/1miYl2oYG8pRhgRQ3JACep9QiiCkxiQg7?usp=sharing" target="_blank">
        Ver Cuaderno Completo en Google Colab
    </a>
</div>
""", unsafe_allow_html=True)

# RAM
st.markdown('<div class="question-box">', unsafe_allow_html=True)

ram = st.select_slider(
    "💾 ¿Cuánta memoria RAM tiene tu computadora?",
    options=[2,4,8,16,32]
)

st.markdown('</div>', unsafe_allow_html=True)

# FUNCIÓN SI/NO
def pregunta_binaria(texto):
    opcion = st.radio(
        texto,
        ["Sí", "No"],
        horizontal=True
    )

    return 1 if opcion == "Sí" else 0

# PREGUNTAS
st.markdown('<div class="question-box">', unsafe_allow_html=True)
gaming = pregunta_binaria("🎮 ¿Te interesa usar la PC para gaming?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="question-box">', unsafe_allow_html=True)
programacion = pregunta_binaria("👨‍💻 ¿Planeas usarla para programación?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="question-box">', unsafe_allow_html=True)
ciberseguridad = pregunta_binaria("🔐 ¿Te interesa la ciberseguridad?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="question-box">', unsafe_allow_html=True)
oficina = pregunta_binaria("📄 ¿La usarás para trabajo de oficina?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="question-box">', unsafe_allow_html=True)
pc_antigua = pregunta_binaria("🖥️ ¿Tu computadora es antigua?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="question-box">', unsafe_allow_html=True)
facilidad = pregunta_binaria("✨ ¿Buscas facilidad de uso?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="question-box">', unsafe_allow_html=True)
avanzado = pregunta_binaria("⚙️ ¿Te consideras un usuario avanzado?")
st.markdown('</div>', unsafe_allow_html=True)

# DATAFRAME
datos = pd.DataFrame({
    'ram_gb':[ram],
    'gaming':[gaming],
    'programacion':[programacion],
    'ciberseguridad':[ciberseguridad],
    'uso_oficina':[oficina],
    'pc_antigua':[pc_antigua],
    'facilidad_uso':[facilidad],
    'usuario_avanzado':[avanzado]
})

# BOTÓN PREDICCIÓN
if st.button("🚀 Analizar y Recomendar"):

    with st.spinner("Analizando perfil del usuario..."):
        time.sleep(2)

    prediccion = modelo.predict(datos)

    sistemas = {
        0:"👾 Kali Linux",
        1:"👾 Linux Mint",
        2:"👾 Ubuntu",
        3:"👾 Windows"
    }

    resultado = sistemas[prediccion[0]]

    st.balloons()

    st.markdown(f"""
    <div class="result-box">
        <div class="result-text">
            Sistema Operativo Recomendado:<br><br>
            {resultado}
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    Desarrollado por Desireé Huaytalla <br>
    Código ISIL: 73037215
</div>
""", unsafe_allow_html=True)

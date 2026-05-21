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

/* Título principal */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00ffe1;
    margin-bottom: 10px;
    text-shadow: 0px 0px 15px #00ffe1;
}

/* Subtítulo */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #bdbdbd;
    margin-bottom: 40px;
}

/* Caja de preguntas */
.question-box {
    background: #1a1d29;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid #2f3547;
    box-shadow: 0px 0px 10px rgba(0,255,225,0.1);
}

/* Resultado */
.result-box {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    animation: aparecer 1s ease-in-out;
    margin-top: 30px;
}

.result-text {
    font-size: 28px;
    font-weight: bold;
    color: white;
}

@keyframes aparecer {
    from {
        opacity: 0;
        transform: scale(0.7);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Botón principal */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00ffe1, #007cf0);
    color: black;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px #00ffe1;
}

/* Créditos */
.footer {
    margin-top: 60px;
    text-align: center;
    color: gray;
    font-size: 14px;
}

/* Caja del colab */
.colab-box {
    background: linear-gradient(135deg, #ff9800, #ff5722);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 40px;
    animation: aparecer 1s ease-in-out;
}

.colab-box a {
    color: white;
    text-decoration: none;
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown('<div class="main-title">💻 OS RECOMMENDER AI</div>', unsafe_allow_html=True)

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
        0:"🟢 Kali Linux",
        1:"🟢 Linux Mint",
        2:"🟢 Ubuntu",
        3:"🟢 Windows"
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

import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
modelo = joblib.load('modelos/modelo_random_forest.pkl')

st.title("Sistema Inteligente de Recomendación de Sistemas Operativos")

st.write("Complete la información del usuario:")

ram = st.selectbox("RAM (GB)", [2,4,8,16,32])

gaming = st.selectbox("¿Uso para gaming?", [0,1])
programacion = st.selectbox("¿Uso para programación?", [0,1])
ciberseguridad = st.selectbox("¿Interés en ciberseguridad?", [0,1])
oficina = st.selectbox("¿Uso de oficina?", [0,1])
pc_antigua = st.selectbox("¿PC antigua?", [0,1])
facilidad = st.selectbox("¿Busca facilidad de uso?", [0,1])
avanzado = st.selectbox("¿Usuario avanzado?", [0,1])

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

if st.button("Recomendar Sistema Operativo"):

    prediccion = modelo.predict(datos)

    sistemas = {
        0:"Kali Linux",
        1:"Linux Mint",
        2:"Ubuntu",
        3:"Windows"
    }

    resultado = sistemas[prediccion[0]]

    st.success(f"El sistema operativo recomendado es: {resultado}")

st.markdown("---")
st.write("Nombre: Desireé Huaytalla")
st.write("Código ISIL: 73037215")

st.markdown("[Ver cuaderno de Google Colab](https://colab.research.google.com/drive/1miYl2oYG8pRhgRQ3JACep9QiiCkxiQg7?usp=sharing)")
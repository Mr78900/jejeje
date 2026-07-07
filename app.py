import streamlit as st

# ===============================
# CONFIGURACIÓN
# ===============================

PASSWORD = st.secrets["PASSWORD"]

st.set_page_config(
    page_title="Acceso protegido",
    page_icon="🔒",
    layout="centered"
)

# ===============================
# ESTILOS
# ===============================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#f2f2f7,#dfe5ec);
}

.main > div{
    max-width:650px;
}

.card{
    background:white;
    padding:40px;
    border-radius:22px;
    box-shadow:0 15px 35px rgba(0,0,0,.12);
    text-align:center;
}

h1{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# INTERFAZ
# ===============================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<h1 style='font-size:60px;'>🔒</h1>",
    unsafe_allow_html=True
)

st.image("foto.png", use_container_width=True)

st.title("Acceso protegido")

st.write("Introduce la contraseña para desbloquear la descarga.")

password = st.text_input(
    "Contraseña",
    type="password"
)

if st.button("Desbloquear"):

    if password == PASSWORD:

        st.success("Acceso concedido ✅")

        with open("archivo.zip","rb") as file:

            st.download_button(
                "📦 Descargar ZIP",
                data=file,
                file_name="archivo.zip",
                mime="application/zip"
            )

    else:

        st.error("❌ Contraseña incorrecta")

st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
from pathlib import Path


def create_sidebar():
    with st.sidebar:
        logo_path = Path(__file__).parent.parent / "logo.png"

        if logo_path.exists():
            st.image(str(logo_path), width=80)
        else:
            st.markdown("### 💻")

        st.markdown("### CodeCraft AI")
        st.markdown("*Enterprise Development Platform*")

        st.markdown("---")
        st.markdown("**Navigation**")
        page = st.radio(
            "Navigate to:",
            ["Home", "Code Generator", "Code Improver", "Code Explainer",
             "Debug Helper", "Code Converter", "Documentation", "Code Formatter", "About"],
            index=0, label_visibility="collapsed"
        )

        st.markdown("---")
        st.markdown("**Configuration**")
        model = st.selectbox(
            "Model",
            ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "openai/gpt-oss-120b"],
            index=0
        )

        temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.3, step=0.1)

        st.markdown("---")
        st.markdown("*Powered by Groq AI*")

    return page, model, temperature
import streamlit as st
from modules.ui_components import create_sidebar
from modules.code_generator import CodeGenerator
from modules.code_improver import CodeImprover
from modules.code_explainer import CodeExplainer
from modules.debug_helper import DebugHelper
from modules.code_converter import CodeConverter
from modules.doc_generator import DocGenerator
from modules.code_formatter import CodeFormatter
from modules.error_handler import validate_input

st.set_page_config(page_title="CodeCraft AI", page_icon="💻", layout="wide")

st.markdown("""
<style>
    .stApp { background: #f0f9ff; }
    .header-banner {
        background: linear-gradient(135deg, #1e3a8a 0%, #0284c7 50%, #0ea5e9 100%);
        color: white;
        padding: 32px 40px;
        border-radius: 16px;
        margin-bottom: 28px;
    }
    .header-banner h1 { margin: 0; font-size: 2rem; font-weight: 700; }
    .header-banner p { margin: 8px 0 0; opacity: 0.95; }
    .metric-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #e0f2fe;
        box-shadow: 0 2px 8px rgba(2, 132, 199, 0.08);
    }
    .metric-value { font-size: 2rem; font-weight: 700; color: #0284c7; }
    .metric-label { color: #64748b; font-size: 0.8rem; margin-top: 8px; }
</style>
""", unsafe_allow_html=True)

generator = CodeGenerator()
improver = CodeImprover()
explainer = CodeExplainer()
debugger = DebugHelper()
converter = CodeConverter()
doc_gen = DocGenerator()
formatter = CodeFormatter()

page, selected_model, temperature = create_sidebar()

if page == "Home":
    st.markdown('<div class="header-banner"><h1>CodeCraft AI</h1><p>Enterprise Development Platform</p></div>',
                unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            '<div class="metric-card"><div class="metric-value">3</div><div class="metric-label">AI Models</div></div>',
            unsafe_allow_html=True)
    with col2:
        st.markdown(
            '<div class="metric-card"><div class="metric-value">8</div><div class="metric-label">Features</div></div>',
            unsafe_allow_html=True)
    with col3:
        st.markdown(
            '<div class="metric-card"><div class="metric-value">~2s</div><div class="metric-label">Response</div></div>',
            unsafe_allow_html=True)
    with col4:
        st.markdown(
            '<div class="metric-card"><div class="metric-value">99%</div><div class="metric-label">Uptime</div></div>',
            unsafe_allow_html=True)

elif page == "Code Generator":
    st.markdown('<div class="header-banner"><h1>Code Generator</h1><p>Generate production-ready code</p></div>',
                unsafe_allow_html=True)
    with st.form("gen_form", clear_on_submit=True):
        prompt = st.text_area("Requirement", placeholder="Example: Create a function to calculate factorial",
                              height=120)
        submitted = st.form_submit_button("Generate")
    if submitted and validate_input(prompt, 10):
        with st.spinner("Generating..."):
            res = generator.generate_code(prompt, selected_model)
        if "Error" not in res:
            st.success("Code generated!")
            st.code(res, language="python")
        else:
            st.error(res)

elif page == "Code Improver":
    st.markdown('<div class="header-banner"><h1>Code Improver</h1><p>Optimize your code</p></div>',
                unsafe_allow_html=True)
    with st.form("imp_form", clear_on_submit=True):
        code = st.text_area("Code", placeholder="def calc(a,b):\n    return a+b", height=200)
        submitted = st.form_submit_button("Improve")
    if submitted and validate_input(code, 10):
        with st.spinner("Improving..."):
            res = improver.improve_code(code, selected_model)
        if "Error" not in res:
            st.success("Code improved!")
            st.code(res, language="python")
        else:
            st.error(res)

elif page == "Code Explainer":
    st.markdown('<div class="header-banner"><h1>Code Explainer</h1><p>Understand any code</p></div>',
                unsafe_allow_html=True)
    with st.form("exp_form", clear_on_submit=True):
        code = st.text_area("Code", placeholder="def fibonacci(n):\n    if n <= 1:\n        return n", height=200)
        submitted = st.form_submit_button("Explain")
    if submitted and validate_input(code, 10):
        with st.spinner("Explaining..."):
            res = explainer.explain_code(code, selected_model)
        if "Error" not in res:
            st.success("Explanation ready!")
            st.markdown(res)
        else:
            st.error(res)

elif page == "Debug Helper":
    st.markdown('<div class="header-banner"><h1>Debug Helper</h1><p>Find and fix errors</p></div>',
                unsafe_allow_html=True)
    with st.form("dbg_form", clear_on_submit=True):
        code = st.text_area("Code", placeholder="def divide(a, b):\n    return a / b", height=160)
        err = st.text_area("Error", placeholder="ZeroDivisionError", height=60)
        submitted = st.form_submit_button("Debug")
    if submitted and validate_input(code, 10):
        with st.spinner("Debugging..."):
            res = debugger.debug_code(code, err, selected_model)
        if "Error" not in res:
            st.success("Debug complete!")
            st.markdown(res)
        else:
            st.error(res)

elif page == "Code Converter":
    st.markdown('<div class="header-banner"><h1>Code Converter</h1><p>Convert between languages</p></div>',
                unsafe_allow_html=True)
    with st.form("conv_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1: src = st.selectbox("From", ["Python", "JavaScript", "Java", "C++"])
        with c2: tgt = st.selectbox("To", ["Python", "JavaScript", "Java", "C++"])
        code = st.text_area("Code", placeholder="def hello():\n    print('Hi')", height=160)
        submitted = st.form_submit_button("Convert")
    if submitted and validate_input(code, 10):
        if src == tgt:
            st.warning("Select different languages")
        else:
            with st.spinner("Converting..."):
                res = converter.convert_code(code, src, tgt, selected_model)
            if "Error" not in res:
                st.success("Converted!")
                st.code(res, language=tgt.lower())
            else:
                st.error(res)

elif page == "Documentation":
    st.markdown('<div class="header-banner"><h1>Documentation</h1><p>Generate docs</p></div>', unsafe_allow_html=True)
    with st.form("doc_form", clear_on_submit=True):
        code = st.text_area("Code", placeholder="def validate(email):\n    return '@' in email", height=160)
        std = st.selectbox("Standard", ["Google", "Sphinx", "NumPy"])
        submitted = st.form_submit_button("Generate")
    if submitted and validate_input(code, 10):
        with st.spinner("Generating..."):
            res = doc_gen.generate_docs(code, std.lower(), selected_model)
        if "Error" not in res:
            st.success("Docs generated!")
            st.markdown(res)
        else:
            st.error(res)

elif page == "Code Formatter":
    st.markdown('<div class="header-banner"><h1>Code Formatter</h1><p>Format code</p></div>', unsafe_allow_html=True)
    with st.form("fmt_form", clear_on_submit=True):
        code = st.text_area("Code", placeholder="x=10;y=20", height=160)
        std = st.selectbox("Standard", ["PEP 8", "Black", "Google"])
        submitted = st.form_submit_button("Format")
    if submitted and validate_input(code, 5):
        with st.spinner("Formatting..."):
            res = formatter.format_code(code, std.lower(), selected_model)
        if "Error" not in res:
            st.success("Formatted!")
            st.code(res, language="python")
        else:
            st.error(res)

elif page == "About":
    st.markdown('<div class="header-banner"><h1>About</h1></div>', unsafe_allow_html=True)
    st.markdown("**CodeCraft AI** - Enterprise Development Platform\n\nPowered by Groq AI")
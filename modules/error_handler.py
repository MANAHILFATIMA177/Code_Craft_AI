import streamlit as st

def handle_error(error_message, error_type="general"):
    error_messages = {
        "api": "API Error: Unable to connect.",
        "rate_limit": "Rate Limit: Too many requests.",
        "empty_input": "Input Required: Please provide valid input.",
        "general": f"Error: {error_message}"
    }
    st.error(error_messages.get(error_type, error_messages["general"]))
    return False

def validate_input(user_input, min_length=5):
    if not user_input or len(user_input.strip()) < min_length:
        handle_error("Input too short", "empty_input")
        return False
    return True
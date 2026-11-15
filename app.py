import streamlit as st

menu = {
    "cupcake": 3.75,
    "cookie": 2.00,
    "muffin": 2.75,
    "scone": 3.25,
    "brownie": 3.00,
}

sample_sales = {
    "Product": ["cupcake", "cookie", "muffin", "scone", "brownie"],
    "Units sold": [18, 30, 12, 10, 15],
}

def apply_discount(subtotal):
    pass

def shipping_fee(subtotal):
    pass

st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")
st.info("Starter file loaded.")

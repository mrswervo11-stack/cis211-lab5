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
    if subtotal >= 50.00:
        return round(subtotal * 0.90, 2)
    return subtotal

def shipping_fee(subtotal):
    if subtotal >= 35.00:
        return 0.0
    return 5.99

st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")

st.write("Delivery for 34.99:", shipping_fee(34.99))
st.write("Delivery for 35.00:", shipping_fee(35.00))
st.write("Items after discount for 49.99:", apply_discount(49.99))
st.write("Items after discount for 50.00:", apply_discount(50.00))

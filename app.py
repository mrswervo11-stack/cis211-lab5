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

# Apply a 10% discount to purchases of $50 or more.
def apply_discount(subtotal):
    if subtotal >= 50.00:
        return round(subtotal * 0.90, 2)
    return subtotal

# Delivery is free when the original subtotal reaches $35.
def shipping_fee(subtotal):
    if subtotal >= 35.00:
        return 0.00
    return 5.99

st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")

st.sidebar.header("Order Details")

customer_name = st.sidebar.text_input("Customer name")
product = st.sidebar.selectbox("Product", list(menu.keys()))
quantity = st.sidebar.number_input(
    "Quantity", min_value=1, max_value=30, value=1, step=1
)
fulfillment = st.sidebar.radio(
    "Fulfillment", ["Pickup", "Delivery"]
)
show_chart = st.sidebar.checkbox("Show sample sales chart")

# Calculate the quote using the selected product and quantity.
unit_price = menu[product]
subtotal = round(unit_price * quantity, 2)
discounted_subtotal = apply_discount(subtotal)
discount_amount = round(subtotal - discounted_subtotal, 2)

if fulfillment == "Delivery":
    delivery_fee = shipping_fee(subtotal)
else:
    delivery_fee = 0.00

total = round(discounted_subtotal + delivery_fee, 2)

st.header("Order Quote")

col1, col2 = st.columns(2)

with col1:
    st.write(f"Product: {product}")
    st.write(f"Quantity: {quantity}")
    st.write(f"Unit price: ${unit_price:.2f}")
    st.write(f"Fulfillment: {fulfillment}")

with col2:
    st.write(f"Subtotal: ${subtotal:.2f}")
    st.write(f"Discount: ${discount_amount:.2f}")
    st.write(f"Delivery fee: ${delivery_fee:.2f}")
    st.metric("Final Total", f"${total:.2f}")

st.header("Bakery Menu")

st.table({
    "Product": list(menu.keys()),
    "Price": [f"${price:.2f}" for price in menu.values()]
})

if show_chart:
    st.header("Fictional Sample Sales")
    st.bar_chart(
        sample_sales, x="Product", y="Units sold"
    )

# Check that the customer entered a nonblank name.
if st.button("Check quote"):
    if not customer_name.strip():
        st.warning("Please enter your customer name.")
    else:
        st.success(
            f"Quote checked for {customer_name.strip()}."
        )

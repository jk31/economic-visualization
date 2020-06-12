import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

st.title("Monopol")

y = np.linspace(0.001, 15, 100)
p = st.sidebar.slider("Intersection of Pricefunction", value=10.0, min_value=1.0, max_value=20.0, step=0.1)
a = st.sidebar.slider("Slope of Pricefunction", value=1.5, min_value=1.0, max_value=5.0, step=0.1)
c_factor = 0.02

#@st.cache
def monopol_figure(y, p, a, c_factor):
    price = p - a*y
    revenue = price * y
    revenue_marginal = p - 2*a*y
    costs = c_factor * y**3
    costs_marginal = c_factor*3 * y**2
    profit = revenue - costs
    # e = (1/p'(y)) *  (p/y)
    e = (1/-a) * ((price)/y)
    return price, revenue, revenue_marginal, costs, costs_marginal, profit, e

price, revenue, revenue_marginal, costs, costs_marginal, profit, e = monopol_figure(y, p, a, c_factor)

st.write(f"Intersection={p}, Slope={a}")

if st.sidebar.checkbox("Price", value=True):
    plt.plot(y, price, color="blue", label="Price")
if st.sidebar.checkbox("Costs"):
    plt.plot(y, costs, color="red", label="Costs")
if st.sidebar.checkbox("Marginal Costs"):
    plt.plot(y, costs_marginal, color="red", ls="dashed", label="Marginal Costs")
if st.sidebar.checkbox("Revenue"):
    plt.plot(y, revenue, color="purple", label="Revenue")
if st.sidebar.checkbox("Marginal Revenue"):
    plt.plot(y, revenue_marginal, color="purple", ls="dashed", label="Marginal Revenue")
if st.sidebar.checkbox("Profit"):
    plt.plot(y, profit, color="green", label="Profit")
if st.sidebar.checkbox("Elasticity"):
    plt.plot(y, e, color="orange", label="Elasticity")

plt.xlabel("Quantity Y")
plt.legend()

ax = plt.axes()
plt.axhline(y=0, color="black", linewidth=1)
ax.set_xlim([0, 15])
ax.set_ylim([-5, 26])

st.pyplot()
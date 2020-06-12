from math import sqrt

import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

topic = st.selectbox("Select a topic", options=["Monopol", "Gaming/Shirking"], index=0) 

st.header(f"{topic}")

if topic == "Monopol":
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

    ax = plt.axes()
    if st.sidebar.checkbox("Price", value=True):
        ax.plot(y, price, color="blue", label="Price")
    if st.sidebar.checkbox("Costs"):
        ax.plot(y, costs, color="red", label="Costs")
    if st.sidebar.checkbox("Marginal Costs"):
        ax.plot(y, costs_marginal, color="red", ls="dashed", label="Marginal Costs")
    if st.sidebar.checkbox("Revenue"):
        ax.plot(y, revenue, color="purple", label="Revenue")
    if st.sidebar.checkbox("Marginal Revenue"):
        ax.plot(y, revenue_marginal, color="purple", ls="dashed", label="Marginal Revenue")
    if st.sidebar.checkbox("Profit"):
        ax.plot(y, profit, color="green", label="Profit")
    if st.sidebar.checkbox("Elasticity"):
        ax.plot(y, e, color="orange", label="Elasticity")

    plt.xlabel("Quantity Y")
    plt.legend()

    plt.axhline(y=0, color="black", linewidth=1)
    ax.set_xlim([0, 15])
    ax.set_ylim([-5, 26])

    st.pyplot()

elif topic == "Gaming/Shirking":

    premium = np.linspace(0, 5, 100) 
    p = st.sidebar.slider("rho", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    b = st.sidebar.slider("beta", value=0.8, min_value=0.0, max_value=1.5, step=0.01)

    st.write(f"Rho={p}, Beta={b}")

    #@st.cache
    def gaming_figure(premium, p, b):
        gaming = premium/2 * (sqrt(p**2 + (1-p)**2) * sqrt(b**2 + (1-b)**2) - (b * p + (1-b)*(1-p)))
        shirking = ((b**2 + (1-b)**2)/4) - (premium/2 * sqrt((p**2 + (1-p)**2)/(b**2 + (1-b)**2)) * (b**2 + (1-b)**2) - (premium/2)**2 * (p**2 + (1-p)**2))
        return gaming, shirking

    gaming, shirking = gaming_figure(premium, p, b)

    ax = plt.axes()
    ax.plot(premium, gaming, color="black", label="Gaming")
    ax.plot(premium, shirking, color="brown", label="Shirking")
    ax.plot(premium, gaming+shirking, color="blue", label="Gaming+Shirking", linestyle='--')

    ax.set_xlim([0, 2])
    ax.set_ylim([0, 0.6])
        
    plt.xlabel("$ \pi^I $")
    plt.ylabel("Costs")
    plt.legend()

    st.pyplot()
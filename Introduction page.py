import streamlit as st

st.set_page_config(
    page_title="E-Commerce Delivery Optimization",
    page_icon="🚚",
    layout="wide"
)

st.title("E-Commerce Delivery Optimization")
st.subheader("Using Flow Model + Routing Strategies")

st.markdown("---")

st.write("""
Welcome to the **E-Commerce Delivery Optimization System**.

This project demonstrates how logistics companies optimize delivery routes
between warehouses and distribution hubs using **graph algorithms and flow models**.
""")

st.markdown("### Project Pages")

st.write("""
Use the sidebar to navigate through the project:

📘 **E-commerce Delivery Optimization**  
- Problem definition  
- Mathematical model  
- Flow optimization approach  
- Routing strategies

🚚 **Delivery Optimizer Module**  
- Interactive logistics network builder  
- Add or remove hubs  
- Create delivery routes  
- Visualize delivery network

💻 **Code Explanation**  
- Step-by-step explanation of the implementation  
- Graph modeling using NetworkX  
- Shortest path computation  
""")


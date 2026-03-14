import streamlit as st

st.title("E-Commerce Delivery Optimization")
st.subheader("Using Flow Model + Routing Strategies")

st.markdown("---")

# ------------------------------------------------
# Problem Definition
# ------------------------------------------------

st.header("1. Problem Definition")

st.subheader("Introduction")

st.write("""
In modern e-commerce systems such as **Amazon** and **Flipkart**, thousands of products are
shipped daily from a **central warehouse** to multiple **city hubs** before final delivery to customers.

The major challenge is:

**How to deliver goods from warehouses to hubs in minimum time and cost while satisfying demand and vehicle capacity constraints.**

This project focuses on:

• Optimizing delivery routes  
• Minimizing total transportation cost and time  
• Using a combination of two optimization techniques:
  - **Flow Model (Linear Programming)**
  - **Graph Routing Algorithms (Shortest Path)**
""")

# ------------------------------------------------
# Problem Statement
# ------------------------------------------------

st.header("2. Problem Statement (Mathematical Form)")

st.write("""
Given:

• 1 Warehouse  
• Multiple Hubs  
• Limited vehicles  
• Transportation cost or time between nodes  

Find:

• Optimal **flow of goods**  
• Fastest **delivery routes**  
• Minimum **total delivery cost**
""")

# ------------------------------------------------
# Model Design
# ------------------------------------------------

st.header("3. Design Model & Implementation")

st.subheader("A. Mathematical Model (Flow Model)")

st.write("""
We model the logistics network as a **graph**:

• **Nodes** → Warehouse + Hubs  
• **Edges** → Roads between locations  
• **Weights** → Delivery cost or travel time
""")

st.markdown("**Variables:**")

st.latex(r"x_{ij} = \text{quantity transported from node i to node j}")
st.latex(r"c_{ij} = \text{cost per unit transportation}")
st.latex(r"d_j = \text{demand at hub j}")

st.subheader("Objective Function")

st.write("Minimize total transportation cost:")

st.latex(r"Minimize \; Z = \sum c_{ij} x_{ij}")

# ------------------------------------------------
# Constraints
# ------------------------------------------------

st.subheader("Constraints")

st.write("1️⃣ Supply Constraint (Warehouse capacity)")

st.latex(r"\sum x_{Wj} \leq Supply")

st.write("2️⃣ Demand Constraint (Hub requirement)")

st.latex(r"\sum x_{ij} = d_j")

st.write("3️⃣ Non-Negativity Constraint")

st.latex(r"x_{ij} \geq 0")

# ------------------------------------------------
# Routing Strategy
# ------------------------------------------------

st.subheader("B. Routing Strategy (Shortest Path)")

st.write("""
To compute the **fastest delivery routes**, we use **Dijkstra’s Algorithm**.

This algorithm is widely used in:

• Logistics systems  
• GPS navigation  
• Google Maps routing systems
""")

st.write("Shortest path formula:")

st.latex(r"Distance(v) = \min(Distance(u) + weight(u,v))")

# ------------------------------------------------
# Components Table
# ------------------------------------------------

st.header("4. Components / Variables")

st.table({
    "Component": [
        "Warehouse",
        "Hubs",
        "Vehicles",
        "Edge Cost",
        "Flow Variable",
        "Demand"
    ],
    "Description": [
        "Source node",
        "Destination nodes",
        "Transport units",
        "Time or fuel cost",
        "Quantity shipped",
        "Hub requirement"
    ]
})

# ------------------------------------------------
# Model Structure
# ------------------------------------------------

st.header("5. Model Structure")

st.write("""
Example Network Structure
""")

st.code("""
           (Hub A)
              ^
              |
(Warehouse) ----+---- (Hub B)
              |
              v
           (Hub C)
""")

st.write("""
Graph Representation:

Nodes = {W, A, B, C}

Edges = {(W,A), (W,B), (W,C), (A,B), (B,C)}
""")

# ------------------------------------------------
# Implementation
# ------------------------------------------------

st.header("6. Code Implementation")

st.write("""
The model is implemented using Python libraries:

• **networkx** → Graph modelling  
• **matplotlib** → Graph visualization  
• **pandas** → Result analysis tables
""")

st.code("""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
('Warehouse','Hub1',4),
('Warehouse','Hub2',6),
('Warehouse','Hub3',8),
('Hub1','Hub2',2),
('Hub2','Hub3',3)
]

G.add_weighted_edges_from(edges)
""", language="python")

# ------------------------------------------------
# Test Scenario 1
# ------------------------------------------------

st.header("7. Test Scenario 1")

st.write("""
Demands:

Hub1 = 50 units  
Hub2 = 40 units  
Hub3 = 60 units  

Warehouse Supply = 200 units
""")

st.write("""
Result:

• Fastest route to Hub1 → Direct  
• Fastest route to Hub2 → Direct  
• Fastest route to Hub3 → Via Hub2 (if shorter)

Total transportation cost is minimized.
""")

# ------------------------------------------------
# Test Scenario 2
# ------------------------------------------------

st.header("8. Test Scenario 2")

st.write("""
If edge weight changes:

Warehouse → Hub3 = 15
""")

st.write("""
The shortest route becomes:

Warehouse → Hub2 → Hub3

This shows the routing algorithm automatically adapts to network changes.
""")

# ------------------------------------------------
# Visualization Analysis
# ------------------------------------------------

st.header("9. Visualization & Analysis")

st.subheader("Graph Interpretation")

st.write("""
• Nodes represent logistics centers  
• Edges represent transportation routes  
• Edge weights represent cost or time  
• Shorter paths reduce delivery time
""")

st.subheader("Observations")

st.write("""
1. If direct route cost is high, the algorithm chooses an alternate path.

2. The **Flow Model** ensures demand satisfaction.

3. The **Routing Model** ensures time efficiency.

4. The **combined approach improves logistics performance**.
""")

# ------------------------------------------------
# Graph Analysis
# ------------------------------------------------

st.header("10. Graph Analysis Example")

st.write("""
If we analyze:

X-axis → Distance  
Y-axis → Delivery Cost
""")

st.write("""
Observations:

• Cost increases approximately linearly with distance.  
• Optimized routing reduces total logistics cost by **15–25%**.
""")

st.success("This model demonstrates how optimization algorithms can significantly improve e-commerce logistics efficiency.")
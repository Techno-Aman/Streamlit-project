import streamlit as st

st.title("Code Explanation")
st.subheader("E-Commerce Delivery Route Optimization Application")

st.markdown("---")

# ------------------------------------------------
# Overview
# ------------------------------------------------

st.header("1. Overview")

st.write("""
This application simulates an **E-commerce delivery network optimizer**.

The system allows users to:

• Add or remove logistics locations (Warehouse / Hubs)  
• Create delivery routes between locations  
• Visualize the delivery network as a graph  
• Compute the **shortest delivery path** between two locations  

The application is implemented using:

• Streamlit → Web interface  
• NetworkX → Graph modelling and shortest path algorithms  
• Matplotlib → Graph visualization
""")

# ------------------------------------------------
# Import Libraries
# ------------------------------------------------

st.header("2. Importing Required Libraries")

st.code("""
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
""", language="python")

st.write("""
• **Streamlit** is used to build the interactive web interface.

• **NetworkX** is used to create and manipulate the delivery network graph.

• **Matplotlib** is used to visualize the graph structure.
""")

# ------------------------------------------------
# Application Title
# ------------------------------------------------

st.header("3. Application Title and Description")

st.code("""
st.title("E-commerce Delivery Route Optimization")
st.write("Find the shortest delivery routes between warehouse and hubs.")
""", language="python")

st.write("""
These commands display the main title and description at the top of the application.
""")

# ------------------------------------------------
# Custom UI Styling
# ------------------------------------------------

st.header("4. User Interface Styling")

st.write("""
Custom CSS styling is applied to improve the appearance of input fields.
""")

st.code("""
st.markdown(\"\"\"
<style>
div[data-baseweb="input"]{
border:2px solid white;
border-radius:8px;
}
</style>
\"\"\", unsafe_allow_html=True)
""", language="python")

st.write("""
This CSS styling adds **white borders and rounded corners** to input fields
to improve the visual appearance of the application.
""")

# ------------------------------------------------
# Graph Creation
# ------------------------------------------------

st.header("5. Graph Initialization")

st.code("""
G = nx.Graph()
""", language="python")

st.write("""
A graph object is created using **NetworkX**.

In this graph:

• Nodes represent **Warehouse and Hubs**  
• Edges represent **delivery routes between locations**  
• Edge weights represent **distance or cost**
""")

# ------------------------------------------------
# Session State
# ------------------------------------------------

st.header("6. Session State (Dynamic Data Storage)")

st.code("""
if "nodes" not in st.session_state:
    st.session_state.nodes = ["Warehouse", "Hub1", "Hub2"]
""", language="python")

st.write("""
Streamlit's **session_state** stores data while the app is running.

It keeps track of:

• Existing locations (nodes)  
• Delivery routes (edges)
""")

# ------------------------------------------------
# Location Management
# ------------------------------------------------

st.header("7. Managing Locations")

st.write("Users can dynamically add or remove hubs.")

st.code("""
new_node = st.sidebar.text_input("Add Hub/Warehouse")

if st.sidebar.button("Add Location"):
    st.session_state.nodes.append(new_node)
""", language="python")

st.write("""
This allows users to **add new delivery locations** to the network.
""")

st.code("""
remove_node = st.sidebar.selectbox("Remove Location", st.session_state.nodes)
""", language="python")

st.write("""
Users can also remove a location from the system.
""")

# ------------------------------------------------
# Edge Removal Logic
# ------------------------------------------------

st.header("8. Removing Routes When Location is Deleted")

st.code("""
st.session_state.edges = [
edge for edge in st.session_state.edges
if edge[0] != remove_node and edge[1] != remove_node
]
""", language="python")

st.write("""
When a location is removed, all routes connected to that location
are also deleted automatically.
""")

# ------------------------------------------------
# Adding Routes
# ------------------------------------------------

st.header("9. Adding Delivery Routes")

st.code("""
node1 = st.sidebar.selectbox("From", st.session_state.nodes)
node2 = st.sidebar.selectbox("To", st.session_state.nodes)

distance = st.sidebar.number_input("Distance", min_value=1)
""", language="python")

st.write("""
Users define a delivery route between two locations and specify the distance.
""")

st.code("""
st.session_state.edges.append((node1, node2, distance))
""", language="python")

st.write("""
The route is stored as an **edge with a weight** in the graph.
""")

# ------------------------------------------------
# Graph Visualization
# ------------------------------------------------

st.header("10. Graph Visualization")

st.code("""
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
""", language="python")

st.write("""
The graph is visualized using a **spring layout**, which positions nodes in a balanced way.

Nodes represent locations and edges represent transportation routes.
""")

# ------------------------------------------------
# Shortest Path Calculation
# ------------------------------------------------

st.header("11. Shortest Path Algorithm")

st.code("""
path = nx.shortest_path(G, start, end, weight="weight")
""", language="python")

st.write("""
The shortest path between two locations is calculated using
**Dijkstra's algorithm** provided by NetworkX.
""")

st.code("""
distance = nx.shortest_path_length(G, start, end, weight="weight")
""", language="python")

st.write("""
This calculates the **minimum delivery distance or cost** between two nodes.
""")

# ------------------------------------------------
# Output Results
# ------------------------------------------------

st.header("12. Output Results")

st.code("""
st.success(f"Shortest Path: {path}")
st.success(f"Total Distance: {distance}")
""", language="python")

st.write("""
The optimized route and total distance are displayed to the user.
""")

# ------------------------------------------------
# Conclusion
# ------------------------------------------------

st.header("13. Conclusion")

st.write("""
This system demonstrates how **graph algorithms can optimize logistics networks**.

The application allows:

• Dynamic creation of logistics networks  
• Visualization of delivery routes  
• Computation of optimal delivery paths  

Such techniques are widely used in modern logistics systems
to improve delivery efficiency and reduce operational costs.
""")
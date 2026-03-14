import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.markdown("""
<style>

/* Main app background */
.stApp{
    background-color: #000370;
}

/* Text color */
h1, h2, h3, p, label{
    color: white;
}

/* Sidebar background */
section[data-testid="stSidebar"]{
background: #0b1a25;
}

/* Neon titles */
h1, h2, h3 {
color:#00eaff;
text-shadow:0px 0px 10px #00eaff;
}

/* Buttons */
.stButton>button {
background-color:#001f2f;
color:#00eaff;
border:1px solid #00eaff;
border-radius:8px;
box-shadow:0px 0px 10px #00eaff;
}

/* Hover effect */
.stButton>button:hover {
background-color:#00334d;
color:white;
box-shadow:0px 0px 15px #00eaff;
}

/* Input boxes */
div[data-baseweb="input"]{
border:1px solid #00eaff;
border-radius:8px;
}

/* Select boxes */
div[data-baseweb="select"]{
border:1px solid #00eaff;
border-radius:8px;
}

/* Number input */
div[data-baseweb="base-input"]{
border:1px solid #00eaff;
border-radius:8px;
}

/* Graph container glow */
.css-1kyxreq{
border:1px solid #00eaff;
box-shadow:0px 0px 20px #00eaff;
padding:10px;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("E-commerce Delivery Route Optimization")

st.write("Find the shortest delivery routes between warehouse and hubs.")
st.markdown("""
<style>

/* Text input field */
div[data-baseweb="input"]{
    border:2px solid white !important;
    border-radius:8px;
}

/* Select box */
div[data-baseweb="select"]{
    border:2px solid white !important;
    border-radius:8px;
}

/* Number input */
div[data-baseweb="base-input"]{
    border:2px solid white !important;
    border-radius:8px;
}

/* Dropdown box for shortest path fields */
div[data-baseweb="popover"]{
    border:2px solid white !important;
}

</style>
""", unsafe_allow_html=True)

# Graph
G = nx.Graph()

# Initialize session state
if "nodes" not in st.session_state:
    st.session_state.nodes = ["Warehouse", "Hub1", "Hub2"]

if "edges" not in st.session_state:
    st.session_state.edges = []

# ---------------------------
# Sidebar Controls
# ---------------------------

st.sidebar.header("Manage Locations")

# Add new hub/warehouse
new_node = st.sidebar.text_input("Add Hub/Warehouse")

if st.sidebar.button("Add Location"):

    if new_node and new_node not in st.session_state.nodes:
        st.session_state.nodes.append(new_node)
        st.success(f"Location '{new_node}' added successfully!")

    elif new_node in st.session_state.nodes:
        st.warning("Location already exists!")

    else:
        st.warning("Please enter a location name.")

# Remove hub/warehouse
remove_node = st.sidebar.selectbox("Remove Location", st.session_state.nodes)

if st.sidebar.button("Remove Location"):

    if remove_node != "Warehouse":

        st.session_state.nodes.remove(remove_node)

        # Remove edges connected to that node
        st.session_state.edges = [
            edge for edge in st.session_state.edges
            if edge[0] != remove_node and edge[1] != remove_node
        ]

        st.success(f"Location '{remove_node}' removed from the network.")

    else:
        st.error("Warehouse cannot be removed.")

# ---------------------------
# Add Route
# ---------------------------

st.sidebar.header("Add Delivery Route")

node1 = st.sidebar.selectbox("From", st.session_state.nodes)
node2 = st.sidebar.selectbox("To", st.session_state.nodes)

distance = st.sidebar.number_input("Distance", min_value=1)
if st.sidebar.button("Add Route"):
    st.session_state.edges.append((node1, node2, distance))
    st.success(f"Route added: {node1} → {node2} (Distance {distance})")

# ---------------------------
# Build Graph
# ---------------------------

G.add_weighted_edges_from(st.session_state.edges)

# ---------------------------
# Show Graph
# ---------------------------

st.subheader("Delivery Network")

fig, ax = plt.subplots()

pos = nx.spring_layout(G,seed = 42)

nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, ax=ax, font_size=10)

labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

st.pyplot(fig)

# ---------------------------
# Shortest Path
# ---------------------------

st.subheader("Find Shortest Delivery Path")

start = st.selectbox("Start Location", st.session_state.nodes)
end = st.selectbox("Destination", st.session_state.nodes)

if st.button("Calculate Shortest Path"):

    try:
        path = nx.shortest_path(G, start, end, weight="weight")
        distance = nx.shortest_path_length(G, start, end, weight="weight")

        st.success(f"Shortest Path: {path}")
        st.success(f"Total Distance: {distance}")

    except:
        st.error("No path exists between these locations.")
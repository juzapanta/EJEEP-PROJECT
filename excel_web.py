import pandas as pd
import streamlit as st
import time
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

sheet_idA = '16CwByzI3-J0o36W7vs4hZ1Ovmyc2uV0DhJH4Cj96rU8'

dfA = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_idA}/export?format=csv")

st.set_page_config(
    page_title="E-jeep Tracker",
    page_icon="https://cdn-icons-png.flaticon.com/512/9249/9249336.png"
)

line = st.selectbox(label="Choose E-jeep Line to view", options=["LINE A", "LINE B"])

def plot_map(title, cell_value, coords, place_coords, place_labels):
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the width and height as needed
    icon_path = 'pin.png'
    icon = plt.imread(icon_path)

    # Add icons and labels to the map
    for (x, y), label in zip(place_coords, place_labels):
        im = OffsetImage(icon, zoom=0.005)
        ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False)
        ax.add_artist(ab)
        ax.text(x + 0.1, y + 0.2, f' {label}', fontsize=8, verticalalignment='center_baseline', zorder=10)

    ax.plot(*zip(*coords), color='lightgray', label='Route')  
    ax.set_title(title, fontsize=14, pad=20)
    ax.axis('off')

    return fig, ax

def highlight_route(ax, start, end, line_coords):
    start_index = line_coords["coords"].index(line_coords["place_coords"][line_coords["place_labels"].index(start)])
    end_index = line_coords["coords"].index(line_coords["place_coords"][line_coords["place_labels"].index(end)])

    num_coords = len(line_coords["coords"])
    highlighted_x = []
    highlighted_y = []

    for i in range(start_index, end_index + 1):
        index = i % num_coords
        highlighted_x.append(line_coords["coords"][index][0])
        highlighted_y.append(line_coords["coords"][index][1])
    
    ax.plot(highlighted_x, highlighted_y, color='red', linewidth=2, label=f'Route {start} to {end}')
    ax.legend()

line_coords = {
    "LINE A": {
        "coords": [(13, 1), (10, 1), (10, 3), (10, 4), (8, 4), (8, 4.5), (11, 4.5), (11, 5), (12.5, 5), (14.5, 5), (15, 5), (13, 1)],
        "place_coords": [(13, 1), (10, 3), (8, 4), (11, 4.5), (12.5, 5), (14.5, 5)],
        "place_labels": ['Hagdan na Bato', 'Old Comm', 'Gate 1', 'Gate 2.5', 'Leong Hall', 'Xavier Hall']
    }, 
    "LINE B":{
        "coords": [(11,1),(15,1),(15,10),(15,17),(15,20),(14,20),(14,7.5),(10,7.5),(8,7.5),(8,5),(9,5),(9,1),(11,1)],
        "place_coords": [(11,1),(15,10),(15,17),(10,7.5),(8,5)],
        "place_labels": ['Xavier Hall','AJHS','ASHS FLC Building','ISO','Arete']
    }
}

if line == "LINE A":
    st.title("Line A")
    
    # A1
    A1 = dfA.iloc[0, 1] 
    fig, ax = plot_map("A1", A1, line_coords["LINE A"]["coords"], line_coords["LINE A"]["place_coords"], line_coords["LINE A"]["place_labels"])

    try:
        last_item = A1

        if last_item == "Hagdan na Bato":
            highlight_route(ax, "Hagdan na Bato", "Old Comm", line_coords["LINE A"])
        elif last_item == "Old Comm":
            highlight_route(ax, "Old Comm", "Gate 1", line_coords["LINE A"])
        elif last_item == "Gate 1":
            highlight_route(ax, "Gate 1", "Gate 2.5", line_coords["LINE A"])
        elif last_item == "Gate 2.5":
            highlight_route(ax, "Gate 2.5", "Leong Hall", line_coords["LINE A"])
        elif last_item == "Leong Hall":
            highlight_route(ax, "Leong Hall", "Xavier Hall", line_coords["LINE A"])
        elif last_item == "Xavier Hall":
            highlight_route(ax, "Xavier Hall", "Hagdan na Bato", line_coords["LINE A"])

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error highlighting route: {e}")
    
    # A2
    A2 = dfA.iloc[1, 1]  
    fig, ax = plot_map("A2", A2, line_coords["LINE A"]["coords"], line_coords["LINE A"]["place_coords"], line_coords["LINE A"]["place_labels"])
    
    try:
        last_item = A2

        if last_item == "Hagdan na Bato":
            highlight_route(ax, "Hagdan na Bato", "Old Comm", line_coords["LINE A"])
        elif last_item == "Old Comm":
            highlight_route(ax, "Old Comm", "Gate 1", line_coords["LINE A"])
        elif last_item == "Gate 1":
            highlight_route(ax, "Gate 1", "Gate 2.5", line_coords["LINE A"])
        elif last_item == "Gate 2.5":
            highlight_route(ax, "Gate 2.5", "Leong Hall", line_coords["LINE A"])
        elif last_item == "Leong Hall":
            highlight_route(ax, "Leong Hall", "Xavier Hall", line_coords["LINE A"])
        elif last_item == "Xavier Hall":
            highlight_route(ax, "Xavier Hall", "Hagdan na Bato", line_coords["LINE A"])

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error highlighting route: {e}")

    # A3
    A3 = dfA.iloc[2, 1]  
    fig, ax = plot_map("A3", A3, line_coords["LINE A"]["coords"], line_coords["LINE A"]["place_coords"], line_coords["LINE A"]["place_labels"])
    
    try:
        last_item = A3

        if last_item == "Hagdan na Bato":
            highlight_route(ax, "Hagdan na Bato", "Old Comm", line_coords["LINE A"])
        elif last_item == "Old Comm":
            highlight_route(ax, "Old Comm", "Gate 1", line_coords["LINE A"])
        elif last_item == "Gate 1":
            highlight_route(ax, "Gate 1", "Gate 2.5", line_coords["LINE A"])
        elif last_item == "Gate 2.5":
            highlight_route(ax, "Gate 2.5", "Leong Hall", line_coords["LINE A"])
        elif last_item == "Leong Hall":
            highlight_route(ax, "Leong Hall", "Xavier Hall", line_coords["LINE A"])
        elif last_item == "Xavier Hall":
            highlight_route(ax, "Xavier Hall", "Hagdan na Bato", line_coords["LINE A"])

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error highlighting route: {e}")

if line == "LINE B":
    st.title("Line B")
    
    # B1
    B1 = dfA.iloc[5, 1] 
    fig, ax = plot_map("B1", B1, line_coords["LINE B"]["coords"], line_coords["LINE B"]["place_coords"], line_coords["LINE B"]["place_labels"])

    try:
        last_item = B1

        if last_item == "Xavier Hall":
            highlight_route(ax, "Xavier Hall", "AJHS", line_coords["LINE B"])
        elif last_item == "AJHS":
            highlight_route(ax, "AJHS", "ASHS FLC Building", line_coords["LINE B"])
        elif last_item == "ASHS FLC Building":
            highlight_route(ax, "ASHS FLC Building", "ISO", line_coords["LINE B"])
        elif last_item == "ISO":
            highlight_route(ax, "ISO", "Arete", line_coords["LINE B"])
        elif last_item == "Arete":
            highlight_route(ax, "Arete", "Xavier Hall", line_coords["LINE B"])

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error highlighting route: {e}")
    
    # B2
    B2 = dfA.iloc[6, 1]  
    fig, ax = plot_map("B2", B2, line_coords["LINE B"]["coords"], line_coords["LINE B"]["place_coords"], line_coords["LINE B"]["place_labels"])

    try:
        last_item = B2

        if last_item == "Xavier Hall":
            highlight_route(ax, "Xavier Hall", "AJHS", line_coords["LINE B"])
        elif last_item == "AJHS":
            highlight_route(ax, "AJHS", "ASHS FLC Building", line_coords["LINE B"])
        elif last_item == "ASHS FLC Building":
            highlight_route(ax, "ASHS FLC Building", "ISO", line_coords["LINE B"])
        elif last_item == "ISO":
            highlight_route(ax, "ISO", "Arete", line_coords["LINE B"])
        elif last_item == "Arete":
            highlight_route(ax, "Arete", "Xavier Hall", line_coords["LINE B"])

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error highlighting route: {e}")
    
    # B3
    B3 = dfA.iloc[7, 1]  
    fig, ax = plot_map("B3", B3, line_coords["LINE B"]["coords"], line_coords["LINE B"]["place_coords"], line_coords["LINE B"]["place_labels"])

    try:
        last_item = B3

        if last_item == "Xavier Hall":
            highlight_route(ax, "Xavier Hall", "AJHS", line_coords["LINE B"])
        elif last_item == "AJHS":
            highlight_route(ax, "AJHS", "ASHS FLC Building", line_coords["LINE B"])
        elif last_item == "ASHS FLC Building":
            highlight_route(ax, "ASHS FLC Building", "ISO", line_coords["LINE B"])
        elif last_item == "ISO":
            highlight_route(ax, "ISO", "Arete", line_coords["LINE B"])
        elif last_item == "Arete":
            highlight_route(ax, "Arete", "Xavier Hall", line_coords["LINE B"])

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error highlighting route: {e}")

st.title("Line A Data")
st.write(dfA.head(3))

st.title("Line B Data")
st.write(dfA.iloc[5:8])

st.title("Express Data")
st.write(dfA.iloc[10:14])

time.sleep(60 * 1) 
st.experimental_rerun()

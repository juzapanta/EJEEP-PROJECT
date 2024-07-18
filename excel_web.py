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

line = st.selectbox(label="Choose E-jeep Line to view", options=["LINE A", "LINE B", "EXPRESS"])

def plot_map(title, cell_value, coords, place_coords, place_labels):
    fig, ax = plt.subplots()
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

    st.pyplot(fig)

line_coords = {
    "LINE A": {
        "coords": [(15, 1), (10, 1), (10, 3), (10, 4), (8, 4), (8, 4.5), (11, 4.5), (11, 5), (12.5, 5), (14.5, 5), (15, 5)],
        "place_coords": [(15, 1), (10, 3), (8, 4), (11, 4.5), (12.5, 5), (14.5, 5)],
        "place_labels": ['HAGDAN NA BATO', 'LS COVERED COURTS', 'GATE 1', 'JSEC', 'LEONG HALL', 'XAVIER HALL']
    }
}

if line == "LINE A":
    st.title("Line A")
    
    # A1
    A1 = dfA.iloc[1, 1] 
    plot_map("A1", A1, line_coords["LINE A"]["coords"], line_coords["LINE A"]["place_coords"], line_coords["LINE A"]["place_labels"])
    st.pyplot(plt)
    

    # A2
    A2 = dfA.iloc[2, 1]  
    plot_map("A2", A2, line_coords["LINE A"]["coords"], line_coords["LINE A"]["place_coords"], line_coords["LINE A"]["place_labels"])
    st.pyplot(plt)

    # A3
    A3 = dfA.iloc[3, 1]  
    plot_map("A3", A3, line_coords["LINE A"]["coords"], line_coords["LINE A"]["place_coords"], line_coords["LINE A"]["place_labels"])
    st.pyplot(plt)


st.title("Line A")
st.write(dfA.head(3))

st.title("Line B")
st.write(dfA.iloc[5:8])

st.title("Express")
st.write(dfA.iloc[10:14])


time.sleep(60 * 1) 
st.experimental_rerun()

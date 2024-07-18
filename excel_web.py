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

st.title("Line A")
st.write(dfA.head(3))

st.title("Line B")
st.write(dfA.iloc[5:8])

st.title("Express")
st.write(dfA.iloc[10:14])

coords = [(15, 1), (10, 1), (10, 3), (10, 4), (8, 4), (8, 4.5), (11, 4.5), (11, 5), (12.5, 5), (14.5, 5), (15, 5)]
x_coords = [15, 10, 10, 10, 8, 8, 11, 11, 12.5, 14.5, 15, 15]
y_coords = [1, 1, 3, 4, 4, 4.5, 4.5, 5, 5, 5, 5, 1]

place_coords = [(15, 1), (10, 3), (8, 4), (11, 4.5), (12.5, 5), (14.5, 5)]
place_labels = ['HAGDAN NA BATO', 'LS COVERED COURTS', 'GATE 1', 'JSEC', 'LEONG HALL', 'XAVIER HALL']

icon_path = 'pin.png'  
icon = plt.imread(icon_path)
fig, ax = plt.subplots()

for (x, y), label in zip(place_coords, place_labels):
    im = OffsetImage(icon, zoom=0.005)  
    ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False)
    ax.add_artist(ab)
    ax.text(x + 0.1, y + 0.2, f' {label}', fontsize=8, verticalalignment='center_baseline', zorder=10)

if line == "LINE A":
    def highlight_route(start, end):
        start_index = coords.index(place_coords[place_labels.index(start)])
        end_index = coords.index(place_coords[place_labels.index(end)])
    
        highlighted_x = x_coords[start_index:end_index+1] 
        highlighted_y = y_coords[start_index:end_index+1]
    
        ax.plot(highlighted_x, highlighted_y, color='red', linewidth=2, label=f'Route {start} to {end}')
        ax.legend()

    try:
        last_item = load_latest_item()

        if last_item == "HAGDAN NA BATO":
            highlight_route("HAGDAN NA BATO", "LS COVERED COURTS")
        elif last_item == "LS COVERED COURTS":
            highlight_route("LS COVERED COURTS", "GATE 1")
        elif last_item == "GATE 1":
            highlight_route("GATE 1", "JSEC")
        elif last_item == "JSEC":
            highlight_route("JSEC", "LEONG HALL")
        elif last_item == "LEONG HALL":
            highlight_route("LEONG HALL", "XAVIER HALL")
        elif last_item == "XAVIER HALL":
            highlight_route("XAVIER HALL", "HAGDAN NA BATO")

        ax.plot(x_coords, y_coords, color='lightgray', label='Other Routes')  
        ax.set_title('Line A Route', fontsize=14, pad=20)  
        ax.axis('off')  

        ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
        ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)

        plt.show()
    

#time.sleep(60 * 1)  # Refresh every 5 minutes (adjust as needed)
#st.experimental_rerun()

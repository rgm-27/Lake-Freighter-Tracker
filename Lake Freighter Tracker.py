import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Lake Freighter Tracker')

# tabs for GUI
tab1, tab2, tab3 = st.tabs(['About', 'Data (Input Required)', 'Plot'])

# high level intro to the application
with tab1:
    st.write('Hello,')

    st.write(
            'This application is meant to track the (13) one thousand foot long lakers on the Great Lakes using  \n\
            historic Automatic Identification System (AIS) data provided by https://marinecadastre.gov/ais/  \n\
            (see "points" data)')

    st.write(
            'The data files are very large and take awhile to load into the program. If you encounter  \n\
            an error due to uploaded file size see Streamlit options such as (--server.maxUploadSize)')

    st.write('To get started please move to the "Data" tab')

# creating dictionary of specific ships to track
if 'ship_dictionary' not in st.session_state:

    st.session_state['ship_dictionary'] = {

        'American Century': {
            'Name': 'American Century',
            'IMO': 'IMO7923196',
            'Overall_Length': '1000',
            'Operator': 'American Steamship Company',
            'Builder': 'Bay Shipbuilding Company',
            'Year_Launched': '1981'},

        'American Integrity': {
            'Name': 'American Integrity',
            'IMO': 'IMO7514696',
            'Overall_Length': '1000',
            'Operator': 'American Steamship Company',
            'Builder': 'Bay Shipbuilding Company',
            'Year_Launched': '1978'},

        'American Spirit': {
            'Name': 'American Spirit',
            'IMO': 'IMO7423392',
            'Overall_Length': '1004',
            'Operator': 'American Steamship Company',
            'Builder': 'American Ship Building Company',
            'Year_Launched': '1978'},

        'Burns Harbor': {
            'Name': 'Burns Harbor',
            'IMO': 'IMO7514713',
            'Overall_Length': '1000',
            'Operator': 'American Steamship Company',
            'Builder': 'Bay Shipbuilding Company',
            'Year_Launched': '1980'},

        'Edger B. Speer': {
            'Name': 'Edger B. Speer',
            'IMO': 'IMO7625952',
            'Overall_Length': '1004',
            'Operator': 'Great Lakes Fleet,Inc',
            'Builder': 'American Ship Building Company',
            'Year_Launched': '1980'},

        'Edwin H. Gott': {
            'Name': 'Edwin H. Gott',
            'IMO': 'IMO7606061',
            'Overall_Length': '1004',
            'Operator': 'Great Lakes Fleet,Inc',
            'Builder': 'Bay Shipbuilding Company',
            'Year_Launched': '1979'},

        'Indiana Harbor': {
            'Name': 'Indiana Harbor',
            'IMO': 'IMO7514701',
            'Overall_Length': '1000',
            'Operator': 'American Steamship Company',
            'Builder': 'Bay Shipbuilding Company',
            'Year_Launched': '1979'},

        'James R. Barker': {
            'Name': 'James R. Barker',
            'IMO': 'IMO7390260',
            'Overall_Length': '1004',
            'Operator': 'Interlake Steamship Company',
            'Builder': 'American Ship Building Company',
            'Year_Launched': '1976'},

        'Mesabi Miner': {
            'Name': 'Mesabi Miner',
            'IMO': 'IMO7390260',
            'Overall_Length': '1004',
            'Operator': 'Interlake Steamship Company',
            'Builder': 'American Ship Building Company',
            'Year_Launched': '1977'},

        'Paul R. Tregurtha': {
            'Name': 'Paul R. Tregurtha',
            'IMO': 'IMO7729057',
            'Overall_Length': '1013.5',
            'Operator': 'Interlake Steamship Company',
            'Builder': 'American Ship Building Company',
            'Year_Launched': '1981'},

        'Presque Isle': {
            'Name': 'Presque Isle',
            'IMO': 'IMO7303877',
            'Overall_Length': '1000',
            'Operator': 'Great Lakes Fleet,Inc.',
            'Builder': 'DeFoe Shipbuilding / Erie Marine',
            'Year_Launched': '1973'},

        'Stewart J. Cort': {
            'Name': 'Stewart J. Cort',
            'IMO': 'IMO7105495',
            'Overall_Length': '1000',
            'Operator': 'Interlake Steamship Company',
            'Builder': 'Erie Marine',
            'Year_Launched': '1972'},

        'Walter J. McCarthy Jr.': {
            'Name': 'Walter J. McCarthy Jr.',
            'IMO': 'IMO7514684', 'Overall_Length': '1000',
            'Operator': 'American Steamship Company',
            'Builder': 'Bay Shipbulding Company',
            'Year_Launched': '1977'}}

# stateful variable for ship data frame
if 'ship_data_frame' not in st.session_state:
    st.session_state['ship_data_frame'] = None


# create statefulness for create_data_frame function excecution
@st.experimental_memo
def create_data_frame(file):

    # access only required columns of standard file format
    st.session_state['ship_data_frame'] = pd.read_csv(file, usecols=(1, 2, 3, 8))

    # verify file is of the correct format
    if set(['BaseDateTime', 'LAT', 'LON', 'IMO']).issubset(st.session_state['ship_data_frame'].columns):
        # trim data frame rows not containing tracked IMO number in ship dictionary
        targets = []
        for key, value in st.session_state['ship_dictionary'].items():
            tmp = (value['IMO'])
            targets.append(tmp)
        st.session_state['ship_data_frame'].query('IMO in @targets', inplace=True)
        return st.session_state['ship_data_frame']

    else:
        # prompt error due to file not having correct format
        with tab2:
            # clear stored data frame
            st.session_state['ship_data_frame'] = None
            # clear saved values associated with this function
            create_data_frame.clear()
            st.write(
                    'UPLOADED FILE IS NOT OF THE CORRECT TYPE. PLEASE REMOVE FILE  \n\
                    AND REPLACE WITH PROPER TYPE FROM https://marinecadastre.gov/ais/')
            return None


# file upload widget
def file_uploader():
    with tab2:
        uploaded_file = st.file_uploader('Select points data file from https://marinecadastre.gov/ais/', type='.csv')
        if uploaded_file is not None:
            create_data_frame(uploaded_file)


# stateful variable for currently selected ship
if 'current_ship' not in st.session_state:
    st.session_state['current_ship'] = None


# create sidebar
def side_bar():
    # place on sidebar
    with st.sidebar:
        # select ship names from dictionary keys
        option = st.selectbox('Please Select a Ship',
               options=st.session_state['ship_dictionary'].keys())
        st.session_state['current_ship'] = option

        # use current_ship and ship_dictionary to display additional information
        st.header('Ship Information')

        st.write(
                'Overall Length (feet):',
                st.session_state['ship_dictionary']
                [st.session_state['current_ship']]['Overall_Length'])

        st.write(
                'Operator:',
                st.session_state['ship_dictionary']
                [st.session_state['current_ship']]['Operator'])

        st.write(
                'Builder:',
                st.session_state['ship_dictionary']
                [st.session_state['current_ship']]['Builder'])

        st.write(
                'Year Launched:',
                st.session_state['ship_dictionary']
                [st.session_state['current_ship']]['Year_Launched'])


# plot ship travel
def plot():
    with tab3:
        # run if proper data frame exists
        if st.session_state['ship_data_frame'] is not None:
            # query to plot information for current_ship
            df_query = st.session_state['ship_data_frame'].loc[st.session_state['ship_data_frame']['IMO'] ==
            st.session_state['ship_dictionary'][st.session_state['current_ship']]['IMO']]

            # query variables
            fig_hover_name = df_query.BaseDateTime
            fig_lat = df_query.LAT
            fig_lon = df_query.LON

            # plot - center on Makinac Bridge
            fig = px.scatter_mapbox(
                None, lat=fig_lat, lon=fig_lon, hover_name=fig_hover_name,
                hover_data=None, color_discrete_sequence=['fuchsia'],
                center=dict(lat=45.8174, lon=-84.7278), zoom=4, height=300)

            # layout options
            fig.update_layout(mapbox_style='open-street-map')
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig, use_container_width=True)

            # if IMO is not in df_query, notify user
            if df_query.IMO.empty:
                st.write('IT APPEARS THE SELECTED SHIP IS NOT TRACKED IN THE UPLOADED DATA FILE')

        # prevent error if no data loaded
        else:
            pass


# driver code
def main():
    file_uploader()
    side_bar()
    plot()


if __name__ == '__main__':
    main()

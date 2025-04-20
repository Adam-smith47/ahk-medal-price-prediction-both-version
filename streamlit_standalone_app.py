import streamlit as st
import time
import warnings
from types import SimpleNamespace
from prediction import predict_data  # your prediction.py must be in the same folder

warnings.filterwarnings('ignore')

def main():
    # st.set_page_config(page_title='Medal Prediction App - Standalone', layout="centered")
    st.title('Medal Prediction App - Standalone')

    st.markdown("<h1 style='text-align: center;'>Medal Unit Price Prediction App</h1>",
                unsafe_allow_html=True)

    st.divider()

    st.markdown('''The Medal Prediction Application offers the ability to estimate unit prices of medals based on their
                unique characteristics and features. Through a user-friendly interface, simply select relevant categories 
                to generate outcome. The results are stemed from a machine learning model trained using historical medal data.''')

    st.subheader('Please enter your inputs:')

    # Inputs
    # Medal dimensions
    medal_width_col, medal_height_col, medal_thickness_col = st.columns(3)

    with medal_width_col:
        medal_width = st.slider(
            "Medal Width (mm)", min_value=20, max_value=120, value=20, step=5)

    with medal_height_col:
        medal_height = st.slider(
            "Medal Height (mm)", min_value=20, max_value=120, value=5, step=5)

    with medal_thickness_col:
        medal_thickness = st.slider(
            "Medal Thickness (mm)", min_value=2, max_value=10, value=2)

    # Front and Back type
    front_type_col, back_type_col = st.columns(2)

    with front_type_col:
        front_type = st.radio("Front Type", ('2D', '3D'))

    with back_type_col:
        back_type = st.radio("Back Type", ('2D', '3D'))

    # Personalisation
    front_personalisation_col, back_personalisation_col = st.columns(2)

    with front_personalisation_col:
        front_personalisation = st.selectbox(
            "Front Finish",(
                'Enamel', 'Unenamel', 'Unglazed', 'Laser Engraving',
                'Offset Printing', 'Digital Printing', 'Epoxy', 'Smooth', 'Black Laser',
                'UV Printing', 'Screen Printing', 'Openwork', 'Engraving'))

    with back_personalisation_col:
        back_personalisation = st.selectbox(
            "Back Finish",(
                'Enamel', 'Engraving', 'Blank', '3M Adhesive', 'Unenamel', 'Unglazed',
                'Grained', 'Wooden plaque', 'Smooth', 'Laser Engraving', 'Molded Base',
                'Offset Printing', 'Epoxy', 'Black Laser', 'Non-Slip Felt', 'Openwork', 'UV Printing'))

    # Number of Colors
    front_no_of_colors_col, back_no_of_colors_col = st.columns(2)

    with front_no_of_colors_col:
            front_no_of_colors = st.select_slider(
            "Front No Of Colors", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    with back_no_of_colors_col:
            back_no_of_colors = st.select_slider(
            "Back No Of Colors", (1, 2, 3, 4, 5, 6, 7, 8))


    # Finishes
    finish_col, second_finish_col, double_finish_col = st.columns(3)

    with finish_col:
        finish = st.selectbox("Medal Finish",(
            'Shiny Silver', 'Antique Bronze', 'Antique Silver', 'Shiny Gold',
            'Patinated Silver', 'Antique Pewter', 'Antique Gold', 'Shiny Nickel',
            'Patinated Bronze', 'Antique Tin', 'Patinated Pewter', 'Satin Nickel',
            'Satin Gold', 'Copper','Aluminum', 'Satin Metal', 'Matt Nickel',
            'Black Nickel', 'Real Gold', 'Antique Nickel', 'Patinated Tin', 'Iron',
            'Matte Black', 'Antique Copper', 'Shiny Gun', 'Shiny Metal', 'Gun Metal',  'Brass'))

    with second_finish_col:
        second_finish = st.selectbox(
            "Second Finish", 
            ('No', 'Shiny Gold', 'Satin Gold', 'Shiny Nickel', 'Antique Silver',
    'Satin Nickel', 'Antique Tin', 'Patinated Pewter', 'Antique Gold',
    'Shiny Metal', 'Satin Metal', 'Antique Pewter', 'Antique Bronze')
        )

    with double_finish_col:
        double_finish = st.selectbox(
            "Double Finish",
            ("No", "Yes"),
            help='Double Finish means the medal has two different finishing styles applied. For example, a mix of Shiny and Antique, or Gold and Silver, used for richer contrast and detailing.'
        )

    
    # Ribbon section
    # Ribbon Needed: Toggle

    with st.expander("Ribbon Options", expanded= True):
        ribbon_needed_toggle = st.toggle('Ribbon Needed?')

        if ribbon_needed_toggle:
            ribbon_needed = 'Needed'
        else:
            ribbon_needed = 'No'

        # If Ribbon is Needed — show the rest of the inputs
        if ribbon_needed == 'Needed':

            ribbon_width_col, ribbon_height_col = st.columns(2)

            # Ribbon Width and Height (assuming mm)
            with ribbon_width_col:
                ribbon_width = st.slider(
                    "Ribbon Width (mm)", min_value=5, max_value=100, value=20, step=1)

            with ribbon_height_col:
                ribbon_height = st.slider(
                    "Ribbon Height (mm)", min_value=5, max_value=150, value=50, step=1)
                

            ribbon_no_of_colors_col, ribbon_print_col, no_of_ribbon_print_side_col = st.columns(3)
            
            # Number of Ribbon Colors
            with ribbon_no_of_colors_col:
                ribbon_no_of_colors = st.select_slider(
                    "Ribbon No Of Colors",
                    options=[1, 2, 3, 4]
                )

            # Ribbon Print Type
            with ribbon_print_col:
                ribbon_print = st.selectbox(
                    "Ribbon Print Type",
                    ['Custom Print', 'Sublimation', 'Offset Print', 'Sewn', 
                    'Velcro', 'Heat Transfer', 'Screen Print']
                )

            # No Of Ribbon Print Side
            with no_of_ribbon_print_side_col:
                no_of_ribbon_print_side = st.select_slider(
                    "Number Of Ribbon Print Sides",
                    options=[1, 2]
                )


        else:
            # If ribbon is not needed — set default "empty" values
            ribbon_no_of_colors = 0
            ribbon_print = 'No'
            no_of_ribbon_print_side = 0
            ribbon_width = 0
            ribbon_height = 0


    # Attachment, Packaging, Quantity
    with st.expander("Packaging & Quantity", expanded=True):
        attachment_col, packaging_col, quantity_col = st.columns(3)

        with attachment_col:
            attachment = st.selectbox("Attachment",(
                'No', 'Screws', 'Clip', 'ATM-23', 'Ribbon attachment', 'Brass cup',
                'Pin Attachment', 'ATM-5Z', 'Studs', 'Ring', 'ATM-9', 'Suction Cups', 'HR502',
                'Chain', 'Foot Attachment', 'ATM-21', 'Bail', 'ATM-1', 'ATM-16'))

        with packaging_col:
            packaging = st.selectbox("Packaging",(
                'Cellophane', 'BTL-102', 'Cardboard Box', 'BTT-201', 'BTC-313','BTL-103',
                'Velvet Pouch', 'Cellophane with AGEC Logo')
            )

        with quantity_col:
            quantity = st.number_input('Quantity', min_value=1, max_value=25000, value=1000, step=100,
                                    help='Please enter values from 1 to 25000')


    # Input
    user_inputs = {
        "front_type": front_type,
        "front_no_of_colors": front_no_of_colors,
        "front_personalisation": front_personalisation,
        "back_type": back_type,
        "back_no_of_colors": back_no_of_colors,
        "back_personalisation": back_personalisation,
        "medal_width": medal_width,
        "medal_height": medal_height,
        "medal_thickness": medal_thickness,
        "finish": finish,
        "second_finish": second_finish,
        "double_finish": double_finish,
        "ribbon_needed": ribbon_needed,
        "ribbon_no_of_colors": ribbon_no_of_colors,
        "ribbon_print": ribbon_print,
        "no_of_ribbon_print_side": no_of_ribbon_print_side,
        "ribbon_width": ribbon_width,
        "ribbon_height": ribbon_height,
        "packaging": packaging,
        "attachment": attachment,
        "quantity": quantity
    }

    # Predict!
    if st.button('Predict', type='primary'):
        with st.spinner('Getting Model Predictions...'):
            time.sleep(1)
            req = SimpleNamespace(**user_inputs)
            resp = predict_data(req)
            price = resp["result"][0]
            st.success(f"**MODEL PREDICTION:** The Unit Price of the Medal is **{price:,.2f}€/pc**")


if __name__ == "__main__":
    main()
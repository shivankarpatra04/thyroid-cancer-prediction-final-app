import streamlit as st
from multiapp import MultiApp

# Add the path to your module directory

# Now you can import your module
def main_page():
    import myapp2,home,data

    main = MultiApp()




    # Add all your application here
    main.add_app("Model",myapp2.thyroid_cancer_prediction_app)
    main.add_app("About Thyroid Cancer",home.show_description)
    main.add_app("Training Dataset", data.show_data)
    main.run()

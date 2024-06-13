import pandas as pd
import pickle
import streamlit as st
import streamlit.components.v1 as components

def thyroid_cancer_prediction_app():
    st.write("""
    # Thyroid Cancer Prediction App

    Assess thyroid nodules to determine cancer risk through thorough analysis, aiding in early detection and appropriate treatment planning.

    Data obtained from the [Kaggle](https://www.kaggle.com/datasets/bibin2001/thyroid-cancer-predition) by PRAKASH NAMBIAR.
    """)

    st.sidebar.header('User Input Features')

    def user_input_features():
        """Gets user input features."""
        mean_radius = st.sidebar.slider('Mean Radius', min_value=0.0, max_value=35.0, value=15.0)
        mean_texture = st.sidebar.slider('Mean Texture', min_value=0.0, max_value=50.0, value=25.0)
        mean_perimeter = st.sidebar.slider('Mean Perimeter', min_value=0.0, max_value=200.0, value=75.0)
        mean_area = st.sidebar.slider('Mean Area', min_value=0.0, max_value=3000.0, value=1500.0)
        mean_smoothness = st.sidebar.slider('Mean Smoothness', min_value=0.0, max_value=0.5, value=0.2)

        data = {'mean_radius': mean_radius,
                'mean_texture': mean_texture,
                'mean_perimeter': mean_perimeter,
                'mean_area': mean_area,
                'mean_smoothness': mean_smoothness
                }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    st.subheader('User Input features')

    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(input_df)

    # Load the pre-trained model from the pickle file
    with open('model_pipeline.pkl', 'rb') as file:
        model = pickle.load(file)

    # Make predictions
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.subheader('Prediction')
    if prediction[0] == 0:
        st.write('Malignant')
    else:
        st.write('Benign')

    st.subheader('Prediction Probability')
    st.write(prediction_proba)


if __name__ == '__main__':
    thyroid_cancer_prediction_app()

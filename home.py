import streamlit as st

def show_description():

    st.header("Thyroid Cancer: An Overview")

    st.write("""
    **Introduction**
    Thyroid cancer occurs in the thyroid gland, located at the base of the neck. This gland produces hormones that regulate heart rate, blood pressure, body temperature, and weight. Although thyroid cancer is relatively uncommon compared to other cancers, its incidence has been increasing over the years. It typically presents as a lump or swelling in the neck, and early detection can significantly improve treatment outcomes.
    """)

    st.subheader("Types of Thyroid Cancer")
    st.write("""
    - **Papillary Thyroid Cancer**: The most common type, accounting for about 80% of cases. It tends to grow slowly and often occurs in one lobe of the thyroid gland.
    - **Follicular Thyroid Cancer**: Makes up about 10-15% of cases and can spread to lymph nodes and distant organs.
    - **Medullary Thyroid Cancer**: Accounts for about 3% of thyroid cancers and can be associated with genetic syndromes.
    - **Anaplastic Thyroid Cancer**: A rare and aggressive form, making up less than 2% of thyroid cancers, often difficult to treat.
    """)

    st.subheader("Risk Factors")
    st.write("""
    Several factors can increase the risk of developing thyroid cancer, including:
    - **Gender and Age**: More common in women and individuals over 30.
    - **Radiation Exposure**: Previous exposure to high levels of radiation.
    - **Family History**: A family history of thyroid cancer or other thyroid diseases.
    - **Genetic Mutations**: Inherited genetic conditions, such as multiple endocrine neoplasia.
    """)

    st.subheader("Symptoms")
    st.write("""
    Common symptoms of thyroid cancer include:
    - A lump in the neck.
    - Swelling or pain in the neck.
    - Hoarseness or difficulty speaking.
    - Difficulty swallowing or breathing.
    - Persistent cough not associated with a cold.
    """)

    st.subheader("Diagnosis")
    st.write("""
    The diagnosis of thyroid cancer involves several steps:
    1. **Physical Examination**: Checking for lumps or swelling in the neck.
    2. **Imaging Tests**: Ultrasound, CT scans, or MRIs to detect abnormalities in the thyroid.
    3. **Biopsy**: Fine needle aspiration biopsy to extract cells for examination.
    4. **Blood Tests**: Checking for abnormal levels of thyroid-stimulating hormone (TSH) and other markers.
    """)

    # Machine Learning Section
    st.header("Machine Learning in Thyroid Cancer Diagnosis")

    st.subheader("Diagnosis Feature")
    st.write("""
    In the context of machine learning, the **diagnosis feature** serves as the target variable. This feature categorizes individuals into classes, typically "benign" (non-cancerous) and "malignant" (cancerous). This is the label that machine learning models aim to predict, helping in the early detection and appropriate treatment of thyroid cancer.
    """)

    st.subheader("Random Forest Classifier")
    st.write("""
    To tackle the problem of predicting thyroid cancer, I utilized a **Random Forest Classifier** with the best hyperparameters. Among all the models tested, the Random Forest Classifier provided the best results. This model is particularly effective due to its ability to handle a large number of input features and its robustness against overfitting.

    - **Random Forest Classifier**: An ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes (classification) of the individual trees.
    - **Best Hyperparameters**: Fine-tuning hyperparameters such as the number of trees, depth of the trees, and criteria for splitting nodes, improved the model's performance.
    """)

    # Conclusion Section
    st.header("Conclusion")
    st.write("""
    The use of machine learning, specifically the Random Forest Classifier, has shown promising results in the diagnosis of thyroid cancer. By accurately categorizing thyroid nodules as benign or malignant, this approach aids in the timely and appropriate treatment of patients, ultimately improving prognosis and survival rates.
    """)

    # Footer or Additional Information
    st.write("""
    This information is integral to understanding thyroid cancer and demonstrates the effectiveness of advanced machine learning models in medical diagnosis.
    """)

def main():
    show_description()

if __name__ == "__main__":
    main()
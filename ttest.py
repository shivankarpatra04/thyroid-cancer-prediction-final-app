import streamlit as st
import pandas as pd
from scipy.stats import ttest_1samp
import numpy as np

def perform_hypothesis_tests(sample_size=100, num_tests=10):
    ThyroidCancerDF = pd.read_csv("Thyroid_train.csv")
    features = ['mean_radius', 'mean_area', 'mean_texture', 'mean_perimeter', 'mean_smoothness']
    test_results = []
    for test_num in range(1, num_tests + 1):
        test_num_results = []
        for feature in features:
            mean = np.mean(ThyroidCancerDF[feature])
            sample = np.random.choice(ThyroidCancerDF[feature], sample_size)
            _, p_value = ttest_1samp(sample, mean)
            if p_value < 0.05:
                result = f"\nFeature: {feature} H0 Rejected ({p_value*100:.2f}% Outside Significance level)"
            else:
                result = f"\nFeature: {feature} H0 Accepted ({p_value*100:.2f}% Under Significance level)"
            test_num_results.append(result)
        test_results.append(test_num_results)
    
    # Display results in Streamlit
    st.title("Hypothesis Testing")
    for test_num, results in enumerate(test_results, start=1):
        st.header(f"Test {test_num} Results:")
        for result in results:
            st.write(result)
        st.write("*************************************")

if __name__ == "__main__":
    perform_hypothesis_tests()


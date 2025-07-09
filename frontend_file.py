import streamlit as st
import requests

st.set_page_config(
    page_title="Iris Predictor",
    page_icon="💮",
    initial_sidebar_state="collapsed"
)

st.title("What Iris is This?")
st.subheader("A Streamlit app to classify iris flowers")
st.write("This app uses a machine learning model to predict the species of iris flowers based on their features.")

st.divider()

st.image("./assets/img/iris-machinelearning.png")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.slider("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)

with col2:
    sepal_width = st.slider("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)

col3, col4 = st.columns(2)
with col3:
    petal_length = st.slider("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.5)
with col4:
    petal_width = st.slider("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)
st.divider()
dict_pred = {
    "sepal_length": sepal_length,
    "sepal_width": sepal_width,
    "petal_length": petal_length,
    "petal_width": petal_width
    }

predict = None
predict_url = "https://my-api-app-1085716130859.europe-west1.run.app/predict"


if st.button("Predict my Iris Species"):
    with st.spinner("Wait for your predicted species..."):
        try:
            response = requests.get(predict_url, params=dict_pred)
            data = response.json()
            predict = data.get('prediction', 'No prediction returned')

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching prediction: {e}")

        except ValueError:
            st.error("Invalid response from the API. Please try again later.")

st.divider()

if predict is not None:
    if predict == 0:
        predict = "Setosa"
    elif predict == 1:
        predict = "Versicolor"
    elif predict == 2:
        predict = "Virginica"
    else:
        predict = "Unknown Species"

if predict is not None:
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"### It should be ")
        st.write(f"## **{predict}**")
    with col8:
        st.image(f"./assets/img/{predict}.png")
else:
    st.write("### No prediction made yet. Please enter your data and click the button to predict.")




st.markdown("""
_created by ChrisLPH for Le Wagon_
""")

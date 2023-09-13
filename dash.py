import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('Excel Data Visualization App')

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        st.write('## Excel Data')
        st.dataframe(df)
        
        st.write('## Bar Chart')
        selected_column = st.selectbox('Select a column for the X-axis:', df.columns)
        bar_data = df[selected_column].value_counts()
        st.bar_chart(bar_data)
        
        st.write('## Pie Chart')
        pie_data = df[selected_column].value_counts()
        st.write('Total data points:', len(df))
        
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)


def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df

if __name__ == '__main__':
    main()

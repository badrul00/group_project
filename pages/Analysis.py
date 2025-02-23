import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df=pd.read_csv('dataset.csv')
df2=pd.read_csv('dataset.csv')

# Sample code for mapping
df["SEX"] = pd.to_numeric(df["SEX"])
df["SEX"] = df["SEX"].map({1:"FEMALE", 2:"MALE", 99:"UNKNOWN"})
# HOSPITALIZED
df["HOSPITALIZED"] = pd.to_numeric(df["HOSPITALIZED"])
df["HOSPITALIZED"] = df["HOSPITALIZED"].map({1:"NO", 2:"YES", 99:"UNKNOWN"})
#intubated
df["INTUBATED"] = pd.to_numeric(df["INTUBATED"])
df["INTUBATED"] = df["INTUBATED"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#PNEUMONIA
df["PNEUMONIA"] = pd.to_numeric(df["PNEUMONIA"])
df["PNEUMONIA"] = df["PNEUMONIA"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#PREGNANCY
df["PREGNANCY"] = pd.to_numeric(df["PREGNANCY"])
df["PREGNANCY"] = df["PREGNANCY"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#SPEAKS_NATIVE_LANGUAGE
df["SPEAKS_NATIVE_LANGUAGE"] = pd.to_numeric(df["SPEAKS_NATIVE_LANGUAGE"])
df["SPEAKS_NATIVE_LANGUAGE"] = df["SPEAKS_NATIVE_LANGUAGE"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#DIABETES
df["DIABETES"] = pd.to_numeric(df["DIABETES"])
df["DIABETES"] = df["DIABETES"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#COPD
df["COPD"] = pd.to_numeric(df["COPD"])
df["COPD"] = df["COPD"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#ASTHMA
df["ASTHMA"] = pd.to_numeric(df["ASTHMA"])
df["ASTHMA"] = df["SEX"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#INMUSUPR
df["INMUSUPR"] = pd.to_numeric(df["INMUSUPR"])
df["INMUSUPR"] = df["INMUSUPR"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#HYPERTENSION
df["HYPERTENSION"] = pd.to_numeric(df["HYPERTENSION"])
df["HYPERTENSION"] = df["HYPERTENSION"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#OTHER_DISEASE
df["OTHER_DISEASE"] = pd.to_numeric(df["OTHER_DISEASE"])
df["OTHER_DISEASE"] = df["OTHER_DISEASE"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#CARDIOVASCULAR
df["CARDIOVASCULAR"] = pd.to_numeric(df["CARDIOVASCULAR"])
df["CARDIOVASCULAR"] = df["CARDIOVASCULAR"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#OBESITY
df["OBESITY"] = pd.to_numeric(df["OBESITY"])
df["OBESITY"] = df["OBESITY"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#CHRONIC_KIDNEY
df["CHRONIC_KIDNEY"] = pd.to_numeric(df["CHRONIC_KIDNEY"])
df["CHRONIC_KIDNEY"] = df["CHRONIC_KIDNEY"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#TOBACCO
df["TOBACCO"] = pd.to_numeric(df["TOBACCO"])
df["TOBACCO"] = df["TOBACCO"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#ANOTHER CASE
df["ANOTHER CASE"] = pd.to_numeric(df["ANOTHER CASE"])
df["ANOTHER CASE"] = df["ANOTHER CASE"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#MIGRANT
df["MIGRANT"] = pd.to_numeric(df["MIGRANT"])
df["MIGRANT"] = df["MIGRANT"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#ICU
df["ICU"] = pd.to_numeric(df["ICU"])
df["ICU"] = df["ICU"].map({1:"YES", 2:"NO", 97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
#OUTCOME
df["OUTCOME"] = pd.to_numeric(df["OUTCOME"])
df["OUTCOME"] = df["OUTCOME"].map({1:"POSITIVE", 2:"NEGATIVE", 3:"PENDING"})
#NATIONALITY
df["NATIONALITY"] = pd.to_numeric(df["NATIONALITY"])
df["NATIONALITY"] = df["NATIONALITY"].map({1:"MEXICAN", 2:"FOREIGN", 3:"UNKNOWN"})

analysis = df.copy()


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Barchart", "Dual-Barchart", "Distribution","Heatmap", "Hue Barchart"])
with tab1:
    # Define age bins
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    analysis['AGE_GROUP'] = pd.cut(df['AGE'], bins=bins, labels=bins[:-1], right=False)
    # Count number of patients in each age group
    covid_age_count = analysis['AGE_GROUP'].value_counts().sort_index()
    # Convert to DataFrame for Plotly
    chart_data = pd.DataFrame({"Age Group": covid_age_count.index.astype(str), "Count": covid_age_count.values})
    # Streamlit UI
    st.title("Covid Patients by Age")
    st.markdown("### Select an Age Group to View Details")
    # Multi-select dropdown for selecting specific age groups
    selected_age_groups = st.multiselect("Select Age Groups", chart_data["Age Group"].tolist(), default=chart_data["Age Group"].tolist())
    # Filter data based on selection
    filtered_data = chart_data[chart_data["Age Group"].isin(selected_age_groups)]
    # Show warning if no data
    if filtered_data.empty:
        st.warning("No data available for the selected criteria.")
    else:
    # Create interactive Plotly bar chart
        fig = px.bar(filtered_data, x="Age Group", y="Count", text="Count",
                 labels={"Count": "Number of Patients", "Age Group": "Age Group"},
                 title="Number of Patients by Age Group")

    # Update layout for better visibility
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(yaxis=dict(title="Number of Patients", tickformat=','),
                      xaxis=dict(title="Age Group"),
                      showlegend=False)

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
with tab2:
    # Define age bins
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    analysis['AGE_GROUP'] = pd.cut(analysis['AGE'], bins=bins, labels=bins[:-1], right=False)

    # Convert 'AGE_GROUP' to string for Streamlit compatibility
    analysis['AGE_GROUP'] = analysis['AGE_GROUP'].astype(str)

    # Group by Age Group & Gender and count
    covid_age_sex_count = analysis.groupby(["AGE_GROUP", "SEX"]).size().reset_index(name="Count")

    # Streamlit UI
    st.title("Covid Patients by Age and Gender")
    st.markdown("### Select Age and Gender to View Details")
    # Fix for multiselect error: Convert categories to strings
    age_groups = list(covid_age_sex_count["AGE_GROUP"].unique())
    genders = list(covid_age_sex_count["SEX"].unique())

    selected_age_groups = st.multiselect("Select Age Groups", options=age_groups, default=age_groups)
    selected_genders = st.multiselect("Select Gender", options=genders, default=genders)

    # Filter data based on selections
    filtered_data = covid_age_sex_count[
        covid_age_sex_count["AGE_GROUP"].isin(selected_age_groups) &
        covid_age_sex_count["SEX"].isin(selected_genders)]

    # Warning if no data is available
    if filtered_data.empty:
        st.warning("No data available for the selected criteria.")
    else:
    # Create interactive grouped bar chart
        fig = px.bar(filtered_data, x="AGE_GROUP", y="Count", color="SEX", barmode="group",
                 labels={"Count": "Number of Patients", "AGE_GROUP": "Age Group", "SEX": "Gender"},
                 title="Number of Patients by Age Group and Gender")
    # Show chart
    st.plotly_chart(fig, use_container_width=True)
with tab3:
    # Count intubation status
    intubation_counts = analysis["INTUBATED"].value_counts().reset_index()
    intubation_counts.columns = ["Intubation Status", "Count"]

    # Plotly interactive bar chart
    fig = px.bar(
    intubation_counts,
    x="Intubation Status",
    y="Count",
    title="Number of Patients by Intubation Status",
    labels={"Count": "Number of Patients"},
    color="Intubation Status",
    text_auto=True)
    # Display chart
    st.plotly_chart(fig, use_container_width=True)
with tab4:
    #Compute correlation
    correlation = df2[["ICU", "DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", 
                   "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY","TOBACCO"]].corr()
    #Convert to long format for Plotly
    corr_df = correlation.reset_index().melt(id_vars="index")
    corr_df.columns = ["Feature1", "Feature2", "Correlation"]
    #Create interactive heatmap
    fig = px.imshow(
    correlation,
    labels=dict(color="Correlation"),
    x=correlation.columns,
    y=correlation.columns,
    color_continuous_scale="RdBu",
    zmin=-1, zmax=1,
    text_auto=".2f")
    # Streamlit UI
    st.title("Correlation Other Diseases With ICU Admission")
    st.plotly_chart(fig, use_container_width=True)
with tab5:
    df2['DATE_OF_DEATH'] = pd.to_datetime(df2['DATE_OF_DEATH'])

    # Define disease columns
    diseases = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", 
            "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"]

    # Compute deceased patient counts per disease
    disease_counts = df2[diseases].apply(lambda x: ((x == 1) & (df2['DATE_OF_DEATH'].notna())).sum())

    # Convert to DataFrame for Plotly
    disease_df = pd.DataFrame({"Disease": disease_counts.index, "Count": disease_counts.values})

    # Create interactive bar chart using Plotly
    fig = px.bar(disease_df, x="Disease", y="Count", 
             title="Common Diseases Among Deceased Patients",
             labels={"Disease": "Disease", "Count": "Number of Deceased Patients"},
             color="Count",
             color_continuous_scale="reds")  # Adjust color theme if needed

    # Streamlit UI
    st.title("Common Disease of Deceased Covid Patients")
    st.plotly_chart(fig, use_container_width=True)













import streamlit as st
import functions as fn

dataset_version = st.sidebar.selectbox("Select Dataset Version", ["Version 1", "Version 2"])
df = fn.load_data_ver1() if dataset_version == "Version 1" else fn.load_data_ver2()

if dataset_version == "Version 1":
    required_columns = ['stars_count', 'forks_count', 'issues_count', 'pull_requests', 'contributors', 'language']
else:
    required_columns = ['stars_count', 'forks_count', 'watchers', 'pull_requests', 'commit_count', 'primary_language', 'languages_used', 'licence']

st.title(f'Github Repositories Analysis: Myungkeun Park - {dataset_version}')

if all(col in df.columns for col in required_columns):
    st.header('Statistical Analysis (values in 2 dp if decimal)')
    columns_to_analyze = required_columns[:-3] if dataset_version == "Version 1" else required_columns[:-4]
    for col in columns_to_analyze:
        st.subheader(f'Statistics for {col}')
        if dataset_version == "Version 1":
            stats = fn.compute_statistics(df, col, 'repositories')
        else:
            stats = fn.compute_statistics(df, col, 'name')
        st.write(stats)

    st.header('Top 10 Languages Used')
    top_langs = fn.top_languages(df, 'primary_language' if dataset_version != "Version 1" else 'language')
    st.write(top_langs)

    if dataset_version == "Version 1":
        st.subheader('Language Distribution')
        fn.plot_language_distribution(df, 'language')
    else:
        st.subheader('Language Distribution - Top 50')
        fn.plot_language_distribution_2(df, 'primary_language', top_n=50)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    if dataset_version != "Version 1":
        st.subheader('Languages Used Stats')
        lang_stats = fn.languages_used_stats(df, 'languages_used')
        st.write(lang_stats)

        st.subheader('Top 10 Licenses')
        top_lic = fn.top_licenses(df)
        st.write(top_lic)

else:
    st.error("ERROR.")

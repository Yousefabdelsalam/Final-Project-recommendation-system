import prepare_files
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

# Page setup
st.set_page_config(
    page_title="Job Cluster Analysis & Recommendation",
    layout="wide",
    page_icon="📊"
)

# Title
st.title("📊 Job Cluster Analysis & Recommendation System")

# Load data - replace with your actual data loading
@st.cache_data
def load_data():
    try:
        # Load your main dataframe
        df_final = pd.read_csv("stremlit_clustring & analysis.csv")
        
        # Ensure we have the expected columns
        required_columns = ['jobs', 'country', 'is_hourly']
        for col in required_columns:
            if col not in df_final.columns:
                raise ValueError(f"Required column '{col}' not found in dataset")

        # Create all required DataFrames based on your questions
        df_country = df_final.groupby(['country', 'jobs']).size().reset_index(name='count')
        jop_type = df_final.groupby(['jobs', 'is_hourly']).size().reset_index(name='count')
        top10_countries = df_final.groupby('country').size().nlargest(10).reset_index(name='count')
        
        # Time-based data (if date column exists)
        job_month = pd.DataFrame()
        job_day = pd.DataFrame()
        job_hour = pd.DataFrame()
        
        if 'date' in df_final.columns:
            try:
                df_final['date'] = pd.to_datetime(df_final['date'])
                df_final['month_name'] = df_final['date'].dt.month_name()
                df_final['day_name'] = df_final['date'].dt.day_name()
                job_month = df_final.groupby(['month_name', 'jobs']).size().reset_index(name='count')
                job_day = df_final.groupby(['day_name', 'jobs']).size().reset_index(name='count')
            except Exception as e:
                st.warning(f"Couldn't process date column: {str(e)}")
        
        if 'time' in df_final.columns:
            try:
                df_final['hour'] = pd.to_datetime(df_final['time']).dt.hour
                job_hour = df_final.groupby(['hour', 'jobs']).size().reset_index(name='count')
            except Exception as e:
                st.warning(f"Couldn't process time column: {str(e)}")
        
        # Create consistent sample data if needed
        unique_jobs = df_final['jobs'].unique()
        num_jobs = len(unique_jobs)
        
        if job_month.empty:
            months = ['Jan', 'Feb', 'Mar']
            job_month = pd.DataFrame({
                'month_name': np.repeat(months, num_jobs),
                'jobs': np.tile(unique_jobs, len(months)),
                'count': np.random.randint(50, 200, len(months)*num_jobs)
            })
        
        if job_day.empty:
            days = ['Mon', 'Tue', 'Wed']
            job_day = pd.DataFrame({
                'day_name': np.repeat(days, num_jobs),
                'jobs': np.tile(unique_jobs, len(days)),
                'count': np.random.randint(20, 100, len(days)*num_jobs)
            })
        
        if job_hour.empty:
            hours = [9, 10, 11]
            job_hour = pd.DataFrame({
                'hour': np.repeat(hours, num_jobs),
                'jobs': np.tile(unique_jobs, len(hours)),
                'count': np.random.randint(10, 50, len(hours)*num_jobs)
            })
        
        # Salary data (sample - replace with your actual data)
        df_melted = pd.DataFrame({
            'jobs': np.repeat(unique_jobs, 2),
            'Hourly Rate': np.tile([45, 30], num_jobs),
            'Rate Type': np.tile(['High', 'Low'], num_jobs)
        })
        
        df_hourly = pd.DataFrame({
            'jobs': unique_jobs,
            'hourly_low': np.random.randint(20, 35, num_jobs),
            'hourly_high': np.random.randint(35, 55, num_jobs)
        })
        df_hourly['hourly_avg'] = (df_hourly['hourly_low'] + df_hourly['hourly_high']) / 2
        top_avg = df_hourly.sort_values(by='hourly_avg', ascending=False).head(20)
        
        df_top10 = df_final[df_final['country'].isin(top10_countries['country'])]
        
        # Create top skills data (replace with actual skills analysis from your data)
        top_skills_data = pd.DataFrame({
            'Skill': ['Graphic Design', 'Web Development', 'JavaScript', 
                     'Python', 'Social Media Marketing', 'Content Writing',
                     'SEO', 'UI/UX Design', 'Mobile App Development', 'Data Analysis'],
            'Frequency': [850, 720, 680, 650, 600, 580, 550, 520, 500, 480]
        })
        
        return {
            'df_final': df_final,
            'df_country': df_country,
            'jop_type': jop_type,
            'top10_countries': top10_countries,
            'job_month': job_month,
            'job_day': job_day,
            'job_hour': job_hour,
            'df_melted': df_melted,
            'df_hourly': df_hourly,
            'top_avg': top_avg,
            'df_top10': df_top10,
            'top_skills_data': top_skills_data
        }
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        return None

@st.cache_data
def load_recommendation_data():
    try:
        df = pd.read_csv("streamlit.csv")
        if 'w2v_vector' not in df.columns:
            raise ValueError("w2v_vector column not found in recommendation data")
        return df
    except Exception as e:
        st.error(f"Error loading recommendation data: {str(e)}")
        return None

# Load all data
data = load_data()
if data is None:
    st.stop()

df_recommend = load_recommendation_data()
if df_recommend is None:
    st.stop()

# Recommendation system
@st.cache_resource
def load_w2v_model():
    try:
        return Word2Vec.load("model_w2v.model")
    except Exception as e:
        st.error(f"Error loading Word2Vec model: {str(e)}")
        return None

model_w2v = load_w2v_model()
if model_w2v is None:
    st.stop()

try:
    X_w2v = np.vstack(df_recommend['w2v_vector'].apply(eval).values)
except Exception as e:
    st.error(f"Error processing word vectors: {str(e)}")
    st.stop()

all_possible_skills = sorted([
    'graphic design', 'adobe photoshop', 'adobe illustrator',
    'logo design', 'video editing', 'adobe premiere', 'after effects',
    'motion graphics', 'branding', 'illustration', 'visual design',
    'ui design', 'html', 'css', 'javascript', 'react', 'node.js',
    'wordpress', 'php', 'python', 'flutter', 'mobile app development',
    'web development', 'ui/ux design', 'api integration', 'django',
    'social media marketing', 'content writing', 'seo', 'google ads',
    'facebook ads', 'email marketing', 'copywriting', 'instagram marketing',
    'analytics', 'tiktok ads', 'content creation', 'marketing strategy'
])

def get_freelancer_vector(skills, model):
    valid_skills = [skill for skill in skills if skill in model.wv]
    if not valid_skills:
        return np.zeros(model.vector_size)
    return np.mean(model.wv[valid_skills], axis=0)

def recommend_jobs(user_skills, top_n=5):
    user_vector = get_freelancer_vector(user_skills, model_w2v)
    df_recommend['similarity'] = cosine_similarity([user_vector], X_w2v)[0]
    return df_recommend.sort_values(by='similarity', ascending=False).head(top_n)

# App navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Select Mode:", 
                           ["Cluster Analysis", "Job Recommendations"])

if app_mode == "Cluster Analysis":
    # Job filter in sidebar
    st.sidebar.header("Filters")
    selected_jobs = st.sidebar.multiselect(
        "Select job clusters to display:",
        options=data['df_final']['jobs'].unique(),
        default=data['df_final']['jobs'].unique()
    )

    # Apply filters to relevant DataFrames
    df_filtered = data['df_final'][data['df_final']['jobs'].isin(selected_jobs)]
    df_country_filtered = data['df_country'][data['df_country']['jobs'].isin(selected_jobs)]
    jop_type_filtered = data['jop_type'][data['jop_type']['jobs'].isin(selected_jobs)]
    job_month_filtered = data['job_month'][data['job_month']['jobs'].isin(selected_jobs)]
    job_day_filtered = data['job_day'][data['job_day']['jobs'].isin(selected_jobs)]
    job_hour_filtered = data['job_hour'][data['job_hour']['jobs'].isin(selected_jobs)]
    df_melted_filtered = data['df_melted'][data['df_melted']['jobs'].isin(selected_jobs)]
    top_avg_filtered = data['top_avg'][data['top_avg']['jobs'].isin(selected_jobs)]
    df_top10_filtered = data['df_top10'][data['df_top10']['jobs'].isin(selected_jobs)]

    # Main dashboard
    tab1, tab2, tab3 = st.tabs(["Overview", "Geographical", "Temporal & Salary"])

    with tab1:
        st.header("Job Cluster Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Most Common Job Clusters")
            fig = px.histogram(data_frame=df_filtered, y='jobs', text_auto=True,
                              title='<b>Distribution of Job Clusters</b>',
                              color='jobs',
                              height=500)
            fig.update_layout(title_x=0.5, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Cluster Proportion")
            fig = px.pie(data_frame=df_filtered, names='jobs',
                         title='<b>Percentage of Each Cluster</b>',
                         hole=0.3,
                         color_discrete_sequence=px.colors.qualitative.Pastel)
            fig.update_layout(title_x=0.5, height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # New Top 10 Skills section
        st.subheader("Top 10 In-Demand Skills")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            fig = px.bar(data['top_skills_data'], x='Frequency', y='Skill', 
                        orientation='h', text='Frequency',
                        title='<b>Most Requested Skills</b>',
                        color='Skill',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
            fig.update_layout(title_x=0.5, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.pie(data['top_skills_data'], names='Skill', values='Frequency',
                        title='<b>Skills Distribution</b>',
                        hole=0.4)
            fig.update_layout(title_x=0.5, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Hourly vs Non-Hourly Jobs")
        fig = px.pie(data_frame=df_filtered, names='is_hourly', 
                     title='<b>Percentage of Hourly Jobs</b>',
                     color='is_hourly',
                     color_discrete_map={'True':'#636EFA', 'False':'#EF553B'})
        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.header("Geographical Distribution")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Top Countries for Selected Clusters")
            fig = px.histogram(data_frame=df_country_filtered, x='country', y='count', 
                              text_auto=True, title='<b>Job Postings by Country</b>',
                              color='jobs')
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Hourly Jobs by Country")
            fig = px.histogram(data_frame=df_top10_filtered, x='country', y='jobs', 
                              color='is_hourly', barmode='group', text_auto=True,
                              title='<b>Hourly Job Distribution by Country</b>',
                              color_discrete_map={'True':'#636EFA', 'False':'#EF553B'})
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.header("Temporal Patterns & Salary Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Monthly Job Postings")
            fig = px.histogram(data_frame=job_month_filtered, x='month_name', y='count',
                              color='jobs', barmode='group', text_auto=True,
                              title='<b>Monthly Job Postings by Cluster</b>')
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Daily Job Postings")
            fig = px.histogram(data_frame=job_day_filtered, x='day_name', y='count',
                              color='jobs', barmode='group', text_auto=True,
                              title='<b>Daily Job Postings by Cluster</b>')
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Hourly Posting Patterns")
        fig = px.line(
            job_hour_filtered,
            x='hour',
            y='count',
            color='jobs',
            markers=True,
            title='<b>Job Posting Times by Hour</b>'
        )
        fig.update_layout(
            xaxis_title='Hour of Day',
            yaxis_title='Number of Postings',
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Salary Analysis")
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                data['df_melted'],
                x='jobs',
                y='Hourly Rate',
                color='Rate Type',
                barmode='group',
                text_auto=True,
                title='<b>Hourly Rate Ranges by Cluster</b>',
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.bar(
                data['top_avg'],
                x='jobs',
                y='hourly_avg',
                text='hourly_avg',
                color='jobs',
                title='<b>Top Paying Job Clusters</b>',
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(title_x=0.5, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    # Key metrics
    st.sidebar.markdown("---")
    st.sidebar.subheader("Key Metrics")
    st.sidebar.metric("Total Jobs", len(df_filtered))
    st.sidebar.metric("Unique Countries", df_filtered['country'].nunique())
    hourly_pct = df_filtered['is_hourly'].value_counts(normalize=True).get(True, 0)*100
    st.sidebar.metric("Hourly Jobs", f"{hourly_pct:.1f}%")

else:
    # Job Recommendation System
    st.header("💼 Job Recommendation System")
    st.write("Get personalized job recommendations based on your skills")
    
    with st.sidebar:
        st.header("🔧 Select Your Skills")
        selected_skills = st.multiselect(
            "Choose skills you have:",
            options=all_possible_skills,
            default=['html', 'css', 'javascript']
        )
    
    if selected_skills:
        st.success(f"✅ Selected Skills: {', '.join(selected_skills)}")
        recommendations = recommend_jobs(selected_skills, top_n=10)
        
        st.subheader("🔍 Recommended Jobs")
        st.dataframe(recommendations[['title', 'description', 'similarity']]
                    .style.format({'similarity': "{:.2f}"}), 
                    use_container_width=True)
        
        fig = px.bar(
            recommendations,
            x='title',
            y='similarity',
            color='similarity',
            text='similarity',
            title='<b>Job Recommendation Scores</b>',
            color_continuous_scale='Bluered'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Show market trends for recommended jobs
        st.subheader("📊 Market Trends for Recommended Jobs")
        recommended_titles = recommendations['title'].unique()
        market_data = data['df_final'][data['df_final']['title'].isin(recommended_titles)]
        
        if not market_data.empty:
            col1, col2 = st.columns(2)
            with col1:
                st.write("Geographical Distribution")
                fig = px.histogram(market_data, x='country', color='title', 
                                 barmode='group', title='<b>Jobs by Country</b>',
                                 color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.write("Employment Type")
                fig = px.pie(market_data, names='is_hourly', 
                            title='<b>Hourly vs Full-time</b>',
                            color_discrete_map={'True':'#636EFA', 'False':'#EF553B'})
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No market data available for these specific jobs")
    else:
        st.info("Please select your skills from the sidebar to get recommendations")

# Download button
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="Download Sample Data",
    data=data['df_final'].to_csv().encode('utf-8'),
    file_name='job_cluster_data.csv',
    mime='text/csv'
)

# Add footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
** Recommendation System & Job Cluster Analysis**  
Developed with Eng: Yousef Abdelsalam  
""")

# import streamlit as st
# import pdfplumber
# import pandas as pd
# import io

# # Page configuration
# st.set_page_config(
#     page_title="PDF to CSV Converter",
#     page_icon="📄",
#     layout="centered"
# )

# # Custom CSS for beautiful styling
# st.markdown("""
#     <style>
#     /* Main container */
#     .main {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#     }
    
#     /* Title styling */
#     .title {
#         text-align: center;
#         font-size: 3em;
#         font-weight: bold;
#         color: #1e293b;
#         margin-bottom: 2rem;
#         padding: 1rem;
#         background: white;
#         border-radius: 15px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     }
    
#     /* Step cards container */
#     .steps-container {
#         display: flex;
#         justify-content: space-around;
#         margin: 2rem 0;
#         gap: 1rem;
#         flex-wrap: wrap;
#     }
    
#     /* Individual step card */
#     .step-card {
#         flex: 1;
#         min-width: 150px;
#         padding: 2rem 1rem;
#         border-radius: 20px;
#         text-align: center;
#         color: white;
#         font-weight: bold;
#         box-shadow: 0 8px 16px rgba(0,0,0,0.2);
#         transition: transform 0.3s ease;
#     }
    
#     .step-card:hover {
#         transform: translateY(-5px);
#     }
    
#     .step-1 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
#     .step-2 { background: linear-gradient(135deg, #fad961 0%, #f76b1c 100%); }
#     .step-3 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
#     .step-4 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    
#     .step-icon {
#         font-size: 3em;
#         margin-bottom: 0.5rem;
#     }
    
#     .step-title {
#         font-size: 1.5em;
#         margin-bottom: 0.5rem;
#     }
    
#     .step-desc {
#         font-size: 0.9em;
#         opacity: 0.9;
#     }
    
#     /* Upload section */
#     .upload-section {
#         background: white;
#         padding: 2rem;
#         border-radius: 15px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         margin: 2rem 0;
#     }
    
#     /* Progress bar */
#     .progress-container {
#         width: 100%;
#         background: #e2e8f0;
#         border-radius: 10px;
#         height: 10px;
#         margin: 1rem 0;
#         overflow: hidden;
#     }
    
#     .progress-bar {
#         height: 100%;
#         background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#         transition: width 0.3s ease;
#         border-radius: 10px;
#     }
    
#     /* Footer */
#     .footer {
#         text-align: center;
#         padding: 2rem;
#         color: #64748b;
#         font-size: 0.9em;
#     }
    
#     /* Button styling */
#     .stButton > button {
#         width: 100%;
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         font-size: 1.2em;
#         padding: 1rem 2rem;
#         border-radius: 10px;
#         border: none;
#         font-weight: bold;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
#     }
    
#     /* File uploader */
#     .uploadedFile {
#         border: 2px dashed #667eea;
#         border-radius: 10px;
#         padding: 1rem;
#     }
    
#     /* Success/Error messages */
#     .stSuccess, .stError, .stInfo {
#         border-radius: 10px;
#         padding: 1rem;
#         margin: 1rem 0;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Progress tracking
# if 'progress' not in st.session_state:
#     st.session_state.progress = 0

# # Title
# st.markdown('<div class="title">Convert Your PDF to CSV</div>', unsafe_allow_html=True)

# # Step cards
# st.markdown("""
#     <div class="steps-container">
#         <div class="step-card step-1">
#             <div class="step-icon">📤</div>
#             <div class="step-title">Upload PDF</div>
#             <div class="step-desc">Drag & drop or choose file</div>
#         </div>
#         <div class="step-card step-2">
#             <div class="step-icon">🔍</div>
#             <div class="step-title">Extraction</div>
#             <div class="step-desc">Reads tables + text from all pages</div>
#         </div>
#         <div class="step-card step-3">
#             <div class="step-icon">📊</div>
#             <div class="step-title">Conversion</div>
#             <div class="step-desc">Clean CSV formatting</div>
#         </div>
#         <div class="step-card step-4">
#             <div class="step-icon">⬇️</div>
#             <div class="step-title">Download</div>
#             <div class="step-desc">Get your CSV instantly</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # Upload section
# st.markdown('<div class="upload-section">', unsafe_allow_html=True)

# # File uploader
# uploaded_file = st.file_uploader("", type="pdf", label_visibility="collapsed")

# if uploaded_file is not None:
#     st.success(f"✅ Uploaded: {uploaded_file.name}")
#     st.session_state.progress = 25
    
#     # Show progress bar
#     st.markdown(f"""
#         <div class="progress-container">
#             <div class="progress-bar" style="width: {st.session_state.progress}%"></div>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Process button
#     if st.button("🚀 Upload & Convert", type="primary"):
#         with st.spinner("Processing PDF..."):
#             try:
#                 st.session_state.progress = 50
#                 st.markdown(f"""
#                     <div class="progress-container">
#                         <div class="progress-bar" style="width: {st.session_state.progress}%"></div>
#                     </div>
#                 """, unsafe_allow_html=True)
                
#                 data = []
                
#                 # Read PDF
#                 with pdfplumber.open(uploaded_file) as pdf:
#                     st.info(f"🔍 Processing {len(pdf.pages)} page(s)...")
#                     st.session_state.progress = 65
                    
#                     for page in pdf.pages:
#                         # Extract tables
#                         tables = page.extract_tables()
#                         if tables:
#                             for table in tables:
#                                 for row in table:
#                                     data.append(row)
#                         else:
#                             # Extract text if no tables found
#                             text = page.extract_text()
#                             if text:
#                                 lines = text.split('\n')
#                                 for line in lines:
#                                     if line.strip():
#                                         data.append([line])
                
#                 st.session_state.progress = 85
                
#                 if not data:
#                     st.error("❌ No data extracted from PDF. The PDF might be empty or contain only images.")
#                     st.session_state.progress = 0
#                 else:
#                     # Create DataFrame
#                     df = pd.DataFrame(data)
                    
#                     st.session_state.progress = 95
                    
#                     # Show preview
#                     st.subheader("📊 Preview (First 10 rows)")
#                     st.dataframe(df.head(10), use_container_width=True)
                    
#                     st.info(f"📈 Total rows extracted: {len(df)}")
                    
#                     # Convert to CSV
#                     csv_buffer = io.StringIO()
#                     df.to_csv(csv_buffer, index=False, header=False)
#                     csv_data = csv_buffer.getvalue()
                    
#                     st.session_state.progress = 100
                    
#                     # Progress bar at 100%
#                     st.markdown(f"""
#                         <div class="progress-container">
#                             <div class="progress-bar" style="width: 100%"></div>
#                         </div>
#                     """, unsafe_allow_html=True)
                    
#                     # Download button
#                     csv_filename = uploaded_file.name.replace(".pdf", ".csv")
#                     st.download_button(
#                         label="⬇️ Download CSV",
#                         data=csv_data,
#                         file_name=csv_filename,
#                         mime="text/csv",
#                         type="primary"
#                     )
                    
#                     st.success("✅ Conversion complete! Click the button above to download.")
                    
#             except Exception as e:
#                 st.error(f"❌ An error occurred: {str(e)}")
#                 st.info("Please make sure your PDF is not corrupted and try again.")
#                 st.session_state.progress = 0
# else:
#     st.info("👆 Please upload a PDF file to get started")
#     st.session_state.progress = 0

# st.markdown('</div>', unsafe_allow_html=True)

# # Footer
# st.markdown("""
#     <div class="footer">
#         © 2025 Specially made for Taxdoctorng. All rights reserved.
#     </div>
# """, unsafe_allow_html=True)








import streamlit as st
import pdfplumber
import pandas as pd
import io
import time

# Page configuration
st.set_page_config(
    page_title="PDF to CSV Converter",
    page_icon="📄",
    layout="centered"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Title styling */
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #1e293b;
        margin-bottom: 2rem;
        padding: 1rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Step cards container */
    .steps-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    /* Individual step card */
    .step-card {
        flex: 1;
        min-width: 150px;
        padding: 2rem 1rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        font-weight: bold;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }
    
    .step-card:hover {
        transform: translateY(-5px);
    }
    
    .step-1 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .step-2 { background: linear-gradient(135deg, #fad961 0%, #f76b1c 100%); }
    .step-3 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
    .step-4 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    
    .step-icon {
        font-size: 3em;
        margin-bottom: 0.5rem;
    }
    
    .step-title {
        font-size: 1.5em;
        margin-bottom: 0.5rem;
    }
    
    .step-desc {
        font-size: 0.9em;
        opacity: 0.9;
    }
    
    /* Upload section */
    .upload-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #64748b;
        font-size: 0.9em;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2em;
        padding: 1rem 2rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    
    /* File uploader */
    .uploadedFile {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Success/Error messages */
    .stSuccess, .stError, .stInfo {
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Convert Your PDF to CSV</div>', unsafe_allow_html=True)

# Step cards
st.markdown("""
    <div class="steps-container">
        <div class="step-card step-1">
            <div class="step-icon">📤</div>
            <div class="step-title">Upload PDF</div>
            <div class="step-desc">Drag & drop or choose file</div>
        </div>
        <div class="step-card step-2">
            <div class="step-icon">🔍</div>
            <div class="step-title">Extraction</div>
            <div class="step-desc">Reads tables + text from all pages</div>
        </div>
        <div class="step-card step-3">
            <div class="step-icon">📊</div>
            <div class="step-title">Conversion</div>
            <div class="step-desc">Clean CSV formatting</div>
        </div>
        <div class="step-card step-4">
            <div class="step-icon">⬇️</div>
            <div class="step-title">Download</div>
            <div class="step-desc">Get your CSV instantly</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Upload section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("", type="pdf", label_visibility="collapsed")

if uploaded_file is not None:
    st.success(f"✅ Uploaded: {uploaded_file.name}")
    
    # Process button
    if st.button("🚀 Upload & Convert", type="primary"):
        
        # Create a progress bar using Streamlit's native component
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Step 1: Starting
            progress_bar.progress(10)
            status_text.text("📂 Opening PDF file...")
            time.sleep(0.3)
            
            data = []
            
            # Step 2: Reading PDF
            progress_bar.progress(30)
            status_text.text("📖 Reading PDF structure...")
            
            with pdfplumber.open(uploaded_file) as pdf:
                page_count = len(pdf.pages)
                progress_bar.progress(40)
                status_text.text(f"🔍 Processing {page_count} page(s)...")
                time.sleep(0.3)
                
                # Process each page with progress updates
                for i, page in enumerate(pdf.pages):
                    # Update progress based on page number
                    page_progress = 40 + int((i / page_count) * 40)
                    progress_bar.progress(page_progress)
                    status_text.text(f"📄 Processing page {i+1} of {page_count}...")
                    
                    # Extract tables
                    tables = page.extract_tables()
                    if tables:
                        for table in tables:
                            for row in table:
                                data.append(row)
                    else:
                        # Extract text if no tables found
                        text = page.extract_text()
                        if text:
                            lines = text.split('\n')
                            for line in lines:
                                if line.strip():
                                    data.append([line])
            
            # Step 3: Creating DataFrame
            progress_bar.progress(85)
            status_text.text("🔄 Converting to CSV format...")
            time.sleep(0.3)
            
            if not data:
                progress_bar.empty()
                status_text.empty()
                st.error("❌ No data extracted from PDF. The PDF might be empty or contain only images.")
            else:
                # Create DataFrame
                df = pd.DataFrame(data)
                
                # Step 4: Finalizing
                progress_bar.progress(95)
                status_text.text("✨ Finalizing your file...")
                time.sleep(0.3)
                
                # Complete
                progress_bar.progress(100)
                status_text.text("✅ Conversion complete!")
                time.sleep(0.5)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Show preview
                st.subheader("📊 Preview (First 10 rows)")
                st.dataframe(df.head(10), use_container_width=True)
                
                st.info(f"📈 Total rows extracted: {len(df)}")
                
                # Convert to CSV
                csv_buffer = io.StringIO()
                df.to_csv(csv_buffer, index=False, header=False)
                csv_data = csv_buffer.getvalue()
                
                # Download button
                csv_filename = uploaded_file.name.replace(".pdf", ".csv")
                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv_data,
                    file_name=csv_filename,
                    mime="text/csv",
                    type="primary"
                )
                
                st.success("✅ Conversion complete! Click the button above to download.")
                
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Please make sure your PDF is not corrupted and try again.")
else:
    st.info("👆 Please upload a PDF file to get started")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        © 2025 Specially made for Taxdoctorng. All rights reserved.
    </div>
""", unsafe_allow_html=True)

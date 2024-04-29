# General info and functions
st.title(":rainbow[**General information on GA properties market**]")
with st.container():
    c1, c2 = st.columns(2)
    with c2:
        st.markdown(" Basic Property Stats:  ")
        display_avg_stats(get_data_and_loaddf())
    with c1:
        st.markdown(" AVG Price County Ranking:  ")
        display_counties_ranking(get_data_and_loaddf())
        
with st.container():
    c1, c2 = st.columns(2)
    with c2:
        display_scatter_map(get_data_and_loaddf())
    with c1:
        display_ga_map(get_data_and_loaddf())
        
st.markdown(":rainbow[**Search Results Information **] ") 

#sidebar configuration
with st.sidebar:
    df = get_data_and_loaddf()
       
    st_lottie(json.load(open("Looking_My_Home/home1.json")), height = 100, quality = "high")
     
        
    st.markdown('<span class="icon type-text">Search</span>' + "  " '<span class="icon type-text2">Your</span>'+ "  "
                '<span class="icon type-text3">GA</span>' + "  " '<span class="icon type-text4">Property</span>', unsafe_allow_html=True)
       
    prop_type = st.selectbox("Property Type", df["propertyType"].unique(), index = None, placeholder= "Chose one:")
    county = st.selectbox("County", df["county"].unique(), index = None, placeholder= "Search your county:")
    price_range = st.slider("Price Range: ", 0, max(df["price"]), (0, max(df["price"])), format="$%d")
        
    with st.container():
        c1,c2 = st.columns(2)
        beds = c2.radio("Bedrooms: ", df["bedrooms"].sort_values().unique() , index=0)
        baths = c1.radio("Bathrooms: ", df["bathrooms"].sort_values().unique() , index=0)  

    st.markdown("") 
  
          
# button!!!      
if st.sidebar.button("**Search**", type= "primary"):
    # dataset configuration
    if prop_type is not None:
        df = df[df["propertyType"] == prop_type]
    if county is not None:
        df = df[df["county"] == county]
    if price_range is not None:
        df = df[(df["price"] >= price_range[0]) & (df["price"] <= price_range[1])]
    if beds is not None:
        df = df[df["bedrooms"] == beds]
    if baths is not None:
        df = df[df["bathrooms"] == baths]
    
    st.balloons()    
    st.dataframe(df, use_container_width=True)
 
# Info and sources
with st.sidebar.container():
    st.markdown(" ")
    st.write("- :red[**Data Source**]: [RentCast API](https://app.rentcast.io/app)")
    st.write("- :blue[**Info**]: This app only shows Georgia state properties. The data is updated every month")
    st.write("- :green[**Sample limit**]: The sample of the total data is 5000 properties per month")
    st.write("- :orange[**Made by**]: [**Carlos Reyes**](https://github.com/carlosreyes98)")
      
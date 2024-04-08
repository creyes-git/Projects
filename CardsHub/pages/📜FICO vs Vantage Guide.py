import streamlit as st
import plotly.express as px
from PIL import Image

cc1, cc2, cc3, cc4, cc5 = st.columns(5)

cc1.image(Image.open("images/fico.png"),width= 200, clamp=True)
cc4.image(Image.open("images/vantage.png"),width= 210, clamp=True)

with st.expander("**What is a credit score?**"):
    st.write("The concept of a credit score may feel complicated, but in essence it looks simply at your payment history, amount of debt, how long you have had debt and how many recent applications you have made for credit accounts. Information about these items are reported to the three credit bureaus, Experian, TransUnion and Equifax, who compile your credit report. The information on your credit report is used to calculate your credit score. Your three-digit credit score captures your experiences with credit and debt and can help you track changes in your financial history over time, from the very first debt you encounter—such as the credit card you opened in college—up to the present. Credit score is a powerful tool that signals to prospective lenders your ability to make payments in a timely manner. This number is unique to you but publicly available under federal law to lenders considering you as a borrower. Your score can be a point of personal pride for good financial management and a point of public documentation. A credit score is an easy way to explain to another person or prospective lender that you can honor your commitment to make timely payments on outstanding debts. In turn, higher scores might lead a lender to extend interest rates lower than they would for consumers with less-favorable credit scores. You can get your credit score as part of a request for a credit report or independently of a credit report. A comprehensive solution is to open a free Credit Sesame account. This provides you with fast access to everything you need to know about your credit history, including your credit score. It includes helpful supporting information that makes sense of your score and report. ")
    
with st.expander("**What are the types of credit scores?**"):
    st.write("There are several different credit scores available to you as a consumer, lender-based scores and generic scores. Lender-based scores are maintained by companies that might consider lending money to you in the future. Common generic scores are the FICO Score and the VantageScore, and they are most widely known by the average consumer. Often, people access their credit score by requesting it from one of the three credit bureaus—Equifax, Experian or TransUnion. You can also access this information in a single location via Credit Sesame. An important note is that your credit score may differ from one report to the next, depending on which bureau lenders report to. Each of the credit bureaus compiles information about your financial history independently of the others. Some credit bureaus might have more information than others. It is possible that a credit report can contain inaccurate information. In this case, you can challenge the innacuracy and have it rectified. It is import to monitor your score regularly and take action if you see a sudden change that cannot be explained by your credit behavior. Rather than focusing only on a single credit score, it’s a good idea to review as many sources as possible with information on your credit history. This gives you a better understanding of your financial health, including strengths and areas for improvement, as you plan future financial decisions. ")
    
st.title("How are credit scores calculated?")

c1, c2, c3 = st.columns(3)

name = ["Payment History", "Credit Age", "Credit Utilization", "Credit MIX", "Enquiries", "Available Credit"]
fico = [35,15,30,10,10,0]
vantage = [40,21,20,11,5,3]

# FICO
c1.plotly_chart(px.pie(names=name, values=fico, title="F I C O   S C O R E", color_discrete_sequence=px.colors.sequential.Sunset_r, hole=0.3), use_container_width=True)
# Vantage
c3.plotly_chart(px.pie(names=name, values=vantage, title="V A N T A G E   S C O R E", color_discrete_sequence=px.colors.sequential.Sunset, hole=0.3), use_container_width=True)


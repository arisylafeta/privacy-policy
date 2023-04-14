import streamlit as st


st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

with st.sidebar:
    st.image('https://i.imgur.com/rycXv9K.jpg')
    st.title('Welcome to ECOTEK')
    st.write('Firm qe merret me prodhimin dhe transportimin e kalldajave dhe termopompave(pomp termike) te kualitet me te larte ne Kosove. Pasqyre e suksesit tone jane knaqesia e klienteve dhe tradita jon 10 vjeqare')


st.title("Privacy Policy")
st.write('This privacy policy explains how our company collects, uses, and protects the personal information of our users who access and use our website and/or our services.')

st.subheader("Collection of Information")
st.write("Our company collects the following personal information from Users:")

st.markdown("•Name and contact information (such as email address, phone number, and physical address)")
st.markdown("•Demographic information (such as age, gender, and location)")
st.markdown("•User-generated content (such as reviews, feedback, and comments")
st.markdown("•Usage information (such as browsing history, device information, and IP address")
st.markdown("•We may collect this information through various methods, including when Users register on our website, subscribe to our newsletter, fill out a form, or use our Services.")

st.subheader('Use of Information')
st.write('Our company may use the personal information collected from Users for the following purposes:')
st.markdown('•To imporve our Services and provide better customer support')
st.markdown("•To personalize the user experience and tailor content to Users' interests")
st.markdown("•To process transactions and payments")
st.markdown("•To send periodic emails and newsletters")
st.markdown("•To respond to Users' inquires, feedback, and requests")
st.markdown("•To comply with legal and regulatory requirements")

st.subheader("Protection of Information")
st.write("Our company takes reasonable measures to protect Users' personal information from unauthorized access, use, disclosure, or alteration. We use appropriate data collection, storage, and processing practices and security measures to protect against unauthorized access, alteration, disclosure, or destruction of Users' personal information, username, password, transaction information, and data stored on our website.")
st.subheader("Sharing of Information")
st.write("Our company does not sell, trade, or rent Users' personal information to others. We may share generic aggregated demographic information not linked to any personal identification information regarding visitors and users with our business partners, trusted affiliates, and advertisers for the purposes outlined above.")
st.subheader("Third-Party Wbsites and Services")
st.write("Users may find content on our website that links to third-party websites and services. We do not control the content or links that appear on these websites and are not responsible for the practices employed by websites linked to or from our website. These websites and services may have their own privacy policies and customer service policies. Browsing and interaction on any other website, including websites that have a link to our website, is subject to that website's own terms and policies.")
st.subheader("Changes to this Policy")
st.write("Our company reserves the right to update this Policy at any time. When we do, we will revise the updated date at the bottom of this page. We encourage Users to frequently check this page for any changes to stay informed about how we are helping to protect the personal information we collect.")
st.subheader("Your Acceptance of these Terms")
st.write("By using our website and/or our Services, you signify your acceptance of this Policy. If you do not agree to this Policy, please do not use our website or our Services. Your continued use of the website and/or our Services following the posting of changes to this Policy will be deemed your acceptance of those changes")
st.subheader("Contacting Us")
st.write("If you have any questions about this Policy, the practices of our company, or your dealings with our website and/or our Services, please contact us at +38348148101.")
st.write("This document was last updated on 14/4/2023")
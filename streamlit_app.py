# Copy code
import streamlit as st
from slack_sdk import WebClient

# Initialize Slack WebClient
slack_token = "YOUR_SLACK_API_TOKEN"
slack_client = WebClient(token=slack_token)

# Streamlit UI
st.title("Calendar App")

# Calendar interface (You can use any calendar library)
# For simplicity, let's assume we have a function to add events
def add_event_to_calendar(event):
    # Add event to the calendar
    pass

event_name = st.text_input("Enter event name:")
event_date = st.date_input("Select event date:")
event_time = st.time_input("Select event time:")

if st.button("Add Event"):
    event = {
        "name": event_name,
        "date": event_date,
        "time": event_time
    }
    add_event_to_calendar(event)
    st.success("Event added successfully!")
    
    # Send notification to Slack
    message = f"New event added: {event_name} on {event_date} at {event_time}"
    response = slack_client.chat_postMessage(channel="#calendar", text=message)
    if response["ok"]:
        st.success("Notification sent to Slack!")
    else:
        st.error("Failed to send notification to Slack.")

# Additional functionalities like viewing/updating/deleting events can be added

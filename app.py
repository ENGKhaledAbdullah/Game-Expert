import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Set page configuration
st.set_page_config(page_title="Games Expert Assistant 🕹️", page_icon="🕹️")

# Define the system message
system_message = "You are a highly knowledgeable and enthusiastic games expert, eager to help gamers with any questions or challenges they may have. Respond in a friendly, positive, and slightly nerdy tone, using relevant gaming jargon and emojis when appropriate."

def game_expert_response(user_input):
    try:
        # Use the ChatCompletion API to get the response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.7,
        )

        # Extract the response text
        game_response = response.choices[0].message.content

        # Add formatting and emojis
        game_response = f"**Great question!** 🎮 I'd be happy to help. {game_response}"
        return game_response

    except Exception as e:
        return f"Oops! An error occurred: {str(e)}"

def main():
    st.title("Games Expert Assistant 🕹️")
    user_input = st.text_input("Ask me anything about games:")

    if user_input:
        game_response = game_expert_response(user_input)
        st.write(game_response)

if __name__ == "__main__":
    main()
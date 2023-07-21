# LangChain Document Response Generator

This is a **Streamlit app** that leverages **LangChain**, a language processing toolchain, to generate responses based on user prompts and perform document similarity searches.

## How to Use

1. **Set up the Environment**

   - Before running the app, make sure you have set your OpenAI API key as an environment variable. You can do this by setting the `OPENAI_API_KEY` variable to your API key value.

2. **Run the App**

   - Run the script, and the Streamlit app will start in your browser.

3. **Input Prompt**

   - In the Streamlit app, you will see a text input labeled "Enter your prompt here." Enter your question or prompt in this field.

4. **Get Response**

   - After entering your prompt, the app will use the GPT-3.5 language model (LLM) to generate a response to your query. The response will be displayed on the app.

5. **Document Similarity Search**

   - The app also allows you to perform a document similarity search based on your input prompt. It will search the provided PDF document ("How_Conversational_Business_Can_Help_You_Get_and_Stay_Closer_to_Customers.pdf") for relevant pages based on the similarity to your prompt.

6. **Results**
   - If you choose to perform the document similarity search, the relevant pages will be displayed in an expandable section below the response.

## Dependencies

The app relies on the following Python packages:

- `os`
- `streamlit`
- `langchain`

Please ensure you have these dependencies installed in your Python environment before running the app.

## API Key

As mentioned earlier, you need to set your OpenAI API key as an environment variable to use the app successfully. Make sure the variable name is `OPENAI_API_KEY`, and the value is your actual API key.

## Note

The LangChain toolchain is designed to handle sets of documents and answer questions related to those documents. The toolchain is backed by the GPT-3.5 language model and the Chroma vectorstore. For more details about the functionalities of the LangChain components, refer to the respective documentation.

If you encounter any issues or have questions, feel free to reach out or create an issue on the [GitHub repository](https://github.com/your_username/your_repository).

Happy document exploration and question-answering!

---

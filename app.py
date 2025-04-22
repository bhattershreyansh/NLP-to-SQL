import streamlit as st
import pandas as pd
import sqlite3
from io import StringIO
import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyB_itsg0VMe9I8fBtwTspV991rT8SCrnEI")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_table_name_from_csv(file_path):
    
    return os.path.splitext(os.path.basename(file_path))[0]

def extract_schema_and_load(file_path, table_name):
    
    table_name = get_table_name_from_csv(file_path)
    df = pd.read_csv(file_path)
    schema = ", ".join([f"{col} ({df[col].dtype})" for col in df.columns])
    conn = sqlite3.connect(":memory:")  
    df.to_sql(table_name, conn, index=False, if_exists="replace") 
    return schema, conn

def generate_prompt_with_schema(schema, user_query, table_name):
    return f"""Table Schema: {schema}

Table Name: {table_name}

User Query: {user_query}

Generate an SQL query using the table name '{table_name}' that directly answers the user's query."""

def generate_sql_using_gemini(prompt):
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    
    response = model.generate_content(prompt)
    
  
    if hasattr(response, 'text'):
        clean_query = response.text.replace('```sql', '').replace('```', '').strip()
    elif hasattr(response, 'result') and hasattr(response.result, 'candidates'):
        
        clean_query = response.result.candidates[0].content.parts[0].text
        clean_query = clean_query.replace('```sql', '').replace('```', '').strip()
    else:
        raise ValueError("Could not extract SQL query from response")
    
    return clean_query

def execute_sql_and_show(conn, sql_query):
    try:
        
        if sql_query.strip().lower().startswith("select"):
            
            result = pd.read_sql(sql_query, conn)
            return result
        else:
            
            cursor = conn.cursor()
            cursor.execute(sql_query)
            conn.commit() 
            print("Query executed successfully. Database updated.")
            return None
    except Exception as e:
        
        print(f"Error executing SQL query: {e}")
        return None


def show_updated_database(conn, table_name):
    try:
        
        query = f"SELECT * FROM {table_name}"
        updated_table = pd.read_sql(query, conn)
        return updated_table
    except Exception as e:
        print(f"Error fetching table data: {e}")
        return None


def extract_schema_and_load(file_obj, table_name):
    df = pd.read_csv(file_obj)
    schema = ", ".join([f"{col} ({df[col].dtype})" for col in df.columns])
    conn = sqlite3.connect(":memory:") 
    df.to_sql(table_name, conn, index=False, if_exists="replace")
    return schema, conn

def main():
    st.title("Natural Language to SQL Query Executor")


    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file:
    
        table_name = uploaded_file.name.split(".")[0]
        file_obj = StringIO(uploaded_file.getvalue().decode("utf-8"))
        
        
        schema, conn = extract_schema_and_load(file_obj, table_name)
        
        st.write("**Extracted Schema:**")
        st.code(schema)
        
        
        user_query = st.text_input("Enter your query in natural language:")
        
        if user_query:
            
            prompt = generate_prompt_with_schema(schema, user_query, table_name)
            st.write("**Generated Prompt:**")
            st.code(prompt)

            
            if st.button("Run Query"):
                
                sql_query = generate_sql_using_gemini(prompt)
                st.write("**Generated SQL Query:**")
                st.code(sql_query)
                
                
                st.write("**Query Result:**")
                result = execute_sql_and_show(conn, sql_query)
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result)
                else:
                    st.write(result)
                
                
                st.write("**Updated Database:**")
                updated_db = show_updated_database(conn, table_name)
                if isinstance(updated_db, pd.DataFrame):
                    st.dataframe(updated_db)
                else:
                    st.write(updated_db)

if __name__ == "__main__":
    main()



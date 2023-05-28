from wordcloud import WordCloud # For plotting wordcloud
import matplotlib.pyplot as plt # For figure or plotting if required
import random
import pandas as pd
from nltk.corpus import stopwords
import seaborn as sns

def desc():
    '''desc: Takes in string of job description and returns a wordcloud and list of words in the job description
    eg: 
       image,list = desc()
        paste job description in the input box'''
    print('Paste Job description\n')
    try:
        input_data = input()
        raw_data = input_data
    except:
        print('Provide input..')
    
    print('')
    print('Paste Resume\n')
    try:
        input_data1 = input()
        raw_data1 = input_data1
    except:
        print('Provide input..')
    try:
        cloud = wc(input_data)
        cloud1 = wc(input_data1)
        return cloud, raw_data, cloud1, raw_data1
    except:
        print('Wordcloud data not provided..')
        
# Function to store the user inputted skills
L_skills = []

def skills_in():
    """skills_in: Takes in strings separated by commas, provide skills, dosen't returns anything but list of your inputted strings can be accessed
                  by calling L_skills.
                  Note: Running function again when it's already has values stored in will erase the previous values and store in new ones"""
    L_skills.clear()
    try:
        skills = input('Insert your skills (separate with comma)')
        List_skills = skills.split(sep=',')
        for skills in List_skills:
            L_skills.append(skills)
    except:
        print('Insert your skills separated with a comma, eg: python,java,c++')
    
    print('\nYour skills:',L_skills)
    print('\n')
    
# Function for plotting wordcloud of description
def wc(text):
    wordcloud = WordCloud(width=1124,height=514)
    wc = wordcloud.generate_from_text(text)
    return wc.to_image()
  
# Process data
def process_data(data_in):
    p0 = data_in.lower() # -> Convert description to lowercase
    p1 = p0.replace('(','').replace(')','').replace('/','').replace('!','').replace(':','').replace('.','').replace('|','').replace('•','').replace(',','') # -> replace special chracters with space
    p2 = p1.split() # -> split words
    p3 = [word for word in p2 if word not in stopwords.words('english')] # -> Loop through description and take out stopwords
    p4 = pd.Series(p3) # ->
    return p4
  
# Function showing count of words
def count(data,data2):
    df1 = pd.DataFrame(data.value_counts(),columns=['Count']).reset_index()
    df2 = pd.DataFrame(data2.value_counts(),columns=['Count']).reset_index()
    df1 = df1.rename({'index':'Job_description keywords'},axis=1)
    df2 = df2.rename({'index':'Resume keywords'},axis=1)
    
    concated_df = pd.concat([df1, df2], axis=1)
    return concated_df
  
# Function which takes in data from job description and resume and shows matched and unmatched words
match = []
not_match = []

#set_1 =set(data)
#set_2 = set(resume_data)

def keyword_matcher(set_1,set_2):
    match.clear()
    not_match.clear()
    for i in set(set_1):
        if i in set(set_2):
            match.append(i)
        else:
            not_match.append(i)
            
# Plotting function to plot distribution of keywords
def plot():
    ax = sns.barplot(x=['Matched keywords','Unmatched keywords'],y=[len(match),(len(match) + len(not_match))])
    ax.set_title('Distribution of keywords')
    for i in ax.containers:
        ax.bar_label(i)
        plt.show()
        
# MAIN function
def main():
    """main function, calls all functions
    returns two cloud -> wordcloud objects, DataFrame consisting of count of keywords -> DataFrame"""
    try:
        skills_in()
    
        cloud,job_data,cloud2,resume_data = desc()
    
        processed_data = process_data(job_data)
        processed_data2 = process_data(resume_data)
    
        concated_df = count(processed_data,processed_data2)
    
        keyword_matcher(processed_data,processed_data2)
        print('\n')
        print('='*185)
        print('\nMatched keywords:',match,'\n\nUnmatched keywords:',not_match)
        print('\n\nKeyword match score:',len(match) / (len(match) + len(not_match)) * 100,'\n\n')
        plot()
        return cloud,cloud2, concated_df
    except:
        print('Run in edit mode')

        
cloud, cloud2, df = main()

cloud # wordcloud for job description
cloud2 # wordcloud for resume
df # DataFrame for keyword count

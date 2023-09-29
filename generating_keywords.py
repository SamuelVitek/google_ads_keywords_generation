import pandas as pd

# Inputs
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Loop creating and filling the list with keywords
keywords_list = []
for product in products:
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])

# Create the DataFrames - exact match, phrase match, final = exact + phrase
keywords_df = pd.DataFrame.from_records(keywords_list)
keywords_df = keywords_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})
keywords_df['Campaign'] = 'SEM_Sofas'
keywords_df['Criterion Type'] = 'Exact match'

keywords_phrase = keywords_df.copy()
keywords_phrase['Criterion Type'] = 'Phrase'

keywords_df_final = pd.concat([keywords_df, keywords_phrase])

# Final steps - saving and printing summary
keywords_df_final.to_csv('final_keywords.csv', index=False)
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(keywords_df_final.head())

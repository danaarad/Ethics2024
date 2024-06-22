import pandas as pd

def validate_prompt(prompt):
    path = "Data.xlsx"
    copyright_data = pd.read_excel(path)
    Full_titles = copyright_data["Full Title"]
    Full_titles = Full_titles.apply(remove_last_char)
    exits, results = search_full_string(Full_titles,prompt)
    if exits:
        print("CopyRight issue was found the interacting copyright texts:")
        for i in range(len(results)):
            if results[i]:
                print(Full_titles[i])
        return False
    return True

def remove_last_char(s):
    if pd.isna(s):
        return s
    if s[-1] == ".":
        return s[:-1]
    return s



def search_full_string(series, search_term):
    search_term_lower = search_term.lower().split()

    def contains_full_string(cell):
        if pd.isna(cell):
            return False
        cell_str = str(cell).lower()
        for word in search_term_lower:
            if word in cell_str:
                return True
        return False

    result = series.apply(contains_full_string)
    exists = result.any()
    return exists, result

#Todo: if there is only one word on our data is this a copy right issue ?
# we are doing now that if at least word in a cell or complete cell exist in our prompt  it is considered a copy right.
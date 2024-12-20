def write_to_excel(data, output_file='result.xlsx'):
    """
    將列表數據寫入Excel文件
    
    Parameters:
    data (list): 包含表頭和數據的二維列表
    output_file (str): 輸出的Excel文件名，默認為'result.xlsx'
    """
    import pandas as pd
    
    # Convert data to DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])
    
    # write to excel
    df.to_excel(output_file, index=False)


# data = [
#     ('result_URL', 'execution_time'), 
#     ('https://d-id-talks-prod.s3.us-west-2.amazonaws.com/auth0%7C6758e9e297052160bbf021a2/tlk_sgtDTEueVU_g2NeeUxCjs/1733886643036.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1733973048&Signature=Fv6p1oroc5rQdiVlDs94N2fVYZs%3D', 12.146722793579102), 
#     ('https://d-id-talks-prod.s3.us-west-2.amazonaws.com/auth0%7C6758e9e297052160bbf021a2/tlk_HoLU3gDWDWFZqjCSdtLSV/1733886654030.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1733973062&Signature=uIvrLeR4%2Bu7SWl67Az8H25pnXTY%3D', 14.861374616622925), 
#     ('https://d-id-talks-prod.s3.us-west-2.amazonaws.com/auth0%7C6758e9e297052160bbf021a2/tlk_Zq-O1ZD_730BXxg5FzpIz/1733886671310.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1733973082&Signature=TEbE80CVgZ7Y7rNCChXHvy6DHLw%3D', 17.478134155273438)
# ]

# write_to_excel(data)
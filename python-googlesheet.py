import pandas as pd

def read_google_sheet(sheet_url):
    # 從URL中提取sheet的ID
    sheet_id = sheet_url.split('/')[5]
    
    # 構建CSV下載網址
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
    
    try:
        # 使用pandas讀取CSV資料
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"讀取Google Sheet時發生錯誤: {e}")
        return None
    
if __name__ == "__main__":
    sheet_url = "https://docs.google.com/spreadsheets/d/13fBumEOLlUXd2LhhLiQpXUrEh9Zkl5ag2oDHatve3Cs/edit?usp=sharing"  # 替換成實際的Google Sheet URL
    data = read_google_sheet(sheet_url)
    
    if data is not None:
        print("成功讀取數據:")
        print(data)
        print()
        print(type(data))

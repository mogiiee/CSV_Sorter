from cgi import print_arguments
import pandas as pd 
import os.path, glob
import csv

pd.set_option("display.max_rows",1200)


# Create a list of all CSV files
files = glob.glob("*.csv")

# Create an empty list to append the df

# for csvv in files:
#     df = pd.read_csv(csvv)
#     df['ErrorFile'] = os.path.basename(csvv)
#     filenames.append(df)

# pp = pd.DataFrame(df)
# # print(pp)
# pp.to_csv("Warnings1.csv")





df_merged = pd.concat(
    map(pd.read_csv, ['newfiles/FileSentByOtherSubmitter1.csv','newfiles/HelixMissingLoyaltyPromotionCode1.csv','newfiles/HelixMissingMultiUnitIndicator1.csv','newfiles/PMUSAMissingMultiUnitIndicator1.csv','newfiles/Rejections1.csv','newfiles/USSTCMissingLoyaltyPromotionCode1.csv','newfiles/USSTCMissingMultiUnitIndicator.csv','newfiles/Warnings1.csv']), ignore_index=True)


# main = pd.read_csv('file2.csv', usecols= ['file2.csv','StoreName', 'WeekEndDate','FileName', "ErrorFile"])
# print(main)

n_data  = df_merged[["RCN",'StoreName', 'WeekEndDate','FileName', "ErrorFile"]]

sorted = n_data.sort_values(by="RCN", ascending= True)

print(sorted)

sorted.to_csv("merged_sorted_with_ErrorFiles.csv")



#what is did 
#so baiscally first add the error file manually... could not figure out a better way to do this.. and then use the code to use the needed coulumns and sort them and then make a file.

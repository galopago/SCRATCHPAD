import csv
import sys

# Reads a CSV file that contains product names and affiliate links and generates 
# a .md file compatible wiht jekill pages
# only elements with flag colum different from "n" are included in the table

def main():

	FLAG_COL   = 0
	NAME_COL   = 1
	DSHEET_COL = 2
	GALOEN_COL = 3
	GALOES_COL = 4
	HSTER_COL  = 5
	INSTR_COL  = 6
	HADAY_COL  = 7
		
	bill_icon = '💸'
	flag_char = 'n'
	datasheet_prefix = '/assets/pdf/' # jekyll path
	
	table_header0 = '| Component         | Get yours! | Datasheet                                          |'+'\n'
	table_header1 = '| -------- | ------ | ------------------------------------------------------------ |'+'\n'	
	table = []
	
	csv_file = 'afflinks.csv'
	md_file = 'comptable.md'
	afflinkid = GALOEN_COL # change according to link track id needed
	
	print("generating MD tables from file:",csv_file)
	
	table.append(table_header0)
	table.append(table_header1)

	#print("table:",table)	

# ########################### sample output table structure ###############################
#| Component         | Get yours! | Datasheet                                          | 
#| -------- | ------ | ------------------------------------------------------------ |
#| 3 pc step drill bit 3-20 mm + centerpunch | [💸](https://s.click.aliexpress.com/e/_9vxJV5 )     |

	with open(csv_file,newline='') as csvfile:
		afflinkslist = csv.reader(csvfile, delimiter=',',quotechar='|')
		afflinksreader=	iter(afflinkslist)
		# skip first (header)
		next(afflinksreader)
		for row in afflinksreader:
			# extracting pdf file name from link		
			spltlnk=row[DSHEET_COL].split("/")
			pdfname=spltlnk[-1]			
			temprow = '| '+row[NAME_COL]+' | ['+bill_icon+'] ('+row[afflinkid]+') | ['+pdfname+'] ('+datasheet_prefix+pdfname+') |'+'\n'
			# add only selected elements to table
			if row[FLAG_COL] != flag_char :
				table.append(temprow)			
				print(row[NAME_COL])
					
	#print(table)

	
	with open(md_file,'w') as outfile:
		outfile.writelines(table)						

	print("MD table saved to file:",md_file)
			
if __name__ == "__main__":
	main()

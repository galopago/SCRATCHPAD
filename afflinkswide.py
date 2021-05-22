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
	datasheet_prefix = 'https://github.com/galopago/logistic/blob/master/datasheet/' # jekyll path
	
	table_header0 = '| Component | Galopago En | Galopago Es | Hackster | Instructables | Hackaday |'+'\n'
	table_header1 = '| --------- | ----------- | ----------- | -------- | ------------- | -------- |'+'\n'
	table_header2 = '| name | GPLUS_absol | GPLUS_autom | YT_chiptuneminuto | YT_chiptuneminute | FB_automatizanos |'+'\n'	
	table = []
	
	csv_file = 'afflinks.csv'
	md_file = 'afflinkswide.md'
	afflinkid = GALOEN_COL # change according to link track id needed
	
	print("generating MD tables from file:",csv_file)
	
	table.append(table_header0)
	table.append(table_header1)
	table.append(table_header2)

	#print("table:",table)	

# ########################### sample output table structure ###############################
#| Component| Datasheet | 
#| -------- | ------ | ------------------------------------------------------------ |
#| 3 pc step drill bit 3-20 mm + centerpunch | https://s.click.aliexpress.com/e/_9vxJV5 |

	with open(csv_file,newline='') as csvfile:
		afflinkslist = csv.reader(csvfile, delimiter=',',quotechar='|')
		afflinksreader=	iter(afflinkslist)
		# skip first (header)
		next(afflinksreader)
		for row in afflinksreader:
			# extracting pdf file name from link		
			spltlnk=row[DSHEET_COL].split("/")
			pdfname=spltlnk[-1]			
			temprow = '| '+row[NAME_COL]+' | [link]('+row[GALOEN_COL]+') | [link]('+row[GALOES_COL]+') | [link]('+row[HSTER_COL]+') | [link]('+row[INSTR_COL]+') | [link]('+row[HADAY_COL]+') |'+'\n'		
			table.append(temprow)			
			print(temprow)
					
	#print(table)

	
	with open(md_file,'w') as outfile:
		outfile.writelines(table)						

	print("MD table saved to file:",md_file)
			
if __name__ == "__main__":
	main()

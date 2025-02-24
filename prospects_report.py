'''
Part 1
The prospects.csv file containts the contact info for information
systems professionals that would make good candidates for an
opening at our company. The job offers 70,000 per year so we are
only interested in candidates that make less than that.

Read the contents of the file and create a new dictionary of those candidates
that meet the criteria. Name the dictionary 'candidates_dict'. The dictionary should 
have the candidate's name as the key and the contact info as the value. Follow 
this format:

{'Amandy Strewther': {'email': 'astrewther1@g.co', 'phone': '773-499-5546', 'salary': 67103.94}}

After creating the dictionary, iterate through it and print out the details of each candidate 
in the following format leaving 2 blank lines between each candidate (first 2 shown):

Name: Amandy Strewther
Email: astrewther1@g.co
Phone: 773-499-5546
Salary: $67,103.94


Name: Valma Greenhalgh
Email: vgreenhalgh9@rediff.com
Phone: 576-374-1155
Salary: $67,475.77



Part 2
Create a VE and name it test1_ve. Install the library - wordcloud. Once you have done so, run this code and it should produce an image named john.png which
represents a word cloud of the most popular words from the book of John in the Bible. Make sure your VE is not in your GitHub repo.


Part 3
Push all your updates to your gitHub repo. Your repo should contain the following 6 files:
1) book of John text.txt
2) mask_oval.png
3) prospects.csv
4) prospects_report.py
5) john.png
6) .gitignore

'''
import csv

#open file



#create csv object



#skip header row




#create a dictionary



# iterate through each row of the csv object using a for loop.



    # check if salary is less than $70,000 and if it is add it to the
    # dictionary
   





# iternate through the dictionary and print out the details as 
# shown in the instructions above











#display the wordcloud
#NOTE: no need to touch the code below. If you install the library correctly, the below code will run and produce an image named 'john.png'.

from pathlib import Path
from wordcloud import WordCloud
import imageio.v2 as imageio
import matplotlib.pyplot as plt


text = Path("book of John text.txt").read_text()
mask_image = imageio.imread("mask_oval.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("john.png")
plt.imshow(wordcloud)
plt.show()
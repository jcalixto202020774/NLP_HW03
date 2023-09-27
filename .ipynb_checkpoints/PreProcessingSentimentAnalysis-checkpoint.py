import os

def transform_reviews():
    for folder in ['books','dvd','electronics','kitchen']:

        print('Consolidating ' + folder)

        # Opening the files
        pos_file = open('data/' + folder + '/' + 'positive.review', 'r', encoding='utf-8', errors='ignore')
        neg_file = open('data/' + folder + '/' + 'positive.review', 'r', encoding='utf-8', errors='ignore')

        #Extracting the content
        pos_content = pos_file.read()
        neg_content = neg_file.read()

        #Closing the files
        pos_file.close()
        neg_file.close()

        #Dividing by reviews
        reviews = pos_content.split('\n') + neg_content.split('\n')
        
        #Writing file
        consolidated = open(folder + '_consolidated.csv','w')
        consolidated.write('review,label\n')
        
        for r in reviews:

            #Separating text from label
            s = r.split('#label#:')

            #Verifing that the review is not empty
            if len(s) == 2:

                #Separating text from label
                text, label = s[0].split(' '), s[1]
        
                #Writing the transformed review
                rev = ''
                for word in text:
                    if len(word) != 0:
                        w = word.split(':')
                        #Adding to the transformed review the word
                        #(replacing '_' by ' ' and multiplying it times the number of ocurrences)
                        rev += (' ' + w[0].replace('_',' '))*int(w[1])

                consolidated.write(rev + ',' + label + '\n')
                
            
transform_reviews()
